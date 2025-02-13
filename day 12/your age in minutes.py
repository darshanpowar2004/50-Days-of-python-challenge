from datetime import datetime

def age_in_minutes():

    while True:
        year_of_birth = int(input("Enter your year of birth : "))
        current_year = datetime.now().year

        if 1900 <= year_of_birth < current_year:
            min_age = (current_year-year_of_birth) * 525600
            return f"you are {min_age:,} minutes old."
        else:
            print(f"{year_of_birth} is invalid year of birth.")



if __name__ == "__main__":
    print(age_in_minutes())