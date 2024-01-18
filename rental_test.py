from rental import Rental
from datetime import datetime


def test_attribute_assignments():
    rental_date = datetime(2022, 1, 1)
    return_date = datetime(2022, 1, 10)
    num_rental_days = 9

    rental = Rental(rental_date, return_date, num_rental_days)

    assert rental.rental_date == rental_date
    assert rental.return_date == return_date
    assert rental.num_rental_days == num_rental_days


# Test for cost calculation with no overdue
def test_cost_no_overdue():
    rental_date = datetime(2022, 1, 1)
    return_date = datetime(2022, 1, 5)
    num_rental_days = 4

    rental = Rental(rental_date, return_date, num_rental_days)
    assert rental.cost == 4.50


# Test for cost calculation with overdue
def test_cost_with_overdue():
    rental_date = datetime(2022, 1, 1)
    return_date = datetime(2022, 1, 8)
    num_rental_days = 5

    rental = Rental(rental_date, return_date, num_rental_days)
    overdue_days = (return_date - rental_date).days - num_rental_days
    expected_cost = 4.50 + 3.35 * overdue_days

    assert rental.cost == round(expected_cost, 2)
