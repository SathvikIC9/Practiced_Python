class Train:
    def __init__(self, name, fare, total_seats):
        self.name = name
        self.fare = fare
        self.total_seats = total_seats
        self.available_seats = total_seats

    def get_status(self):
        print(f"Train Name: {self.name} . The number of seats are {self.total_seats} ")
      

    def get_fare_info(self):
        print(f"Fare for the train '{self.name}' is ₹{self.fare}")

    def book_ticket(self):
        if self.available_seats > 0:
            self.available_seats -= 1
            print("Ticket booked successfully!")
            print(f"Remaining seats: {self.available_seats}")
        else:
            print("Sorry, no seats available.")

train1 = Train("Rajdhani Express", 1500, 5)

train1.get_status()
train1.get_fare_info()
train1.book_ticket()
train1.book_ticket()
train1.get_status()
