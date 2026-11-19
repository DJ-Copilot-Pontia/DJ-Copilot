"""Uso: python cliente_mert.py (con AZURE_SAS_URL en el entorno)
Pide al servidor el embedding de cada canción del contenedor y lo guarda en salida/embeddings_servidor/<carpeta>/<título>.npy."""
from pathlib import Path
from urllib.parse import unquote, urlsplit

import numpy as np
import requests
from enumerar_temas_contenedor_azure import listar_canciones, sas_url

sas = urlsplit(sas_url).query
destino = Path(__file__).resolve().parent / "salida" / "embeddings_servidor"
rutas = [(carpeta, url) for carpeta, urls in sorted(listar_canciones().items()) for url in sorted(urls)]
for numero, (carpeta, url) in enumerate(rutas, 1):
    ruta = Path(unquote(urlsplit(url).path))
    print(f"[{numero}/{len(rutas)}] {carpeta}/{ruta.stem}")
    respuesta = requests.get("http://127.0.0.1:8000/embedding", params={"url": f"{url}?{sas}"})
    respuesta.raise_for_status()
    (destino / carpeta).mkdir(parents=True, exist_ok=True)
    np.save(destino / carpeta / f"{ruta.stem}.npy", np.array(respuesta.json(), dtype=np.float32))
