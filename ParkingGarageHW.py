class ParkingGarage:
    def __init__(self):
        self.tickets = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.parkingSpaces = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.currentTicket = {}

    def takeTicket(self):
        if self.tickets and self.parkingSpaces:
            ticket_number = self.tickets.pop(0)
            parking_space = self.parkingSpaces.pop(0) # Takes the first index from the list
            self.currentTicket[ticket_number] = {'paid': False, 'parking_space': parking_space} # adds a dictionary to the ticket number key with 2 keys "paid" and "parking space"
            print(f"Ticket {ticket_number} taken. Please proceed to parking space {parking_space}.")
        else:
            print("Sorry, no tickets or parking spaces available.")

    def payForParking(self): 
        ticket_number = int(input("Enter your ticket number: "))
        payment = input("Please pay for your ticket here: ")
        if payment == 'payment':
            print("Thank you, your payment has been received.")
        else:
            print("Invalid payment. Please try again.")
        if ticket_number in self.currentTicket and not self.currentTicket[ticket_number]['paid']: # checks to see if ticket number value is in dictionary and checks to see if the ticket is paid for
            self.currentTicket[ticket_number]['paid'] = True
            print("Payment successful. You have 15 minutes to leave.")
            return ticket_number
        else:
            print("Invalid ticket number or ticket already paid.")
   
    def leaveGarage(self, ticket_number):
        if ticket_number is not None and ticket_number in self.currentTicket and self.currentTicket[ticket_number]['paid']:
            print("Thank you, have a nice day!")
            parking_space = self.currentTicket[ticket_number]['parking_space']
            self.parkingSpaces.append(parking_space)
            self.tickets.append(ticket_number)
            del self.currentTicket[ticket_number]
        else:
            print("Ticket not paid.")
            payment = input("Please make a payment to exit the parking lot: ")
            if payment == "payment":
                self.currentTicket[ticket_number]['paid'] = True
                print("Payment successful. You may now leave the garage. Thank you, have a nice day!")
                parking_space = self.currentTicket[ticket_number]['parking_space']
                self.parkingSpaces.append(parking_space)
                self.tickets.append(ticket_number)
                del self.currentTicket[ticket_number]
            else:
                print("Payment not received. YOU ARE TRAPPED HERE MUAHAHAH!")


# Create an instance of ParkingGarage
garage = ParkingGarage()

# Take a ticket
garage.takeTicket()

# Pay for the ticket and get the ticket number
ticket_number = garage.payForParking()

# Leave the garage using the ticket number
garage.leaveGarage(ticket_number)