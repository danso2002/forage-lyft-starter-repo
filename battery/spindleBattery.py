from battery.battery import Battery

class SpindleBattery(Battery):
    def __init__(self, service_date, current_date) -> None:
        self.service_date = service_date
        self.current_date= current_date

    
        
   