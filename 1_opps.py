class employee():
    
    def __init__(self):
        self.id=101
        self.sallary=50000
        self.designation="banglore"
        
    def travel(self,designation):
        print(f"my desgnation is {designation} and its my dream city")

sam=employee()
print(sam.id)
sam.travel("banglore")
    