import ROOT 
from array import array
import numpy as np
from numpy.random import beta

import sys


################################################################################
def calc_energy(mass,px,py,pz):

    energy = np.sqrt(mass*mass + px*px + py*py + pz*pz)

    return energy

################################################################################

nevents = 1000
if len(sys.argv)>1:
    nevents = int(sys.argv[1])

# Create the file and "cd" into it.
name = 'HEP_narrow_file_ROOT_n%d.root' % (nevents)
f = ROOT.TFile(name, "RECREATE")
f.cd()


print("HERE")

# Make the tree
tree = ROOT.TTree( 'T', 'My tree' )

njet = array('i', [-1]); tree.Branch('njet', njet, 'njet/I')
jete = array('f', 16*[-1.]); tree.Branch('jete', jete, 'jete[njet]/F')
jetpx = array('f', 16*[-1.]); tree.Branch('jetpx', jetpx, 'jetpx[njet]/F')
jetpy = array('f', 16*[-1.]); tree.Branch('jetpy', jetpy, 'jetpy[njet]/F')
jetpz = array('f', 16*[-1.]); tree.Branch('jetpz', jetpz, 'jetpz[njet]/F')
jetbtag = array('f', 16*[-1.]); tree.Branch('jetbtag', jetbtag, 'jetbtag[njet]/F')


nmuon = array('i', [-1]); tree.Branch('nmuon', nmuon, 'nmuon/I')
muone = array('f', 16*[-1.]); tree.Branch('muone', muone, 'muone[nmuon]/F')
muonpx = array('f', 16*[-1.]); tree.Branch('muonpx', muonpx, 'muonpx[nmuon]/F')
muonpy = array('f', 16*[-1.]); tree.Branch('muonpy', muonpy, 'muonpy[nmuon]/F')
muonpz = array('f', 16*[-1.]); tree.Branch('muonpz', muonpz, 'muonpz[nmuon]/F')
muonq = array('f', 16*[-1.]); tree.Branch('muonq', muonq, 'muonq[nmuon]/F')

nelectron = array('i', [-1]); tree.Branch('nelectron', nelectron, 'nelectron/I')
electrone = array('f', 16*[-1.]); tree.Branch('electrone', electrone, 'electrone[nelectron]/F')
electronpx = array('f', 16*[-1.]); tree.Branch('electronpx', electronpx, 'electronpx[nelectron]/F')
electronpy = array('f', 16*[-1.]); tree.Branch('electronpy', electronpy, 'electronpy[nelectron]/F')
electronpz = array('f', 16*[-1.]); tree.Branch('electronpz', electronpz, 'electronpz[nelectron]/F')
electronq = array('f', 16*[-1.]); tree.Branch('electronq', electronq, 'electronq[nelectron]/F')

nphoton = array('i', [-1]); tree.Branch('nphoton', nphoton, 'nphoton/I')
photone = array('f', 16*[-1.]); tree.Branch('photone', photone, 'photone[nphoton]/F')
photonpx = array('f', 16*[-1.]); tree.Branch('photonpx', photonpx, 'photonpx[nphoton]/F')
photonpy = array('f', 16*[-1.]); tree.Branch('photonpy', photonpy, 'photonpy[nphoton]/F')
photonpz = array('f', 16*[-1.]); tree.Branch('photonpz', photonpz, 'photonpz[nphoton]/F')

nMET = array('i', [-1]); tree.Branch('nMET', nMET, 'nMET/I')
METpt = array('f', 16*[-1.]); tree.Branch('METpt', METpt, 'METpt[nMET]/F')
METphi = array('f', 16*[-1.]); tree.Branch('METphi', METphi, 'METphi[nMET]/F')

'''
hp.create_group(data,'muon',counter='nmuon')
hp.create_dataset(data,['e','px','py','pz','q'],group='muon',dtype=float)

hp.create_group(data,'electron',counter='nelectron')
hp.create_dataset(data,['e','px','py','pz','q'],group='electron',dtype=float)

hp.create_group(data,'photon',counter='nphoton')
hp.create_dataset(data,['e','px','py','pz'],group='photon',dtype=float)

hp.create_group(data,'MET',counter='nMET')
hp.create_dataset(data,['pt','phi'],group='MET',dtype=float)

'''

nevents = 1000
if len(sys.argv)>1:
    nevents = int(sys.argv[1])


for i in range(0,nevents):

    if i%1000==0:
        print(i)


    njet[0] = np.random.randint(16)
    for n in range(njet[0]):
        jetpx[n] = 300*beta(2,9)
        jetpy[n] = 300*beta(2,9)
        jetpz[n] = 300*beta(2,9)
        mass = 5*beta(2,9)
        jete[n] = calc_energy(mass,jetpx[n],jetpy[n],jetpz[n])
        jetbtag[n] = np.random.random()

    nmuon[0] = np.random.randint(16)
    for n in range(nmuon[0]):
        muonpx[n] = 300*beta(2,9)
        muonpy[n] = 300*beta(2,9)
        muonpz[n] = 300*beta(2,9)
        mass = 5*beta(2,9)
        muone[n] = calc_energy(mass,muonpx[n],muonpy[n],muonpz[n])
        muonq[n] = 2*np.random.randint(2) - 1

    nelectron[0] = np.random.randint(16)
    for n in range(nelectron[0]):
        electronpx[n] = 300*beta(2,9)
        electronpy[n] = 300*beta(2,9)
        electronpz[n] = 300*beta(2,9)
        mass = 5*beta(2,9)
        electrone[n] = calc_energy(mass,electronpx[n],electronpy[n],electronpz[n])
        electronq[n] = 2*np.random.randint(2) - 1

    nphoton[0] = np.random.randint(16)
    for n in range(nphoton[0]):
        photonpx[n] = 300*beta(2,9)
        photonpy[n] = 300*beta(2,9)
        photonpz[n] = 300*beta(2,9)
        mass = 5*beta(2,9)
        photone[n] = calc_energy(mass,photonpx[n],photonpy[n],photonpz[n])

    tree.Fill()

# Go back "into" the file and close and write it.
print("Writing the file...")
f.cd()
f.Write()
f.Close()


