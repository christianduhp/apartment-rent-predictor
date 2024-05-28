
# Apartment Rental Price Prediction Dashboard

This project is a web-based dashboard for predicting apartment rental prices in São Paulo using a machine learning model. The dashboard is built using Dash and Plotly, and it utilizes a RandomForestRegressor model to provide accurate rental price estimates based on various apartment features.

## Table of Contents

- [Features](#features)
- [Setup Instructions](#setup-instructions)
- [Usage](#usage)
- [Screenshots](#screenshots)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Interactive Map**: Visualize apartment locations and rental prices on a map.
- **Prediction Form**: Input apartment features to get a rental price estimate.
- **Detailed Explanation**: Understand how the prediction model works and what factors influence the rental price.
- **Responsive Design**: Works on both desktop and mobile devices.

## Setup Instructions

1. **Clone the repository**:
   ```sh
   git clone https://github.com/christianduhp/apartment-rent-predictor
   cd apartment-rent-predictor
   ```

2. **Create and activate a virtual environment**:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install dependencies**:
   ```sh
   pip install -r requirements.txt
   ```

4. **Set up environment variables**:
   Create a `.env` file in the root directory and add your Mapbox access token:
   ```env
   MAPBOX_ACCESS_TOKEN=your_mapbox_token
   ```

5. **Run the app**:
   ```sh
   python app.py
   ```

## Usage

Once the app is running, open your web browser and navigate to `http://localhost:8080`. You will see the dashboard where you can interact with the map and input apartment features to get rental price estimates.

## Screenshots

![image](https://github.com/christianduhp/christianduhp/assets/85292359/8794711e-9355-4768-82ba-a7893ca60696)

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the MIT License.
