# House Price Prediction uisng Machine Learning

## Overview

This project implements a house price prediction model using linear regression. The model predicts house prices based on features such as location, total square feet, number of bathrooms, and the number of bedrooms (BHK). The backend is built with Flask, and a simple HTML frontend is used for user interaction.

## Features

- **Linear Regression Model:** Utilizes linear regression to predict house prices.
- **Flask Backend:** Handles API requests and serves the prediction model.
- **HTML Form:** Provides a user interface for inputting house details and receiving predictions.

## Technologies

- **Python**: Programming language used.
- **Flask**: Web framework for handling HTTP requests.
- **scikit-learn**: Library for machine learning, used for training the linear regression model.
- **HTML/CSS/JavaScript**: Frontend technologies for creating the user interface.

## Installation

### Prerequisites

Ensure you have Python and pip installed on your system. You will also need the following Python libraries:

- Flask
- scikit-learn
- pandas
- numpy
- matplotlib
- pickle


### Clone the Repository

Clone this repository to your local machine:

```bash
git clone https://github.com/2003HARSH/House-Price-Prediction-using-Machine-Learning
cd house-price-prediction
```
You can install the required libraries using pip:

```bash
pip install -r requirements.txt
```

## Running the Application

### Start the Flask Server

Run the Flask server with the following command:

```bash
python app.py
```

The server will start and listen on `http://127.0.0.1:4000/` .

### Using the HTML Form

After the form is open enter the required values to get the output.

## API Endpoint

### POST /predict

**Description:** Receives house details and returns the predicted price.

**Request Body:**

```json
{
    "location": "near banglore",
    "total_sqft": 1500,
    "bath": 2,
    "bhk": 3
}
```

**Response:**

```json
{
    "predicted_price": 550000.00
}
```

## Project Structure

- `app.py`: Flask backend script.
- `model.pkl`: Serialized linear regression model.
- `index.html`: Frontend HTML form for user input.
- `README.md`: This file.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


## Contact

For any questions or issues, please contact [harshnkgupta@gmail.com](mailto:harshnkgupta@gmail.com).

