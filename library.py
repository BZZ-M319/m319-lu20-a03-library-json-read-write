from rental import Rental
from datetime import datetime
import json

def init_books():
    with open('books.json', 'r') as file:
        return json.load(file)


def read_rental():
    rental_date = read_date('Enter rental date (dd.mm.yyyy): ')
    num_rental_days = read_int('Enter number of rental days: ', 1, 99)
    return_date = read_date('Enter return date (dd.mm.yyyy): ')
    return Rental(rental_date, return_date, num_rental_days)


def add_rental(books):
    while True:
        book_name = input('Enter the book name: ')
        if book_name in books:
            rental = read_rental()
            books[book_name].append(rental)
            choice = input('Do you want to add another rental? (y/n): ').strip().lower()
            if choice != 'y':
                break
    else:
        print('Book not found in the library.')


def show_balance(books):
    for book, rentals in books.items():
        print(f'Statement for {book}')
        total_cost = 0

        for rental in rentals:
            print(f'  - {rental.rental_date.strftime("%d.%m.%Y")}: CHF {rental.cost}')
            total_cost += rental.cost

        print(f'Total: CHF {round(total_cost, 2)}')


def read_int(prompt, minimum=None, maximum=None):
    while True:
        try:
            num = int(input(prompt))
        except ValueError:
            print('Please, enter a whole number!')
            continue
        else:
            if minimum is not None and num < minimum:
                print('Please, enter a number greater than or equal to', minimum)
                continue
            if maximum is not None and num > maximum:
                print('Please, enter a number less than or equal to', maximum)
                continue
            return num


def read_date(prompt):
    while True:
        try:
            date_str = input(prompt)
            rental_date = datetime.strptime(date_str, '%d.%m.%Y')
            return rental_date
        except ValueError:
            print('Please enter a valid date.')


def main():
    books = init_books()
    while True:
        print('\nLibrary Management System')
        print('1. Add Rental')
        print('2. Show Balances')
        print('3. Exit')
        choice = read_int('Enter your choice (1/2/3): ', 1, 3)

        if choice == 1:
            add_rental(books)
        elif choice == 2:
            show_balance(books)
        elif choice == 3:
            break


if __name__ == '__main__':
    main()
