def my_discount():
    price = float(input("Enter price : ₹"))
    discount = float(input("Enter discount : %"))

    discount_price = round(((price*discount)/100),2)

    return price - discount_price


if __name__ == "__main__":
    final_price = my_discount()
    print(f"The final price after discount is : ₹{final_price}")