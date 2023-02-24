#create a funtion that user inputs his age
#the function prints number of months user has lived

age = int(input("Enter your age"))
print(age)

def multiplytwonums(num1, num2):


    results = (num1 * num2)
    print(f"you have lived {results} months")
multiplytwonums(age, 12)




def calculate_months():
    age =int(input("enter your age"))
    months_lived = age * 12
    print(f"you have lived{months_lived} months")

calculate_months()
