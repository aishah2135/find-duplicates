# -*- coding: utf-8 -*-
"""
Created on Wed Feb  2 18:34:05 2022

@author: aisha
"""

ssn_name_pairs = {"123-45-6789": "Jonny Boy", 
                  "000-00-0002": "Danny SoHo", 
                  "999-00-0005": "Pam Ham", 
                  "888-88-8888": "Jonny Boy", 
                  "999-00-0006": "Pam Ham", 
                  "999-00-0007": "Pam Ham"}
#{"Jonny Boy": ["123-45-6789", "888-88-8888"], 
# "Pam Ham": ["999-00-0005", "999-00-0006", "999-00-0007"]}

def find_duplicate_names(ssn_name_dictionary: dict) -> dict: 
    result = {}
    names = list(ssn_name_dictionary.values())
    
    for (ssn, name) in ssn_name_dictionary.items(): 
        if names.count(name) > 1:
            result[name] = result.get(name, [])
            result[name].append(ssn)
            
    return result
        
duplicate_name_ssns = find_duplicate_names(ssn_name_pairs)
        
for (name, ssns) in duplicate_name_ssns.items():
            print(f"Found duplicate name {name} with SSNs: {ssns}")