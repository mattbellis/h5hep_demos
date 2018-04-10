import sys
import matplotlib.pylab as plt

infile = sys.argv[1] 

time = []

with open(infile) as f:
    f = f.readlines()
    for line in f:
        if '%' in line:
            time.append(line)

for t in range(len(time)):
    s = time[t].split(" ")[2]
    s = s.split(":")
    time[t] = int(s[0])*60 + float(s[1])

ratio = []

print(len(time))

for i in range(4):
    ratio.append(time[i]/time[i+4])


infile2 = sys.argv[2]

alltime = []

with open(infile2) as f:
    f = f.readlines()
    for line in f:
        if '%' in line:
            alltime.append(line)

for t in range(len(time)):
    s = alltime[t].split(" ")[2]
    s = s.split(":")
    alltime[t] = int(s[0])*60 + float(s[1])

ratioall = []

for i in range(4):
    ratioall.append(alltime[i]/alltime[i+4])


x = [1000,10000, 100000, 1000000]

plt.figure(figsize=(12,8))
[xt.set_fontsize(24) for xt in plt.gca().get_xticklabels()]
[yt.set_fontsize(24) for yt in plt.gca().get_yticklabels()]
plt.plot(x,[1,1,1,1],'--')
plt.plot(x,ratio,'o',markersize=15,label='Read only relevant data out')
plt.plot(x,ratioall,'^',markersize=15,label='Read full data out')
plt.xscale("log")
plt.ylim(0,2)
plt.title('Ratio of times to read data',fontsize=24)
plt.xlabel('Number of events in file',fontsize=24)
plt.ylabel('hdf5/ROOT',fontsize=24)

plt.tight_layout()
plt.legend(fontsize=18)
plt.show()
