from matplotlib import pyplot as plotter
import numpy as np
from scipy import stats

from pyodide.http import pyfetch
from matplotlib import font_manager

#Plot 2:
y_venturiCrct = [23.87, 
18.28, 
16.59, 
6.27, 
13.11, 
9.40, 
7.68, 
6.27
]

y_orificeCrct = [21.47, 
19.54, 
17.15, 
13.52, 
13.23, 
9.35, 
7.98, 
5.64
]

y_variableArea = [20, 
18, 
16, 
14, 
12, 
8, 
6, 
4
]

x_volumeCollect = [20.94, 
18.89, 
17.05, 
15.60, 
12.67, 
10.57, 
7.55, 
5.59
]

##plotter.scatter(x_idealVenturi,y_volumeCollect,color="red", s=25, label="Venturi Meter") #s is dot size
# marker=, edgecolor= dot edge, linestyle= "--"

url = "https://raw.githubusercontent.com/google/fonts/main/ofl/ptserif/PT_Serif-Web-Regular.ttf"
resp = await pyfetch(url)
with open("PTSerif.ttf", "wb") as f:
    f.write(await resp.bytes())

font_manager.fontManager.addfont("PTSerif.ttf")
plotter.rcParams['font.family'] = 'PT Serif'

plotter.xlabel("Volume Collection Method Volume Flow Rate (L/Min)");
plotter.ylabel("Variable Area, Venturi & Orifice Meter Flow Rate (L/Min)");
#plotter.xscale("log")  
#plotter.yscale("log") - rescales based on 10^0, 10^1...

plotter.xlim(2.5,25);
plotter.ylim(2.5,22);
#plotter.autoscale_y()

degLineX = [0,5,10,20,22.5]
degLineY = [0,5,10,20,22.5]

plotter.plot(degLineX,degLineY, c = "grey", linestyle="dashed", label="45 Degree Line",linewidth=1)

#---error bars---
uVolumeCollect = [0.70, 
0.63, 
0.57, 
0.52, 
0.42, 
0.35, 
0.25, 
0.19
]

uVariableArea = 1

#plotter.grid(linewidth = 0.5)

plotter.scatter(x_volumeCollect,y_venturiCrct,color="crimson", s=25, label="Venturi Meter")
plotter.scatter(x_volumeCollect,y_orificeCrct,color="blue", s=30, marker="^",label="Orifice Meter")

plotter.errorbar(x_volumeCollect,y_variableArea,xerr=uVolumeCollect,yerr=uVariableArea, 
fmt='o', capsize=2, elinewidth=0.5,ecolor="black", barsabove=False, label ="Variable Area Meter", c="goldenrod", marker="s")


plotter.legend()
#---------



#plotter.savefig('EGR2500_Graph1.jpg')
plotter.show()
