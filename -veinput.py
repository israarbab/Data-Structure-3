def input_numbers():
    num = int(input("Enter your number : "))
    if num >= 0:
        print("Number +ve")
        input_numbers()
    else:
        print("Number -ve")

# Start the recursive input process
input_numbers()
