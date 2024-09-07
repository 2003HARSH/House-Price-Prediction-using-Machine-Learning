# House Price Prediction uisng Machine Learning

## Overview

This project implements a house price prediction model using linear regression, predicting prices based on features like location, total square feet, number of bathrooms, and bedrooms (BHK), with a Flask backend and a simple HTML frontend for user interaction. Building on the initial version, I've integrated a CI/CD pipeline using GitHub Actions for automated testing and deployment, added unit test cases with `pytest` to ensure code quality, and automated Docker containerization for consistent deployments across environments. These enhancements significantly improve the application's robustness, maintainability, and scalability, making it production-ready.

![https://github.com/2003HARSH/House-Price-Prediction-using-Machine-Learning/blob/main/artifacts/1.png](https://github.com/2003HARSH/House-Price-Prediction-using-Machine-Learning/blob/main/artifacts/1.png)
![https://github.com/2003HARSH/House-Price-Prediction-using-Machine-Learning/blob/main/artifacts/5.jpeg](https://github.com/2003HARSH/House-Price-Prediction-using-Machine-Learning/blob/main/artifacts/5.jpeg)
![https://github.com/2003HARSH/House-Price-Prediction-using-Machine-Learning/blob/main/artifacts/6.jpeg](https://github.com/2003HARSH/House-Price-Prediction-using-Machine-Learning/blob/main/artifacts/6.jpeg)
![https://github.com/2003HARSH/House-Price-Prediction-using-Machine-Learning/blob/main/artifacts/4.jpeg](https://github.com/2003HARSH/House-Price-Prediction-using-Machine-Learning/blob/main/artifacts/4.jpeg)


## Features

- **Linear Regression Model**: Utilizes linear regression to predict house prices.
- **Flask Backend**: Handles API requests and serves the prediction model.
- **HTML Form**: Provides a user interface for inputting house details and receiving predictions.
- **Experiment Tracking**: Integrated MLflow for tracking experiments, providing deeper insights into model performance.
- **Hyperparameter Tuning**: Optimized model performance using GridSearchCV and Hyperopt.
- **Interactive Visualizations**: Leveraged MLflow's web interface for visualizing and comparing experiment results.
- **CI/CD Pipeline**: Implemented using GitHub Actions to automate testing and deployment.
- **Unit Tests**: Developed test cases using `pytest` to ensure application reliability.
- **Automated Docker Containerization**: Dockerized the application for easy deployment.

## Technologies

- **Python**: Core programming language.
- **Flask**: Web framework for handling HTTP requests.
- **scikit-learn**: Machine learning library used for model training.
- **HTML/CSS/JavaScript**: Frontend technologies for creating a user interface.
- **MLflow**: Tool for experiment tracking.
- **GitHub Actions**: CI/CD for automated testing and deployment.
- **Docker**: Containerization tool for packaging the application.

## Installation

### Prerequisites

Ensure you have Python and pip installed on your system. You will also need the following Python libraries:

- Flask
- scikit-learn
- pandas
- numpy
- matplotlib
- pickle
- mlflow


### Clone the Repository

Clone this repository to your local machine:

```bash
git clone https://github.com/2003HARSH/House-Price-Prediction-using-Machine-Learning
cd House-Price-Prediction-using-Machine-Learning
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

The server will start and listen on `http://127.0.0.1:5000/` .

### Using the HTML Form

After the form is open enter the required values to get the output.

---

## **Installation using Docker**

1. **Pull the Docker Image:**

   ```sh
   docker pull 2003harsh/house_price_prediction
   ```

2. **Run the Docker Container:**

   ```sh
   docker run -p 5000:5000 2003harsh/house_price_prediction
   ```

3. **Access the Application:**

   Open your web browser and navigate to `http://localhost:5000` to use the app.

---

# Plots
![https://github.com/2003HARSH/House-Price-Prediction-using-Machine-Learning/blob/main/artifacts/plots/1.png](https://github.com/2003HARSH/House-Price-Prediction-using-Machine-Learning/blob/main/artifacts/plots/1.png)
![https://github.com/2003HARSH/House-Price-Prediction-using-Machine-Learning/blob/main/artifacts/plots/2.png](https://github.com/2003HARSH/House-Price-Prediction-using-Machine-Learning/blob/main/artifacts/plots/2.png)
![https://github.com/2003HARSH/House-Price-Prediction-using-Machine-Learning/blob/main/artifacts/plots/3.png](https://github.com/2003HARSH/House-Price-Prediction-using-Machine-Learning/blob/main/artifacts/plots/3.png)
![https://github.com/2003HARSH/House-Price-Prediction-using-Machine-Learning/blob/main/artifacts/plots/4.png](https://github.com/2003HARSH/House-Price-Prediction-using-Machine-Learning/blob/main/artifacts/plots/4.png)
![https://github.com/2003HARSH/House-Price-Prediction-using-Machine-Learning/blob/main/artifacts/plots/6.png](https://github.com/2003HARSH/House-Price-Prediction-using-Machine-Learning/blob/main/artifacts/plots/6.png)
![https://github.com/2003HARSH/House-Price-Prediction-using-Machine-Learning/blob/main/artifacts/plots/7.png](https://github.com/2003HARSH/House-Price-Prediction-using-Machine-Learning/blob/main/artifacts/plots/7.png)
![https://github.com/2003HARSH/House-Price-Prediction-using-Machine-Learning/blob/main/artifacts/plots/8.png](https://github.com/2003HARSH/House-Price-Prediction-using-Machine-Learning/blob/main/artifacts/plots/8.png)
![https://github.com/2003HARSH/House-Price-Prediction-using-Machine-Learning/blob/main/artifacts/plots/9.png](https://github.com/2003HARSH/House-Price-Prediction-using-Machine-Learning/blob/main/artifacts/plots/9.png)

---

## API Endpoint

### POST /predict

**Description:** Receives house details and returns the predicted price.

**Request Body:**

```json
{
    "location": "Sarjapur",
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

