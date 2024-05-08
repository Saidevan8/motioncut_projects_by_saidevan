#TAKING USER NAME AND MOD OF QUIZ
user=input("ENTER YOUR USER NAME:")
mode=input("ENTER YOUR MODE OF QUIZ \n1:EASY 2:NORMAL 3:HARD---->")
#function for EASY mode of Quiz
def easy():
    print(user,"You select the EASY mode in quiz")
    #questions
    questions=['What is the capital city of Australia?','What is the largest planet in our solar system?','What is the largest mammal in the world?']
    #options
    options=[['1)Sydney','2)Melbourne','3)Canberra','4)Brisbane'],['1)Earth',"2)Mercury",'3)Pluto','4)Jupiter'],['1)Elephant','2)Blue Whale','3)Giraffe','4)Hippopotamus']]
    #original answers
    answers=[3,4,2]
    #taking user answers and store in th u_answers
    u_answer=[]
    for i in range(1,4):
        print('==================================================')#design
        print("Question",i,":",questions[i-1])#printing question
        for j in range(1,5):#printing options for the questions
            print(options[i-1][j-1])
        user_answer=int(input("Enter your answer:"))#taking answer for the user
        u_answer.append(user_answer)
    #verifing answers
    if(u_answer==answers):
        return ['3/3',answers,u_answer]
    else:
        count=0
        for i in range(len(u_answer)):
            if(u_answer[i]==answers[i]):
                count+=1
        return [str(count)+'/'+str(len(answers)),answers,u_answer]
#function for NORMAL mode of Quiz
def normal():
    print(user,"You select the NORMAL mode in quiz")
    #questions
    questions=['Which planet in our solar system has the most moons?','Which element has the atomic number 79 in the periodic table?','Which famous scientist introduced the theory of general relativity?']
    #options
    options=[['1)Saturn',"2)Mars",'3)Neptune','4)Jupiter'],['1)Silver','2)Copper','3)Gold','4)Iron'],['1)Isaac Newton','2)Albert Einstein','3)Galileo Galilei','4)Marie Curie']]
    #original answers
    answers=[4,3,2]
    #taking user answers and store in th u_answers
    u_answer=[]
    for i in range(1,4):
        print('==================================================')#design
        print("Question",i,":",questions[i-1])#printing question
        for j in range(1,5):#printing options for the questions
            print(options[i-1][j-1])
        user_answer=int(input("Enter your answer:"))#taking answer for the user
        u_answer.append(user_answer)
    #verifing answers
    if(u_answer==answers):
        return ['3/3',answers,u_answer]
    else:
        count=0
        for i in range(len(u_answer)):
            if(u_answer[i]==answers[i]):
                count+=1
        return [str(count)+'/'+str(len(answers)),answers,u_answer]
#function for HARD mode of Quiz
def hard():
    print(user,"You select the HARD mode in quiz")
    #questions
    questions=['Who painted the famous artwork "The Last Supper"?','Who wrote the original version of the novel "War and Peace"?','Who painted the famous artwork "The Starry Night"?']
    #options
    options=[['1)Michelangelo','2)Raphael','3)Leonardo da Vinci','4)Titian'],['1)Fyodor Dostoevsky',"2)Leo Tolstoy",'3)Anton Chekhov','4)Ivan Turgenev'],['1)Pablo Picasso','2)Salvador Dalí','3)Claude Monet','4) Vincent van Gogh']]
    #answers
    answers=[3,2,4]
    #taking answers from user and store in th u_answers
    u_answer=[]
    for i in range(1,4):
        print('==================================================')
        print("Question",i,":",questions[i-1])#printing question
        for j in range(1,5):#printing options for the questions
            print(options[i-1][j-1])
        user_answer=int(input("Enter your answer:"))#taking answer for the user
        u_answer.append(user_answer)
    #verifing answers
    if(u_answer==answers):
        return ['3/3',answers,u_answer]
    else:
        count=0
        for i in range(len(u_answer)):
            if(u_answer[i]==answers[i]):
                count+=1
        return [str(count)+'/'+str(len(answers)),answers,u_answer]
#we have 3 modes EASY,NORMAL,HARD so we took conditional statements otherwise we took the 'match' for more modes
if mode=="1":
    result=easy()
    print("------------------------------")
    print("******************************")
    print("Youe result is:",result[0])
    print("******************************")
    for i in range(len(result[1])):
        print("QUESTION",i+1,'----->','CORRECT ANSWERS IS:',result[1][i],'----->','YOUR ANSWE IS:',result[2][i])
    print("------------------------------")
elif mode=="2":
    result=normal()
    print("------------------------------")
    print("******************************")
    print("Youe result is:",result[0])
    print("******************************")
    for i in range(len(result[1])):
        print("QUESTION",i+1,'----->','CORRECT ANSWERS IS:',result[1][i],'----->','YOUR ANSWE IS:',result[2][i])
    print("------------------------------")
else:
    result=hard()
    print("------------------------------")
    print("******************************")
    print("Youe result is:",result[0])
    print("******************************")
    for i in range(len(result[1])):
        print("QUESTION",i+1,'----->','CORRECT ANSWERS IS:',result[1][i],'----->','YOUR ANSWE IS:',result[2][i])
    print("------------------------------")
