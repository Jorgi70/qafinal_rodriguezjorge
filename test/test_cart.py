from selenium.webdriver.common.by import By
from selenium import webdriver
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
import pytest
from pages.login_page import LoginPage


@pytest.mark.parametrize("usuario,password",
                         [("standard_user","secret_sauce")])
def test_cart(login_in_driver,usuario,password):
    try:
        
        driver = login_in_driver
        
        LoginPage(driver).login_completo(usuario,password)
        
        inventory_page = InventoryPage(driver)
        
        #agregar al carrito el producto
        inventory_page.agregar_primer_producto()
        
        #abrir carrito
        inventory_page.abrir_carrito()
        
        #validar el producto
        cartPage = CartPage(driver)
        
        productos_en_carrito = cartPage.obtener_productos_carrito()
        
        assert len(productos_en_carrito) == 1
        
        #assert False, "Fallo de prueba forzado"
        
        
    except Exception as e:
        print(f"El error fue: {e}");
        raise;
   