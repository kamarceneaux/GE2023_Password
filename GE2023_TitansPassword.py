import json, time

def main():
    titanName = askForName()                    #First, asks for the name.
    jsonFileName = createDataFile(titanName)    #If a data file isn't found for the selected Titan, a new one will be created
    login(jsonFileName)                         #Asks the user for the password and security question in their data file.
    viewDataFile(jsonFileName)                  #If both the password and security question are successful, allows access into the file.

def askForName():
    titanNames = ["Robin", "Starfire", "Raven", "Cyborg", "Beast Boy"]                          #Defines the names for each Teen Titan. No encryption needed because everyone knows who the Teen Titans are
    inputName = input("Who is attempting to access their files? (ONE INPUT ALLOWED) ").title()  #Gathers user input for who accesses the program
    if inputName in titanNames:                                                                 #Checks to see if the input name is in the list
        print("Access granted!")                                                                #If it is, grants access
        return inputName                                                                        #Returns the value of inputName to the rest of the program
    elif inputName == "Slade Wilson" or inputName == "Slade" or inputName == "Deathstroke":     #If input name isn't in the list and includes one of Slade's aliases...
        print("Really, Slade?? Access NOT granted!")                                            #Ends program immediately. Sorry, Slade!
        time.sleep(5)                                                                           #Waits five seconds
        exit()                                                                                  #Ends program
    else:                                                                                       #If input name isn't in the list and isn't Slade
        print("User not found in registry! Ending program...")                                  #Prints that user isn't found
        time.sleep(5)                                                                           #Waits five seconds
        exit()                                                                                  #Ends program

def createDataFile(titanName):
    jsonFileName = str(titanName) + str(".json")                                                                        #Sets the name of the .json file to the titan name + .json (example being Robin.json or Cyborg.json)
    try:
        dataFile = open(jsonFileName, "r")                                                                              #Tries to open said .json file first and see if it exists
        dataFile.close()                                                                                                #If file is found, immediately recloses it
        print("File for", titanName, "found successfully!")                                                             #Prints that file has been found

    except FileNotFoundError:                                                                                           #If the .json file can't be found, it likely doesn't exist and a new one needs to be made
        creating = True                                                                                                 #Creates boolean to determine if file is currently being created
        input("Data file not found for " + titanName + "! Input anything to begin creating a new file. ")               #Prints that file couldn't be found, and prompts the user to begin creating a new one
        while creating == True:                                                                                         #While the boolean is true, creation process is executed
            password = input("What will be a good password for " + titanName + "? ")                                    #Prompts user for password input
            securityQuestion = input("What would you like your security question to be? ")                              #Prompts user for security question input
            securityAnswer = input("And the answer to your security question? ")                                        #Prompts user for answer to security question
            print("\nPassword:", password, "\nSecurity Question:", securityQuestion, "\nAnswer:", securityAnswer)       #Prints the inputted password, security question, and answer for confirmation
            done = input("\nAre you okay with this? Y/N ").upper()                                                      #Prompts the user to input Y or N if they're okay with it
            if done == "Y":
                print("Great! Please login again.\n")                                                                   #If Y is inputted, login process can begin
                creating = False                                                                                        #Sets boolean to false so creation process can end
            elif done == "N":
                print("Please try again.")                                                                              #If N is inputted, restarts creation process
            else:
                print("Invalid input. Restarting...")                                                                   #If an invalid input is inputted, restarts creation process

        fileContents = {"titan name": titanName, "password": password, "security question": securityQuestion, "answer": securityAnswer, "contents": "Empty"}      #Creates dictionary assigning Titan name, password, security question, and answer to their respective values
        fileJson = json.dumps(fileContents)     #Dumps contents of dictionary into a .json file format
        dataFile = open(jsonFileName, "w")      #Opens a new .json file named after jsonFileName (like Robin.json) with the intent to write to it
        dataFile.write(fileJson)                #Writes contents of dictionary into the created .json file
        dataFile.close()                        #Closes file after it's finished being written in

    return(jsonFileName)                        #Returns the name of the .json file to the rest of the program so other functions can access it

