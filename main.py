
numbers = []
while True:
    try:
        x = int(input("Input an integer: "))
        numbers.append(x)
    except:
        print("The mean average is", sum(numbers)/len(numbers))
        break

quit()