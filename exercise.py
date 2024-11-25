def print_greeting():
    # Declare the variable and set it to True
    python_is_fun = True
    
    # Check the condition
    if python_is_fun:
        # Print the message
        print("Python is fun!")

# Call the function
print_greeting()

# Prompt the user for a letter and check if it is a vowel or consonant
def check_letter():
    letter = input("Enter a letter (a-z or A-Z): ").lower()
    
    if letter.isalpha() and len(letter) == 1:  # Ensure it's a single alphabetic character
        if letter in "aeiou":
            return f"The letter {letter} is a vowel."
        else:
            return f"The letter {letter} is a consonant."
    else:
        return "Invalid input. Please enter a single letter."

# Call the function
print(check_letter())


# Prompt the user for their age and check voting eligibility
def check_voting_eligibility():
    try:
        age = int(input("Please enter your age: "))  # Convert input to integer
        
        if age < 0:  # Check for impossible values
            return "Age cannot be negative. Please enter a valid age."
        else:
            voting_age = 18  # Define the voting age
            if age >= voting_age:
                return "You are old enough to vote!"
            else:
                return f"You are not old enough to vote. You need to wait {voting_age - age} more years."
    except ValueError:
        return "Invalid input. Please enter a numerical value for age."

# Call the function
print(check_voting_eligibility())


# Prompt the user for a dog's age and calculate the age in dog years
def calculate_dog_years():
    try:
        age = float(input("Input a dog's age: "))  # Convert input to a float for partial years
        
        if age < 0:
            return "Age cannot be negative. Please enter a valid age."
        else:
            if age <= 2:
                dog_years = age * 10  # First two years count as 10 dog years each
            else:
                dog_years = 20 + (age - 2) * 7  # First two years are 20, subsequent years count as 7 each
            
            return f"The dog's age in dog years is {dog_years:.1f}."
    except ValueError:
        return "Invalid input. Please enter a numerical value for the dog's age."

# Call the function
print(calculate_dog_years())


# Prompt the user for weather conditions and provide clothing advice
def weather_advice():
    cold = input("Is it cold? (yes/no): ").strip().lower()
    raining = input("Is it raining? (yes/no): ").strip().lower()

    # Validate inputs
    if cold not in ["yes", "no"] or raining not in ["yes", "no"]:
        return "Invalid input. Please enter 'yes' or 'no'."
    else:
        is_cold = cold == "yes"
        is_raining = raining == "yes"
        
        # Provide advice based on the conditions
        if is_cold and is_raining:
            return "Wear a waterproof coat."
        elif is_cold and not is_raining:
            return "Wear a warm coat."
        elif not is_cold and is_raining:
            return "Carry an umbrella."
        else:
            return "Wear light clothing."

# Call the function
print(weather_advice())


# Determine the season based on the month and day
def determine_season():
    try:
        # Get user input
        month = input("Enter the month of the year (Jan - Dec): ").strip().capitalize()
        day = int(input("Enter the day of the month: "))
        
        # Validate month input
        months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        if month not in months:
            return "Invalid month. Please use the three-letter format (e.g., Jan, Feb)."
        
        # Validate day input
        if day < 1 or day > 31:
            return "Invalid day. Please enter a valid day of the month (1-31)."
        
        # Determine season
        if (month == "Dec" and day >= 21) or month in ["Jan", "Feb"] or (month == "Mar" and day <= 19):
            season = "Winter"
        elif (month == "Mar" and day >= 20) or month in ["Apr", "May"] or (month == "Jun" and day <= 20):
            season = "Spring"
        elif (month == "Jun" and day >= 21) or month in ["Jul", "Aug"] or (month == "Sep" and day <= 21):
            season = "Summer"
        elif (month == "Sep" and day >= 22) or month in ["Oct", "Nov"] or (month == "Dec" and day <= 20):
            season = "Fall"
        else:
            return "The date is invalid."

        return f"{month} {day} is in {season}."
    
    except ValueError:
        return "Invalid input. Please enter numbers for the day."

# Call the function
print(determine_season())
