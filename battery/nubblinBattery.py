from battery.battery import Battery

class NubblinBattery(Battery):
    def __init__(self, service_date, current_date) -> None:
        self.service_date = service_date
        self.current_date= current_date

    def nubbin_battery_should_by_serviced(self):
        if  self.current_date - self.service_date == 4 :
            return True
        else:
            return False



    
        