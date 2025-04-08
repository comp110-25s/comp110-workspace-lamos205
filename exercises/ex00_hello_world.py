def fuel_needed(distance: int, mpg: int) -> float:
    return distance / mpg


def total_fuel_cost(distance: int, mpg: int, price_per_gallon: int) -> float:
    return fuel_needed(distance=distance, mpg=mpg) * price_per_gallon


print(total_fuel_cost(distance=300, mpg=25, price_per_gallon=4))
