# Here is a dating app practice
# Starting on Feb 22, 2026

# Encapsulate a universal input functions
# Function 1: Get string input (with length verification)
import json

def get_string_input(prompt, min_length=1):
    while True:
        user_input = input(prompt).strip()
        if len(user_input) >= min_length:
            return user_input
        print(f"Invalid input! Minimum length is {min_length} characters.")

# Function 2: Get number input (with range verification)
def get_number_input(prompt, min_val=None, max_val=None):
    while True:
        user_input = input(prompt).strip()
        try:
            num = float(user_input)
            if (min_val is not None and num < min_val) or (max_val is not None and num > max_val):
                print(f"Invalid input! Please enter between {min_val} and {max_val}.")
                continue
            return num
        except ValueError:
            print("Invalid input! Please enter a number (e.g., 175 / 50000).")

# Function 3: Get option input (such as 0/1/2, yes/no)
def get_option_input(prompt, options):
    while True:
        user_input = input(prompt).strip().lower()
        if user_input in options:
            return user_input
        valid_options = ", ".join(options)
        print(f"Invalid input! Please enter one of: {valid_options}.")


# Main program
print("-Perfect Match Dating App Registration-")
# sign up functions and save them in a dictionary
user_info = {}

# Set the username and call function 1
username = get_string_input("Tell me your nickname (>=2 chars): ", min_length=2)
user_info["nickname"] = username
print(f"Hello {username}! Ready to meet your crush?")

# Set the password and call function 1
while True:
    password = get_string_input("Set your unique password(case sensitive): ")
    confirm_pwd = get_string_input("Confirm your password: ")
    # check the pwd
    if password.lower() == confirm_pwd.lower():
        user_info["password"] = password.lower()
        print(f"{username}! Congratulations! Password set successfully!")
        break
    print("Oops! It might be something wrong. Please try again!")

# Set the email address and call function 3
print("\nCan we contact you via email?")
email_choice = get_option_input("Yes or No?: ", ["yes", "no"])
if email_choice == "yes":
        email_address = get_string_input("Well.Enter your email, please: ").strip()
        user_info["email"] = email_address
        print("Got it! You are on your way to meet your crush!")
else:
        print("OK! Maybe we need more time to know each other!")

# Height and call function 2
height = get_number_input("\nHow tall are you?(cm): ")
user_info["height"] = int(height)

# Gender and call function 3
print("\nWhat is your gender? ")
gender_map = {"0": "Male", "1": "Female", "2": "Other"}
for key, value in gender_map.items():
    print(f"{key} : {value}")
gender_choice = get_option_input("Enter your answer(0/1/2)", ["0", "1", "2"])
selected_gender = gender_map[gender_choice]
user_info["gender"] = selected_gender
print(f"{username}! Your gender is {selected_gender}!")

# The logic of height matching
if selected_gender == "Male":
    print(f"Hey guy! Your perfect match's height is {int(height) - 10}cm.")
elif selected_gender == "Female":
    print(f"Hey girl! your perfect match's height is {int(height) + 10}cm.")
else:
    print("You can find your true love here in your ideal height.")

# Age and call function 2
age = get_number_input("\nHow old are you?", min_val=18, max_val=80)
user_info["age"] = int(round(age))
print(f"{username}! Your age is {user_info['age']}")

# Annual income and call function 2
income = get_number_input("\nWhat is your annual income?(For example:50000($)): ")
user_info["income"] = int(income)
if income <= 100000:
    print(f"{username}! We will give you some dating advice if you are ready.")
else:
    print(f"{username}! Wanna create a happy future with him/her? Here's some tailored service.")
    tailored_svc_map = {
        0: "1 vs 1 Dating coach",
        1: "Personal appearance improvement service",
        2: "Relationship improvement",
    }
    for key, value in tailored_svc_map.items():
        print(f"{key} : {value}")
    svc_choice = get_option_input("Enter your answer(0/1/2): ", ["0", "1", "2"])
    selected_svc = tailored_svc_map[int(svc_choice)]
    user_info["tailored_service"] = selected_svc
    print(f"Got it! We will provide you with {selected_svc}!")

# Occupation and call function 3
print("\nWhat's your occupation? ")
occupation_map = {
    0: "Student",
    1: "Working Professional",
    2: "Entrepreneur",
    3: "Retired"
}
for key, value in occupation_map.items():
    print(f"{key} : {value}")
# Collect user input
occupation_choice = get_option_input("Enter your answer(0/1/2/3): ", ["0", "1", "2", "3"])
selected_occupation = occupation_map[int(occupation_choice)]
user_info["occupation"] = selected_occupation
print(f"{username}! Your occupation is {selected_occupation}.")

# Ideal match
# Gender of ideal match
print("\nWhat's your ideal match's gender? ")
for key, value in gender_map.items():
    print(f"{key} : {value}")
ideal_gender_choice = get_option_input("Enter your answer(0/1/2)", ["0", "1", "2"])
selected_ideal_gender = gender_map[ideal_gender_choice]
user_info["ideal_gender"] = selected_ideal_gender
print(f"{username}! Your ideal match's gender is {selected_ideal_gender}.")

