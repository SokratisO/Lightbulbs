import random

#Lists
answerList = {'a': '001' ,'b' : '010' ,'c' : '011' , 'd' : '100'}
commandList = ['001','100','101','010','111']
numberList = commandList + ['011','110','111']
choices = {'001': 1,'010': 2,'011': 3,'100': 4,'101': 5,'110': 6,'111': 7}
choicesExt = {'001': 8,'010': 9,'011': 10,'100': 11,'101': 12,'110': 13,'111': 14}

#Read the answer file
with open ('ExamAnswers.txt','r') as rf:
    print("Answers taken from the answer sheet")
    contents = rf.read()

print(contents)

print("\n")


#Debug show lists
#print(commandList)
#print(numberList)

#Show table
print(" Hello ")
print(" This will be a communication software to use with a 3 lightbulb")
print(" The commands for the person asking and answering questions will be as follows\n")
print(" Ask\t\t|Code|\t Answer\t\t|Code|")
print(" ---------------------------------------------")
print(" Hello\t\t| 110|\t Hello back\t| 011|")
print(" Error\t\t| 001|\t Error\t\t| 001|")
print(" Finish\t\t| 100|\t Finish\t\t| 100|")
print(" Add 7\t\t| 101|\t Not Sure\t| 010|")
print(" ---------------------------------------------")
print(" 0 0 0\t\t  -->\t\t\t 4 2 1\n")
print(" 1 1 1\t\t  -->\t\t\t  Exit\n")
print(" Begin the communication \n")

#basic menu
menu =1
temp=0
while menu == 1:
    #handshake
    code1 = input("1--->")
    while code1 != "110":
        print("There was an error detected. No Handshake confirmed")
        code1 = input("1--->")
    print("\t\t\t011<---1")
    #message
    code2 = input("2--->")
    while code2 not in numberList:
        print(" no such command")
        code2 = input("2--->")
    #command
    code3 = input("3--->")
    while code3 not in commandList:
        print(" no such command")
        code3 = input("3--->")
    if code3 == '001':
        print ("restarting with error code 001")
    elif code3 == '111':
        input("Exiting, press return to continue...")
        break
    else:

        #associate the choice with a number
        if code3 == '101':
            result = choicesExt.get(code2, 'default')
        else:
            result = choices.get(code2, 'default')

        #find the answer from the file
        foundAnswer=int(contents.find(str(result)))
        if result >9:
            foundAnswer+=3
        else:
            foundAnswer+=2
        foundAnswerToEncode=(contents[foundAnswer])
        result2 = answerList.get(foundAnswerToEncode)
        print("\t\t\t"+str(result2)+"<---2")
        print("\t\t\t100<---3")
    