def login(jsonFileName):
    dataFile = open(jsonFileName, "r")                                                  #Opens .json file using the name of the .json file
    data = json.loads(dataFile.read())                                                  #Loads content of .json file onto variable "data"
    
    password = data["password"]                                                         #Extracts password from file and assigns to variable
    securityQuestion = data["security question"]                                        #Extracts security question from file and assigns to variable
    answer = data["answer"]                                                             #Extracts answer from file and assigns to variable
    correct = 0

    passwordAttempts = 3                                                                #Sets the total amount of password attempts to 3
    while passwordAttempts != 0:                                                        #While password attempts don't equal zero, allows password attempts
        passwordInput = input("What is the passsword? ")                                #Asks for user input for password
        if passwordInput == password:                                                   #If password input is equal to actual password...
            print("Correct!")                                                           #Marks password as correct
            passwordAttempts = 0                                                        #Sets password attempts to zero since password is correct
            correct = 1                                                                 #Sets variable "correct" to 1 
        else:
            passwordAttempts = passwordAttempts - 1                                     #If password input is not equal to actual password, removes one attempt
            print("Incorrect. Attempts remaining:", passwordAttempts)                   #Prints amount of attempts remaining

    if correct == 1:                                                                    #If "correct" is equal to 1, or if password has been successfully guessed, moves on to security question
        questionAttempts = 3                                                            #Sets the total amount of question attempts to 3
        while questionAttempts != 0:                                                    #While question attempts don't equal zero, allows question attempts
            questionInput = input("Security question: " + securityQuestion + " ")       #Prints security question, and prompts user for answer
            if questionInput == answer:                                                 #If answer input is equal to actual answer...
                print("Correct!")                                                       #Marks answer as correct
                questionAttempts = 0                                                    #Sets password attempts to zero since password is correct
                correct = 2                                                             #Sets variable "correct" to 2
            else:
                questionAttempts = questionAttempts - 1                                 #If answer input is not equal to answer answer, removes one attempt
                print("Incorrect. Attempts remaining:", questionAttempts)               #Prints amount of attempts remaining
    else:
        print("You are out of password attempts. Ending program...")                    #If password attempts run out, ends program
        time.sleep(5)                                                                   #Waits five seconds
        exit()                                                                          #Ends program

    if correct == 2:                                                                    #If "correct" is equal to 2, or if password and question have been successfully guessed, allows access
        print("Password and security question both correct. Welcome in!")               #Welcome in!
    else:
        print("You are out of question attempts. Ending program...")                    #If question attempts run out, ends program
        time.sleep(5)                                                                   #Wait five seconds
        exit()                                                                          #Ends program

def viewDataFile(jsonFileName):
    dataFile = open(jsonFileName, "r")                                                  #Opens .json file using the name of the file
    data = json.loads(dataFile.read())                                                  #Loads content of .json file onto variable "data"

    print("Hello,", data["titan name"] +". Welcome to the Teen Titans Registry.")       #Prints the titan's name using contents of .json file
    while True:                                                                         #Keeps going until program ends
        dataFile = open(jsonFileName, "r")                                              #Reopens .json file in order to refresh it, allowing overwrites to be viewed
        data = json.loads(dataFile.read())                                              #Reloads content of file into variable "data"
        selection = input("\nTo view the contents of your file, type View. \nTo overwrite the contents of your file, type Overwrite. \nTo end the program, type Exit. ").title()        #View views content; Overwrite overwrites content; Exit exits
        if selection == "View":
            print("\n" + data["contents"])                                                     #If the selection is View, prints what's written in the file for "contents"
        elif selection == "Overwrite":
            write = input("Please type what you would like to overwrite your file with. \n")    #If the selection is Overwrite, prompts the user to overwrite the contents of the file
            dataOverwrite = {"titan name": data["titan name"], "password": data["password"], "security question": data["security question"], "answer": data["answer"], "contents": write}   #Redoes all of the data inside of the file, except for the variable "contents" now being what was written
            dataFile = open(jsonFileName, "w")                                          #Opens file with intent to write
            dataJson = json.dumps(dataOverwrite)                                        #Dumps contents of overwritten file into variable dataJson
            dataFile.write(dataJson)                                                    #Writes contents of dataJson onto the data file
            dataFile.close()                                                            #Temporarily closes file
        elif selection == "Exit":
            print("Ending program. Goodbye!")                                           #If the selection is Exit, exits
            time.sleep(5)                                                               #Waits five seconds
            exit()                                                                      #Closes program
        else:
            print("Invalid input. Please try again.")                                   #If the selection is anything other than what was listed, asks to try again
    
main()  #Calls to main program and begins everything
