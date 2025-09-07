from relationship_app.models import Author, Book, Library, Librarian

# --- Sample Data Setup ---
# Create an author (or get if already exists)
author1, _ = Author.objects.get_or_create(name="Chinua Achebe")

# Create books
book1, _ = Book.objects.get_or_create(
    title="Things Fall Apart", author=author1, publication_year=1958
)
book2, _ = Book.objects.get_or_create(
    title="No Longer at Ease", author=author1, publication_year=1960
)

# Create a library and add books
library1, _ = Library.objects.get_or_create(name="Central Library")
library1.books.add(book1, book2)

# Create a librarian for the library
librarian1, _ = Librarian.objects.get_or_create(name="John Doe", library=library1)


# --- Queries ---
# 1. Query all books by a specific author
print("Books by Chinua Achebe:")
author = Author.objects.get(name="Chinua Achebe")  # explicit query
for book in author.books.all():
    print(f"- {book.title} ({book.publication_year})")

# 2. List all books in a library
print("\nBooks in Central Library:")
library = Library.objects.get(name="Central Library")  # explicit query
for book in library.books.all():
    print(f"- {book.title} by {book.author.name}")

# 3. Retrieve the librarian for a library
print("\nLibrarian for Central Library:")
print(library.librarian.name)
