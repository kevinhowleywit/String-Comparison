#just wrote this so i could check md5 values for an assignment
#very simple.....nothing amazing
def main():
	print("Enter the first string for comparison")
	string1=input()
	print("")
	print("Enter the string to compare")
	string2=input()	
	if string1.lower()==string2.lower():
		print("Strings are the same")
		print("Compare more strings??? y/n")
		choice=input()
		if choice.lower()=="y":
			main()
		else:
			#anything other than y/Y causes the program to quit
			exit
	else:
		print("Strings are Different")
		print("Compare more strings??? y/n")
		choice=input()
		if choice.lower()=="y":
			main()
		else:
			#anything other than y/Y causes the program to quit
			exit

#main route
main()