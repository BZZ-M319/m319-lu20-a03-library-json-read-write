from rental import Rental
from datetime import datetime


def test_attribute_assignments():
    rental_date = datetime(2022, 1, 1)
    return_date = datetime(2022, 1, 10)
    num_rental_days = 9

    rental = Rental(rental_date, return_date, num_rental_days)

    expected_datetimes = [rental_date, return_date]
    expected_ints = [num_rental_days]
    datetimes_found = []
    ints_found = []

    # Iteriere durch die Attribute des Objekts und speichere die Werte
    for attr in rental.__dict__.values():
        if isinstance(attr, datetime):
            datetimes_found.append(attr)
        elif isinstance(attr, int):
            ints_found.append(attr)

    # Überprüfe, ob die gefundenen Werte mit den erwarteten Werten übereinstimmen
    assert all(date in datetimes_found for date in expected_datetimes), "Nicht alle erwarteten datetime-Werte gefunden."
    assert all(num in ints_found for num in expected_ints), "Nicht alle erwarteten int-Werte gefunden."



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
