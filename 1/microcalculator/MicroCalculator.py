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

