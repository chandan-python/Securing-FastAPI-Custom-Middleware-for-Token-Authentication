# Securing FastAPI: Implementing Token Authentication with Custom Middleware

This project demonstrates how to secure a FastAPI application by implementing token authentication with custom middleware. The application includes user login and signup APIs, along with file upload functionality. The backend is built using FastAPI, and it connects to a MySQL database.

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Running the Application](#running-the-application)
- [Project Structure](#project-structure)
- [Usage](#usage)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)

## Features
- Middleware for token authentication

## Prerequisites

- Python 3.8+
- Git

## Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/yourusername/securing-fastapi-token-auth.git
    cd securing-fastapi-token-auth
    ```

2. **Create and activate a virtual environment:**

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages:**

    ```sh
    pip install -r requirements.txt
    ```


## Configuration

1. **Create a `.env` file in the root directory and add your database credentials:**

    ```env
    SECRET_KEY=
    ALGORITHM=
    ```


## Running the Application



1. **Start the FastAPI application:**

    ```sh
    uvicorn app.main:app --reload
    ```

2. **Access the API documentation:**

    Open your browser and navigate to `http://127.0.0.1:8000/docs` to view the automatically generated API documentation.


## OverView
Authentication and authorization are crucial aspects of modern web applications to ensure that only authorized users can access certain resources. FastAPI, a modern web framework for building APIs with Python, provides convenient tools for implementing authentication mechanisms. In this article, we will explore how to validate access tokens using FastAPI middleware.


#### Understanding Middleware:
Middleware acts as a layer between the client’s request and the server’s response in web applications. It intercepts incoming requests and outgoing responses, allowing developers to execute additional logic or perform modifications before and after handling the request.

In the context of FastAPI, middleware functions are Python callables that receive a request, perform certain actions, and optionally pass the request to the next middleware or route handler. These middleware functions can be used to implement authentication.

#### Conclusion:
By implementing custom middleware in FastAPI, we’ve enhanced web development with token authentication. Middleware intercepts requests, validating access tokens using verify_access_token. This ensures secure access to protected routes. Integrating this approach strengthens authentication and authorization in FastAPI projects, fostering secure web application development.