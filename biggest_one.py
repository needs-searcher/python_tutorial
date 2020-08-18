num1=int(input('num1:'))
num2=int(input('num2:'))
num3=int(input('num3:'))
result=0

if num1>=num2:
	if num1>=num3:
		result=num1
	else:
		result=num3
else :
	if num2>=num3:
		result=num2
	else:
		result=num3
print(result)
      
