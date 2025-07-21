# Library Management System

A Django-based application to manage library operations efficiently, including book management, admin registration, and a student view for accessing library resources. The project is implemented with RESTful APIs using Django REST Framework (DRF).

---

## Table of Contents
1. [Project Overview](#project-overview)
2. [Features](#features)
3. [Technologies Used](#technologies-used)
4. [Setup and Installation](#setup-and-installation)
5. [Usage](#usage)
6. [API Endpoints](#api-endpoints)
7. [Screenshots](#screenshots)
8. [License](#license)

---

## Project Overview

The **Library Management System** streamlines library workflows by providing modules for book CRUD operations, admin registration, and a student interface. It uses token-based authentication for secure access to APIs and ensures scalability for future enhancements.

---

## Features

- **Admin Signup**: Register new admin users with secure validation.
- **Book Management**:
  - Add, edit, view, and delete books.
  - Token-based authentication for admin operations.
- **Student View**:
  - Search and view available books in the library.
- **Home Page**: A welcoming interface with navigation links to key features.

---

## Technologies Used

- **Backend**:
  - Python 3.8+
  - Django 4.x
  - Django REST Framework (DRF)
- **Frontend**:
  - HTML5
  - CSS3
- **Database**:
  - SQLite (default) or MySQL (optional)
- **Authentication**:
  - Token-based authentication using DRF.

---

## Setup and Installation

### Prerequisites
1. Python 3.8 or higher installed. [Download Python](https://www.python.org/downloads/)
2. Virtual Environment (optional but recommended):
   ```bash
   pip install virtualenv
   ```

### Steps
1. **Clone the Repository**:
   ```bash
   git clone <https://github.com/Mayur2157/Library-Management-System>
   cd library_management
   ```

2. **Create and Activate Virtual Environment**:
   ```bash
   python -m venv venv
   # Activate the virtual environment
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
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

5. **Create a Superuser** (for accessing the admin panel):
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the Development Server**:
   ```bash
   python manage.py runserver
   ```

7. **Access the Application**:
   - Admin panel: [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)
   - Student view: [http://127.0.0.1:8000/student](http://127.0.0.1:8000/student)

---

## Usage

### Admin Operations
1. Register as an admin via the admin signup endpoint: `/admin/signup/`.
2. Use the token generated for secure access to book management endpoints.

### Student View
1. View the list of books in the library by navigating to `/student/`.

---

## API Endpoints

### Authentication
- **Admin Signup**: `/admin/signup/` (POST)

### Book Management
- **List All Books**: `/books/` (GET)
- **Create a Book**: `/books/` (POST)
- **Update a Book**: `/books/<id>/` (PUT)
- **Delete a Book**: `/books/<id>/` (DELETE)

### Student View
- **View Available Books**: `/student/` (GET)

---

## Screenshots

### Home Page
![Home Page](screenshots/home_page.png)

### Student View
![Student View](screenshots/student_view.png)

### Admin Panel
![Admin Panel](screenshots/admin_panel.png)

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Contributing

We welcome contributions to improve this project! Please follow these steps:
1. Fork the repository.
2. Create a feature branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add your feature description"
   ```
4. Push to the branch:
   ```bash
   git push origin feature/your-feature-name
   ```
5. Submit a pull request.

For major changes, please open an issue first to discuss what you would like to change.

---

## Contact

For any queries or support, please reach out to:

- **Name**: Mayur Gadekar
- **Email**: mayurgadekar2157@gmail.com
- **GitHub**: https://github.com/Mayur2157/Library-Management-System
