import ROOT 

import sys

chain = ROOT.TChain("T")

filenames = sys.argv[1:]

for filename in filenames:
    print("Adding file to chain: ",filename)
    chain.AddFile(filename)



# Open the file
#f = ROOT.TFile(sys.argv[1])
#f.ls() # Print out what's in it.

# Pull out the tree
#tree = f.Get("T")
#tree.Print() # Print what branches it has

# Event loop
nev = chain.GetEntries()

energies = []

for n in range (nev):
    chain.GetEntry(n)

    '''
    print(tree.nmuon)

    for i in range(tree.nmuon):
        print(tree.muonpt[i])
    '''

    #njets = tree.njet

    energies += chain.jete

print(len(energies))
