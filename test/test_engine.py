import pytest
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine

def test_capulet_engine():
    capulet_engine =  CapuletEngine(2020, 80000, 40)
    assert(capulet_engine.engine_should_be_serviced() == True)

def test_sternman_engine():
    sternman_engine =  SternmanEngine(2020, True)
    assert(sternman_engine.engine_should_be_serviced() == True)

def test_willoughby_engine():
    willoughby_engine =  WilloughbyEngine(2020, 80000, 40)
    assert(willoughby_engine.engine_should_be_serviced() == True)