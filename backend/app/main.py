"""
Punto de entrada de la aplicación.

Crea la instancia de FastAPI, registra los
endpoints y permite iniciar el servidor 
Uvicorn cuando se ejecuta en local.
"""

import uvicorn
from fastapi import FastAPI
from app.api.router import api_router

# Crea la aplicación FastAPI que procesará
# las peticiones HTTP recibidas por la API.
app = FastAPI(title="DJ-Copilot API")  

# Registra en la aplicación los endpoints
# definidos en los routers de la API.
app.include_router(api_router)

if __name__=="__main__":

    # Inicia el servidor Uvicorn. Recibe las
    # peticiones HTTP y las entrega a la 
    # aplicación FastAPI definida en 'app'
    uvicorn.run (
        "main:app", 
        host="127.0.0.1", 
        port=8000,
        log_level="info"
    )

