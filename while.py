#first pattern program
i=1
while i<=5:
    print('*'*i)
    i+=1

#second program for guessing number
S_num = int(input("Enter the secret number: "))
i=0
while i<=3:
    guess=int(input("enter the guess number: "))
    i+=1
    if (guess==S_num):
        print("You win")
        break
    else:
        print("You are failed")

