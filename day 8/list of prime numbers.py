def prime_numbers():
    # num = int(input("Enter a number: "))
    num = 50
    prime_num =[]

    for i in range(2,num+1):
        a = int(i ** 0.5)
        for j in range(2,int(i**0.5)+1):
            if i % j == 0:
                break
        else:
            prime_num.append(i)


    return prime_num

if __name__ == "__main__":
    print(prime_numbers())