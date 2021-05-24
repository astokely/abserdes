from typing import List, Optional, Union
from userinput import UserInput
import abserdes

def test_deserialize_user_input_float_list():
    user_input = UserInput()
    user_input.deserialize("user_input.xml", user_input=True)
    assert user_input.positive_float_list == [
        1.0, 2.0, 3.0
    ]
    assert user_input.positive_float_list_of_lists == [
        [1.0, 2.0, 3.0], 
        [1.0, 2.0, 3.0], 
        [1.0, 2.0, 3.0], 
    ]
    assert user_input.negative_float_list== [
        -1.0, -2.0, -3.0
    ]
    assert user_input.negative_float_list_of_lists == [
        [-1.0, -2.0, -3.0], 
        [-1.0, -2.0, -3.0], 
        [-1.0, -2.0, -3.0], 
    ]
    assert user_input.mixed_float_list == [
        1.0, -2.0, 3.0
    ]
    assert user_input.mixed_float_list_of_lists == [
        [1.0, -2.0, 3.0], 
        [1.0, -2.0, 3.0], 
        [1.0, -2.0, 3.0], 
    ]
    assert user_input.positive_int_list == [
        1, 2, 3
    ]
    assert user_input.positive_int_list_of_lists == [
        [1, 2, 3], 
        [1, 2, 3], 
        [1, 2, 3], 
    ]
    assert user_input.negative_int_list== [
        -1, -2, -3
    ]
    assert user_input.negative_int_list_of_lists == [
        [-1, -2, -3], 
        [-1, -2, -3], 
        [-1, -2, -3], 
    ]
    assert user_input.mixed_int_list == [
        1, -2, 3
    ]
    assert user_input.mixed_int_list_of_lists == [
        [1, -2, 3], 
        [1, -2, 3], 
        [1, -2, 3], 
    ]
    assert user_input.mixed_int_list_of_lists == [
        [1, -2, 3], 
        [1, -2, 3], 
        [1, -2, 3], 
    ]

    assert user_input.str_list == [
        "step(distance(g1, g2)^2 - radius^2",
        "0.5*k*(theta-theta0)^2",
    ]
    
    
