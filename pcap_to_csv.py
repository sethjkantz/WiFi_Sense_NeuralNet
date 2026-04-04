from csiread import Nexmon
import numpy as np
import pandas as pd

FNAME = "csi.pcap"
OUTNAME = FNAME + ".csv"

csidata = Nexmon(FNAME, chip="43455c0")
csidata.read()


# Convert to magnitude
# @TODO should we also include complex in CSV?
csi_mag = np.abs(csidata.csi)

df = pd.DataFrame(csi_mag.reshape(csi_mag.shape[0], -1))
df.to_csv(OUTNAME, index=False)
