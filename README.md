# Valoros - Finances Manager

Valoros is a Django-based web application designed to help users manage their basic finances efficiently. Initially created as a full-stack learning project, the application is currently in early development.

---

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Development Log](#development-log)
- [Contributing](#contributing)
- [License](#license)

---

## Features

### Functional Features

- **User Authentication**
  - **Registration:**
    - Users register with a username, email, and password.
    - Username must be alphanumeric.
    - Email must be valid.
    - Password must be at least 6 characters long.
    - Registration data is stored in a PostgreSQL database as an unactivated account.
  - **Email Confirmation:**
    - An activation link is sent to the registered email.
    - Clicking the link activates the account.
  - **Login/Logout:**
    - Once activated, users can log in and log out as needed.

- **Responsive Design**
  - Real-time Ajax validation checks for username and email availability.
  - Instant feedback messages for actions like registration success or invalid credentials.

- **Main Page**
  - Features a sidebar (with upcoming tools) and provides logout functionality.

### Upcoming Features

- **Preference Management:** Enable users to manage settings such as currency and account configurations.
- **CRUD Operations:** Implement create, read, update, and delete functionality for managing expenses and income.
- **Ajax Search:** Integrate an asynchronous search system to dynamically display results.
- **Date Template Filters:** Develop date filters for daily, monthly, and yearly financial tracking.
- **Income Comparison:** Compare income and expenses over recent months.
- **Data Visualization:** Use Chart.JS to present finance graphs.
- **Data Export:** Allow financial data to be exported in PDF, Excel, CSV, and XLS formats.
- **Enhanced UI:** Improve the visual design and add a dark mode option.
- **Password Reset:** Implement user password reset functionality.
- **Multithreading:** Enhance performance during user registration using multithreading.

---

## Technologies Used

- **Backend:** Python, Django
- **Frontend:** HTML, CSS, JavaScript
- **Database:** PostgreSQL
- **Authentication:** Django's built-in authentication system
- **Templates:** Django Templates
- **Static Files:** Managed using Django's static files framework

---

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/valoros.git
   cd valoros
   ```

2. **Create a Virtual Environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Apply Migrations:**

   ```bash
   python manage.py migrate
   ```

5. **Create a Superuser:**

   ```bash
   python manage.py createsuperuser
   ```

6. **Run the Development Server:**

   ```bash
   python manage.py runserver
   ```

7. **Access the Application:**

   Open your web browser and navigate to [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

---

## Usage

- **Register:** Create a new account with your email and password.
- **Activate:** Activate your account via the link sent to your email.
- **Login:** Sign in using your credentials.

---

## Project Structure

```plaintext
valoros/
├── authentication/
│   ├── migrations/
│   ├── templates/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── expenses/
│   ├── migrations/
│   ├── templates/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── expenseswebsite/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── userpreferences/
│   ├── migrations/
│   ├── templates/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── templates/
│   ├── base.html
│   ├── base_auth.html
│   └── ...
├── staticfiles/
│   ├── css/
│   ├── js/
│   └── ...
├── manage.py
└── requirements.txt
```

---

## Development Log

The application is in its early stages. Current features include user authentication, responsive design, and a basic main page. Future updates will add more comprehensive financial management tools and UI enhancements.

---

## Project Images
![image](https://github.com/user-attachments/assets/816ecc2a-d5d0-4072-8a71-ee314bf0512e)

![image](https://github.com/user-attachments/assets/e4eacbf3-c706-4d70-84ea-c592245eb990)

![image](https://github.com/user-attachments/assets/f655078a-5239-455a-84f6-e0d1a38bb73e)

![InvalideCredentials](https://github.com/user-attachments/assets/deaa9573-110a-4b24-b224-b4e7f65cfbbf)

![MainPage](https://github.com/user-attachments/assets/a027e5da-f51c-4742-ad47-9514093da235)

![Logout](https://github.com/user-attachments/assets/b77a94bc-e834-4761-af0f-022a4eb6f2b5)

## Contributing

Contributions are welcome! Please fork the repository, make your changes, and submit a pull request.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
