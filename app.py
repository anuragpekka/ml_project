import os
import sys
from flask import Flask
from housing.logger import logging
from housing.exception import HousingException

ROOT_DIR = os.getcwd()
LOG_FOLDER_NAME = "logs"
LOG_DIR = os.path.join(ROOT_DIR, LOG_FOLDER_NAME)

app=Flask(__name__)


@app.route("/",methods=['GET','POST'])
def index():
    try:
        raise Exception("We are testing custom exception")
    except Exception as e:
        housing = HousingException(e, sys)
        logging.error(housing.error_message)
        logging.error(f"Exception occured...")
    
    return "CI CD pipeline has been established."


if __name__=="__main__":
    app.run(debug=True) #default port 5000
