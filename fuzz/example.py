# -*- coding: utf-8 -*-
# @Author: Caleb Stewart
# @Date:   2016-05-31 16:43:54
# @Last Modified by:   Caleb Stewart
# @Last Modified time: 2016-05-31 19:42:07
from fuzz.fuzzer import Fuzzer

class ExampleFuzzer(Fuzzer):
	def __init__(self, ID, queue):
		super(ExampleFuzzer, self).__init__(ID, queue)

	def fuzz(self, target):
		yield ([], None, '', False)
		#yield (['WAIT'], None, '', False) 
