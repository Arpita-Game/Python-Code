try:
    age = int(input("Enter the age: "))
    print(age)
    income = 50000
    n=int(input("Enter the months: "))
    sal = income/n
    print(sal)
except ValueError:
    print("Invalid Value")
except ZeroDivisionError:
    print("Income cannot divide by zero")
