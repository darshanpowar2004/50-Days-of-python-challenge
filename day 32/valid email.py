# Valid Email

def email_validator(arr : list):
    valid_email = []
    for mail in arr:
        email = mail
        if "@" in email and not email.startswith("@") and email.count("@")==1:
            if email.endswith(".com"):
                valid_email.append(email)

    if valid_email:
        return valid_email
    else:
        return "all email are invalid."

if __name__ == '__main__':
    emails = ['ben@mail.com', 'john@mail.cm', 'kenny@gmail.com', '@list.com']
    print(email_validator(emails))