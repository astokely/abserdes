from typing import List, Optional, Union
import abserdes

class UserInput(abserdes.Serializer):

    def __init__(
            self,
            positive_float_list: Optional[Union[List, None]] = None,
            positive_float_list_of_lists: Optional[
                Union[List, None]] = None,
            negative_float_list: Optional[Union[List, None]] = None,
            negative_float_list_of_lists: Optional[
                Union[List, None]] = None,
            mixed_float_list: Optional[Union[List, None]] = None,
            mixed_float_list_of_lists: Optional[
                Union[List, None]] = None,
            ) -> None:
        self.positive_float_list = positive_float_list
        self.positive_float_list_of_lists = positive_float_list_of_lists
        self.negative_float_list = negative_float_list
        self.negative_float_list_of_lists = negative_float_list_of_lists
        self.mixed_float_list = mixed_float_list
        self.mixed_float_list_of_lists = mixed_float_list_of_lists

def test_float_list_user_input_deserialization():
    user_input = UserInput()
    user_input.deserialize("userinput.xml", user_input=True)
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
    
    
