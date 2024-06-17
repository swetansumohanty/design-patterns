"""
Observer Design Pattern
=======================
It is a behavioral design pattern,
that allows some objects to notify other objects about changes in their state.
"""

class Subscriber:
    
    def __init__(self,name,channel_owner):
        self.name = name
        self.channel_owner = channel_owner
    
    def update(self):
        print(f"Hey, {self.name.upper()}  {type(self.channel_owner).__name__} has uploaded a new video ! < watch now >")
 

class Publisher:

    subscribers: list = []

    def __init__(self,name):
        self.name = name

    def add(self, subscriber:Subscriber):
        self.subscribers.append(subscriber)

    def remove(self, subscriber:Subscriber):
        self.subscribers.remove(subscriber)
        

    def notify(self):
        for subr in self.subscribers:
            subr.update()

    def upload(self):
        print("uploading ...")
        print("uploaded :)")
        self.notify()


# publishers 
publisher1 :Publisher = Publisher("edureka")

# subscribers     
Subscriber1 :Subscriber = Subscriber("Harish", publisher1)
Subscriber2 :Subscriber = Subscriber("sambhav", publisher1)

publisher1.add(Subscriber1)
publisher1.add(Subscriber2)

publisher1.upload()





        




