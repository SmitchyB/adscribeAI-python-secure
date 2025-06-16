# AdScribe.AI - Python/Flask (Secure Version)

This repository contains the Python/Flask stack version of the AdScribe.AI application. This version has been refactored to be secure and serves as a test case for a university research project evaluating the effectiveness of secure coding practices and SAST (Static Analysis Security Testing) tools.

## Application Purpose

AdScribe.AI is a simple marketing tool that uses the OpenAI API to generate compelling product descriptions based on a product name and user-provided keywords.

## Research Context: The Security Fix

The purpose of this repository is to demonstrate the correct, secure method for handling secrets in a Python application.

The vulnerability present in the "unsecure" version (a hardcoded API key) has been mitigated by using environment variables. The secret key is now loaded from a `.env` file at runtime using the `python-dotenv` library and is never exposed in the source code. The `.env` file is explicitly ignored by `.gitignore` to prevent it from ever being committed to version control. This build is used to verify that security scanning tools no longer detect the hardcoded secret vulnerability.

## How to Run This Application

This is a standard Python application with a React frontend and a Python/Flask backend.

### Prerequisites
* Python 3 installed.
* An active OpenAI API key.

### Instructions

1.  **Clone the repository:**
    ```bash
    git clone <your-repo-url>
    ```

2.  **Create the `.env` file (Backend):**
    * Navigate to the `backend/` directory.
    * Create a new file and name it exactly `.env`.
    * Inside the `.env` file, add the following line, replacing the placeholder with your actual OpenAI API key:
        ```
        OPENAI_API_KEY='sk-YourActualKeyHere'
        ```

3.  **Set up the Backend (Python):**
    * Navigate to the `backend/` directory.
    * Create and activate a virtual environment:
        ```bash
        # Create the virtual environment
        python -m venv venv
        # Activate on Windows (PowerShell)
        .\venv\Scripts\Activate.ps1
        # Activate on Mac/Linux
        source venv/bin/activate
        ```
    * Create a `requirements.txt` file for your dependencies:
        ```bash
        pip freeze > requirements.txt
        ```
    * Install the Python dependencies:
        ```bash
        pip install -r requirements.txt
        ```

4.  **Set up the Frontend (React):**
    * In a second terminal, navigate to the `frontend/` folder.
    * Install the Node.js dependencies:
        ```bash
        npm install
        ```

5.  **Run the Application:**
    * In your backend terminal (with the venv active), navigate to the project root folder and run:
        ```bash
        flask --app backend/server run
        ```
        The backend will run on `http://localhost:5001`.
    * In your frontend terminal, run:
        ```bash
        npm start
        ```
        The application will open in your browser at `http://localhost:3000`.
