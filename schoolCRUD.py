import json


class Student:
    def __init__(self, name, grade, gpa):
        self.name = name
        self.grade = grade
        self.set_gpa(gpa)
    
    def get_gpa(self):
        return self.__gpa
    
    def set_gpa(self, gpa):
        if 0.00 < gpa < 4.00:
            self.__gpa = gpa
        else:
            raise ValueError('GPA value must be inbetween 0.00 and 4.00!')
    


with open('studentData.json', 'r') as f:
    studentData = json.load(f)
    students = []
    for student in studentData["student"]:
        studentList = Student(student["name"], student["grade"], student["gpa"])
        students.append(studentList)



def studentUpdate():
    updatedDataStudent = {"student":[]}
    for student in students:
        updatedDataStudent["student"].append({"name": student.name, "grade": student.grade, "gpa": student.get_gpa()})
        
    with open('studentData.json', 'w') as f:
        json.dump(updatedDataStudent, f, indent=4)
        


def studentAdd():
    while True:
        studentName = ''
        while studentName == '':
            studentName = input('Please input student`s name: ')
            if studentName == '':
                print('Student name must be filled!')
            
        try:
            while True:
                studentGrade = int(input('Please input student grade: '))
                if 9 <= studentGrade <= 12:
                    try:
                        studentGpa = float(input('Please input corresponding student`s score: '))
                    except ValueError:
                        print('Please input a float type number! (0.00)')
                    else:
                        studentData = {"name":studentName,"grade":studentGrade,"gpa":studentGpa}
                        break
                else:
                    print('Please input a number between 9 and 12!')
        except ValueError:
            print('Please input a number!')     
            
        while True:    
            while True:
                try:
                    tempData = Student(studentData["name"], studentData["grade"], studentData["gpa"])
                    students.append(tempData)
                    break
                except ValueError as e:
                    print(e)
                    studentGpa = float(input('Please re-enter a valid GPA: '))
                    studentData["gpa"] = studentGpa
            
            confirmInput = input(f'Input {studentData} into database? (y/n) ')

            if confirmInput == 'y':
                print(f'{studentName} data has successfully added to the database!')
                studentUpdate()
                
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
            
            
        
def studentView():
    count = 1
    if students == []:
        print('Student data is still empty!')
        return
    else:
        print(f'{'No.':<5}{'Name':<20} {'Grade':<10} {'Score:'}')
        print('-' * 45)
        for student in students:
            print(f'{count:<5} {student.name:<20} {student.grade:<10} {student.get_gpa()}')
            count += 1
        return



def studentDelete():
    if students == []:
        print('Student data is still empty!')
        return
    else:
        while True:
            count = 1
            print(f'{'No.':<5}{'Name':<20} {'Grade':<10} {'Score:'}')
            print('-' * 45)
            for student in students:
                print(f'{count:<5} {student.name:<20} {student.grade:<10} {student.get_gpa()}')
                count += 1
            
            try:    
                inputDelete = int(input('Please select the student that want to be deleted... (0 to exit)'))
                if inputDelete == 0:
                    return
                elif type(inputDelete) is int:
                    inputDelete = inputDelete - 1
                    print(f'{students[inputDelete].name}`s data has been deleted!\n')
                    students.pop(inputDelete)
                    studentUpdate()
                    return
                else:
                    print('Please enter a valid parameter!')
            except ValueError:
                print('Please input a number!')
            except IndexError:
                print('Please input available column only!')
            

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


mainMenu()