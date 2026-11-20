"""Arranque: python servidor_mert.py (escucha en 127.0.0.1:8000).
GET /embedding?url=URL_DEL_AUDIO devuelve en JSON el embedding MERT de la canción, de forma [25, 1024]."""
import io

import requests
import soundfile
import torch
import torchaudio.functional
import uvicorn
from fastapi import FastAPI
from transformers import AutoModel, Wav2Vec2FeatureExtractor

# trust_remote_code ejecuta el código del repositorio de Hugging Face: se fija el commit.
IDENTIFICADOR = "m-a-p/MERT-v1-330M"
REVISION = "5240c2708a5acaee1007f43fb9735c7dcd0b78c9"
dispositivo = "cuda" if torch.cuda.is_available() else "cpu"
extractor = Wav2Vec2FeatureExtractor.from_pretrained(IDENTIFICADOR, revision=REVISION, trust_remote_code=True)
modelo = AutoModel.from_pretrained(IDENTIFICADOR, revision=REVISION, trust_remote_code=True).to(dispositivo).eval()
hz = extractor.sampling_rate
app = FastAPI()


@app.get("/embedding")
def embedding(url: str):
    respuesta = requests.get(url)
    respuesta.raise_for_status()
    datos, hz_original = soundfile.read(io.BytesIO(respuesta.content), dtype="float32", always_2d=True)
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
    return torch.stack(medias).mean(dim=0).cpu().tolist()


if __name__ == "__main__":
    uvicorn.run(app)
