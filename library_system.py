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

    def issue_book(self, book_id, user_id):
        if book_id in self.books and self.books[book_id]["available"]:
            self.books[book_id]["available"] = False
            if user_id not in self.issued_books:
                self.issued_books[user_id] = []
            self.issued_books[user_id].append(book_id)
            print(f"Book ID {book_id} issued to User {user_id}.")
        else:
            print(f"Book ID {book_id} is not available.")

    def return_book(self, book_id, user_id):
        if user_id in self.issued_books and book_id in self.issued_books[user_id]:
            self.books[book_id]["available"] = True
            self.issued_books[user_id].remove(book_id)
            print(f"Book ID {book_id} returned by User {user_id}.")
        else:
            print(f"Book ID {book_id} was not issued to User {user_id}.")

    def get_available_books(self):
        return [book_id for book_id, info in self.books.items() if info["available"]]

    def get_issued_books(self):
        issued = []
        for user_id, book_ids in self.issued_books.items():
            for book_id in book_ids:
                issued.append((user_id, book_id, self.books[book_id]["title"]))
        return issued

    def display_summary(self):
        print("\n--- Library Summary ---")
        print(f"Total Books: {len(self.books)}")
        print(f"Available Books: {len(self.get_available_books())}")
        print(f"Issued Books: {len(self.get_issued_books())}")
        print("\nIssued Books Details:")
        for user_id, book_id, title in self.get_issued_books():
            print(f"User {user_id}: {title} (ID: {book_id})")   