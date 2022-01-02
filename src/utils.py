'''
pyMP (https://github.com/goncrust/pyMP)

Copyright (C) 2022 goncrust
Released under the GPL v3.0
https://github.com/goncrust/pyMP/blob/master/LICENSE.md
'''

import math


def secondsToMinutes(seconds):
    """Convert seconds to minutes
    """

    minutes = math.floor(seconds / 60)
    rseconds = seconds - (minutes*60)

    return str(minutes) + ":" + str(rseconds)


def bytesToMegabytes(b):
    return b/1048576
