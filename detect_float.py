# Detect floating point number with - or + sign at starting 
import re
for _ in range(input()):
    print bool(re.match(r'^[-+]?[0-9]+\.[0-9]+$',raw_input()))
