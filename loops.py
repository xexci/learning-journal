names = ["Mimi", "Xerxcii", "John", "Jane"]

for name in names:
    print(f"Hello, {name}!")

count = 1

while count <= 4:
    print(f"Count: {count}")
    count = count + 1

print("Done counting!")  

def greet(name):
    return f"Good morning, {name}! Welcome to the team."

message = greet("Xerxcii")
print(message)

teammates = ["Mimi", "Ada", "Kofi", "Zara"]

for teammate in teammates:
    print(greet(teammate))