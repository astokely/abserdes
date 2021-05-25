from typing import List, Optional, Union
import numpy as np
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
            positive_float64_numpy_array: Optional[
                Union[np.ndarray, None]] = None,
            positive_float64_numpy_array_of_numpy_arrays: Optional[
                Union[np.ndarray, None]] = None,
            negative_default_float_numpy_array: Optional[
                Union[np.ndarray, None]] = None,
            negative_default_float_numpy_array_of_numpy_arrays: \
                Optional[Union[np.ndarray, None]] = None,
            mixed_complex128_numpy_array: Optional[
                Union[np.ndarray, None]] = None,
            mixed_complex128_numpy_array_of_numpy_arrays: \
                Optional[Union[np.ndarray, None]] = None,
            mixed_complex64_numpy_array: Optional[
                Union[np.ndarray, None]] = None,
            mixed_complex64_numpy_array_of_numpy_arrays: \
                Optional[Union[np.ndarray, None]] = None,
            positive_int32_numpy_array: Optional[
                Union[np.ndarray, None]] = None,
            positive_int32_numpy_array_of_numpy_arrays: Optional[
                Union[np.ndarray, None]] = None,
            mixed_int64_numpy_array: Optional[
                Union[np.ndarray, None]] = None,
            mixed_int64_numpy_array_of_numpy_arrays: \
                Optional[Union[np.ndarray, None]] = None,
            negative_int_float_cast_numpy_array: Optional[
                Union[np.ndarray, None]] = None,
            negative_int_float_cast_numpy_array_of_numpy_arrays: \
                Optional[Union[np.ndarray, None]] = None,
            str_expr_list: Optional[Union[List, None]] = None,
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
        self.positive_float64_numpy_array = \
            positive_float64_numpy_array
        self.positive_float64_numpy_array_of_numpy_arrays = \
            positive_float64_numpy_array_of_numpy_arrays
        self.negative_default_float_numpy_array = \
            negative_default_float_numpy_array
        self.negative_default_float_numpy_array_of_numpy_arrays = \
            negative_default_float_numpy_array_of_numpy_arrays
        self.mixed_complex128_numpy_array = \
            mixed_complex128_numpy_array
        self.mixed_complex128_numpy_array_of_numpy_arrays = \
            mixed_complex128_numpy_array_of_numpy_arrays
        self.mixed_complex64_numpy_array = \
            mixed_complex64_numpy_array
        self.mixed_complex64_numpy_array_of_numpy_arrays = \
            mixed_complex64_numpy_array_of_numpy_arrays
        self.positive_int32_numpy_array = \
            positive_int32_numpy_array
        self.positive_int32_numpy_array_of_numpy_arrays = \
            positive_int32_numpy_array_of_numpy_arrays
        self.mixed_int64_numpy_array = \
            mixed_int64_numpy_array
        self.mixed_int64_numpy_array_of_numpy_arrays = \
            mixed_int64_numpy_array_of_numpy_arrays
        self.negative_int_float_cast_numpy_array = \
            negative_int_float_cast_numpy_array
        self.negative_int_float_cast_numpy_array_of_numpy_arrays = \
            negative_int_float_cast_numpy_array_of_numpy_arrays


        self.str_expr_list = str_expr_list
        self.str_list = str_list
