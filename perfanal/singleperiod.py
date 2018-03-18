'''
Created on Mar 18, 2018

@author: Paul
'''


# Returns a percentage
def singlePeriod(start_value, end_value):
    try:
        # could also use ((end_value/start_value)-1)*100
        return (end_value - start_value) / start_value * 100
    except ZeroDivisionError:
        raise ValueError("Must pass non zero start value")
    
