from csiread import Nexmon
import numpy as np
import pandas as pd
from pathlib import Path

#FNAME = "walk_test_1038.pcap"
#OUTNAME = FNAME + ".csv"

PCAP_DIR = Path("hf_dataset/raw_pcap")

print("test")
print("Exists:", PCAP_DIR.exists())
print("Absolute:", PCAP_DIR.resolve())

for pcap_file in PCAP_DIR.rglob("*.pcap"):
    FNAME = str(pcap_file)
    OUTNAME = str(pcap_file.with_suffix(".csv"))
    print(f"Processing: {FNAME}...")

    if "80_" in FNAME:
        bandwidth = 80
    else:
        bandwidth = 40

    print(f"BW: {bandwidth}...")

    csidata = Nexmon(FNAME, chip="43455c0",bw=bandwidth)
    csidata.read()


    # Convert to magnitude
    # @TODO should we also include complex in CSV?
    csi_mag = np.abs(csidata.csi)

    df = pd.DataFrame(csi_mag.reshape(csi_mag.shape[0], -1))
    df.to_csv(OUTNAME, index=False)
    print(f"Done")

