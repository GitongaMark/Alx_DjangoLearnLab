📚 LibraryProject – Django Learn Lab

This repository contains my solutions for the ALX Django Learn Lab, where I set up a Django development environment, created models, practiced CRUD operations, and customized the Django admin interface.

🚀 Tasks Overview
0. Introduction to Django Development Environment Setup

Installed Django using pip install django.

Created a new Django project named LibraryProject.

Verified the setup by running the development server at http://127.0.0.1:8000/

Explored key files:

settings.py → project configuration.

urls.py → URL routing.

manage.py → project management utility.

📂 Files: Project scaffold inside LibraryProject/

1. Implementing and Interacting with Django Models

Created a new Django app: bookshelf.

Defined a Book model with the following fields:

title (CharField, max_length=200)

author (CharField, max_length=100)

publication_year (IntegerField)

Ran migrations to apply the model to the database.

Performed CRUD operations using Django shell:

Create: Added a book instance (1984 by George Orwell, 1949).

Retrieve: Queried the created book.

Update: Changed title to Nineteen Eighty-Four.

Delete: Removed the book instance.

📂 Documentation for CRUD operations:

CRUD_operations.md

2. Utilizing the Django Admin Interface

Registered the Book model in bookshelf/admin.py.

Customized the admin panel with:

list_display = ("title", "author", "publication_year")

list_filter = ("publication_year", "author")

search_fields = ("title", "author")

This makes it easy to manage and filter books directly in the Django admin.

📂 File: bookshelf/admin.py

🛠️ Setup Instructions

Clone this repo:

git clone https://github.com/gitongamark/Alx_DjangoLearnLab.git
cd Alx_DjangoLearnLab/Introduction_to_Django/LibraryProject


Install dependencies:

pip install django


Apply migrations:

python manage.py migrate


Run the development server:

python manage.py runserver


Visit the project in your browser:
http://127.0.0.1:8000/

👤 Author

Gitonga Mark

Backend Learner @ ALX

