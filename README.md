# URL Shortener API

A lightweight URL shortening service built using Flask. This project allows users to shorten long URLs into compact codes, access the original URLs via redirection, and view analytics including click counts and timestamps.

---

## Project Overview

This application provides a simple RESTful API for:
- Generating a shortened URL from a long one
- Redirecting users using the short code
- Retrieving analytics (clicks, timestamp, and original URL)

All operations are handled in memory using basic Python data structures, without an external database.

---

## Folder Structure

The project is divided into two main folders:
- `app/` contains the core application logic (API routes, models, utilities)
- `tests/` includes test cases written using Pytest

There is also a requirements file and this README file at the root.

---

## Key Features

- Accepts long URLs via a POST request and returns a shortened version
- Supports redirecting using short codes
- Tracks the number of times each short URL is accessed
- Returns metadata like creation timestamp and original URL via an analytics endpoint
- Includes unit tests for API functionality and error handling

---

## API Endpoints

1. Shorten URL  
   Accepts a long URL in JSON format and returns a shortened code and URL.

2. Redirect  
   Redirects to the original long URL when the short code is accessed. Returns 404 if the code does not exist.

3. Stats  
   Returns JSON with the total number of redirects, the original URL, and the timestamp of when the short URL was created.

---

## How It Works

- URLs are validated before being accepted
- A 6-character alphanumeric short code is generated for each unique URL
- All data (mappings, click counts, timestamps) is stored in memory
- Redirect count is incremented on each access
- Timestamp is attached at the time of creation

---

## Testing

The application is tested using Pytest:
- The health check route is tested for availability
- The URL shortening and redirect functionality is validated
- Stats endpoint is tested to ensure click tracking and metadata retrieval
- Error cases (invalid URL, non-existent short codes) are also covered

---
## Use of AI Tools

During the development of this project, AI tools were used to assist in certain areas:

- **ChatGPT (OpenAI)** was used to:
  - Review Flask routing patterns and test structure
  - Help design efficient short code generation logic
  - Suggest error handling best practices and edge case validation

- **Google Gemini** was consulted to:
  - Cross-check API design and response formats
  - Simplify explanations of test coverage approaches
  - Compare in-memory data storage alternatives for small-scale apps

All AI-generated suggestions were reviewed and modified as needed to ensure quality, accuracy, and relevance. No code was directly pasted without validation or adaptation.

---

## Running Locally

To run the application locally, ensure you have Python installed, install the dependencies, and run the Flask app. The API will be available at `http://localhost:5000`.

You can test the API using tools like Postman or cURL, or by writing test cases with Pytest.

---

## License

This project is open for educational and personal use.
