import numpy as np
import sys
import h5hep as hp

import matplotlib.pylab as plt

filename = sys.argv[1]
data,event = hp.hd5events(filename)

nevents = data['nevents']
print("nevents: ",nevents)

hp.get_event(event,data,n=0)

event.keys()


