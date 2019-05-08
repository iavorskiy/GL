#!/usr/bin/env python3.6

import psutil
from sys import argv

errmsg = 'Please choose cpu or mem'

try:
    param = argv[1]
    if param == 'cpu':
        metrics = dict(psutil.cpu_times()._asdict())
        for k, v in metrics.items():
            print('system.cpu.' + ' ' + k, v)
    elif param == 'mem':
        metrics = dict(psutil.virtual_memory()._asdict()) 
        for k, v in metrics.items():
            print('virtual' +  ' ' + k, v)
        metrics = dict(psutil.swap_memory()._asdict()) 
        for k, v in metrics.items():
            print('swap' + ' ' + k, v)

    else:
        print ('Wrong argument!' + ' ' + errmsg)
        
except LookupError : 
    print ('You missed argument!' + ' ' + errmsg)



