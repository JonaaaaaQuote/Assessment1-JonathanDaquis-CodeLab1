List_Name = ["Jake","Zac", "Ian", "Ron", "Sam", "Dave"] #Stores the list on names in a list

while True: #Starts an infinite loop for asking an input for the name your looking for
    print(f'Who are You Looking For?: {List_Name}') #Prints the List_Name
    Name_input = input("Enter the Name of Who Your Looking For: ").title() #Asks for the Input

    if Name_input in List_Name: #Starts the if statement that if Name_input is in List_name it Prints but if not it restarts the program
        print(f"'{Name_input}' This Name is in the Database.")
        break  
    else:
        print(f"'{Name_input}' This Name is not in the Database\n")

def Names(): #Creates a function that prints the Name "Is a Registered name in the Data Base"
    print(Name_input,"Is a Registered name in the Data Base")

Names() #Calls for the function
   

