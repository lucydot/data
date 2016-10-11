#!/usr/local/bin/python
import matplotlib.pyplot as plt
import re

read_in = open('OUTCAR','r').read()
free_energies = re.findall("free\senergy\s*TOTEN\s*=\s*([-.\d\s]+)",read_in) # 2 spaces for ionic energy step, 1 space if wanted electronic steps
[float(i) for i in free_energies]

x_coords = range(1, len(free_energies)+1)

print free_energies

sc = plt.scatter(x_coords,free_energies)
plt.show() 
