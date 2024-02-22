guests = open("guests.txt", "w")
initial_guests = ["Bob", "Andrea", "Manuel", "Polly", "Khalid"]

for guest in initial_guests:
  guests.write(guest + "\n")

guests.close()

# with open("guests.txt") as guests:
#   for line in guests:
#     print(line)

new_guests = ["Sam", "Danielle", "Jacob"]

with open("guests.txt", "a") as guests:
  for guest in new_guests:
    guests.write(guest + "\n")

# with open("guests.txt") as guests:
#   for line in guests:
#     print(line)


checked_out = ["Andrea", "Manuel", "Khalid"]
temp_list = []

with open("guests.txt", "r") as guests:
  for guest in guests:
    temp_list.append(guest.strip())

with open("guests.txt", "w") as guests:
  for name in temp_list:
    if name not in checked_out:
      guests.write(name + "\n")

with open("guests.txt") as guests:
  for line in guests:
    print(line)