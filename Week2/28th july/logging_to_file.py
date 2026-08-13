#logging to file 
import logging

logging.basicConfig(
    filename="app.log",
    level=logging.INFO
)

logging.info("Program Started")
logging.error("Database Failed")