#Even or Uneven number
def evenOrEven():
    
    print("---Welcome to Even or Uneven numbers---")
    print("---Write anything else to exit---")
    try:
        number = int(input("What number are you thinking? >> "))
        while True:
            if number%2 == 0:
                print("It's an even number!, Can you add another number? ")
                number = int(input(">> "))
            else:
                print("It's an uneven number!, Can you add another number?")
                number = int(input(">> "))
    except:
        return print("GoodBye!")
evenOrEven()
