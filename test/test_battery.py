from battery.nubblinBattery import NubblinBattery
from battery.spindleBattery import SpindleBattery


def test_nubbin_battery():
    nubblin_battery = NubblinBattery(2020, 2022)
    assert(nubblin_battery.nubbin_battery_should_by_serviced() == False)

def test_battery_battery():
    spindle_battery = SpindleBattery(2020, 2022)
    assert(spindle_battery.spindle_battery_should_by_serviced() == True)   