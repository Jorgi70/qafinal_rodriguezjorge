import logging
import pathlib

#Creamos la carpeta logs
audit_dir = pathlib.Path('logs')
#Verificamos que la carpeta exista
audit_dir.mkdir(exist_ok=True)
#Creamos el Archivos .log
log_file = audit_dir/ 'suite.log'

#testeamosa el archivo como loger
logger = logging.getLogger("TalentoTech")
#loger de paso a paso
logger.setLevel(logging.INFO)

#Verificamos que no haya loger duplicados
if not logger.handlers:
    file_handler = logging.FileHandler(log_file,mode="a", encoding="utf-8")#mode a de append o abrir
    
    formatter = logging.Formatter(
        "%(asctime)s %(levelname)s %(name)s: %(message)s",
        datefmt="%Y-%m-%d : %H:%M:%S"
    )
    
    file_handler.setFormatter(formatter)
    #agregamos el formato al logger
    logger.addHandler(file_handler)