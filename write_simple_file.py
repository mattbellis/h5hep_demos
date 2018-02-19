import numpy as np
import sys
from h5hep import *

data = initialize()

create_group(data,'pixels',counter='npixels')
create_dataset(data,['x','y'],group='pixels',dtype=float)

create_dataset(data,['petals'],group='flowers',dtype=int)
create_dataset(data,['height'],group='mountains',dtype=int)

event = create_single_event(data)

#'''
for i in range(0,1000):

    clear_event(event)

    npixels = np.random.randint(50,150)
    event['pixels/npixels'] = npixels

    for n in range(npixels):
        event['pixels/x'].append(100*np.random.random())
        event['pixels/y'].append(100*np.random.random())

    

    event['flowers/nflowers'] = 1
    event['flowers/petals'].append(np.random.randint(500,1000))
    event['mountains/nmountains'] = 1
    event['mountains/height'].append(np.random.randint(1,20))

    fill(data,event)

print("Writing the file...")
#hdfile = write_to_file('output.hdf5',data)
hdfile = write_to_file('demo_of_h5hep.hdf5',data,comp_type='gzip',comp_opts=9)
#'''

