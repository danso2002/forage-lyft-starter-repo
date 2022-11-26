
class Carrigan_tire():
    wear_array = []

    def should_be_service(self):
        should_be_served = False
        for i in self.wear_array:
            if i > 0.9:
                should_be_served = True
        return should_be_served