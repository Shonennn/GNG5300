#version1 Basic function finished HOWEVER,need to deal with fiel I/O 

class course:
    '''def __init__(self, courseName,courseNum, stuNum):
        self.courseName = courseName
        self.courseNum = courseNum
        self.stuNum = stuNum'''
    global Course
    Course={}
        
    def addCourse(self):
        courseNum=input("Input your Course number to add:")
        courseName=input("Input the Course name you want to add:")
        tempDict={courseNum:courseName}
        Course.update(tempDict)
        print("Successfully updated:",Course)

    def searchCourse(self):
        courseNum = input("Input the course number:")
        print("Here's your search result:", Course.get(courseNum))

    def showCourse(self):
        print(str(Course))

    def delCourse(self):
        courseName=input("Input your Course number to delete:")
        Course.pop(courseName)
        print("Successfully deleted:",Course)
        
    def updateCourse(self):
        courseNum=input("Input your Course number to update:")
        courseName=input("Input the Course name you want to update:")
        Course[courseNum]=courseName
        print("Successfully updated:",Course)

class stu:
    '''def __init__(self, stuName,stuNum, courseNum,score):
        self.stuName = stuName
        self.stuNum = stuNum
        self.courseNum = courseNum
        self.score=score'''

    global Student
    global Grades
    global Enroll
    Student = {'300250':'Alex'}
    Grades = {'300250':['230','90']}
    Enroll={}
    def enrolCourse(stuNum):
        stuNum=input("Input your student number to confirm:")
        courseNum=input("Input the Course Number you want to enroll:")
        
        if (stuNum in Enroll & (courseNum!=Student.get(stuNum))): 
            # this is to make sure student and admin can add more than one course
            # and make sure there is no repeat course being added          
            tempValue=[Student.get(stuNum)].append(courseNum)
            tempDict={stuNum:tempValue}
            Enroll.update(tempDict)
        else:
            tempDict={stuNum:courseNum}
            Enroll.update(tempDict)
        print(Enroll)
    def dropCourse(stuNum):
        stuNum=input("Input your student number to confirm:")
        Enroll.pop(stuNum)

class admin(stu): 
    '''def __init__(self, adminNum):
        self.adminNum = adminNum'''
    def addStu(self):
        stuNum=input("Input the student number you want to add:")
        stuName=input("Input the student name you want to add:")
        tempDict={stuNum:stuName}
        Student.update(tempDict)
        print("Successfully added:")
        print(str(Student))


    def searchStu(self):
        stuNum = input("Input the student number:")
        print("Here's your search result:", Student.get(stuNum))
    def showStu(self):
        print(str(Student))

    def delStu(self):
        stuNum=input("Input the student's student number you want to delete:")
        Student.pop(stuNum)
        print("Successfully deleted:")
        print(str(Student))

    def updateStu(self):
        stuNum=input("Input the student number you want to update:")
        stuName=input("Input the student name you want to update:")
        if stuNum in Student:
            Student[stuNum]=stuName
            print("Successfully updated:",Student)
        else:
            print("This student doesn't exist")

    def addGrades(self):
        tempValue=[]
        stuNum=input("Input the student number:")
        courseNum=input("Input the coursenumber:")
        grade=input("Input the grade of this person:")
        tempValue=[courseNum,grade]
        tempDict={stuNum:tempValue}
        Grades.update(tempDict)
        print("Successfully added:")
        print(str(Grades))

    def deleteGrades(self):
        stuNum=input("Input the student number:")
        Grades.pop(stuNum)
        print("Successfully deleteed:")
        print(str(Grades))

    def searchGrades(self):
        stuNum=input("Input the student number:")
        print("Here's your search result:",Grades.get(stuNum))

    def updateGrades(self):
        tempValue=[]
        stuNum=input("Input the student number:")
        if stuNum in Grades:
            courseNum = input("Input the coursenumber:")
            tempValue.append(courseNum)
            grade = input("Input the score:")
            tempValue.append(grade)
            Grades[stuNum] = tempValue
            print("Successfully updated:", str(Grades))
        else:
            print("This student doesn't exist")

class user:
   
    global sysuser
    sysuser={'300250':0,'300':1}
    # 0 means admin; 1 means student
    def adminMenu(self):
        inputFunc=''
        while(inputFunc!=0):
            operater=admin()
            print("Please choose among the following functions:")
            print("1.User management")
            print("2.Course management")
            print("3.Grades management")
            print("4.Enroll management")
            print("0.Exit")
            inputFunc=input()
            if inputFunc=='1':
                userFlag=''
                print("Please choose among the following functions:")
                print("1.Add student")
                print("2.Update student")
                print("3.Delete student")
                print("4.Search student")
                print("5.Show all students")
                print("0.Go back to previous menu")
                userFlag=input()
                while(userFlag):
                    if userFlag=='1':
                        operater.addStu()
                    elif userFlag=='2':
                        operater.updateStu()
                    elif userFlag=='3':
                        operater.delStu()
                    elif userFlag == '4':
                        operater.searchStu()
                    elif userFlag == '5':
                        operater.showStu()
                    elif userFlag=='0':
                        break
                    self.adminMenu()
            elif inputFunc=='2':
                courfunc=course()
                courseFlag=''
                print("Please choose among the following functions:")
                print("1.Add course")
                print("2.Update course")
                print("3.Delete course")
                print("4.Search course")
                print("5.Show all courses")
                print("0.Go back to previous menu")
                courseFlag=input()
                while(courseFlag):
                    if courseFlag=='1':
                        courfunc.addCourse()
                    elif courseFlag=='2':
                        courfunc.updateCourse()
                    elif courseFlag=='3':
                        courfunc.delCourse()
                    elif courseFlag == '4':
                        courfunc.searchCourse()
                    elif courseFlag == '5':
                        courfunc.showCourse()
                    elif courseFlag=='0':
                        break
                    self.adminMenu()
            elif inputFunc=='3':
                gradesFlag=''
                print("Please choose among the following functions:")
                print("1.Add grades")
                print("2.Update grades")
                print("3.Delete grades")
                print("0.Go back to previous menu")
                gradesFlag=input()
                while(gradesFlag):
                    if gradesFlag=='1':
                        operater.addGrades()
                    elif gradesFlag=='2':
                        operater.updateGrades()
                    elif gradesFlag=='3':
                        operater.deleteGrades()
                    elif gradesFlag=='0':
                        break
                    self.adminMenu()
            elif inputFunc=='4':
                enrollFlag=''
                print("Please choose among the following functions:")
                print("1.Enroll student")
                print("2.Drop student")
                print("0.Go back to previous menu")
                enrollFlag=input()
                while(enrollFlag):
                    if enrollFlag=='1':
                        operater.enrolCourse()
                    elif enrollFlag=='2':
                        operater.dropCourse()
                    elif enrollFlag=='0':
                        break
                    self.adminMenu()
            else:
                break
    def stuMenu(self):
        stuOperater=stu()
        enrollFlag=''
        print("Please choose among the following functions:")
        print("1.Enroll course")
        print("2.Drop course")
        print("0.Go back to previous menu")
        enrollFlag=input()
        while(enrollFlag):
            if enrollFlag=='1':
                stuOperater.enrolCourse()
            elif enrollFlag=='2':
                stuOperater.dropCourse()
            elif enrollFlag=='0':
                break

            self.stuMenu()
    def login(self):
        userNum=input("Input your user number:")
        if(sysuser[userNum]):
            print("Your user type is admin")
            self.adminMenu()
        else:
            print("Your user type is student")
            self.stuMenu()
        
ape=user()
ape.login()


    
  