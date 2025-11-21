name_month = { #Adds the Month and the number of days into the dictionary
"January": 31,
"February": 28,
"March" : 31,
"April" : 30,
"May" : 31,
"June" : 30,
"July" : 31,
"August" : 31,
"September" :30,
"October" : 31,
"November" :30,
"December" : 31,
}

month = str(input("Enter The Name of the Month: ")).capitalize() #asks for the input "Enter the name of the month" and capitalizes the input

if month in name_month : #Asks the directory if the input placed by the user is found in the dictionary

    if month == "February": #Asks the system if the input is "February" and asks the user if the year is a leap year and capitalizes the input
        leap_year = input("Is it a Leap Year? Answer Yes or No: ") .capitalize()
        if leap_year == "yes":
            name_month["febuary"] = 29 #Changes the value in the dictionary to 29 days for february

    print (f"{month} has {name_month[month]} days." ) #Prints the month and days. Example ("January has 31 days.")

else:
   print("Invalid Response. Answer with The name of the month") #Provides the stiplulation that if any other answer that isnt a month it will provide a invalid response