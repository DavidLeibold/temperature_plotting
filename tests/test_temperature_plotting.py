#!/usr/bin/env python
# coding: utf-8

import os
import pytest
import temperature_plotting as tpl






def test_compute_mean():
    calc = tpl.compute_mean([0, 10, 20])
    assert calc == 10
    assert type(calc) == float
    
    calc = tpl.compute_mean([-10, 10])
    assert calc == 0
    
    calc = tpl.compute_mean([0, 10, 0])
    assert round(calc, 4) == 3.3333
    
    with pytest.raises(TypeError) as e:
        calc = tpl.compute_mean(["a", "b", "c"])
    assert e is not None, "We should not be able to average strings."
    
    calc = tpl.compute_mean([])
    assert math.isnan(calc) == True





# Definition of test:
def test_create_name():
    calc = tpl.create_name(3)
    assert calc == "plot_3.png"
    
    with pytest.raises(AssertionError):
        calc = tpl.create_name("3")
    
    with pytest.raises(AssertionError):
        calc = tpl.create_name(3.3)
    # print(calc)
    
    calc = tpl.create_name(int(1E6))
    assert calc == "plot_1000000.png"
    
    calc = tpl.create_name(-3)
    assert calc == "plot_-3.png"
    
    with pytest.raises(AssertionError):
        calc = tpl.create_name(None)
    
    with pytest.raises(AssertionError):
        calc = tpl.create_name(float('nan'))
        
    with pytest.raises(TypeError):
        calc = tpl.create_name()

    

# integration test
def test_main():
    tpl.main()
    assert os.path.exists("plot_25.png")





