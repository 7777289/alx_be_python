# Update Operation

This demonstrates how to update an existing Book record using Django ORM.

## Update a book's publication year

```python
from bookshelf.models import Book

# Get the book by ID
book = Book.objects.get(id=1)

# Update the publication year
book.publication_year = 1950
book.save()

print(book)
# Output: 1984 by George Orwell (1950)
book = Book.objects.get(id=1)
book.title = "Nineteen Eighty-Four"
book.author = "G. Orwell"
book.save()

print(book)
# Output: Nineteen Eighty-Four by G. Orwell (1950)
