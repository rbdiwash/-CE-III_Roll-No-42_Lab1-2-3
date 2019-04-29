from mergeTime import getTimeArray as mT
from insertionTime import getTimeArray as iT
from insertionTime import getSizeArray as iS
import matplotlib.pyplot as plt

fig, ax = plt.subplots(1, 1)
ax.plot(iS(),mT(), label = 'Merge Sort')
ax.plot(iS(),iT(), label = 'Insertion Sort')
legend = ax.legend(loc = 'upper center', shadow = True, fontsize = 'large')
plt.show()
