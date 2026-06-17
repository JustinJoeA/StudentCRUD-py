status = False
studentsCollection = []


def studentAdd():
    while True:
        StudentName = input('Please input student`s name: ')
        
        try:
            StudentScore = float(input('Please input corresponding student`s score: '))
        except ValueError:
            print('Please input a float type number! (0.00)')
        else:
            studentData = [StudentName, StudentScore]
            
            while True:    
            
                confirmInput = input(f'Input {studentData} into database? (y/n) ')

                if confirmInput == 'y':
                    print(f'{StudentName} data has successfully added to the database!')
                    studentsCollection.append(studentData)
                        
                    while True:
                        continueInput = input('Continue adding student`s data? (y/n) ')
                        if continueInput == 'n':
                            return
                        elif continueInput == 'y':
                            break
                        else:
                            print('Please input a y or n!')  
                            
                elif confirmInput == 'n':
                    while True:
                        continueInput = input('Inputted data would be deleted, continue? (y/n)')
                        if continueInput == 'y':
                            studentData.clear()
                            print('Inputted data has been deleted! ')
                            print('Returning to main menu...')
                            return
                        elif continueInput == 'n':
                            break
                        else:
                            print('Please input a y or n!')  
                            
                else:
                    print('Please input a y or n!') 
                
                break

def studentView():
    if studentsCollection == []:
        print('Student data is still empty!')
        return
    else:
        count = 1
        print(f'{'No.':<5}{'Name':<20} {'Score'}')
        print('-' * 30)
        for student in studentsCollection:
            print(f'{count:<5} {student[0]:<20} {student[1]}')
            count+=1
        return


def studentDelete():
    if studentsCollection == []:
        print('Student data is still empty!')
        return
    else:
        while True:
            count = 1
            print(f'{'No.':<5}{'Name':<20} {'Score'}')
            print('-' * 30)
            for student in studentsCollection:
                print(f'{count:<5} {student[0]:<20} {student[1]}')
                count+=1

            inputDelete = int(input('Please select the student that want to be deleted... (0 to exit)'))
            
            if inputDelete == 0:
                return
            elif type(inputDelete) is int:
                inputDelete = inputDelete - 1
                print(f'{studentsCollection[inputDelete][0]}`s data has been deleted!\n')
                studentsCollection.pop(inputDelete)
                return
            else:
                print('Please enter a valid parameter!')
    

def mainMenu():
    while True:
        print('''
======= MAIN MENU =======
1. Add Student
2. View Student
3. Delete Student
0. Exit
            ''')
        try:
            menuChoice = int(input('Please select an option: '))
        except ValueError:
            print('Please input a number!')
        else:
            if menuChoice == 1:
                studentAdd()
            elif menuChoice == 2:
                studentView()
            elif menuChoice == 3:
                studentDelete()
            elif menuChoice == 0:
                print('Thank you for using our system, have a nice day!\n')
                break
            else:
                print('Please select a valid menu!')
        

while status == False:
    try:
        userLogin=input('Welcome user, do you want to login? (y/n) ')
    except:
        print('Invalid input, please try again!')
    else:
        if userLogin == 'y':
            status = True
            mainMenu()
        elif userLogin == 'n':
            print('Program terminated, have a nice day!')
            break
        else:
            print('Invalid input, please try again!')
