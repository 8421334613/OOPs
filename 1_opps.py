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
        num=int(input("1.sinup\n2.signin\n3.write a post\n4.massage a friend\n5.exit\n"))
        
        if num==1:
            self.sinup()
        elif num==2:
            self.signin()
        elif num==3:
            self.mypost()
        elif num==4:
            self.massage()
        elif num==5:
            exit()
            
    def sinup(self):
        self.username=input("enter your name:")
        self.pasword=int(input("enter your pasword:"))
        print("sucessfully sinup")
        print("\n")
        self.menu()
        
    def signin(self):
        use=input("enter your name:")
        passw=int(input("enter your pasword:"))
        if use==self.username and passw==self.pasword:
            print("sucessfully signin")
            self.menu()
        else:
            print("press 1 and sign up first")
            self.menu()
    def mypost(self):
        if self.login==True:
            post=input("write your post:")
            print("your post is:",post)
            
    def massage(self):
        if self.login==True:
            friend=input("enter your friend name:")
            msg=input("enter your massage:")
            print(f"your massage to {friend} is:{msg}")
            
    def exit(self):
        print("thank you for using our app")
        self.login=False
        
    
        
onj=chatbot()
onj.sinup()