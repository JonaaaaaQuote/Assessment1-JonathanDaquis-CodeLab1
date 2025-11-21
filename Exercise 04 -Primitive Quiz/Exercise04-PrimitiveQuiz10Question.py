print("Primitive Quiz") #Prints the title of the quiz

while True: #Starts the loop 
 answer = input("Do you want to answer the quiz?\nAnswer Yes or No: ").lower() #Asks for the input whether or not the user wants to proceed and converts the answer to lower case 
 
 if answer == "yes": #If the user inputs "yes" the quiz starts and prints "Let's start thr Quiz!"
    print("Let's Start the Quiz!")
    
    Question1 = input("1. What is the capital of France? ").lower() #Asks for the input on the question "What is the capital of France?" and converts the answer to lower case

    if Question1 == "paris": #Provides the stipulation that if the answer given is "Paris" then it prints "Your answer is Correct" and exits the terminal
      print("Your Answer is Correct!")
    else:
      print("Your Answer is Incorrect") #If the answer is anything else that isnt Paris then it marks it as incorrect and restarts the program

    Question2 = input("2. What is the capital of Austria? ").lower() 

    if Question2 == "vienna": 
     print("Your Answer is correct")
    else:
      print("Your Answer is Incorrect") 

    Question3 = input("3. What is the capital of Belgium? ").lower() 

    if Question3 == "brussels": 
     print("Your Answer is correct")
    else:
      print("Your Answer is Incorrect") 

    Question4 = input("4. What is the capital of Croatia? ").lower() 

    if Question4 == "zagreb": 
     print("Your Answer is correct")
    else:
      print("Your Answer is Incorrect") 

    Question5 = input("5. What is the capital of Denmark? ").lower() 

    if Question5 == "copenhagen": 
     print("Your Answer is correct")
    else:
      print("Your Answer is Incorrect") 

    Question6 = input("6. What is the capital of Germany? ").lower() 

    if Question6 == "berlin": 
     print("Your Answer is correct")
    else:
      print("Your Answer is Incorrect") 

    Question7 = input("7. What is the capital of Greece? ").lower() 

    if Question7 == "athens": 
     print("Your Answer is correct")
    else:
      print("Your Answer is Incorrect") 

    Question8 = input("8. What is the capital of Ireland? ").lower() 

    if Question8 == "dublin": 
     print("Your Answer is correct")
    else:
      print("Your Answer is Incorrect") 

    Question9 = input("9. What is the capital of Spain? ").lower() 

    if Question9 == "madrid": 
     print("Your Answer is correct")
    else:
      print("Your Answer is Incorrect") 

    Question10 = input("10. What is the capital of Italy? ").lower() 

    if Question10 == "rome": 
     print("Your Answer is correct")
    else:
      print("Your Answer is Incorrect") 
      


    
 elif answer == "no": #Privides the other sequence that if the user does not want to proceed with the quiz it will output "Okay try again next time"
   print("Okay Try Again Next Time!")
 else:
   print("Invalid Response. Answer with Yes or No") #Provides the other output for the beginning that if the user did not answer "Yes" or "No" the program outputs An invalid reponse
                                                 #And restarts the program

