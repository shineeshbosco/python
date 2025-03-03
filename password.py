def create_password(name, nickname, pet_name):
    # Ensure the name and nickname are at least 4 characters long
    if len(name) < 4 or len(nickname) < 4:
        raise ValueError("Name and nickname must be at least 4 characters long.")
    
    # Ensure the pet name is at least 2 characters long
    if len(pet_name) < 2:
        raise ValueError("Pet name must be at least 2 characters long.")
    
    # Extract the first 4 characters from the name
    part1 = name[:4]
    
    # Extract the first 4 characters from the nickname
    part2 = nickname[:4]
    
    # Extract the first 2 characters from the pet name
    part3 = pet_name[:2]
    
    # Combine the parts to form the password
    password = part1 + part2 + part3
    
    return password

# Prompt the user for inputs
name = input("Enter your name: ")
nickname = input("Enter your nickname: ")
pet_name = input("Enter your pet's name: ")

# Generate the password
try:
    password = create_password(name, nickname, pet_name)
    print(f"Generated password: {password}")
except ValueError as e:
    print(e)
