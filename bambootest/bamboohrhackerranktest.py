#!/bin/python3

import math
import os
import random
import re
import sys
import json


#
# Complete the 'generateJSON' function below.
#
# The function is expected to return a STRING.
# The function accepts 2D_STRING_ARRAY lines as parameter.
#


def generateJSON(lines):
    # Write your code here
    result = []
    for item in lines:
        
        # Check for empty input
        if item[1] == "": 
            continue
        
        # Convert manager_id to JSON NULL if empty
        if item[2] == "":
            manager_id = None
        else:
            manager_id = int(item[2])
            
        # Transform array to dictionary
        result.append({
            "id": int(item[0]),
            "name": item[1],
            "manager_id": manager_id
        })
        
    return json.dumps(result, separators=(',', ':'))
    

print(generateJSON([
  [
    "1",
    "Gregory Gwilliam",
    "2"
  ],
  [
    "2",
    "Brice Martin",
    ""
  ]
]))