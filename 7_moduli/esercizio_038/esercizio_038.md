# User Registration Form Exercise

In this exercise, you will create a simple user registration form using Flask. The application will present the user with a form to enter their username, email, and password. Upon submission, the application will return a success message.

## Requirements

1. **Form Page (`/`):** When the user visits the root URL (`/`), they should see a form with fields for username, email, and password. The form should also include a "Submit" button for the user to submit their registration.

2. **Success Page (`/success`):** When the user submits the form, the application should display a success message on a new page. The message should include the username and email that the user entered.

3. **Data Handling:** The form data should be sent from the client to the server when the user submits the form. The server should extract the username and email from the form data to include in the success message.

4. **HTTP Methods:** The form page should be accessible via a GET request to the root URL (`/`). The form should be submitted via a POST request to the `/success` URL.

## Bonus

If you finish the main part of the exercise and want an extra challenge, try adding the following features:

- **Input Validation:** Check that the username, email, and password meet certain requirements (e.g., minimum length, contains certain characters). If the input is invalid, show an error message to the user.

- **Password Hashing:** Instead of sending the password as plain text, hash it on the client side before sending it to the server.

## Example

https://github.com/angelogalantiscuola/IT/blob/main/python/modules_library_packages/examples/flask_request_example.py
