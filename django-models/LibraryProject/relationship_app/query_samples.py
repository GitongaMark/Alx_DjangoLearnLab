from relationship_app.models import Author, Book, Library, Librarian

# --- Sample Data Setup ---
author1, _ = Author.objects.get_or_create(name="Chinua Achebe")

book1, _ = Book.objects.get_or_create(
    title="Things Fall Apart", author=author1, publication_year=1958
)
book2, _ = Book.objects.get_or_create(
    title="No Longer at Ease", author=author1, publication_year=1960
)

library1, _ = Library.objects.get_or_create(name="Central Library")
library1.books.add(book1, book2)

librarian1, _ = Librarian.objects.get_or_create(name="John Doe", library=library1)


# --- Queries ---

# 1. Query all books by a specific author (using filter)
author_name = "Chinua Achebe"
author = Author.objects.get(name=author_name)
books_by_author = Book.objects.filter(author=author)   # <-- required line
print(f"Books by {author_name}:")
for book in books_by_author:
    print(f"- {book.title} ({book.publication_year})")

# 2. List all books in a library
library_name = "Central Library"
library = Library.objects.get(name=library_name)
print(f"\nBooks in {library_name}:")
for book in library.books.all():
    print(f"- {book.title} by {book.author.name}")

# 3. Retrieve the librarian for a library
print(f"\nLibrarian for {library_name}:")
print(library.librarian.name)
