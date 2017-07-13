###############################################################################
## 
## parts.py
##
##   Minimal Python library for common list functions related to partitioning
##   lists (and recombining them).
##
##   Web:     github.com/lapets/parts
##   Version: 0.0.1.0
##
##

###############################################################################
##

class PartsError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

def parts(xs, number = None, length = None):
    if number is not None and length is None:
        length = (len(xs) // number) + 1
    elif number is None and length is not None:
        pass # Length is specified so nothing else to do.
    elif number is not None and length is not None:
        if length * number != len(xs):
            raise PartsError("List cannot be split into " + str(number) + " parts each of length " + str(length) + ".")
    else: # Neither is specified.
        raise PartsError("Must specify number of parts or length of each part.")

    # Yield successive parts of specified length from input list.
    for i in range(0, len(xs), length):
        yield xs[i:i + length]
        
##eof