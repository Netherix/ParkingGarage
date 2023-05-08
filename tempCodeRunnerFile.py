arage = ParkingGarage()

# Take a ticket
garage.takeTicket()

# Pay for the ticket and get the ticket number
ticket_number = garage.payForParking()

# Leave the garage using the ticket number
garage.leaveGarage(ticket_number)