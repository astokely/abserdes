from typing import List, Optional, Union
import pytest
from userinput import UserInput
import numpy as np
import abserdes


class Dictionary(abserdes.Serializer):

	def __init__(self):
		self.dictionary = {}
		self.nested_dictionary = {}
		self.tuple_key_dictionary = {}
		self.float_key_dictionary = {}
		self.int_key_dictionary = {}
		self.float64_key_dictionary = {}
		self.float128_key_dictionary = {}
		self.nested_tuple_key_dictionary = {}

def test_dictionary_serialization():
	dictionary = Dictionary()
	dictionary.dictionary = {
		'a' : 1, 
		'b' : 2, 
		'c' : 3
	}
	dictionary.nested_dictionary = {
		'a' : {'a' : 1}, 
		'b' : {'b' : 2}, 
		'c' : {'c' : 3}
	}
	dictionary.tuple_key_dictionary = {
		(1, 2, 3) : 1, 
		(4, 5, 6) : 2, 
		(7, 8, 9) : 3
	}
	dictionary.float_key_dictionary = {
		1.23 : 1, 
		4.56 : 2, 
		7.89 : 3
	}
	dictionary.int_key_dictionary = {
		1 : 1, 
		4 : 2, 
		7 : 3
	}
	dictionary.float64_key_dictionary = {
		np.float64(1.23) : 1, 
		np.float64(4.56) : 2, 
		np.float64(7.89) : 3
	}
	dictionary.float128_key_dictionary = {
		np.float128(1.23) : 1, 
		np.float128(4.56) : 2, 
		np.float128(7.89) : 3
	}
	dictionary.nested_tuple_key_dictionary = {
		(1, 2, 3) : {6.6658 : {(9.332, np.float128(5.223)) : 'abc'}}, 
		(4, np.float64(5.2), 6) : {
			np.float64(10.6658) : {
				(9.332, np.float128(5.223)) : 'a81981bc'
			}
		}, 
		(4, 5, 6) : {
			np.float64(10.6658) : {
				(9.332, np.float128(5.223)) : 'a81981bc'
			}
		}, 
	}

	dictionary.serialize("dictionary.xml")
	deserialized_dictionary = Dictionary()
	deserialized_dictionary.deserialize("dictionary.xml")
	assert deserialized_dictionary.dictionary == dictionary.dictionary

def test_tuple_key_dictionary_serialization():
	dictionary = Dictionary()
	dictionary.dictionary = {
		'a' : 1, 
		'b' : 2, 
		'c' : 3
	}
	dictionary.nested_dictionary = {
		'a' : {'a' : 1}, 
		'b' : {'b' : 2}, 
		'c' : {'c' : 3}
	}
	dictionary.tuple_key_dictionary = {
		(1, 2, 3) : 1, 
		(4, 5, 6) : 2, 
		(7, 8, 9) : 3
	}
	dictionary.float_key_dictionary = {
		1.23 : 1, 
		4.56 : 2, 
		7.89 : 3
	}
	dictionary.int_key_dictionary = {
		1 : 1, 
		4 : 2, 
		7 : 3
	}
	dictionary.float64_key_dictionary = {
		np.float64(1.23) : 1, 
		np.float64(4.56) : 2, 
		np.float64(7.89) : 3
	}
	dictionary.float128_key_dictionary = {
		np.float128(1.23) : 1, 
		np.float128(4.56) : 2, 
		np.float128(7.89) : 3
	}
	dictionary.nested_tuple_key_dictionary = {
		(1, 2, 3) : {6.6658 : {(9.332, np.float128(5.223)) : 'abc'}}, 
		(4, np.float64(5.2), 6) : {
			np.float64(10.6658) : {
				(9.332, np.float128(5.223)) : 'a81981bc'
			}
		}, 
		(4, 5, 6) : {
			np.float64(10.6658) : {
				(9.332, np.float128(5.223)) : 'a81981bc'
			}
		}, 
	}

	dictionary.serialize("dictionary.xml")
	deserialized_dictionary = Dictionary()
	deserialized_dictionary.deserialize("dictionary.xml")
	assert deserialized_dictionary.tuple_key_dictionary == dictionary.tuple_key_dictionary

