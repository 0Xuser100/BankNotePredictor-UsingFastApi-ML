## Kaggle Notebook  
[🔗 View the Kaggle Notebook](https://www.kaggle.com/code/triblex/banknotepredictor-usingfastapi-ml-99-accuracy)
```markdown
# Bank Note Authentication

This repository contains an end-to-end project for authenticating bank notes using the UCI Bank Note Authentication dataset.
The project demonstrates how to load the dataset, train a machine learning model (Random Forest Classifier),
and serve predictions using a FastAPI web service.

## Repository Structure

```bash
bank-note-authentication/
├── app.py                           # FastAPI application with endpoints for prediction
├── banknote_schema.py               # Pydantic model for validating input data
├── classifier.pkl                   # Pre-trained model saved using pickle
├── Bank_Note_Authentication_UCI_data.ipynb  # Notebook for data exploration, training, and model saving
├── requirements.txt                 # List of Python dependencies
└── README.md                        # Documentation and instructions
```

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/0Xuser100/BankNotePredictorUsingFastApi-Predict-real-vs.-fake-banknotes-using-ML.git
   cd BankNotePredictorUsingFastApi-Predict-real-vs.-fake-banknotes-using-ML
   ```

2. **Set up a virtual environment (optional but recommended):**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

The FastAPI application is defined in `app.py`. To run the API locally:

```bash
uvicorn app:app --reload
```

This will start the server at [http://127.0.0.1:8000](http://127.0.0.1:8000).

### API Endpoints

```bash
# GET /
# Returns a simple welcome message.
curl -X GET "http://127.0.0.1:8000/"

# GET /{name}
# Returns a personalized welcome message using the URL parameter.
curl -X GET "http://127.0.0.1:8000/John"

# POST /predict
# Accepts a JSON request body with bank note features and returns a prediction.
curl -X POST "http://127.0.0.1:8000/predict" \
-H "Content-Type: application/json" \
-d '{"variance": 4, "skewness": 6, "curtosis": 4, "entropy": 4}'
```

## Data and Model

```bash
# The Bank Note Authentication UCI dataset is loaded using kagglehub in the notebook.
# The dataset is processed and used to train a Random Forest Classifier.
# The trained model is saved as classifier.pkl using the pickle module.
```

## Development

```bash
# You can use the Jupyter Notebook Bank_Note_Authentication_UCI_data.ipynb to:
# - Explore the dataset.
# - Train and evaluate the model.
# - Save the trained model to be used by the FastAPI application.
```

## Contributing

```bash
# Feel free to fork the repository and submit pull requests if you have improvements or bug fixes.
```

## License

```bash
# This project is licensed under the MIT License.
```

---

## File Overviews

### **app.py**

```bash
# This file contains the FastAPI web service. It loads the pre-trained classifier and defines the following endpoints:
# - GET / for a welcome message.
# - GET /{name} for a personalized greeting.
# - POST /predict for making predictions on bank note data.
```

### **banknote_schema.py**

```bash
# Defines a Pydantic model (banknote_schema) that validates the JSON request body.
# It ensures that the data provided for prediction includes variance, skewness, curtosis, and entropy as floats.
```

### **classifier.pkl**

```bash
# A pre-trained Random Forest model saved using the pickle module.
# This file is loaded in the FastAPI app to provide predictions.
```

### **Bank_Note_Authentication_UCI_data.ipynb**

```bash
# A Jupyter Notebook that contains code to:
# - Load the dataset using kagglehub.
# - Preprocess and explore the data.
# - Train a Random Forest Classifier.
# - Evaluate the model.
# - Save the trained model to classifier.pkl.
```

### **requirements.txt**

```bash
# Lists all the Python packages needed to run this project.
# Ensure that these packages are installed in your environment.
```

---

## Conclusion

```bash
# This end-to-end repository allows you to train a model for bank note authentication and deploy it as an API using FastAPI.
# Use the provided notebook for model training and exploration, and the FastAPI app for real-time predictions.
# Feel free to update or extend this repository as needed for your project. Happy coding!
```
```

---
 
