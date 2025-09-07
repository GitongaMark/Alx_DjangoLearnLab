📚 Library Management System (Django)

A Django-based project showcasing advanced model relationships, user authentication, role-based access control, and custom permissions.
This project demonstrates how to effectively manage libraries, books, authors, and librarians while restricting actions based on user roles.

🚀 Features

Models & Relationships

   Author → Book (ForeignKey)

   Library ↔ Book (ManyToManyField)

   Library → Librarian (OneToOneField)

   User → UserProfile with role (OneToOneField)

Authentication

   User Registration

   Login / Logout

   Session Management

Role-Based Access Control (RBAC)

   Roles: Admin, Librarian, Member

   Restricted views per role using @user_passes_test

Custom Permissions

   can_add_book → Only certain users can add books

   can_change_book → Only certain users can edit books

   can_delete_book → Only certain users can delete books

Views

   Function-based view: List all books

   Class-based view: Display library details

   Secured views for Admin, Librarian, and Member dashboards

📂 Project Structure
LibraryProject/
│── LibraryProject/         # Main project settings
│── relationship_app/       # Core application
│   ├── models.py           # Models: Author, Book, Library, Librarian, UserProfile
│   ├── views.py            # Views (FBV + CBV + RBAC + permissions)
│   ├── urls.py             # App URL routes
│   ├── query_samples.py    # Example ORM queries
│   └── templates/
│       └── relationship_app/
│           ├── login.html
│           ├── logout.html
│           ├── register.html
│           ├── list_books.html
│           ├── library_detail.html
│           ├── add_book.html
│           ├── edit_book.html
│           ├── delete_book.html
│           ├── admin_view.html
│           ├── librarian_view.html
│           └── member_view.html
│── manage.py

⚙️ Setup & Installation

Clone this repository

   git clone https://github.com/GitongaMark/Alx_DjangoLearnLab.git
   
   cd library-management-django

Run migrations

   python manage.py makemigrations
   
   python manage.py migrate


Create a superuser (admin account)

   python manage.py createsuperuser


Run the server

   python manage.py runserver


Access the app

   Frontend: http://127.0.0.1:8000/

   Admin panel: http://127.0.0.1:8000/admin/

🔐 Roles & Permissions

  Admin

   Full access to all system features

  Librarian

   Can manage library books and assist members

  Member

   Can view and borrow books

🛠️ Technologies Used

   Python 3.10.11

   Django 5.2.6

   SQLite (default, can be swapped with PostgreSQL/MySQL)

   HTML & Django Templates
