class Library:
    def __init__(self):
        self.books = {}  # {book_id: {"title": str, "available": bool}}
        self.issued_books = {}  # {user_id: [book_ids]}

    def add_book(self, book_id, title):
        if book_id not in self.books:
            self.books[book_id] = {"title": title, "available": True}
            print(f"Book '{title}' added successfully.")
        else:
            print(f"Book ID {book_id} already exists.")

    def remove_book(self, book_id):
        if book_id in self.books and self.books[book_id]["available"]:
            del self.books[book_id]
            print(f"Book ID {book_id} removed successfully.")
        else:
            print(f"Book ID {book_id} does not exist or is issued.")