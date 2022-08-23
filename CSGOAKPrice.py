#Here we are going to plot a the graphs
#run this in conjunction in ibpyn and will print all the outcomes of the last version
skins= ["BS", "WW", "FT", "MW", "FN","STBS", "STWW", "STFT", "STMW", "STFN"]
prices= [98.00, 133.41, 175.33, 248.25, 368.74, 56.71, 77.53, 88.94, 151.20, 373.75]


xpos = np.arange(len(skins))

plt.bar(xpos, prices)
plt.xticks(xpos, skins)
