
# SuperKart Sales Forecasting and Deployment

This project focuses on building and deploying a robust machine learning solution for SuperKart, a retail chain, to accurately forecast sales revenue for its outlets. The solution leverages historical sales data to predict future sales, optimizing inventory management and informing regional sales strategies. The deployed system consists of a Flask API for predictions and a Streamlit application for an interactive user interface, both containerized using Docker and deployed with GitHub Codespaces.

## Project Structure

```
. # Root directory of the repository
├── backend_files/
│   ├── app.py                     # Flask application for predictions
│   ├── Dockerfile                 # Dockerfile for the Flask backend
│   ├── requirements.txt           # Python dependencies for the backend
│   └── superkart_model.joblib     # Serialized trained ML model pipeline
├── frontend_files/
│   ├── streamlit_app.py           # Streamlit application for user interface
│   ├── Dockerfile                 # Dockerfile for the Streamlit frontend
│   └── requirements.txt           # Python dependencies for the frontend
├── docker-compose.yml             # Defines multi-container Docker application
└── README.md                      # Project overview and deployment guide (this file)
```

## Deployment with GitHub Codespaces

This project is set up for easy deployment using GitHub Codespaces. The `docker-compose.yml` file orchestrates two services:
- **`backend`**: A Flask API that serves machine learning predictions.
- **`frontend`**: A Streamlit application that provides an interactive user interface to interact with the backend.

### Steps to Deploy:

1.  **Fork/Clone the Repository**: Ensure you have this repository cloned or forked to your GitHub account.

2.  **Open with Codespaces**: In your GitHub repository, click on the green `Code` button and select `Open with Codespaces`.

    *   **Note**: If you're creating a new Codespace, it might take a few minutes for the environment to provision and the Docker images to build.

3.  **Automatic Container Start**: GitHub Codespaces will automatically detect the `docker-compose.yml` file and start building and running your Docker containers for the backend (Flask API) and frontend (Streamlit app).

4.  **Access the Applications (Port Forwarding)**:
    Once the containers are running, GitHub Codespaces will automatically forward the ports defined in your `docker-compose.yml`:
    *   **Flask Backend (Port 7860)**: You should see a notification or a 'Ports' tab in your Codespace interface for port `7860`. This is your prediction API.
    *   **Streamlit Frontend (Port 8501)**: Similarly, you'll find port `8501` forwarded. Click on the forwarded port for Streamlit to open your interactive sales predictor application in a new browser tab.

### Using the Deployed Application:

#### Streamlit Frontend:

*   **Interactive Predictions**: The Streamlit app provides an intuitive form where you can input product and store details. Click 'Predict Sales' to get an immediate prediction from the Flask backend.
*   **Batch Predictions**: You can also upload a CSV file with multiple entries for batch predictions. The app will display the predictions and allow you to download the results.

#### Flask Backend (API):

You can interact directly with the Flask API using tools like `curl`, `Postman`, or the `requests` library in Python (as demonstrated in the original notebook).

*   **Base URL**: The base URL for your API will be the forwarded address for port `7860` from your Codespace (e.g., `https://your-codespace-name-7860.app.github.dev`).
*   **Single Prediction**: Send a `POST` request to `/v1/predict` with a JSON payload of features.
    *   Example `curl` command (replace `YOUR_API_URL`):
        ```bash
        curl -X POST -H "Content-Type: application/json" \
             -d '{"Product_Weight": 12.66, "Product_Sugar_Content": "Low Sugar", "Product_Allocated_Area": 0.027, "Product_MRP": 117.08, "Store_Id": "OUT004", "Store_Establishment_Year": 2009, "Store_Size": "Medium", "Store_Location_City_Type": "Tier 2", "Store_Type": "Supermarket Type2", "Product_Id": "FD0000"}' \
             YOUR_API_URL/v1/predict
        ```
*   **Batch Prediction**: Send a `POST` request to `/v1/predictbatch` with a CSV file attached (using `multipart/form-data`).
    *   Example `curl` command (replace `YOUR_API_URL` and `path/to/your/batch_data.csv`):
        ```bash
        curl -X POST -F "file=@path/to/your/batch_data.csv" \
             YOUR_API_URL/v1/predictbatch
        ```

## Conclusion

This setup allows for a robust and reproducible deployment of the SuperKart Sales Forecasting model, enabling both interactive exploration via Streamlit and programmatic access through a Flask API.
