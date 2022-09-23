#version1 Basic function finished HOWEVER,need to deal with the problem of function's scope 
class stu_Grades:
    global Grades
    Grades={'lisa':90,'jack':80}
    inputFunc=''
    def add():
        Name=input("Input the name:")
        grade=input("Input the grade of this person:")
        tempDict={Name:grade}
        Grades.update(tempDict)
        print("Successfully added:")
        print(str(Grades))
    def delete(name):
        Grades.pop(name)
        print("Successfully deleteed:")
        print(str(Grades))
    def search(name):
        print("Here's your search result:",Grades.get(name))
    def update(name):
        Score=input("Input the score:")
        Grades[name]=Score
        print("Successfully updated:")
        print(str(Grades))
    while(inputFunc!=0):
        print("Please choose the following functions:")
        print("1.Add user's grade")
        print("2.Search user's grade")
        print("3.Update user's grade")
        print("4.Delete user")
        print("0.Exit")
        inputFunc=input()
        if inputFunc=='1':
            Grades=add()
        elif inputFunc=='2':
            Name=input("Input the name you want to search:")
            search(Name)
        elif inputFunc=='3':
            Name=input("Input the person'sname you that want to update score:")
            update(Name)
        elif inputFunc=='4':
            Name=input("Input the name you want to delete:")
            delete(Name)
        else:
            break
  