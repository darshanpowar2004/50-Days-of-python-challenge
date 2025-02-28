# Day 24
# Average Calories
from datetime import date
def average_calories():
    today_date = date.today()
    calories = 0
    i = 0
    while True:
        try:
            user = input(f"{today_date} : Enter calories ('done' for exit): ")
            if user.lower() == 'done':
                break
            calories += int(user)
        except Exception as e:
            print(e)
        else:
            i += 1

    return f"Average of calories : {calories / i}"

if __name__ == '__main__':
    result = average_calories()
    print(result)