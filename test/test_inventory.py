from selenium.webdriver.common.by import By
from selenium import webdriver
from pages.inventory_page import InventoryPage
import pytest

@pytest.mark.parametrize("usuario,password",
                         [("standard_user","secret_sauce")])
def test_inventory(login_in_driver):
    try:
        
        driver = login_in_driver;
        inventory_page = InventoryPage(driver)
        
        #Verificar los productos
        assert len(inventory_page.obtener_todos_los_productos()) > 0, "El inventario no tiene productos"
        
        #Verificar vacio el carrito al inicio
        assert inventory_page.obtener_conteo_carrito() == 0,f"Se esperaba 0 pero es {inventory_page.obtener_conteo_carrito()}"
        
        #Agregar el primer producto
        inventory_page.agregar_primer_producto()
        
        #Verificar el contrador del carrito
        assert inventory_page.obtener_conteo_carrito()  == 1,f"Se esperaba 1 pero es {inventory_page.obtener_conteo_carrito()}"
        
        
    except Exception as e:
        print(f"El error fue: {e}");
        raise;
    finally:
        driver.quit();