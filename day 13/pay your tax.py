def your_tax():
    while True:
        try:
            price = int(input("Enter your item price : "))
            vat = int(input("Enter your VAT (vat should be a percentage) don't use '%' : "))
        except ValueError:
            print(f"Invalid input!")
        else:
            tax = (price * vat) // 100
            final_price = price + tax
            return final_price


if __name__ == "__main__":
    print(your_tax())