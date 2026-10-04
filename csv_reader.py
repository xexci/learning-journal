try:
    file = open("traders.csv", "r")
    next(file)  # Skip the header line

    count = 1
    for line in file:
        print(f"{count}: {line.strip()}")
        count = count + 1
    
    file.close()

except FileNotFoundError:
    print("Error: the traders.csv file could not be found.")

import csv

print("\n--- Using the CSV module ---")

try:
    with open("traders.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(f"{row['name']} works as a {row['role']} in {row['city']}")

except FileNotFoundError:
    print("Error: traders.csv could not be found.")