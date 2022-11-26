from engine.model.engine import Engine

from car import Car


class SternmanEngine(Engine):
    def __init__(self, last_service_date, warning_light_is_on):
        self.warning_light_is_on = warning_light_is_on

    def engine_should_be_serviced(self):
        if self.warning_light_is_on:
            return True
        else:
            return False

