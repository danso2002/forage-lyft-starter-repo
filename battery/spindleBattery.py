from battery.battery import Battery

class SpindleBattery(Battery):
    def __init__(self, service_date, current_date) -> None:
        self.service_date = service_date
        self.current_date= current_date

    def spindle_battery_should_by_serviced(self):
        if  self.current_date - self.service_date > 3 :
            return True
        else:
            return False

    
        
   