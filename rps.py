import random
a={1:'R',2:'P',3:'S'}

while(True):
	c=a[random.randint(1,3)]
	p=input("enter r or p or s :")
	print("Comp chooses",c)
	if(c==p):
		print("tie")
	elif((c=='R' and p=='S') or (c=='P' and p=='R') or (c=='S' and p=='P')):
		print("comp wins ")


	else:
		print("player wins")
		
		
		
		

