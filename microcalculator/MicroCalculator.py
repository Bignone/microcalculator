"""
Micro Calculator Main Class
"""

import os
import sys
import time
import json
from .ModelBase import ModelBase

class MicroCalculator(ModelBase):

    def __init__(self):
        super().__init__()
        self.name = "Micro calculator"
        self.version = 0
        self.description = "Model to calculate math expressions"
        self.more_info = 'Example: {"expression": "2 + 3 * 6"}'

    def calculate(self, expression):
        result = None
        try:
            result = eval(expression)
        except:
            result = "Not valid math expression"
        
        return result

    def sumatory(self, values):
        result = None
        try:
            total_sum = 0
            for value in values:
                total_sum += value
            
            result = total_sum

        except:
            result = "Not valid values"
        
        return result

    def multiply(self, values):
        result = None
        try:
            total_mul = 1
            for value in values:
                total_mul *= value
            
            result = total_mul

        except:
            result = "Not valid values"
        
        return result

            
        

