import math
class Student():
    def __init__(self,name,roll,mark):
        self.name=name
        self.roll=roll
        self.mark=mark
    def __str__(self):
        return f"{self.name}:: {self.roll}::{self.mark}"
        #self.name+':'+str(self.roll) +' ::'+ str(self.mark)
        
def Marks(rec,name,roll,mark):
    rec.append(Student(name,roll,mark))
    #print("rec:", rec)
    return rec
    
record=[]
x='y'
while x=='y':
    name= input("enter name of the student: ")
    roll=input("roll no: ")
    mark=input("mark: ")
    record=Marks(record,name,roll,mark)
    #print(record[0])
    x=input("another student? y/n: ")

newlist=[]
n=1
for r in record:
    print(n," : " , r)
    n=n+1
#print(type(record))
newlist=[x for x in record if "v" in x]
print(newlist)

"""score=[[roll],[name,mark]]
i=0
j=0
while i<len(score):
    print("roll no:", score[i], ": name and mark: ", score[i][j])
    i+=1"""
