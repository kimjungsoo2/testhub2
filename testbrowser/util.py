#!/usr/bin/env python

from collections import defaultdict

# list contains ',' separated three values
def put_nested_dict(inputlist):
    # create nested dictionary
    nested_dict = defaultdict(lambda: defaultdict(list))
    
    # populate nested dictionary from the list
    for k, v, m in inputlist:
        nested_dict[k][v].append(m)
        
    return nested_dict

def iterate_nested_dict(nested_dict):
    
    outputlist = []
    
    for key, val_dict in nested_dict.iteritems():
        outputlist.append(key)
        
        for key2, values in dict(val_dict).iteritems():
            outputlist.append(key2)
            
            for v in values:
                outputlist.append(v)
                
    return outputlist