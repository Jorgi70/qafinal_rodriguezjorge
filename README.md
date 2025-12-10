# Proyecto de Automatizaci0n de Pruebas QA con Selenium y Pytest

![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg)
![Selenium](https://img.shields.io/badge/Selenium-4.x-green.svg)
![Pytest](https://img.shields.io/badge/Pytest-7.x-purple.svg)
![License](https://img.shields.io/badge/License-MIT-lightgrey.svg)


## 📄 Descripción General del Proyecto

Este repositorio contiene la **Pre-Entrega** del curso de Automatización QA, cuyo enfoque principal es la aplicación práctica de los conocimientos adquiridos. El proyecto se centra en la automatización de las interacciones esenciales en el sitio web de comercio electrónico de prueba **`https://www.saucedemo.com`**.

El objetivo es establecer una base sólida para el testing automatizado, cubriendo desde el acceso al sistema hasta la gestión básica del carrito de compras, utilizando las mejores prácticas con Python y Selenium.

## 🚀 Funcionalidades Automatizadas (Casos de Prueba)

Se han cubierto los siguientes escenarios de usuario:

| Módulo | Escenario de Prueba | Objetivo de la Validación |
| :---   | :--- | :--- |
| **Login** | Acceso al Sistema | Verificar el inicio de sesión exitoso con credenciales estándar. |
| **Inventario** | Validación de Interfaz | Comprobar el título de la página y la presencia de productos y elementos clave (filtros, menú). |
| **Carrito** | Interacción con Productos | Añadir un producto, validar el incremento del contador del carrito y confirmar su presencia en la vista del carrito. |

## 💻 Tecnologías Usadas

Este proyecto de automatización de pruebas utiliza las siguientes tecnologías y librerías clave, todas basadas en el ecosistema **Python**:

| Tecnología | Propósito en el Proyecto |
| :--- | :--- |
| **Python** | Lenguaje principal de programación utilizado para escribir todos los *scripts* de prueba, *fixtures* y la lógica de automatización. |
| **Selenium** | Herramienta fundamental para la **automatización del navegador (Web UI)**. Permite simular interacciones de usuario (clics, ingresos de texto, navegación) en la aplicación web para realizar pruebas *end-to-end*. |
| **Webdriver-manager** | Librería crucial para la **gestión automática de los *drivers* del navegador**. Elimina la necesidad de descargar y configurar manualmente los *drivers*. |
| **Requests** | Se utiliza para realizar **peticiones HTTP** a APIs y *endpoints* del *backend*. Es esencial para las pruebas de servicios (API Testing). |
| **Faker** | Genera **datos de prueba realistas y aleatorios** (nombres, correos electrónicos, etc.) para las pruebas de formularios y simulación de usuarios. |
| **Pytest** | *Framework* principal para la **ejecución de pruebas**. Proporciona una estructura robusta para escribir, descubrir y ejecutar pruebas de manera eficiente. |
| **Pytest-check** | Extensión de `pytest` que permite **realizar múltiples aserciones** dentro de una misma prueba sin detener la ejecución tras la primera falla. |
| **Pytest-html** | *Plugin* de `pytest` que genera un **reporte de pruebas en formato HTML** legible y detallado después de cada ejecución. |
| **Behave** | *Framework* de **Desarrollo Guiado por Comportamiento (BDD)**. Se utiliza para escribir escenarios de prueba en lenguaje natural (Gherkin). |
| **Git & GitHub** | Sistema de control de versiones y hosting del código fuente. |

## 📁 Estructura del Repositorio

La organización del proyecto se adhiere a una estructura modular para facilitar la escalabilidad y el mantenimiento:

```
preentrega-rodriguezjorge/ 
├── test/ 
│     ├── test_login.py         # Pruebas relacionadas con el Login. 
│     ├── test_inventory.py     # Pruebas de Inventario y Elementos. 
│     └── test_productos.py     # Pruebas de Carrito y Flujo de Productos.
│ 
├── utils.py                # Funciones Login (Inicialización de Chrome/Driver). 
├── conftest.py             # Hooks de Pytest, fixtures. 
├── report.html             # Reporte final generado por pytest. 
├── README.md               # Describe las funcionalidades del programa. 
├── run_tests.py            # Archivo main para la ejecución de los tests. 
└── requirements.txt        # Listado de dependencias del proyecto.
```

⚙️ Configuración e Instalación

1. Clonar el Repositorio

```
    git clone https://github.com/Jorgi70/qafinal_rodriguezjorge.git

    cd preentrega-rodriguezjorge

```
2. Instalar Dependencias

    Asegúrate de tener Python instalado. Luego, instala las bibliotecas necesarias:
```
selenium
pytest
webdriver-manager
pytest-html
pytest-check
requests
faker
behave

```
(Instalar todo con ***pip install -r requirements.txt*** )

📊 **Reporte de Resultados**

Tras la ejecución, el reporte report.html contendrá un resumen ejecutivo de la corrida de pruebas, incluyendo:

Detalle de los casos de prueba ejecutados.

Resultado de cada prueba (Éxito passed o Falla failed).

Duración de la ejecución.

🎯 **Proyección y Mejoras** (Próximos Pasos)

El proyecto está diseñado para ser la base de la entrega final. Las futuras mejoras planeadas
