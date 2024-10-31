import os 
import sys
from visa_prediction_system.exception import VisaException
from visa_prediction_system.logger import logging
from visa_prediction_system.constants import DATABASE_NAME, MONGODB_URL_KEY
import pymongo
import certifi

ca = certifi.where()

class MongoDBClinet:
    """
    Class Name  : export_data_into_feature_store
    Description : This method exports the dataframe from mongodb feature store as dataframe
    
    Output      : connection to mongodb database
    On Failure  : raises an exception
    """
    client = None
    
    def __init__(self, database_name=DATABASE_NAME) -> None:
        try:
            if MongoDBClinet.client is None:
                mongo_db_url = os.getenv(MONGODB_URL_KEY)
                if mongo_db_url is None:
                    raise Exception(f"Envirnment key: {MONGODB_URL_KEY} is not set.")
                MongoDBClinet.client = pymongo.MongoClient(mongo_db_url, tlsCAFILE=ca)
            self.client = MongoDBClinet.client
            self.database = self.client[database_name]
            self.database_name = database_name
            logging.info("MongoDB connection successfull")
        except Exception as e:
            raise VisaException(e, sys)