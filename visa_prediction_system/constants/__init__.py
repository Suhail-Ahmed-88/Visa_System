import os
from datetime import datetime

DATABASE_NAME = "visaDB"

COLLECTION_NAME = "visa_data"

MONGODB_URL_KEY = "mongodb_url"

PIPELINE_NAME = "visa"

ARTIFACT_DIR = "artifact"

FILE_NAME = "visadataset.csv"

TRAIN_FILE_NAME = "train.csv"

TEST_FILE_NAME = "test.csv"

MODEL_FILE_NAME = "model.pkl"

"""
Data Ingestion related constant start with DATA_INGESTION VAR NAME
"""

DATA_INGESTION_COLLECTION_NAME:str = "visa_data"
DATA_INGESTION_DIR_NAME:str = "data_ingestion"
DATA_INGESTION_FEATURE_SOTRE_DIR:str = "feature_store"
DATA_INGESTION_INGESTED_DIR:str = "ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO: float = 0.2
