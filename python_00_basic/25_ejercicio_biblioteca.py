# https://www.notion.so/mau-dev/Ejercicio-Biblioteca-con-POO-ae026fd40d7b4cbcb31551203e727d56
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_available = True

    # Metodo para prestar un libro
    def borrow(self):
        if self.is_available:
            self.is_available = False
            print(f"El librio {self.title} ha sido prestado")
        else:
            print(f"El libro {self.title} no esta disponible")

    def return_book(self):
        self.is_available = True
        print(f"El libro {self.title} ha sido devuelto")

class User:
    def __init__ (self, name, user_id):
        self.name = name
        self.user_id = user_id
        self.borrowed_book = []
    
    def borrow_book(self, book):
        if book.is_available:
            book.borrow()
            self.borrowed_book.append(book)
        else:
            print(f"El libro {self.title} no esta disponible")

    def return_book(self, book):
        if book in self.borrowed_book:
           book.return_book()
           self.borrowed_book.remove(book)
        else:
            print(f"El libro {book.title} no existe en la lista de prestados")
    
class Library:
    def __init__(self):
         self.books = []
         self.users = []

    def add_book(self, book):
        self.books.append(book)   
        print(f"El libro {book.title} ha sido agregado")

    def user_register(self, user):
        self.users.append(user)
        print(f"El usuario {user.name} ha sido registrado")

    def show_available_books(self):
        print("Libros disponibles")
        for book in self.books:
            if book.is_available:
                print(f"{book.title}, Autor: {book.author}")

book_a = Book("El principito", "Antoine de Saint-Exupéry")  
book_b = Book("The Lord Of the Ring", "J. R. Tolkien")  
book_c = Book("IT", "Stephen King")  

user_a = User("Mauricio","001")   
user_b = User("Pepe","002")   

library = Library()
library.add_book(book_a)
library.add_book(book_b)
library.add_book(book_c)

library.user_register(user_a)
library.user_register(user_b)

library.show_available_books()

user_a.borrow_book(book_a)

library.show_available_books()

user_a.return_book(book_a)

library.show_available_books()