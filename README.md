# NotifyNow

NotifyNow is a Django-based application designed to send reminders to users via email and SMS. Users can create reminders, set their schedule, and choose their preferred delivery method. This project is ideal for anyone looking to implement a notification system for timely alerts and reminders.

## Features

- User authentication and management
- Create, update, and delete reminders
- Schedule reminders with specific date and time
- Choose between email and SMS delivery methods
- View list of all reminders
- Secure and user-friendly interface

## Technologies Used

- Python
- Django
- MySQL
- Celery (for background tasks)
- Redis (as a message broker for Celery)
- SMTP (for sending emails)
- Twilio (for sending SMS)

## Getting Started

### Prerequisites

Make sure you have the following installed on your system:

- Python 3.x
- MySQL
- Redis
- Virtualenv

### Installation

1. **Clone the repository:**
    ```sh
    git clone https://github.com/your-username/NotifyNow.git
    cd NotifyNow
    ```

2. **Create a virtual environment and activate it:**
    ```sh
    virtualenv venv
    source venv/bin/activate
    ```

3. **Install the required packages:**
    ```sh
    pip install -r requirements.txt
    ```

4. **Set up the MySQL database:**

    - Create a database named `notifynow_db` in MySQL.
    - Update the `DATABASES` configuration in `NotifyNow/settings.py` with your MySQL credentials.

5. **Apply migrations:**
    ```sh
    python manage.py makemigrations
    python manage.py migrate
    ```

6. **Create a superuser:**
    ```sh
    python manage.py createsuperuser
    ```

7. **Run the development server:**
    ```sh
    python manage.py runserver
    ```

8. **Run the Celery worker:**
    ```sh
    celery -A NotifyNow worker --loglevel=info
    ```

### Configuration

- **Email Settings:** Update the email configuration in `NotifyNow/settings.py` to use your email provider.
- **SMS Settings:** Add your Twilio credentials in `NotifyNow/settings.py`.

### Usage

1. **Sign Up:** Create a new account or log in with your superuser account.
2. **Create Reminders:** Navigate to the "Create Reminder" page to add a new reminder.
3. **View Reminders:** Check your reminders on the "Reminders List" page.
4. **Manage Reminders:** Edit or delete reminders as needed.

## Folder Structure

