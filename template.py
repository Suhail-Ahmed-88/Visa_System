import os 
from pathlib import Path

project_nmae = "visa_prediction_system"

list_of_files =[
    f"{project_nmae}/__init__.py",
    f"{project_nmae}/components/__init__.py",
    f"{project_nmae}/components/data_ingestion.py",
    f"{project_nmae}/components/data_validation.py",
    f"{project_nmae}/components/data_transformation.py",
    f"{project_nmae}/components/model_trainer.py",
    f"{project_nmae}/components/model_evaluation.py",
    f"{project_nmae}/components/model_pusher.py",
    f"{project_nmae}/constants/__init__.py",
    f"{project_nmae}/configuration/__init__.py",
    f"{project_nmae}/constant/__init__.py",
    f"{project_nmae}/entity/__init__.py",
    f"{project_nmae}/entity/config_entity.py",
    f"{project_nmae}/entity/artifact_entity.py",
    f"{project_nmae}/logger/__init__.py",
    f"{project_nmae}/pipeline/__init__.py",
    f"{project_nmae}/pipeline/training_pipeline.py",
    f"{project_nmae}/pipeline/predictoin_pipeline.py",
    f"{project_nmae}/utils/__init__.py",
    f"{project_nmae}/utils/main_utils.py",
    "app.py",
    "requirements.txt",
    "setup.py",
    "Dockerfile",
    ".dockerignore",
    "demo.py",
    "config/model.yaml",
    "config/schema.yaml",
 
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        # logging.info(f"Creating directory: {filedir} for file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            # logging.info(f"Creating empty file: {filepath}")

    else:
        # logging.info(f"{filename} already exists")
        print(f"file is already present at: {filepath}")
        
      