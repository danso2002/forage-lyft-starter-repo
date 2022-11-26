from engine.model.engine import Engine

from car import Car


class CapuletEngine(Engine):
    def __init__(self, last_service_date, current_mileage, last_service_mileage):
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    def engine_should_be_serviced(self):
        if self.current_mileage - self.last_service_mileage > 30000:
            return True

