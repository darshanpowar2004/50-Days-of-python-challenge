# Day 23

def basic_calculator():
    while True:
        try:
            maths_str = input("Enter your math operation (exp. 1+2,1*2.etc) use 'quit' for stop: ")

            if maths_str.lower() == "quit":
                break

            print(eval(maths_str))

        except Exception as e:
            print(f"Error! -> {e} ")

if __name__ == '__main__':
    basic_calculator()