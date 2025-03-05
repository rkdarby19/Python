name = input("Enter name: ")

try:
    age = int(input("Enter age: "))
    
except Exception as xcpt:
    print("Error:", xcpt)
