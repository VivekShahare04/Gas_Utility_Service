# Gas Utility Service

## Project Overview
The **Gas Utility Service** is a Django-based web application designed to manage service requests for a gas utility company. It allows customers to create and track service requests, while support representatives can manage and resolve these requests.

---

## Project Structure

Below is the structure of the Django application:

gasutilityservice/                # Root project directory
├── config/                      # Main Django project configuration
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py                  # Main URL routing
│   └── wsgi.py
│
├── apps/                        # All Django applications
│   ├── accounts/                # User authentication app
│   │   ├── migrations/
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── forms.py            # Registration/login forms
│   │   ├── models.py           # Custom User model
│   │   ├── urls.py             # Account-related URLs
│   │   └── views.py            # Authentication views
│   │
│   ├── service_requests/        # Customer service requests app
│   │   ├── migrations/
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── forms.py            # Service request forms
│   │   ├── models.py           # ServiceRequest model
│   │   ├── urls.py             # Request-related URLs
│   │   └── views.py            # Request handling views
│   │
│   └── customer_support/       # Support representative tools
│       ├── migrations/
│       ├── __init__.py
│       ├── admin.py
│       ├── apps.py
│       ├── forms.py            # Support ticket forms
│       ├── models.py           # SupportTicket model
│       ├── urls.py             # Support-related URLs
│       └── views.py            # Support dashboard views
│
├── templates/                  # Base templates directory
│   ├── base.html               # Main template
│   ├── accounts/
│   │   ├── landing.html        # Account landing page
│   │   ├── login.html          # Login form
│   │   └── register.html       # Registration form
│   ├── service_requests/
│   │   ├── request_create.html # New request form
│   │   ├── request_detail.html # Request details
│   │   ├── request_list.html   # All requests view
│   │   └── request_update.html # Request update form
│   └── customer_support/
│       ├── dashboard.html      # Support dashboard
│       ├── request_detail.html # Support view of request
│       └── ticket_update.html # Ticket management
│
├── static/                     # Static files
│   ├── css/
│   │   └── style.css           # Custom CSS
│   └── js/                     # (Optional JavaScript files)
│
├── media/                      # User-uploaded files (created automatically)
│   └── service_request_attachments/  # Request attachments
│
├── manage.py                   # Django management script
└── requirements.txt            # Python dependencies

---

## Workflow

### 1. **User Authentication**
- Users can register and log in using the `accounts` app.
- After logging in, users are redirected to their respective dashboards based on their roles (e.g., customer or support representative).

### 2. **Service Requests**
- Customers can create new service requests using the `service_requests` app.
- Each service request includes details such as type, priority, description, and optional attachments.
- Customers can view the status of their requests and update them if necessary.

### 3. **Customer Support**
- Support representatives can view all service requests and update their statuses (e.g., "In Progress," "Resolved").
- They can also add resolution notes and mark requests as resolved.

### 4. **Admin Management**
- Admin users can manage users, service requests, and other data through the Django admin interface.

---

## How to Run the Project

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/Gas_Utility_Service.git
   cd Gas_Utility_Service
   ```

2. **Create and Activate Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply Migrations**:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create Superuser**:
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the Server**:
   ```bash
   python manage.py runserver
   ```

**Access the Application: Open your browser and navigate to**:

Admin Panel: http://127.<vscode_annotation details='%5B%7B%22title%22%3A%22hardcoded-credentials%22%2C%22description%22%3A%22Embedding%20credentials%20in%20source%20code%20risks%20unauthorized%20access%22%7D%5D'>0</vscode_annotation>.0.1:8000/admin/
Login Page: http://127.0.0.1:8000/accounts/login/


**Features**
User Authentication: Login, registration, and role-based access.
Service Request Management: Create, view, update, and resolve service requests.
Customer Support Dashboard: Manage and resolve customer issues.
Admin Panel: Full control over users and data.

**Technologies Used**
Backend: Django
Frontend: HTML, CSS, Bootstrap
Database: SQLite
Authentication: Django's built-in authentication system


