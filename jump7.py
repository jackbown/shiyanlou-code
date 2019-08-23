i = 1;
while(i<=100):
    if(i%7==0):
	i+=1
	continue
    elif('7' in str(i)):
	i+=1
	continue
    else:
	print(i)
	i+=1


