finished = False
result = 0
while not finished:
    try:
        result = int(input("enter number"))
        finished = True

    # TODO - add something after except
    except ValueError:
        print("Please enter a valid integer.")
print("Valid result is:", result)