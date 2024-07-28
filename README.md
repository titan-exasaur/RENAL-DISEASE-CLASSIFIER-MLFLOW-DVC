# Renal Disease Classifier with MLflow and DVC
This repository contains a project for classifying renal disease using machine learning techniques. The project leverages MLflow for tracking experiments and DVC (Data Version Control) for managing data and model versions.

![image](https://github.com/user-attachments/assets/d315e51f-4328-4b66-88d1-7ccbbf483bc6)


# Table of Contents
1. Project Overview
2. Getting Started
  2a. Prerequisites
  2b. Installation
3. Usage
  3a. Running the Application
  3b. MLflow Tracking
4. Project Structure
5. Contributing

## 1. Project Overview
The Renal Disease Classifier project aims to build a machine learning model to classify renal disease. The project uses a combination of Python, MLflow, and DVC to ensure reproducibility and effective data management.

## 2. Getting Started
### 2a. Prerequisites
1. Python 3.8 or higher
2. Docker
3. Git
4. DVC
5. MLflow

### 2b. Installation
1. Clone the repository:

```
git clone https://github.com/titan-exasaur/RENAL-DISEASE-CLASSIFIER-MLFLOW-DVC.git
cd RENAL-DISEASE-CLASSIFIER-MLFLOW-DVC
```

2. Create and activate a virtual environment:
```
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

3. Install the required Python packages:
```
pip install -r requirements.txt
```


## 3. Usage
### 3a. Running the Application
1. To run the application, use the following command:
```
python main.py
```

### 3b. MLflow Tracking
To start the MLflow UI for tracking experiments, run:
```
mlflow repro
```

3. Then, navigate to **http://localhost:5000** to access the MLflow UI.

## 4. Project Structure
```
.
├── .dvc/                  # DVC specific files
├── .github/               # GitHub workflows and configurations
├── build/                 # Build related files
├── config/                # Configuration files
├── logs/                  # Logs directory
├── model/                 # Model related files
├── research/              # Research related files
├── src/                   # Source code
│   ├── data/              # Data processing scripts
│   ├── models/            # Model definition scripts
│   ├── utils/             # Utility scripts
├── templates/             # Template files
├── .dvcignore             # DVC ignore file
├── .gitattributes         # Git attributes file
├── .gitignore             # Git ignore file
├── Dockerfile             # Dockerfile for containerization
├── app.py                 # Flask application
├── dvc.lock               # DVC lock file
├── dvc.yaml               # DVC pipeline file
├── main.py                # Main script
├── params.yaml            # Parameters file
├── requirements.txt       # Python requirements
├── scores.json            # Scores file
├── setup.py               # Setup script for packaging
├── template.py            # Template script
└── README.md              # Readme file
```

## 5. Contributing
Contributions are welcome! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch (git checkout -b feature-branch).
3. Make your changes.
4. Commit your changes (git commit -m 'Add some feature').
5. Push to the branch (git push origin feature-branch).
6. Open a pull request.
