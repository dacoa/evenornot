#Even or Uneven number
print("---Welcome to Even or Uneven numbers---")
print("-----Write Q or anything else to exit------")
def evenOrEven():
    try:
        number = int(input("What number are you thinking? between 1 and 1.000 >> "))
        if number >= 1 and number <= 1000:    
            while True:
                if number%2 == 0:
                    print("It's an even number!, Can you add another number? ")
                    number = int(input(">> "))
                else:
                    print("It's an uneven number!, Can you add another number?")
                    number = int(input(">> ")) 
        else:
            print("****Please follow the instructions****")
            evenOrEven()
    except:
        return print("GoodBye!")
evenOrEven()

#date: 28 - 4- 22
#Thank you
#Adding git branch