# Advanced API Project
This Django project implements a RESTful API using Django REST Framework, featuring custom serializers, generic views, filtering, searching, ordering, and comprehensive unit tests.
## Setup Instructions

### 1. Run the setup script to create the environment and install dependencies:
bash setup.sh


### 2. Activate the virtual environment:
source venv/bin/activate

### 3. Run migrations:
python manage.py makemigrations
python manage.py migrate


### 4. Create a superuser for admin access:
python manage.py createsuperuser


### 5. Start the development server:
python manage.py runserver



## API Endpoints

### . Books
#### . GET /api/books/: List all books (supports filtering, searching, ordering)
POST /api/books/: Create a new book (authenticated users only)
GET /api/books/<id>/: Retrieve a book
PUT /api/books/<id>/: Update a book (authenticated users only)
DELETE /api/books/<id>/: Delete a book (authenticated users only)


### Authors
GET /api/authors/: List all authors with nested books
POST /api/authors/: Create a new author (authenticated users only)
GET /api/authors/<id>/: Retrieve an author with nested books
PUT /api/authors/<id>/: Update an author (authenticated users only)
DELETE /api/authors/<id>/: Delete an author (authenticated users only)



## Filtering, Searching, and Ordering

Filtering: Use query parameters like ?title=Book&publication_year=2020&author__name=Author
Searching: Use ?search=keyword to search in title and author name
Ordering: Use ?ordering=title or ?ordering=-publication_year for ascending/descending order

## Testing
Run the test suite:
python manage.py test api

The tests cover:

CRUD operations for books
Authentication and permission checks
Filtering, searching, and ordering functionalities

## Notes

The API uses IsAuthenticatedOrReadOnly permissions: read operations are open to all, write operations require authentication.
BookSerializer validates that publication_year is not in the future.
Use tools like Postman or curl to test the API endpoints.
