import matplotlib.pylab as plt
import sys

infile = sys.argv[1] 

time ={'h5hep': {'1000':[], '10000':[], '100000':[], '1000000':[]},'ROOT':{'1000':[], '10000':[], '100000':[], '1000000':[]}}

keep = False

with open(infile) as f:
    f = f.readlines()
    for line in f:
        if keep == True:
            time[filetype][filesize].append(line)
            keep = False
        else:
            if "Writing the file..." in line:
                if "root" in line:
                    keep = True
                    filetype = 'ROOT'
                if "1000000" in line:
                    filesize = "1000000"
                elif "100000" in line:
                    filesize = "100000"
                elif "10000" in line:
                    filesize = "10000"
                else:
                    filesize = "1000"
            elif "MET/nMET" in line:
                keep = True
                filetype = 'h5hep'



for key in time.keys():
    for f in time[key].keys():
        for i in range(len(time[key][f])):
            s = time[key][f][i].split(" ")[2]
            s = s.split(":")
            time[key][f][i] = int(s[0])*60 + float(s[1]) 
      

items = len(time['h5hep']['1000'])

hsum = [0,0,0,0]
rsum = [0,0,0,0]

print(time)


for i in range(items):
    
    hsum[0] += time['h5hep']['1000'][i]
    rsum[0] += time['ROOT']['1000'][i]
    hsum[1] += time['h5hep']['10000'][i]
    rsum[1] += time['ROOT']['10000'][i]
    hsum[2] += time['h5hep']['100000'][i]
    rsum[2] += time['ROOT']['100000'][i]
    hsum[3] += time['h5hep']['1000000'][i]
    rsum[3] += time['ROOT']['1000000'][i]


for i in range(4):
    hsum[i] = hsum[i]/4
    rsum[i] = rsum[i]/4


ratio = []

for i in range(4):
    ratio.append(hsum[i]/rsum[i])


x = [1000,10000,100000,1000000]

plt.figure(figsize=(12,8))
[xt.set_fontsize(24) for xt in plt.gca().get_xticklabels()]
[yt.set_fontsize(24) for yt in plt.gca().get_yticklabels()]
plt.plot(x,[1,1,1,1],'-')
plt.plot(x,ratio,'o',markersize=15)
plt.xscale("log")
plt.ylim(.9,1.1)
plt.title('Ratio of file creation times',fontsize=24)
plt.xlabel('Number of events in file',fontsize=24)
plt.ylabel('hdf5/ROOT',fontsize=18)
plt.tight_layout()
plt.show()
