import datetime


class VehicleType:
    BIKE = 'bike'
    CAR = 'car'
    TRUCK = 'truck'


class ParkingSpotStatus:
    EMPTY = 'empty'
    FILLED = 'filled'


class ParkingPrice:
    BASE_PRICE = 10 # 10$ per hour


class ParkingTicketStatus:
    CREATED = 'created'
    PAID = 'paid'


class Vehicle:
    def __init__(self, vehicle_tye, plate):
        self.vehicle_type = vehicle_tye
        self.plate = plate
        self.spot = None
        self.entry_time = None

    def mark_parked(self, spot):
        self.entry_time = datetime.datetime.now()
        self.spot = spot

    def mark_exited(self):
        self.entry_time = None
        self.spot = None


class ParkingSpot:
    def __init__(self, name, vehicle_type, status=ParkingSpotStatus.EMPTY):
        self.name = name
        self.vehicle_type = vehicle_type
        self._status = status
        self.vehicle = None

    def get_status(self):
        return self._status

    def set_status(self, new_status):
        self._status = new_status

    def fill_spot(self, vehicle):
        self.vehicle = vehicle
        self._status = ParkingSpotStatus.FILLED

    def empty_spot(self):
        self.vehicle = None
        self._status = ParkingSpotStatus.EMPTY


class ParkingLot:
    def __init__(self, spots):
        self.parking_spots = spots

    def get_spot(self, vehicle_type):
        for spot in self.parking_spots:
            if spot.vehicle_type == vehicle_type and spot.get_status() == ParkingSpotStatus.EMPTY:
                return spot

    def reserve_spot(self, vehicle):
        spot = self.get_spot(vehicle.vehicle_type)
        if not spot:
            raise Exception(f'No more slots left for {vehicle.vehicle_type} vehicle type.')
        spot.fill_spot(vehicle)
        vehicle.mark_parked(spot)

    @staticmethod
    def get_parking_ticket(vehicle):
        return ParkingTicket.generate_parking_ticket(vehicle)

    @staticmethod
    def exit_parking(vehicle, parking_ticket):
        if vehicle == parking_ticket.vehicle and parking_ticket.status == ParkingTicketStatus.PAID:
            spot = vehicle.spot
            vehicle.mark_exited()
            spot.empty_spot()
        else:
            raise Exception('Invalid Ticket Vehicle Combo')


class ParkingTicket:
    def __init__(self, vehicle, time_in_parking):
        self.vehicle = vehicle
        self.parking_time = time_in_parking
        self.status = ParkingTicketStatus.CREATED
        self.amount = self.generate_amount_payable()

    def generate_amount_payable(self):
        hours_parked = self.parking_time.seconds / (60 * 60)
        return ParkingPrice.BASE_PRICE * hours_parked

    def pay(self):
        self.status = ParkingTicketStatus.PAID

    @staticmethod
    def generate_parking_ticket(vehicle):
        exit_time = datetime.datetime.now()
        time_in_parking = vehicle.entry_time - exit_time
        return ParkingTicket(vehicle, time_in_parking)


if __name__ == '__main__':
    spots = []
    for i in range(100):
        spots.append(ParkingSpot(f'C{i}' , VehicleType.CAR))
    for i in range(20):
        spots.append(ParkingSpot(f'B{i}',VehicleType.BIKE))
    for i in range(40):
        spots.append(ParkingSpot(f'T{i}' ,VehicleType.TRUCK))
    parking_lot = ParkingLot(spots)
    v1 = Vehicle(VehicleType.CAR, 'CAR123')
    parking_lot.reserve_spot(v1)
    # wait some time
    parking_ticket = parking_lot.get_parking_ticket(v1)
    parking_ticket.pay()
    parking_lot.exit_parking(v1, parking_ticket)