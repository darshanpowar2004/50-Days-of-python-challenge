# Day 44
# Save Email

import csv

def save_emails():
    while True:
        user = input("Enter email or done: ").lower()
        if user.lower() == "done":
            break

        if user.count("@") == 1 and user.count(".com") == 1:
            with open("save_email_csv.csv",mode="a",newline='') as file:
                writer = csv.writer(file)

                writer.writerow([user])
        else:
            print("Please enter valid email!")

def open_emails():
    with open("save_email_csv.csv", mode="r", newline='') as file:
        return file.read()

if __name__ == "__main__":
    # save_emails()
    print(open_emails())