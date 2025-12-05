from selenium.webdriver.common.by import By
from selenium import webdriver
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from util.lector_jason import leer_json_productos
from pages.login_page import LoginPage
import pytest

RUTA_JSON = "datos/productos.json"

@pytest.mark.parametrize("usuario,password",
                         [("standard_user","secret_sauce")])
@pytest.mark.parametrize("nombre_producto",leer_json_productos(RUTA_JSON))
def test_cart_json(login_in_driver,usuario,password,nombre_producto):
    try:
        
        driver = login_in_driver
        LoginPage(driver).login_completo(usuario,password)
        inventory_page = InventoryPage(driver)
        
        #agregar al carrito el producto
        inventory_page.agregar_producto_por_nombre(nombre_producto)
        
        #abrir carrito
        inventory_page.abrir_carrito()
        
        #validar el producto
        cartPage = CartPage(driver)
        
        assert cartPage.obtener_nombre_productos_carrito() == nombre_producto
        
     
    except Exception as e:
        print(f"El error fue: {e}");
        raise;
   