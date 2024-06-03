# Crpto Currency Price Prediction Using Random forest and KNN Technique

This project is a web application that predicts crpto currency price prediction using random forest and KNN technique. The application is built using Flask and allows users to select between different models (Random Forest and K-Nearest Neighbors) to make predictions and evaluate their performance.

## Features

- Load and preprocess price data from a CSV file
- Train machine learning models to predict prices
- Evaluate model performance using RMSE (Root Mean Squared Error)
- Simple web interface for model selection and prediction

## Installation

### Prerequisites

- Python 3.x
- Flask
- Pandas
- Scikit-learn

### Steps

1. Clone the repository:

    ```sh
    git clone https://github.com/aravind1000/Crypto_Currency_Price_Prediction_Using_Random-forest-and-KNN_Techniques.git
    cd Crypto_Currency_Price_Prediction_Using_Random-forest-and-KNN_Techniques
    ```

2. Create a virtual environment and activate it:

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:

    ```sh
    pip install -r requirements.txt
    ```

4. Make sure the dataset file is placed in the `Datasets` directory.

## Running the Application

1. Start the Flask application:

    ```sh
    python main.py
    ```

2. Open your web browser and navigate to `http://127.0.0.1:5000/`.

## Usage

1. On the home page, select a machine learning model from the dropdown menu.
2. Click the 'Predict' button to train the model and display the RMSE.

## Project Structure

- `main.py`: The main Flask application file.
- `templates/`: Directory containing HTML templates.
- `Datasets/`: Directory containing the dataset file `ethereum.csv`.
- `requirements.txt`: File listing all required Python packages.
