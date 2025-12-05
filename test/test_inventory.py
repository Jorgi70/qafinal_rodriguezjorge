from selenium.webdriver.common.by import By
from selenium import webdriver
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
import pytest

@pytest.mark.parametrize("usuario,password",
                         [("standard_user","secret_sauce")])
def test_inventory(login_in_driver,usuario,password):
    try:
        driver = login_in_driver
        LoginPage(driver).login_completo(usuario,password)
        inventory_page = InventoryPage(driver)
        
        #Verificar los productos
        assert len(inventory_page.obtener_todos_los_productos()) > 0, "El inventario no tiene productos"
        
        #Verificar vacio el carrito al inicio
        assert inventory_page.obtener_conteo_carrito() == 0
        
        #Agregar el primer producto
        inventory_page.agregar_primer_producto()
        
        #Verificar el contrador del carrito
        assert inventory_page.obtener_conteo_carrito()  == 1,f"Se esperaba 1 pero es {inventory_page.obtener_conteo_carrito()}"
        
        
    except Exception as e:
        print(f"El error fue: {e}");
        raise;
  