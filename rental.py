from dataclasses import dataclass
from datetime import datetime, timedelta


@dataclass
class Rental:
    rental_date: datetime
    return_date: datetime
    num_rental_days: int

    @property
    def cost(self):
        base_cost = 4.50
        overdue_days = (self.return_date - self.rental_date).days - self.num_rental_days
        penalty_cost = 3.35 * overdue_days
        total_cost = base_cost + penalty_cost
        return round(total_cost, 2)
