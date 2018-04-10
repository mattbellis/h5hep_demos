import h5py as h5
import numpy as np
import matplotlib.pylab as plt
import time

import h5hep as hp

import sys

filenames = sys.argv[1:]

energies = []

for filename in filenames:

    print("Opening ",filename)

    data,event = hp.hd5events(filename)
    #data,event = hp.hd5events(filename,desired_datasets=['jet'])

    # Print out what has been read in from the files.
    '''
    for key in event.keys():
        print(key)
    '''

    nevents = data['nevents']
    print("nevents: ",nevents)
    print(type(data),type(event))

    energies += data['jet/e'].tolist()

    #'''
    for i in range(0,nevents):

        if i%10000==0:
            print(i)

        hp.get_event(event,data,n=i)

        energy = event['jet/e']

        energies += energy.tolist()
    #'''

    del data
    del event


print(len(energies))

#plt.figure()
#plt.hist(energies,bins=100,range=(0,500))

#plt.show()
