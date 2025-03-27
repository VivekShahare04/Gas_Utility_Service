# Gas Utility Service

## Project Overview
The **Gas Utility Service** is a Django-based web application designed to manage service requests for a gas utility company. It allows customers to create and track service requests, while support representatives can manage and resolve these requests.

---

## Project Structure

Below is the structure of the Django application:

![Project Structure](path/to/your/image.png)

Replace `path/to/your/image.png` with the actual relative path to the image file in your repository. For example, if the image is saved in the root directory of your project, you can use:

```markdown
![Project Structure](project_structure.png)
```

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
Authentication: Django's built-in authentication system