# Height range of ideal match
print("\nWhat's your ideal match's height range(cm)? ")
height_range_map = {
    0: (0, 150),
    1: (151, 160),
    2: (161, 170),
    3: (171, 180),
    4: (181, 250),
}
for key, value in height_range_map.items():
    print(f"{key} : {value[0]}-{value[1]}cm")
height_range_choice = get_option_input("Enter your answer(0/1/2/3/4): ", ["0", "1", "2", "3", "4"])
selected_height_range = height_range_map[int(height_range_choice)]
user_info["ideal_height_range"] = selected_height_range
print(f"{username}! Your ideal match's height range is {selected_height_range}.")

# Age range of ideal match
print("\nWhat's your ideal match's age range? ")
age_range_map = {
    0: (18, 25),
    1: (26, 35),
    2: (36, 45),
    3: (46, 55),
    4: (55, 80)
}
for key, value in age_range_map.items():
    print(f"{key} : {value[0]}-{value[1]}")
age_range_choice = get_option_input("Enter your answer(0/1/2/3/4): ", ["0", "1", "2", "3", "4"])
selected_age_range = age_range_map[int(age_range_choice)]
user_info["ideal_age_range"] = selected_age_range
print(f"{username}! Your ideal match's age range is {selected_age_range}.")

# Annual income of ideal match
print("\nWhat's your ideal match's annual income? ")
income_range_map = {
    0: (0, 50000),  # Under $50K
    1: (50001, 100000),
    2: (100001, 150000),
    3: (150001, 1000000000)  # Over $100K
}
for key, value in income_range_map.items():
    print(f"{key} : {value}")
income_range_choice = get_option_input("Enter your answer(0/1/2/3): ", ["0", "1", "2", "3"])
selected_income_range = income_range_map[int(income_range_choice)]
user_info["ideal_income_range"] = selected_income_range
print(f"{username}! Your ideal match's annual income is {selected_income_range}.")

# Occupation of ideal match
print("\nWhat's your ideal match's occupation? ")
for key, value in occupation_map.items():
    print(f"{key} : {value}")
ideal_ocp_choice = get_option_input("Enter your answer(0/1/2/3): ", ["0", "1", "2", "3"])
selected_ideal_ocp_choice = occupation_map[int(ideal_ocp_choice)]
user_info["ideal_occupation"] = selected_ideal_ocp_choice
print(f"{username}! Your ideal match's occupation is {selected_ideal_ocp_choice}.")


# Sign in process
print("\nYou are one of the Perfect Match's members now. ")
while True:
    login_username = get_string_input("Please enter your nickname: ").lower()
    login_password = get_string_input("Please enter your password: ").lower()
    if login_username == user_info["nickname"].lower() and login_password == user_info["password"]:
        print(f"{login_username}! Welcome back!")
        break
    else:
        print("Invalid username or password. Please try again.")

