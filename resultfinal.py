math =  int(input("Enter your math number: "))
physics =  int(input("Enter your physics number: "))
biology =  int(input("Enter your biology number: "))
chemestry =  int(input("Enter your chemestry number: "))
english =  int(input("Enter your english number: "))
bangla =  int(input("Enter your bangla number: "))

if(math>100):
    print("something is problem in 'math'")


elif(physics>100):
    print("something is problem in 'physics'")
elif(biology>100):
    print("something is problem in 'biology'")
elif(chemestry>100):
    print("something is problem in 'chemestry'")
elif(english>100):
    print("something is problem in 'english'")
elif(bangla>100):
    print("something is problem in 'bangla'")

result = (math+physics+biology+chemestry+english+bangla)/6
print("your avarage mark is ", result)


if(100>result>80):
    print("your grade: A+")
    print("your gpa: 5.00")

elif(80>result>70):
    print("your grade: A")
    print("your gpa: 4.__")
elif(70>result>60):
    print("your grade: A-")
    print("your gpa: 3.__")
elif(70>result>60):
    print("your grade: B")
    print("your gpa: 3.__")
elif(60>result>50):
    print("your grade: C")
    print("your gpa: 3.__")
elif(50>result>33):
    print("your grade: D")
    print("your gpa: 2.__")
elif(result<33):
    print("FAil")






