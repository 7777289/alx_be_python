# Django ORM CRUD Operations

This document demonstrates how to perform **Create**, **Retrieve**, **Update**, and **Delete** operations using Django’s ORM on the `Book` model.

---

## ✅ Create

```python
from bookshelf.models import Book

book = Book.objects.create(
    title="1984",
    author="George Orwell",
    publication_year=1949
)

print(book)
# Output: 1984 by George Orwell (1949)
from bookshelf.models import Book

# Get all books
books = Book.objects.all()
print(books)

# Get book by ID
book = Book.objects.get(id=1)
print(book)

# Filter by author
books_by_orwell = Book.objects.filter(author="George Orwell")
print(books_by_orwell)
from bookshelf.models import Book

book = Book.objects.get(id=1)
book.title = "Nineteen Eighty-Four"
book.save()

print(book)
# Output: Nineteen Eighty-Four by George Orwell (1949)
from bookshelf.models import Book

book = Book.objects.get(id=1)
book.delete()

print(Book.objects.all())
# Output: <QuerySet []>
# Django ORM CRUD Operations for Book Model

This document demonstrates how to perform basic Create, Retrieve, Update, and Delete operations using Django's ORM for the `Book` model.

---

## ✅ Create

```python
from bookshelf.models import Book

book = Book.objects.create(
    title="1984",
    author="George Orwell",
    publication_year=1949
)
print(book)
# Output: 1984 by George Orwell (1949)
from bookshelf.models import Book

# Get all books
books = Book.objects.all()
print(books)

# Get book by ID
book = Book.objects.get(id=1)
print(book)

# Filter by author
books_by_orwell = Book.objects.filter(author="George Orwell")
print(books_by_orwell)
from bookshelf.models import Book

book = Book.objects.get(id=1)
book.title = "Nineteen Eighty-Four"
book.save()

print(book)
# Output: Nineteen Eighty-Four by George Orwell (1949)
from bookshelf.models import Book

book = Book.objects.get(id=1)
book.delete()

print(Book.objects.all())
# Output: <QuerySet []>