# Recommend ideal partners according to users' preferences and circumstances.
# annual income <=$100000 will get 3 options while >$100000 will get 5 options
match_pool = [
    {"nickname": "Lily", "gender": "Female", "height": 165, "age": 28, "income": 50000, "occupation": "Student"},
    {"nickname": "Mike", "gender": "Male", "height": 180, "age": 30, "income": 80000, "occupation": "Working Professional"},
    {"nickname": "Jane", "gender": "Female", "height": 170, "age": 25, "income": 60000, "occupation": "Entrepreneur"},
    {"nickname": "Tom", "gender": "Male", "height": 190, "age": 65, "income": 90000, "occupation": "Retired"},
    {"nickname": "Amy", "gender": "Female", "height": 160, "age": 27, "income": 70000, "occupation": "Student"},
    {"nickname": "Bob", "gender": "Male", "height": 185, "age": 32, "income": 100000, "occupation": "Working Professional"},
    {"nickname": "Cindy", "gender": "Female", "height": 165, "age": 26, "income": 80000, "occupation": "Entrepreneur"},
    {"nickname": "David", "gender": "Male", "height": 180, "age": 58, "income": 110000, "occupation": "Retired"},
    {"nickname": "Eva", "gender": "Female", "height": 170, "age": 28, "income": 90000, "occupation": "Student"},
    {"nickname": "Frank", "gender": "Male", "height": 190, "age": 40, "income": 120000, "occupation": "Working Professional"},
    {"nickname": "Grace", "gender": "Female", "height": 160, "age": 25, "income": 70000, "occupation": "Entrepreneur"},
    {"nickname": "Henry", "gender": "Male", "height": 185, "age": 60, "income": 100000, "occupation": "Retired"},
    {"nickname": "Iris", "gender": "Female", "height": 165, "age": 27, "income": 80000, "occupation": "Student"},
    {"nickname": "James", "gender": "Male", "height": 180, "age": 35, "income": 110000, "occupation": "Working Professional"},
    {"nickname": "Kevin", "gender": "Male", "height": 190, "age": 45, "income": 130000, "occupation": "Working Professional"},
    {"nickname": "Lucy", "gender": "Female", "height": 170, "age": 30, "income": 90000, "occupation": "Entrepreneur"},
    {"nickname": "Mary", "gender": "Female", "height": 160, "age": 28, "income": 90000, "occupation": "Student"},
    {"nickname": "Nancy", "gender": "Female", "height": 165, "age": 26, "income": 80000, "occupation": "Entrepreneur"},
    {"nickname": "Oscar", "gender": "Male", "height": 185, "age": 50, "income": 120000, "occupation": "Retired"},
    {"nickname": "Peter", "gender": "Male", "height": 180, "age": 40, "income": 110000, "occupation": "Working Professional"},
    {"nickname": "Quinn", "gender": "Female", "height": 165, "age": 27, "income": 80000, "occupation": "Student"},
    {"nickname": "Rachel", "gender": "Female", "height": 170, "age": 25, "income": 70000, "occupation": "Student"}

]
def recommend_matches(user_info):
    matches = []
    for match in match_pool:
        # Check gender
        if match["gender"] != user_info["ideal_gender"]:
            continue
        # Check height(in the range)
        if not (user_info["ideal_height_range"][0] <= match["height"] <= user_info["ideal_height_range"][1]):
            continue
        # Check age(in the range)
        if not (user_info["ideal_age_range"][0] <= match["age"] <= user_info["ideal_age_range"][1]):
            continue
        # Check income(in the range)
        if not (user_info["ideal_income_range"][0] <= match["income"] <= user_info["ideal_income_range"][1]):
            continue
        # Check occupation
        if match["occupation"] != user_info["ideal_occupation"]:
            continue
        # Add match to list
        matches.append(match)
    # Sort matches by user's annual income
    if user_info["income"] <=100000:
        recommended = matches[:3]
        print(f"{username}! We recommend 3 ideal matches for you (24h valid):")
    else:
        recommended = matches[:5]
        print(f"{username}! We recommend 5 ideal matches for you (24h valid):")

    if not recommended:
        print("Sorry, no matches found for your preference this time.")
        more_choice = get_option_input("Would you like to see similar matches?(more/no): ", ["more", "no"])
        if more_choice == "more":
            recommend_similar_matches(user_info)
        return[]
    for i, m in enumerate(recommended, 1):
        print(f"\nMatch {i}: ")
        print(f"Nickname: {m['nickname']}")
        print(f"Gender: {m['gender']}")
        print(f"Height: {m['height']} cm")
        print(f"Age: {m['age']} years old")
        print(f"Income: ${m['income']}")
        print(f"Occupation: {m['occupation']}")
    return recommended


# Recommend similar matches
def recommend_similar_matches(user_info):
    """
    Recommend ideal partners according to users' preferences and circumstances.
    Rules: The gender should be the user's ideal gender; the height should follow the gender-matching rules;
    the age should be within ±5 years; the income should be within ±20,000; and the occupation should be the same.
    """
    similar_matches = []
    if user_info["gender"] == "Male" and user_info["ideal_gender"] == "Female":
        target_height = user_info["height"] - 10
    elif user_info["gender"] == "Female" and user_info["ideal_gender"] == "Male":
        target_height = user_info["height"] + 10
    else:
        target_height = int((user_info["ideal_height_range"][0] + user_info["ideal_height_range"][1])/2)
    age_min = user_info["age"] - 5
    age_max = user_info["age"] + 5
    income_min = user_info["income"] - 20000
    income_max = user_info["income"] + 20000

    for match in match_pool:
        if match["gender"] != user_info["ideal_gender"] or match["occupation"] != user_info["occupation"]:
            continue
        if (age_min <= match["age"] <= age_max and
            income_min <= match["income"] <= income_max and
                (target_height - 5) <= match["height"] <= (target_height + 5)):
            similar_matches.append(match)

    # Reuse the original logic for the number of recommendations
    if user_info["income"] <=100000:
        recommended = similar_matches[:3]
        print(f"{username}! We recommend 3 similar matches for you (24h valid):")
    else:
        recommended = similar_matches[:5]
        print(f"{username}! We recommend 5 similar matches for you (24h valid):")
    if not recommended:
        print("Sorry, no similar matches found for your preference this time.")
        return []


    for i, m in enumerate(recommended, 1):
        print(f"\nMatch {i}: ")
        print(f"Nickname: {m['nickname']}")
        print(f"Gender: {m['gender']}")
        print(f"Height: {m['height']} cm")
        print(f"Age: {m['age']} years old")
        print(f"Income: ${m['income']}")
        print(f"Occupation: {m['occupation']}")

recommend_matches(user_info)

# Ensure that all values are of numeric type, not string type.
user_info_json = json.dumps(user_info, indent=4)
print("\n--- User Info (JSON Format for Web) ---")
print(user_info_json)

# If the Replit web client needs to read via a file, a JSON file can be written.
with open("user_info.json", "w") as f:
    json.dump(user_info, f, indent=4)
print("\nUser info saved to user_info.json (for web access)")