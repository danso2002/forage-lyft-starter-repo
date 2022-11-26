
class Octoprime_tire():
    wear_array = []

    def should_be_service(self):
        sum = 0
        for i in self.wear_array:
            sum += i
        if sum >= 3:
            return True
        else:
            return False
