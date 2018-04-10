import matplotlib.pylab as plt

h5hep = [.530, 4.69, 46.4, 461]
root = [.516,5.12,51.2,502]

ratio = []

for i in range(len(h5hep)):
    ratio.append(h5hep[i]/root[i])


plt.figure(figsize=(12,8))
[xt.set_fontsize(24) for xt in plt.gca().get_xticklabels()]
[yt.set_fontsize(24) for yt in plt.gca().get_yticklabels()]
plt.plot([1000,10000,100000,1000000],[1,1,1,1],'--')
plt.plot([1000,10000,100000,1000000],ratio,'o',markersize=15)
plt.xscale('log')
plt.ylim(.9,1.1)
plt.xlabel('Number of events',fontsize=24)
plt.ylabel('hdf5/ROOT',fontsize=24)
plt.title('Ratio of file sizes',fontsize=24)
plt.tight_layout()

plt.show()
