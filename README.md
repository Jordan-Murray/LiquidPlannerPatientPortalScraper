# LiquidPlanner Patient Portal Scraper

This project is a Python-based web scraper that logs into LiquidPlanner, searches for rows in tables related to "Patient Portal," and saves the data to an Excel file with auto-adjusted columns. The scraper handles authentication using CSRF tokens and maintains session cookies.

## Features

- Logs into the LiquidPlanner site securely
- Searches for rows in tables related to "Patient Portal"
- Saves the relevant data into an Excel file (`.xlsx`), with auto-adjusted columns for better readability
- Uses environment variables for credentials, ensuring security when sharing the project

## Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.x**
- **pip** (Python package installer)

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/Jordan-Murray/liquidplanner-patient-portal-scraper.git
    cd liquidplanner-patient-portal-scraper
    ```

2. Install the required Python packages:

    ```bash
    pip install -r requirements.txt
    ```

3. Set up your environment variables by creating a `.env` file in the project root directory with the following content:

    ```plaintext
    # .env file
    LIQUIDPLANNER_EMAIL={{your email}}
    LIQUIDPLANNER_PASSWORD={{your password}}
    ```

4. Make sure the `.env` file is not tracked by Git by adding it to `.gitignore`:

    ```plaintext
    .env
    ```

## Running the Scraper

1. Ensure that the `.env` file contains your correct LiquidPlanner credentials.

2. Run the Python script:

    ```bash
    python scraper.py
    ```

3. The scraper will log into LiquidPlanner, search for "Patient Portal" rows, and save the data into an Excel file (`patient_portal_data.xlsx`) in the same directory.

## Project Structure

