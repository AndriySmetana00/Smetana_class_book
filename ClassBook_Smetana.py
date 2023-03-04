# Написати клас "Книга", який містить властивості:
# "назва", "автор" та "рік видання".
# Додати метод для виведення інформації про
# книгу та метод для обчислення віку книги.
# Дане завдання виконуємо в командах по 2-3
# (бажано по 2) з повним циклом
# використання GIT-a. Детальний опис ДЗ був в кінці
# уроку, за потреби перегляньте
# пояснення ще раз, запис є)

# Цей клас написав Андрій Сметана, інший користувач має написати
# екземпляри класу(так як на парі робили по зразку)

class Book:

    def __init__(self, name, author, year_of_publication):
        self.name = name
        self.author = author
        self.year_of_publication = year_of_publication

    def get_book_info(self):
        return f'Name: {self.name}\nAuthor: {self.author}\nYear of publication: {self.year_of_publication}'

    def get_age_of_book(self):
        current_year = 2023
        try:
            if self.year_of_publication < 0:
                raise ValueError
            return f'The age of this book is {current_year - self.year_of_publication}'
        except ValueError:
            return 'Error! Wrong value for year of publication!'
        except TypeError:
            return 'Error! You must enter only integers for year of publication!'

user_1 = Book('Markys', 'Fodich', 2020)
user_1.get_book_info(), user_1.get_age_of_book()