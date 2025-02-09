#Python script to split SMHI open data into separate text files based on content.
import numpy as np
import glob
#Define function which loads a file and parses it into an array. Skips unimportant rows.
def Cleaner(fname):
    fileArr = np.loadtxt(fname, dtype=str, skiprows=26, delimiter=";")

    return fileArr
#Read all csv files in folder.
fnames = np.array(glob.glob("*.csv"))
#Loop over filenames and save as txt:s depending on column name. 
for fname in fnames:
    print("Processing dataset " + fname)

    cleanData = Cleaner(fname)

    dates = np.empty(len(cleanData), dtype = "U100")
    times = np.empty(len(cleanData), dtype = "U100")
    temps = np.empty(len(cleanData), dtype = float)
    quals = np.empty(len(cleanData), dtype = "U100")

    for i in range(0, len(cleanData)):
        dates[i] = cleanData[i][0]
        times[i] = cleanData[i][1]
        temps[i] = cleanData[i][2]
        quals[i] = cleanData[i][3]

    np.savetxt(fname + "_dates.txt", dates, fmt="%s")
    np.savetxt(fname + "_times.txt", times, fmt="%s")
    np.savetxt(fname + "_temps.txt", temps)
    np.savetxt(fname + "_quals.txt", quals, fmt="%s")

    print("Done")
