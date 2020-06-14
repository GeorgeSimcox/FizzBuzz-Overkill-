def menu(menu_message):
    print("\n"*50)
    print(menu_message)
    print("*" * 50)
    print("Welcome to George's Over Kill Fizz Buzz Program")
    print("*" * 50)
    print("")
    print("*" * 50)
    print("(0) Quick Use \n-For all of your quick Fizz Buzz uses-")
    print("*" * 15)
    print("(1) Advance Use\n-For all of your more advance Fizz Buzz uses-")
    print("*" * 15)
    print("(2) Complex Use\n-For all of your more complex Fizz Buzz uses-")
    print("*" * 15)
    print("(8) Settings\n-For all of your Fizz Buzz Settings-")
    print("*" * 15)
    print("(9) Credits\n-Display all the credits for the program-")
    print("*" * 50)
    print("(10) Quit\n-End the program-")
    print("*" * 50)
    menuChoice = intinput(0, 10, "Please input the part of the program that you wish to use: ")
    if menuChoice == 0:
        quickUse()

    if menuChoice == 1:
        advance()

    if menuChoice == 2:
        menu("To be Added 2")

    if menuChoice == 8:
        menu("To be Added 8")

    if menuChoice == 9:
        credit()

    if menuChoice == 10:
        print("*"*50)
        print("Goodbye")
        print("*"*50)
        quit()


def credit():
    print("*" * 50, "\nAll Credit goes to George J Simcox\n", "*" * 49)

    quitOption = charInput("QqRr", "Press Q to Quit or R to repeat: ")
    if quitOption == ("Q" or "q"):
        menu()
    elif quitOption == ("R" or "r"):
        credit()
    else:
        "How did you get thought my validation"


def quickUse():  # The quick use, e.g. Every 3 for Fizz and every 5 for buzz
    quickStart = settingLookUp("QuickRunStart")  # get the setting value from the setting.txt
    quickEnd = settingLookUp("QuickRunEnd")  # get the setting value from the setting.txt

    intQuickStart = int(quickStart[1])  # for some reason this is needed to convertto intger
    intQuickEnd = int(quickEnd[1])
    intQuickEnd = intQuickEnd + 1  # plus cos python range go upto the last value.

    quickFizz = settingLookUp("quickFizz")  # get the setting value from the setting.txt
    quickBuzz = settingLookUp("quickBuzz")  # get the setting value from the setting.txt

    intquickFizz = int(quickFizz[1])
    intquickBuzz = int(quickBuzz[1])

    for i in range(intQuickStart, intQuickEnd):
        output = []
        if i % intquickFizz == 0:
            output.append("Fizz")
        if i % intquickBuzz == 0:
            output.append("Buzz")
        if output == []:
            output.append(i)
        print(output)
    i = +1

    quitOption = charInput("QqRr", "Press Q to Quit or R to repeat: ")
    if quitOption == ("Q" or "q"):
        menu("Returning to Menu")
    elif quitOption == ("R" or "r"):
        quickUse()
    else:
        "How did you get thought my validation"


def advance():
    Start= intinputinfinate("What value do you want to start at? ")
    End = intinputinfinate("What value do you want to start at? ")

    advFizz = settingLookUp("advFizz")  # get the setting value from the setting.txt
    advBuzz = settingLookUp("advBuzz")  # get the setting value from the setting.txt

    intadvFizz = int(advFizz[1])
    intadvBuzz = int(advBuzz[1])

    if Start > End:
        print("Start is bigger than End, Switching Values")
        Start,End=End,Start

    BuzzTotal=0
    FizzTotal=0

    for i in range(Start, End):
        output = []
        if i % intadvFizz == 0:
            output.append("Fizz")
            BuzzTotal += 1
        if i % intadvBuzz == 0:
            output.append("Buzz")
            FizzTotal +=1
        if output == []:
            output.append(i)
        print(output)
    i = +1

    print("*"*50,"\nSummary:")
    print("Total Fizz:",FizzTotal)
    print("Total Buzz:",BuzzTotal)
    print("Total Numbers Checked:",(End-Start))
    print("*"*50)

    quitOption = charInput("QqRr", "Press Q to Quit or R to repeat: ")
    if quitOption == ("Q"):
        menu("Returning to Menu")
    elif quitOption == ("q"):
        menu("Returning to Menu")
    elif quitOption == ("R"):
        advance()
    elif quitOption == ("r"):
        advance()
    else:
        "How did you get thought my validation?"


