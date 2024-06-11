# Django Project with Google reCAPTCHA

This is a Django project that includes Google reCAPTCHA for forms to prevent spam and automated abuse.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Environment Variables](#environment-variables)
- [Running the Project](#running-the-project)
- [Contributing](#contributing)
- [License](#license)

## Features

- User registration and login
- Form with Google reCAPTCHA v2
- Secure handling of sensitive data with environment variables
- Responsive and modern UI with glassmorphism effects

## Installation

### Prerequisites

- Python 3.x
- Django 3.x or later
- pip (Python package installer)

### Steps

1. Clone the repository

2. Create a virtual environment and activate it:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Set up the environment variables:

    Create a `.env` file in the root directory of your project and add the following:

    ```env
    SECRET_KEY=your-secret-key
    RECAPTCHA_PUBLIC_KEY=your-site-key
    RECAPTCHA_PRIVATE_KEY=your-secret-key
    ```

    Replace `your-secret-key` and `your-site-key` with the actual keys you obtained from the Google reCAPTCHA admin console.

5. Apply migrations:

    ```bash
    python manage.py migrate
    ```

## Usage

1. Run the development server:

    ```bash
    python manage.py runserver
    ```

2. Open your web browser and go to `http://127.0.0.1:8000/` to see the project in action.

## Environment Variables

The following environment variables need to be set in your `.env` file:

- `SECRET_KEY`: The secret key for your Django project.
- `RECAPTCHA_PUBLIC_KEY`: The site key for Google reCAPTCHA.
- `RECAPTCHA_PRIVATE_KEY`: The secret key for Google reCAPTCHA.

## Running the Project

To run the project locally, use the following command:

```bash
python manage.py runserver

