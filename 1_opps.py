# class employee():
    
#     def __init__(self):
#         self.id=101
#         self.sallary=50000
#         self.designation="banglore"
        
#     def travel(self,designation):
#         print(f"my desgnation is {designation} and its my dream city")

# sam=employee()
# print(sam.id)
# sam.travel("banglore")
    
    
class chatbot:
    def __init__(self):
        self.username="sam"
        self.pasword=23
        self.login=True
        self.menu()
        
        
    def menu(self):
        num=int(input("1.login\n2.logout\n3.write a post\n4.massage a friend\n5.exit\n"))
        
        if num==1:
            pass
        elif num==2:
            pass
        elif num==3:
            pass
        elif num==4:
            pass
        elif num==5:
            exit()
        
onj=chatbot()