def settingLookUp(settingSearch):
    foundSetting = []       #declaring list.
    import csv

    with open("Setting.txt", ) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')

        for row in csv_reader:

            try:
                if row[0] == settingSearch:
                    print("*" * 50)
                    print("The Setting", row[0], "has the value of", row[1], "it is classed as a", row[2])  # for debugging
                    print("*" * 50)
                    foundSetting = [row[0], row[1], row[2]]
                    break

            except IndexError: #no data on line (set temp=1 for no reason but to stop indentation error)
                temp=1

        csv_file.close()

    with open("Setting.txt","a" ) as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',')

        if foundSetting == []: # setting not found!

            print("*" * 50)
            print("Error Unable to located setting")
            print("*" * 50)

            csv_writer.writerow(settingDefaults(settingSearch))


        else: # setting not found
            return foundSetting

    csv_file.close()


def settingDefaults(settingSearch):
    import csv
    print("*" * 50)
    print("Restoring Defualt Setting For:",settingSearch)
    print("*" * 50)
    foundDefaultSetting = []

    with open("SettingDefault.txt") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')

        for row in csv_reader:

            try:
                if row[0] == settingSearch:
                    #print("*" * 50)
                    #print("The Setting", row[0], "has the value of", row[1], "it is classed as a", row[2])  # for debugging
                    #print("*" * 50)
                    foundDefaultSetting = [row[0], row[1], row[2]]
                    break

            except IndexError:  # no data on line (set temp=1 for no reason but to stop indentation error)
                temp = 1


        if foundDefaultSetting == []:               #if no defulat settings is found
            print("*"*50)
            print("Error Unable to located default setting")
            print("Please input the default value")
            print("Title: ",settingSearch)
            value= input("Please input the value of the setting: ")
            type= input("Please input the type of the setting: ")
            print("*" * 50)
            with open("SettingDefault.txt", "a") as csv_file:
                csv_writer = csv.writer(csv_file, delimiter=',')

                foundDefaultSetting = [settingSearch, value, type]

                csv_writer.writerow(foundDefaultSetting)

            return foundDefaultSetting

        else:
            return foundDefaultSetting

    csv_file.close()


def modifyingSettings():
    print("To Be Added")


def intinput(min, max, message):
    while True:
        try:
            inti = int(input(message))
            if inti < min:
                print("Sorry the number enter is to small, please enter a number between:",min,"and",max)
            elif inti > max:
                print("Sorry the number enter is to large, please enter a number between:",min,"and",max)
            else:
                return (inti)
        except ValueError:
            print("Sorry you didn't enter an interger, please could you input an interger(A whole number).")


def intinputinfinate(message):
    while True:
        try:
            inti = int(input(message))
            return (inti)
        except ValueError:
            print("Sorry you didn't enter an interger, please could you input an interger(A whole number).")


def charCompare(allowed, charInput, errorCode):
    allowedReturn = ""

    for i in range(len(allowed)):
        if allowed[i] == charInput:
            # print("Correct", allowed[i])
            allowedReturn += str(allowed[i])
    if len(allowedReturn) == 0:
        return (errorCode)
    else:
        return (allowedReturn)


def charInput(allowed, message):
    while True:
        try:
            chari = (input(message))
            if len(chari) == 1:
                if (charCompare(allowed, chari, "Error")) == chari:
                    return (chari)
                else:
                    print("Invalid character")

            else:
                print("The Value inputted was to long or contained no value")
        except ValueError:
            print("Please input an character")


def startUp():
    menu("Starting Up")

startUp()