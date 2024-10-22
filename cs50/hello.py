name = input("whats your name? ").strip().title()

#split the name into first and last name
first, last = name.split(" ")

print(f"hello, {first}")