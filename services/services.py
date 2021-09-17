from .models import Booking
from listing.models import Room
import datetime
#def create_booking(data):
def Check_availability(room,check_in,check_out):
	bookings = Booking.objects.filter(place=room).order_by('-created')
	
	for booking in bookings:
		#This list variables hols a splited version of the incomming date 
		chkin =  check_in.split('-')

		new_check_in = datetime.date(int(chkin[0]),int(chkin[1]),int(chkin[2]))
		#after working with the list it does not need to be stored in memory so its replaced
		chkin = check_out.split('-')

		new_check_out = datetime.date(int(chkin[0]),int(chkin[1]),int(chkin[2]))
		booked_check_in = datetime.date(booking.check_in.year,booking.check_in.month,booking.check_in.day)
		booked_check_out = datetime.date(booking.check_out.year,booking.check_out.month,booking.check_out.day)

		#comparing the new booking dates with all other existing booking dates of each room to determine availability
		if new_check_in >= booked_check_in and new_check_out <= booked_check_out :
			return False

		else:
			return True



#def reserve_space():