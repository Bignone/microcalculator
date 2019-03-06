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
        result = eval(expression)
        
        return result



if __name__ == "__main__":
    M = MicroCalculator()
    print(M.calculate("2 + 2"))