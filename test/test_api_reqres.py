import pytest
import requests
from util.logger import logger

@pytest.mark.skipif("se vencio el ApiKey")
# OBTENER USUARIO
def test_get_user(url_base,api_key):
    
    
    url = f"{url_base}/2"
    logger.info(f"realizando solicitud GET a {url_base}")
    response = requests.get(url,headers=api_key)
    
    assert response.status_code == 200
    
    data = response.json()
    #verfificamos que estamoe en user 2
    assert data["data"]["id"] == 2
    

# CREAR USUARIO
@pytest.mark.skipif("se vencio el ApiKey")    
def test_create_user(url_base,api_key):
        
        payload = {
            "name" : "Jose",
            "job" : "Profesor"
        }
        logger.info(f"Agregando usuario: {payload["name"]}, {payload["job"]}")
        response = requests.post(url_base,headers=api_key,json=payload)
        
        assert response.status_code == 201
        
        data = response.json()
        
        assert data["name"] == payload["name"]


# ELIMINAR USUARIO
@pytest.mark.skipif("se vencio el ApiKey")
def test_delete_user(url_base,api_key):
    logger.info("Eliminando el usuario /2")
    response = requests.delete(f"{url_base}/2", headers=api_key)
    
    assert response.status_code == 204

