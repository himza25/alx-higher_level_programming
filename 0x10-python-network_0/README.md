# Network Programming with Bash and Python

This repository contains a series of scripts demonstrating various network programming tasks using Bash and Python. The scripts interact with a web server to perform different HTTP requests and handle responses.

## Tasks

### 0. cURL body size

- **Description**: A Bash script that sends a request to a URL and displays the size of the response body in bytes.
- **Usage**: `./0-body_size.sh 0.0.0.0:5000`
- **File**: `0-body_size.sh`

### 1. cURL to the end

- **Description**: Sends a GET request to a URL and displays the body of the response, specifically for a 200 status code.
- **Usage**: `./1-body.sh 0.0.0.0:5000/route_1`
- **File**: `1-body.sh`

### 2. cURL Method

- **Description**: Sends a DELETE request to a URL and displays the body of the response.
- **Usage**: `./2-delete.sh 0.0.0.0:5000/route_3`
- **File**: `2-delete.sh`

### 3. cURL only methods

- **Description**: Displays all HTTP methods a server will accept for a given URL.
- **Usage**: `./3-methods.sh 0.0.0.0:5000/route_4`
- **File**: `3-methods.sh`

### 4. cURL headers

- **Description**: Sends a GET request with a custom header and displays the body of the response.
- **Usage**: `./4-header.sh 0.0.0.0:5000/route_5`
- **File**: `4-header.sh`

### 5. cURL POST parameters

- **Description**: Sends a POST request with specific data and displays the body of the response.
- **Usage**: `./5-post_params.sh 0.0.0.0:5000/route_6`
- **File**: `5-post_params.sh`

### 6. Find a peak

- **Description**: Python function to find a peak in a list of unsorted integers.
- **Usage**: `./6-main.py`
- **Files**: `6-peak.py`, `6-peak.txt`

### 7. Only status code

- **Description**: Sends a request to a URL and displays only the status code of the response.
- **Usage**: `./100-status_code.sh 0.0.0.0:5000`
- **File**: `100-status_code.sh`

### 8. cURL a JSON file

- **Description**: Sends a JSON POST request with the contents of a file and displays the body of the response.
- **Usage**: `./101-post_json.sh 0.0.0.0:5000/route_json my_json_0`
- **File**: `101-post_json.sh`

### 9. Catch me if you can!

- **Description**: Makes a request to a specific URL that causes the server to respond with a specific message.
- **Usage**: `./102-catch_me.sh`
- **File**: `102-catch_me.sh`

## Testing

The scripts are tested against a web server running on port 5000. Ensure that the server is configured correctly to respond as expected to each script.

## Author

Samari Hamza
