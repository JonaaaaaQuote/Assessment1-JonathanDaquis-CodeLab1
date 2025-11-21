print("Is it Even") #Prints "Is it Even"

def Even_orOdd(Number): #Function to check if a number is even or off
    if (Number % 2) == 0: #Check if the number can be divided by 2
        return f"the Number {Number} is Even" #Returns the message "The Number __ is even" if the number is even
    else:
        return  f"the Number {Number} is Odd"  #Returns the message "The Number __ is odd" if the number is odd

def main(): #Function for the input and output
 Number = int(input("Enter the Number Here : ")) #Asks the user for the number they want to check
 answer= Even_orOdd(Number) #Calls the function to check if the number is even or odd
 print(answer) #Prints the message of the first function

if __name__ == "__main__": #If statement that ensures that the main function only runs when executed
   main()
