import random


# print(random.randrange(1,1000))



class Train:
	def __init__(self):
		self.metro_id = random.randrange(1,1000)
		self.station_no = 0
		self.direction = ['east','west']
		self.pass_total = 0


	# def __init__(self,metro_id):
	# 	self.metro_id = metro_id


	def get_metro_id(self):
		return self.metro_id

	def set_metro_id(self,metro_id):
		self.metro_id = metro_id

	def get_station_no(self):
		return self.station_no

	def set_station_no(self,station_no):
		self.station_no = station_no

	def get_direction(self):
		return self.direction

	def set_direction(self,direction):
		self.direction = direction

	def get_pass_total(self):
		return self.pass_total

	def set_pass_total(self,pass_total):
		self.pass_total = pass_total

	def nextStation(self,lastStation):
		return lastStation


	def __str__(self):
		return str("Metro Id "+self.metro_id+"  Station No. "+self.station_no+" Direction "+self.direction+" Total Passengers in Train: "+self.pass_total)	
		



def get_on_pass():
	return random.randrange(300)

def get_off_pass(passenger):
	return random.randrange(passenger)


def main():
	print("Welcome !!")
	stations = 0
	while (stations<3):
		stations = int(input(" Enter the number of metro Stations (minimum 3) : "))
		station_name = []
		for i in range(stations):
			station_name.append(input(f"Enter the name of station {i+1}: "))

	obj = Train()

	get_of = 0

	for station in range(stations):
		print(f"Train no. {obj.metro_id} leaving station {station+1} with {obj.pass_total} passenger(s)")
		print(f'No. of passenger getting off from train : {get_of}')
		waiting_passengers = get_on_pass()
		get_of = get_off_pass(34)
		obj.pass_total = obj.pass_total - get_of
		print(f'No. of new passenger waiting to board  : {waiting_passengers}')
		if obj.pass_total < 250 :
			total = obj.pass_total+waiting_passengers
			if total > 251:
				obj.pass_total = 250
				passenger_left = total-250




# if 'name' == '__main__':
main()


