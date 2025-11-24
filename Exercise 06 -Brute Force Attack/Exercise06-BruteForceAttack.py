print ("Brute Force Attack Password Simulation") #Prints title

password = "12345" #Declares the values of the correct password, the no. of attempts and the maximum no. of attempts
attempt = 0
Max_attempt = 5

while attempt < Max_attempt: #looks if the no. of attempts is lower than the maximum amoung
    access = int(input("Enter Your 5 Digit Password: ")) #Declares the "access" as a variable and inputs the 5 digit password
    if access == password: #Checks to see if password inputed and "password" variable is the same and prints "Correct Password"
        print("Correct Password.")
        break #Ends Program
    else:
      attempt += 1 #Adds +1 to the no. of attempts
      remaining_attempt = Max_attempt - attempt #Creates the variable for the remaining attempts by subtracting Max_attempt to attempt
      if remaining_attempt > 0 : #Checks to see if the remaining_attempt is higher than 0
         print("Wrong Password, You have",remaining_attempt, "tries left") #Prints wrong password and the amount of remaining attempts
      else:
         print("The Max Amount of attempts has been reached.") #when the amount of attempts go to 0 then it prints max amount has been reached
6