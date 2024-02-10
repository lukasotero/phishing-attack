# phishing-attack
## Overview
This documentation provides an overview of a phishing attack project implemented using Python and Flask. Phishing is a fraudulent attempt to obtain sensitive information such as usernames, passwords, and credit card details by disguising oneself as a trustworthy entity in an electronic communication. The project demonstrates a simple phishing attack targeting a login page, where users unknowingly submit their credentials to the attacker.

## Project Structure
The project consists of the following files and directories:

```
project_root/
│
├── env/                  # Virtual environment directory
│
├── static/               # Directory for static assets
│   └── css/              # Directory for CSS files
│
├── templates/            # Directory for HTML templates
│   └── login.html        # Fake login page template
│
├── app.py                # Main Flask application file
└── credentials.txt       # File to store captured credentials
```

## Implementation Details
The `app.py` file contains the Flask application implementation. It defines routes for handling GET and POST requests to /login. Upon a POST request, the user-entered credentials are captured and stored in a file named credentials.txt. After capturing the credentials, the user is redirected to a legitimate-looking login page (in this case, a fake Facebook login page).

#### templates/login.html
The login.html file in the templates directory serves as the fake login page. It contains HTML and form elements mimicking a legitimate login page, prompting users to enter their username and password.

#### credentials.txt
The credentials.txt file is used to store the captured credentials. Each line in the file contains the username and password submitted by users during the phishing attack.

## Usage
1. Ensure you have Python installed on your system.
2. Create a virtual environment and activate it.
3. Install Flask using pip: pip install flask.
4. Run the Flask application by executing python app.py.
5. Access the phishing login page at ```http://localhost:5000/login```.

## Disclaimer
Important: This project is for educational purposes only. Phishing attacks are illegal and unethical. It is the responsibility of the user to use this code responsibly and only in authorized, legal, and ethical penetration testing or security assessment activities with proper consent. The author and contributors of this project disclaim any liability for any misuse or damage caused by the use of this code.

## Conclusion
This documentation provides an overview of a simple phishing attack project implemented using Python and Flask. It outlines the project structure, implementation details, usage instructions, and a disclaimer regarding the ethical use of the code.