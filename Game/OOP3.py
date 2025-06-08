from random import randint


class Train:
    def __init__(self,TrainName,TrainNo,Destination,Departure):
        self.TrainName= TrainName
        self.TrainNo= TrainNo
        self.Departure= Departure
        self.Destiantion=Destination
        self.TicketFare = randint(300,600)
        print(f"The train Name is {self.TrainName} and its Number is {TrainNo} ...From: {Departure} to {Destination}...Ticket Fare is {self.TicketFare}")
        print(f"The ticket fare is {self.TicketFare} ")




TrainName= str(input("Train name: "))
TrainNo= str(input("Train number: "))
Departure= str(input("From station: "))
Destiantion= str(input("To station: "))

b = Train(TrainName, TrainNo, Destiantion, Departure)
