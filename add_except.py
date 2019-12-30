#!/usr/bin/python3

#  now using  exception handling in python3
import pyttsx3,time
try :
	print("Enjoy add and div program :- ")
	n1=input("plz enter first number : ")
	n2=input("plz enter second number : ")

	sum=int(n1)+int(n2)
	output=int(n1)/int(n2)
	print("sum of the numbers is ",sum)
	print("div of the numbers are ",output)

except  (NameError,ValueError):
	print("Plz type numbers only ")
	s=pyttsx3.init()
	s.say("learn about numbers first")
	s.runAndWait()
except  ZeroDivisionError:
	print("sorry apse nhi ho payega :- ")
	time.sleep(2)
	print("plz don't use 0 as a number ")


except:
	print("may be u need to learn some maths first !!")


finally :
	print("great job we are improving ..")

