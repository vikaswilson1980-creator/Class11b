num=int(input("Enter a number to check if they are amstrong numbers or not:"))
sum=0
temp=num
while temp>0:
    digit= temp%10
    sum= sum+digit**3
    temp= temp//10
print(sum)
if(num==sum):
    print(num,"is an amstrong number")
else:
    print(num,"is not am amstrong number")