#!/usr/bin/env python

import struct
import sys

from hidapi import hidapi
import ctypes

# hiddev = hidapi.hid_open(0x1d50, 0x6080, None)
hiddev = hidapi.hid_open(0x1ccf, 0x1014, None)

if not hiddev:
    raise RuntimeError('Target not found.')

temp_a = -1000
temp_b = -1000

while 1:
    data = ctypes.create_string_buffer(5)
    if hidapi.hid_read(hiddev, data, 5) != 5:
        raise RuntimeError('Reading failed.')

    report_id, a, b = struct.unpack('<xHBB', data)

    #if b != 0:
    #    print a, b
    if temp_a == a and temp_b == b:
        pass
        # do nothing, no change.
    else:
        sys.stdout.write("report_id: {:_>4}, a: {:_>4}, b: {:_>4}\r".format(report_id, a, b))
        # report_id, a, b
        temp_a = a
        temp_b = b
        sys.stdout.flush()
