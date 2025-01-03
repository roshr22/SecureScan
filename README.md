# SecureScan

## Overview
This tool is designed to audit the security of websites by checking for common vulnerabilities and security misconfigurations. It performs essential checks, including URL validation, HTTP status checks, and port scanning for potential open ports. It also verifies SSL/TLS certificate validity to ensure a secure connection.

## Features

### 1. **URL Validation**
The tool validates the input URL to ensure it follows a correct format.

- Checks for valid URL structure using the `validators` library.
- Supports both `http` and `https` protocols.

### 2. **HTTP Status Code Check**
The tool checks if the website is reachable and returns a valid HTTP status code.

- Verifies that the status code is in the range 200 to 399.
- Flags URLs that are unreachable or return unexpected status codes.

### 3. **Port Scanning**
Scans for open ports on the target website. It checks a set of commonly used ports and reports which ones are open.

- Scans the following common ports: 20, 21, 22, 23, 25, 53, 80, 110, 123, 143, 161, 194, 443, 465, 993, 995, 3306, 3389, 5900, 8080.
- Optionally scans a specified port if provided.

### 4. **SSL/TLS Certificate Validation**
The tool checks the SSL/TLS certificate of the website to ensure it is valid and secure.

- Verifies the certificate’s status during connection setup.
- Flags expired or invalid certificates.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/website-security-audit-tool.git
    ```
2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the tool with the desired URL:
    ```bash
    python security_audit.py
    ```

2. Enter the URL you wish to scan when prompted.

### Example
```code
Enter URL: https://example.com
```
## Reporting
The tool outputs results in the terminal, showing whether the URL is reachable, which ports are open, and any SSL certificate issues.

### Example Output
```code
Enter URL: https://example.com
Port Scanning for the most commonly used ports...
Open ports: 80, 443
```
## Contributing
Feel free to fork the project and submit pull requests for improvements, bug fixes, or new features.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
