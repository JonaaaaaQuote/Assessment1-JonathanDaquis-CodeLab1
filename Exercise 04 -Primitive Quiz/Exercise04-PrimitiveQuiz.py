print("Primitive Quiz") #Prints the title of the quiz

while True: #Starts the loop 
 answer = input("Do you want to answer the quiz?\nAnswer Yes or No: ").lower() #Asks for the input whether or not the user wants to proceed and converts the answer to lower case 
 
 if answer == "yes": #If the user inputs "yes" the quiz starts and prints "Let's start thr Quiz!"
    print("Let's Start the Quiz!")
    
    Question1 = input("What is the capital of France? ").lower() #Asks for the input on the question "What is the capital of France?" and converts the answer to lower case

    if Question1 == "paris": #Provides the stipulation that if the answer given is "Paris" then it prints "Your answer is Correct" and exits the terminal
      print("Your Answer is Correct!")
      exit()
    else:
      print("Your Answer is Incorrect") #If the answer is anything else that isnt Paris then it marks it as incorrect and restarts the program

    
 elif answer == "no": #Provides the other sequence that if the user does not want to proceed with the quiz it will output "Okay try again next time"
   print("Okay Try Again Next Time!")
 else:
   print("Invalid Response. Answer with Yes or No") #Provides the other output for the beginning that if the user did not answer "Yes" or "No" the program outputs An invalid reponse
                                                 #And restarts the program

