"""
Micro Calculator Main Class
"""

import os
import sys
import time
import json

class MicroCalculator:

    def __init__(self):
        pass

    def calculate(self, expression):
        result = None
        try:
            result = eval(expression)
        except:
            pass
        
        return result

