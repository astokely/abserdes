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
            positive_int_list: Optional[Union[List, None]] = None,
            positive_int_list_of_lists: Optional[
                Union[List, None]] = None,
            negative_int_list: Optional[Union[List, None]] = None,
            negative_int_list_of_lists: Optional[
                Union[List, None]] = None,
            mixed_int_list: Optional[Union[List, None]] = None,
            mixed_int_list_of_lists: Optional[
                Union[List, None]] = None,
            str_list: Optional[Union[List, None]] = None,
            ) -> None:
        self.positive_float_list = positive_float_list
        self.positive_float_list_of_lists = positive_float_list_of_lists
        self.negative_float_list = negative_float_list
        self.negative_float_list_of_lists = negative_float_list_of_lists
        self.mixed_float_list = mixed_float_list
        self.mixed_float_list_of_lists = mixed_float_list_of_lists
        self.positive_int_list = positive_int_list
        self.positive_int_list_of_lists = positive_int_list_of_lists
        self.negative_int_list = negative_int_list
        self.negative_int_list_of_lists = negative_int_list_of_lists
        self.mixed_int_list = mixed_int_list
        self.mixed_int_list_of_lists = mixed_int_list_of_lists
        self.str_list = str_list
