
def count_occurrences(cars: list):
    for car in set(cars):
        print(f"{car} => {cars.count(car)}")
    return

vehicles = ['car', 'car', 'truck', 'car', 'SUV', 'truck',
            'motorcycle', 'motorcycle', 'car', 'truck']

count_occurrences(vehicles)