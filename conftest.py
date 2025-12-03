import pytest
from selenium import webdriver
from utils import login
from pages.login_page import LoginPage
from selenium.webdriver.chrome.options import Options
from datetime import datetime
import time

#agregamos la var target para creacion de carpeta para lo screen
import pathlib

target = pathlib.Path("reports/screens")
target.mkdir(parents=True, exist_ok=True)

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
   #LoginPage(driver).abrir_pagina().login_completo(usuario,password) Borramos para los screenshot
   LoginPage(driver).abrir_pagina()
   return driver

@pytest.fixture
def url_base():
    return "https://reqres.in/api/users"

@pytest.fixture
def api_key():
    return {"x-api-key": "reqres-free-v1"}

#SCREENSHOTS
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item,call):
    outcome = yield
    #obtenemos lo que se esta ejecutando
    report = outcome.get_result()
    
    if report.when in ("setup","call") and report.failed:
        driver = item.funcargs.get("driver", None)
        
        if driver:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S") 
            timestamp_unix = int(time.time())
            file_name = target / f"{report.when}_{item.name}_{timestamp}.png"
            driver.save_screenshot(str(file_name))