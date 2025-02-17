# Data Product for Airline Company

## Project Overview
This project focuses on predicting flight ticket prices using data from 16 origin and 16 destination airports, totaling 40 million entries with various features. The group divided the workload, assigning each member 4 airports. The final deliverable will include a unified model and a Streamlit application for flight ticket price prediction.

## Data Structure
- Each group member works with different airport datasets
- Datasets are shared in respective notebook directories  
- Contains approximately 40 million data entries
- Features various flight-related parameters

## Project Organization

```
├── data                   # Contains project datasets
├── docs                   # Documentation files for the project
├── models                 # Trained and serialized models
│   ├── catboost_final_model.cbm     # CatBoost model
│   ├── linear_reg_pipeline.joblib   # Linear regression model pipeline
│   ├── pred_pipe_lgb.joblib         # LightGBM model pipeline
│   ├── xgb_pipeline.joblib          # XGBoost model pipeline
│   └── ...                          # Other trained model artifacts
│
├── notebooks   
│   ├── dataprep                   # Individual member's data preparation work
│   ├── data_prep                  # Individual member's data preparation work
│   ├── data_prep_25091570         # Individual member's data preparation work
│   └── model_notebooks            # Various model training notebooks by team members
│
├── references            # Data dictionaries and reference materials
├── reports               # Generated analysis reports
├── src                   # Source code for the project (scripts and modules)
├── pyproject.toml        # Project dependencies and configuration (managed by Poetry)
└── requirements.txt      # Required packages for reproducing the environment
```
--------------------------------


## Project Structure
The project is divided into two main components:

1. Data Preprocessing & Analysis
   - Located in `notebooks/` folder
   - Contains data cleaning and analysis notebooks
   
2. Model Training
   - Located in `notebooks/` directory
   - Contains model training and evaluation notebooks

## Installation
1. Check `pyproject.toml` for required packages and versions
2. Install dependencies using:
   ```bash
   pip install -r requirements.txt
   ```   


If any package is missing, install using:
```bash
pip install package_name
```      


### Model Artifacts

- Trained models are stored in the models folder
- Follow the git repository path to access the application

### Running the Project

#### For Data Preprocessing:

- Navigate to notebooks/folder
- Follow the data cleaning and analysis notebooks


### For Model Training:

- Navigate to notebooks directory
- Use the model training notebooks

Application
The Streamlit application for this project is hosted in a separate repository:

Streamlit App Repository: [https://github.com/Ratana-Sovann/adv_mla_at3_app](https://github.com/Ratana-Sovann/adv_mla_at3_app)


### Important Notes

- Install packages with versions specified in pyproject.toml to avoid conflicts
- Each team member's dataset is available in their respective notebook directories


### Contributors
- FM Farhan Faiyaz
- Ratana Sovann
- Yee Ting Li
- Md Sadman Sakib