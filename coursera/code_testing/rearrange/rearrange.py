#!/usr/bin/env python3

import re

def rearrange_name(name):
    #print(name)
    result = re.search(r"^([\w .]*), ([\w .]*)$",name)
    
    if result is None :
        return name

    return "{} {}".format(result[2], result[1])


#print(rearrange_name("Jameson, Idaho G."))

