class Book():
    def __init__(self, title, author):
        self.author = title
        self.title = author

        def display():
            print(title, author)

        display()

book1 = Book('Of Mice and Men,', 'written by John Steinbeck')
book2 = Book('To Kill a Mockingbird,', 'written by Harper Lee')

book1
book2

