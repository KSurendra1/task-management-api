## Task Management API - Django REST Framework
Django
DRF
Python

A robust Task Management API built with Django REST Framework that allows users to create tasks, assign them to users, and retrieve tasks assigned to specific users.

## Features
User Management: Custom user model with extended fields

Task Operations: Create, assign, and manage tasks

RESTful API: Fully compliant with REST standards

Admin Interface: Powerful Django admin dashboard

Authentication: Session and optional JWT authentication

## Requirements
Python 3.8+

Django 3.2+

Django REST Framework 3.12+

## Installation
1. Clone the repository
bash
Copy
git clone https://github.com/ksurendra1/task-management-api.git
cd task-management-api
2. Create and activate virtual environment
bash
Copy
python -m venv venv
# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate
3. Install dependencies
bash
Copy
pip install -r requirements.txt
4. Configure database
bash
Copy
python manage.py migrate
5. Create superuser
bash
Copy
python manage.py createsuperuser
6. Run development server
bash
Copy
python manage.py runserver
API Endpoints
Endpoint	Method	Description	Authentication Required
/api/tasks/create/	POST	Create new task	Yes
/api/tasks/{id}/assign/	PUT	Assign task to users	Yes
/api/tasks/user/{user_id}/	GET	Get tasks for specific user	Yes
/api/auth/login/	POST	Login (for session auth)	No
/api/auth/logout/	POST	Logout	Yes
Sample Requests
Create Task
bash
Copy
curl -X POST http://localhost:8000/api/tasks/create/ \
  -H "Content-Type: application/json" \
  -d '{"name": "Complete project", "description": "Finish API documentation", "task_type": "WORK"}'
Assign Task to Users
bash
Copy
curl -X PUT http://localhost:8000/api/tasks/1/assign/ \
  -H "Content-Type: application/json" \
  -d '{"user_ids": [1, 2]}'
Get User Tasks
bash
Copy
curl http://localhost:8000/api/tasks/user/1/
Admin Interface
Access the admin dashboard at http://localhost:8000/admin/ using your superuser credentials.

Admin features include:

User management

Task management

Bulk operations

Advanced filtering

Custom statistics views

## Testing
Run the test suite with:

bash
Copy
python manage.py test
Deployment
For production deployment, consider:

Setting up a proper database (PostgreSQL recommended)

Configuring environment variables

Using Gunicorn or uWSGI as application server

Setting up Nginx as reverse proxy

Example production requirements:

bash
Copy
pip install gunicorn psycopg2-binary
Environment Variables
Create a .env file with:

ini
Copy
SECRET_KEY=your-secret-key-here
DEBUG=False
ALLOWED_HOSTS=yourdomain.com,localhost
DATABASE_URL=postgres://user:password@localhost:5432/dbname
Contributing
Fork the project

Create your feature branch (git checkout -b feature/AmazingFeature)

Commit your changes (git commit -m 'Add some AmazingFeature')

Push to the branch (git push origin feature/AmazingFeature)

Open a Pull Request

## License
Distributed under the MIT License. See LICENSE for more information.

Contact
Project Maintainer - Surendra Kumar

Project Link: https://github.com/ksurendra1/task-management-api
