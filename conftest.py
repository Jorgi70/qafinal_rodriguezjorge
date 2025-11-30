import pytest
from selenium import webdriver
from utils import login
from pages.login_page import LoginPage
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--incognito")
    driver = webdriver.Chrome()
    driver.implicitly_wait(7)
    yield driver
    driver.quit()
    
# Aca llamaos a la CLASE 
@pytest.fixture
def login_in_driver(driver,usuario,password):
   LoginPage(driver).abrir_pagina().login_completo(usuario,password)
   return driver

@pytest.fixture
def url_base():
    return "https://reqres.in/api/users"

@pytest.fixture
def api_key():
    return {"x-api-key": "reqres-free-v1"}