def test_int_key_dictionary_serialization():
	dictionary = Dictionary()
	dictionary.dictionary = {
		'a' : 1, 
		'b' : 2, 
		'c' : 3
	}
	dictionary.nested_dictionary = {
		'a' : {'a' : 1}, 
		'b' : {'b' : 2}, 
		'c' : {'c' : 3}
	}
	dictionary.tuple_key_dictionary = {
		(1, 2, 3) : 1, 
		(4, 5, 6) : 2, 
		(7, 8, 9) : 3
	}
	dictionary.float_key_dictionary = {
		1.23 : 1, 
		4.56 : 2, 
		7.89 : 3
	}
	dictionary.int_key_dictionary = {
		1 : 1, 
		4 : 2, 
		7 : 3
	}
	dictionary.float64_key_dictionary = {
		np.float64(1.23) : 1, 
		np.float64(4.56) : 2, 
		np.float64(7.89) : 3
	}
	dictionary.float128_key_dictionary = {
		np.float128(1.23) : 1, 
		np.float128(4.56) : 2, 
		np.float128(7.89) : 3
	}
	dictionary.nested_tuple_key_dictionary = {
		(1, 2, 3) : {6.6658 : {(9.332, np.float128(5.223)) : 'abc'}}, 
		(4, np.float64(5.2), 6) : {
			np.float64(10.6658) : {
				(9.332, np.float128(5.223)) : 'a81981bc'
			}
		}, 
		(4, 5, 6) : {
			np.float64(10.6658) : {
				(9.332, np.float128(5.223)) : 'a81981bc'
			}
		}, 
	}

	dictionary.serialize("dictionary.xml")
	deserialized_dictionary = Dictionary()
	deserialized_dictionary.deserialize("dictionary.xml")
	assert deserialized_dictionary.int_key_dictionary == dictionary.int_key_dictionary


def test_float128_key_dictionary_serialization():
	dictionary = Dictionary()
	dictionary.dictionary = {
		'a' : 1, 
		'b' : 2, 
		'c' : 3
	}
	dictionary.nested_dictionary = {
		'a' : {'a' : 1}, 
		'b' : {'b' : 2}, 
		'c' : {'c' : 3}
	}
	dictionary.tuple_key_dictionary = {
		(1, 2, 3) : 1, 
		(4, 5, 6) : 2, 
		(7, 8, 9) : 3
	}
	dictionary.float_key_dictionary = {
		1.23 : 1, 
		4.56 : 2, 
		7.89 : 3
	}
	dictionary.int_key_dictionary = {
		1 : 1, 
		4 : 2, 
		7 : 3
	}
	dictionary.float64_key_dictionary = {
		np.float64(1.23) : 1, 
		np.float64(4.56) : 2, 
		np.float64(7.89) : 3
	}
	dictionary.float128_key_dictionary = {
		np.float128(1.23) : 1, 
		np.float128(4.56) : 2, 
		np.float128(7.89) : 3
	}
	dictionary.nested_tuple_key_dictionary = {
		(1, 2, 3) : {6.6658 : {(9.332, np.float128(5.223)) : 'abc'}}, 
		(4, np.float64(5.2), 6) : {
			np.float64(10.6658) : {
				(9.332, np.float128(5.223)) : 'a81981bc'
			}
		}, 
		(4, 5, 6) : {
			np.float64(10.6658) : {
				(9.332, np.float128(5.223)) : 'a81981bc'
			}
		}, 
	}

	dictionary.serialize("dictionary.xml")
	deserialized_dictionary = Dictionary()
	deserialized_dictionary.deserialize("dictionary.xml")
	assert deserialized_dictionary.float128_key_dictionary == dictionary.float128_key_dictionary














