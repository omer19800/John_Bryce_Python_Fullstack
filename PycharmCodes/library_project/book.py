class Book:

    def __init__(self, book_id: int, name: str, author: str, year: int, book_type: int):
        self.book_id = id
        self.name = name
        self.author = author
        self.year = year
        self.book_type = type
        self.loaned = bool

    def __str__(self):
        pass

    def get_book_id(self):
        return self.book_id

    def get_name(self):
        return self.name

    def get_author(self):
        return self.author

    def get_publish_year(self):
        return self.year

    def get_type(self):
        return self.book_type

    def max_loan_length(self):
        book_type = self.book_type
        if book_type is 1:
            return 10
        elif book_type is 2:
            return 5
        elif book_type is 3:
            return 2
        else:
            return None

    def check_if_loaned(self):
        return self.loaned


#types: 1 up to 10 days, 2 up to 5 days, 3 up to 2 days

