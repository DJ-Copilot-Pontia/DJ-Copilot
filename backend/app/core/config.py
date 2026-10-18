"""
Configuración de la conexión a MongoDB.
"""

import os
from dotenv import load_dotenv

# Carga las variables de .env si no existen
# previamente en el entorno (terminal/Docker)
load_dotenv()

# Obtiene la URI de conexión a MongoDB. La URI
# indica como conectarse al servidor MongoDB
# (protocolo://servidor:puerto)
MONGO_URI = os.getenv(
    "MONGO_URI",
    "mongodb://localhost:27017" 
)

# Obtiene el nombre de la base de datos
MONGO_DB = os.getenv(
    "MONGO_DB",
    "djcopilot"
)

