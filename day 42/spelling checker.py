# Day 42
# Spelling Checker
from textblob import TextBlob

def spelling_checker():
    while True:
        text = input("Enter a word or sentence: ")
        spell = TextBlob(text)
        corrected_word = spell.correct()

        if text != corrected_word:
            user_input = input(f"Did you mean: '{corrected_word}'? Type 'yes' or 'no': ")

            if user_input.lower() == "yes":
                return corrected_word
            elif user_input.lower() == "no":
                print("Please enter again!")
                continue
            else:
                print("Invalid input. Try again!")
        elif text == corrected_word:
            return  corrected_word

if __name__ == "__main__":
    result = spelling_checker()
    print(f"Corrected text: {result}")