num=int(input("Enter No.: "))

order=len(str(num))

sum=0

#find the sum of the cube of each digit
temp = num
while temp > 0:
    digit = temp %10
    sum+=digit**order
    temp//=10


#display the result
    if num == sum:
        print(num,"is an Armstrong")
    else:
        print(num,"is not an Armstrong")


