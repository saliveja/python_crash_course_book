# importing modules and functions with and without alias
import function_8_16

# importing module

info = function_8_16.member_list('Emma', 'Karlsson',
                                 Email='emk@riseup.net',
                                 Number='0736514239')

print(info)

import function_8_16 as fn

# importing module with alian

info = fn.member_list('Emma', 'Karlsson',
                      Email='emk@riseup.net',
                      Number='0736514239')

print(info)

from function_8_16 import member_list

# importing function from module

info = member_list('Emma', 'Karlsson',
                   Email='emk@riseup.net',
                   Number='0736514239')

print(info)

from function_8_16 import member_list as ml

# when we import the function we don't need to write the name of the module
info = ml('Emma', 'Karlsson',
          Email='emk@riseup.net',
          Number='0736514239')

print(info)

from function_8_16 import *

# when we import everything we also don't need to write the name of the module
info = member_list('Emma', 'Karlsson',
                   Email='emk@riseup.net',
                   Number='0736514239')

print(info)
