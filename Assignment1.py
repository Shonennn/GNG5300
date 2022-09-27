#version1 Basic function finished HOWEVER,need to deal with fiel I/O 

    
class course:
    def __init__(self, courseName,courseNum, stuNum):
        self.courseName = courseName
        self.courseNum = courseNum
        self.stuNum = stuNum
        global Course
        Course={}
class stu:
    def __init__(self, stuName,stuNum, courseNum):
        self.stuName = stuName
        self.stuNum = stuNum
        self.courseNum = courseNum
        global Student
        Student={}
    def enrolCourse(stuNum,courseNum):
        stuNum=input("Input your student number to confirm:")
        courseNum=input("Input the Course Number you want to enroll:")
        tempDict={stuNum:courseNum}
        Course.update(tempDict)
    def dropCourse(stuNum,courseNum):
        stuNum=input("Input your student number to confirm:")
        courseNum=input("Input the Course Number you want to enroll:")
        Course.pop(stuNum,courseNum)
sel=course(aaa,120)


    
  