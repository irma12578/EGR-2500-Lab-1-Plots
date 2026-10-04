from matplotlib import pyplot as plotter
import numpy as np
from scipy import stats

from pyodide.http import pyfetch
from matplotlib import font_manager

#Plot 1: Vcollect vs Videal
x_idealVenturi = [25.95, 
19.87, 
18.03, 
6.81, 
14.25, 
10.22, 
8.35, 
6.81
]

x_idealOrifice = [34.64, 
31.51, 
27.66, 
21.81, 
21.33, 
15.08, 
12.86, 
9.10
]

y_volumeCollect = [20.94, 
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

plotter.xlabel("Ideal Venturi & Orifice Flow Rate (L/Min)");
plotter.ylabel("Volume Collection Method Volume Flow Rate (L/Min)");
#plotter.xscale("log")  
#plotter.yscale("log") - rescales based on 10^0, 10^1...

plotter.xlim(5.0,37.5);
plotter.ylim(5.0,22.5);
#plotter.autoscale_y()

#---linear regression---
x_V = np.array(x_idealVenturi)
x_O = np.array(x_idealOrifice)
y   = np.array(y_volumeCollect)

slopeV0 = np.sum(x_V * y) / np.sum(x_V**2)
slopeO0 = np.sum(x_O * y) / np.sum(x_O**2)

# R² for a through-origin fit (use the same definition for both)
def r2_origin(x, y, m):
    ss_res = np.sum((y - m*x)**2)
    ss_tot = np.sum((y - np.mean(y))**2)
    return 1 - ss_res/ss_tot

print(slopeV0, r2_origin(x_V, y, slopeV0))
print(slopeO0, r2_origin(x_O, y, slopeO0))

xs = np.linspace(5, 37.5, 100)
plotter.plot(xs, slopeV0*xs, c="coral", linestyle="dashed", label="Best-Fit (Venturi)")
plotter.plot(xs, slopeO0*xs, c="teal", linestyle="dashed", label="Best-Fit (Orifice)")

plotter.text(17.5,20, "y = 0.92x \n R\u00b2 = 0.53")
plotter.text(25,14, "y = 0.62 \n R\u00b2 = 0.97")


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

uOrifice = [0.60, 
0.66, 
0.75, 
0.95, 
0.97, 
1.37, 
1.61, 
2.27
]

uVenturi = [0.22, 
0.29, 
0.32, 
0.85, 
0.41, 
0.57, 
0.70, 
0.85
]

#plotter.grid(linewidth = 0.5)
plotter.errorbar(x_idealVenturi,y_volumeCollect,xerr=uVenturi,yerr=uVolumeCollect, 
fmt='o', capsize=2, elinewidth=1,ecolor="black", barsabove=False, label ="Venturi Meter", c="crimson",)

plotter.errorbar(x_idealOrifice,y_volumeCollect, xerr=uOrifice, yerr=uVolumeCollect, fmt='^', c="darkblue", label="Orifice Plate", 
capsize=2, elinewidth=1, ecolor="black", barsabove=False)

plotter.legend()
#---------



#plotter.savefig('EGR2500_Graph1.jpg')
plotter.show()

