from flask import Flask, render_template, request
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error

app = Flask(__name__)

# Load the data
try:
    crypto_data = pd.read_csv('Datasets/ethereum.csv', parse_dates=['date'])
    if 'price' in crypto_data.columns:
        # Remove non-numeric characters from 'price' column and convert to float
       crypto_data['price'] = crypto_data['price'].replace(r'[^\d.]', '', regex=True).astype(float)
except FileNotFoundError:
    print("Error: CSV file not found.")
except Exception as e:
    print(f"Error loading data: {e}")

X = crypto_data.drop(['price', 'Currency'], axis=1)  # Drop 'Currency' column if not needed
y = crypto_data['price']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    model_type = request.form['model']
    try:
        if model_type == "Random Forest":
            model = RandomForestRegressor(n_estimators=100, random_state=42)
        elif model_type == "KNN":
            model = KNeighborsRegressor(n_neighbors=5)
        else:
            return "Invalid model selected."
        
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        rmse = mean_squared_error(y_test, y_pred, squared=False)
        return f"RMSE using {model_type}: {rmse:.4f}"
    except Exception as e:
        return f"Error occurred during prediction: {e}"

if __name__ == '__main__':
    app.run(debug=True)
