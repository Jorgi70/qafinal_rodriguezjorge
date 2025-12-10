# Proyecto de Automatizacion de Pruebas QA con Selenium y Pytest

![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg)
![Selenium](https://img.shields.io/badge/Selenium-4.x-green.svg)
![Pytest](https://img.shields.io/badge/Pytest-7.x-purple.svg)
![License](https://img.shields.io/badge/License-MIT-lightgrey.svg)



## 📄 Descripción General del Proyecto

Este repositorio contiene lo aprendido del curso de Automatización QA, cuyo enfoque principal es la aplicación práctica de los conocimientos adquiridos. El proyecto se centra en la automatización de las interacciones esenciales en el sitio web de comercio electrónico de prueba **`https://www.saucedemo.com`**.

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
/
├── test/                   # Contiene todos los scripts de pruebas (UI y API)
│   ├── test_login.py
│   ├── test_inventory.py
│   ├── test_cart.py
│   └── test_api_reqres.py
│
├── pages/                  # Implementación del Page Object Model (POM)
│   ├── login_page.py
│   ├── inventory_page.py
│   └── cart_page.py
│
├── datos/                  # Datos de prueba externos
│   ├── data_login.csv
│   └── productos.json
│
├── reports/                # Almacena capturas de pantalla de pruebas fallidas
│
├── util/                   # Módulos de utilidades (logger, lector de datos)
│
├── conftest.py             # Fixtures y hooks globales de Pytest
├── run_tests.py            # Script para ejecutar la suite de pruebas
├── requirements.txt        # Dependencias del proyecto
└── README.md               # Documentación del proyecto
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

## Reportes y Logs

El proyecto genera tres tipos principales de resultados durante la ejecucion de las prubas: **reporte HTML**, **capturas de pantalla**, **archivo de log**

### Reporte HTML
Se genera un reporte HTML detallado con el nombre de ```reporte.hmtl``` en la **carpeta raiz** del proyecto

### Logs de ejecución
Tambien se genera un log con informacion detallada de toda la ejecución de las pruebas en la siguiente ubicacion: ```logs/suite.log```

### Capturas de pantalla

Se realizan capturas de pantalla por cada test que haya fallado y se encuentran en la siguiente ubicacion: ```reports/screens/```

## Ejuctar todas las pruebas
Para iniciar la ejecucion de las pruebas debes ejecutar la siguiente linea:

```bash
python -m run_test.py
```

## ¿Como interpretar los reportes?
- Al ejecutar `run_test.py`, se genera un archivo HTML en la carpeta raiz.
- El reporte incluye:
    - Lista completa de test ejecutados
    - El estado de cada prueba
    - La duracion de cada test
    - Las capturas de pantalla para pruebas fallidas

## Pruebas incluidas
- Login exitoso y fallido
- Login exitoso y fallido usando faker
- Comportamiento de la pagina de inventario
- Comportamiento de la pagina del carrito
- API (Reqres): GET users, POST create user, DELETE user, validaciones de codigos HTTP, validaciones de estructura JSON

## Manejo de datos de prueba
- En la carpeta `datos` se incluyen archivos como:
    - `data_login.csv` -> datos de usuarios validos o invalidos
    - `productos.json` -> datos de productos para validacion

### Conclusion
Este proyecto ofrece una estructura organizada y escalable para automatizar pruebas de API utilizando Python y Pytest. Incluye un flujo simple de ejeucion mediante `run_test.py`, generacion automatica de reporte HTML facilitando el analisis de las pruebas.

La arquitectura del proyecto esta pensada para agregar nuevos casos de prueba y configuraciones sin modificar el nucleo del proyecto, manteniendo buenas practicas y permitiendo su escalabilidad en el tiempo.


## 📄 Licencia
Este proyecto se distribuye bajo la licencia MIT. Consulta el archivo `LICENSE` para más detalles.
