class Vehicle:
    def __init__(self,wheels,tank,seat,speed):
        self.wheels = wheels
        self.tank = tank
        self.seat = seat
        self.speed = speed
    def drive(self):
        print("Vehicle is in driving mode")