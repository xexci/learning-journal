try:
    file = open("traders.txt", "r")
    
    for line in file:
        print(f"Found trader: {line.strip()}")
    
    file.close()

except FileNotFoundError:
    print("Error: the traders.txt file could not be found.")