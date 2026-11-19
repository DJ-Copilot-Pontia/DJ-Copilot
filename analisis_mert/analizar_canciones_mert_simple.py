"""Uso: python analizar_canciones_mert_simple.py CARPETA [95M|330M]
Calcula un embedding MERT por canción y capa y muestra las 5 canciones más parecidas a cada una."""
import sys
from pathlib import Path

import numpy as np
import soundfile
import torch
import torchaudio.functional
from transformers import AutoModel, Wav2Vec2FeatureExtractor

# trust_remote_code ejecuta el código del repositorio de Hugging Face: se fija el commit.
MODELOS = {
    "95M": ("m-a-p/MERT-v1-95M", "12af15fef9d0ac838c3f475bfbbf26d2060dd4f5"),
    "330M": ("m-a-p/MERT-v1-330M", "5240c2708a5acaee1007f43fb9735c7dcd0b78c9"),
}
carpeta = Path(sys.argv[1])
nombre_modelo = sys.argv[2] if len(sys.argv) > 2 else "330M"
identificador, revision = MODELOS[nombre_modelo]
dispositivo = "cuda" if torch.cuda.is_available() else "cpu"
extractor = Wav2Vec2FeatureExtractor.from_pretrained(identificador, revision=revision, trust_remote_code=True)
modelo = AutoModel.from_pretrained(identificador, revision=revision, trust_remote_code=True).to(dispositivo).eval()
hz = extractor.sampling_rate

extensiones = {".aiff", ".aif", ".wav", ".flac", ".mp3", ".ogg", ".m4a"}
rutas = sorted(f.relative_to(carpeta).as_posix() for f in carpeta.rglob("*") if f.suffix.lower() in extensiones)
embeddings = []
for numero, ruta in enumerate(rutas, 1):
    print(f"[{numero}/{len(rutas)}] {ruta}")
    datos, hz_original = soundfile.read(carpeta / ruta, dtype="float32", always_2d=True)
    audio = torch.from_numpy(datos.mean(axis=1)).to(dispositivo)
    audio = torchaudio.functional.resample(audio, hz_original, hz).cpu().numpy()
    # Ventanas de 10 s; la última se conserva si dura al menos 1 s.
    ventanas = [audio[inicio:inicio + 10 * hz] for inicio in range(0, len(audio) - hz + 1, 10 * hz)]
    medias = []
    with torch.inference_mode():
        for ventana in ventanas:
            entrada = extractor(ventana, sampling_rate=hz, return_tensors="pt").input_values.to(dispositivo)
            capas = modelo(input_values=entrada, output_hidden_states=True).hidden_states
            medias.append(torch.stack([capa.mean(dim=1)[0] for capa in capas]))
    embeddings.append(torch.stack(medias).mean(dim=0).cpu().numpy())
embeddings = np.stack(embeddings)

generos = [ruta.split("/")[0] if "/" in ruta else "(raíz)" for ruta in rutas]
titulos = [Path(ruta).stem for ruta in rutas]
salida = Path(__file__).resolve().parent / "salida" / f"embeddings_{nombre_modelo}_simple.npz"
salida.parent.mkdir(exist_ok=True)
np.savez(salida, embeddings=embeddings, rutas_blob=np.array(rutas), generos=np.array(generos),
         titulos=np.array(titulos), modelo=np.array(identificador))

vectores = embeddings[:, 1:, :].mean(axis=1)  # la capa 0 es la entrada del transformer
vectores /= np.linalg.norm(vectores, axis=1, keepdims=True)
similitudes = vectores @ vectores.T
np.fill_diagonal(similitudes, -np.inf)  # una canción no es vecina de sí misma
for indice, vecinos in enumerate(np.argsort(-similitudes, axis=1)[:, :5]):
    print(f"\n{titulos[indice]} [{generos[indice]}]")
    for vecino in vecinos:
        print(f"  {similitudes[indice, vecino]:.4f}  {titulos[vecino]} [{generos[vecino]}]")
