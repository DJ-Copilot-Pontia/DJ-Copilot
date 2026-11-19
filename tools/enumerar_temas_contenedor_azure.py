# pip install azure-storage-blob
import os
from collections import defaultdict
from urllib.parse import urlsplit, urlunsplit
from azure.storage.blob import ContainerClient

EXTENSIONES = {".mp3", ".wav", ".flac", ".aiff", ".aif", ".m4a", ".ogg"}

sas_url = os.environ["AZURE_SAS_URL"]  # URL del contenedor con el SAS token
contenedor = ContainerClient.from_container_url(sas_url)

def listar_canciones():
    canciones = defaultdict(list)
    for blob in contenedor.list_blobs():
        carpeta, _, nombre = blob.name.rpartition("/")

        if os.path.splitext(nombre)[1].lower() in EXTENSIONES:
            url = contenedor.get_blob_client(blob.name).url
            # Quita el SAS token (la parte después de "?")
            url = urlunsplit(urlsplit(url)._replace(query=""))
            canciones[carpeta or "(raíz)"].append(url)

    return canciones

if __name__ == "__main__":
    canciones = listar_canciones()
    for carpeta in sorted(canciones):
        print(f"\n{carpeta} ({len(canciones[carpeta])} canciones)")
        for url in sorted(canciones[carpeta]):
            print(f"  {url}")
        