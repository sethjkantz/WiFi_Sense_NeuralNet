#!/usr/bin/env python3

from pathlib import Path
import pandas as pd
import numpy as np
from pathlib import Path

# how long we tested for storing data
IDLE_TEST_LEN_MIN = 24
WALK_TEST_LEN_MIN = 2

NUM_CSV_PER_MIN = 2 # split into 30s intervals for ease of training

NUM_IDLE_CSVS = IDLE_TEST_LEN_MIN * NUM_CSV_PER_MIN # 4,8 30s breaks
NUM_WALK_CSVS = WALK_TEST_LEN_MIN * NUM_CSV_PER_MIN # 4, 30s breaks

def split_csv(input_fname, split_nums):
    df = pd.read_csv(input_fname)

    # Split into chunks
    chunks = np.array_split(df, split_nums)

    for i, chunk in enumerate(chunks):
        # update name
        out_file = input_fname.replace(".csv", f"_split_{i+1:02d}.csv")
        chunk.to_csv(out_file, index=False)
        print(f"Saved: {out_file}")

PCAP_DIR = Path("hf_dataset/pcap_csvs")

print("test")
print("Exists:", PCAP_DIR.exists())
print("Absolute:", PCAP_DIR.resolve())

print("splitting tests into 30s long CSVs for training")

for pcap_file in PCAP_DIR.rglob("*.csv"):
    FNAME = str(pcap_file)
    if "split" in FNAME:
        print(f"skipping: {FNAME}...")
        continue
    else:
        print(f"Processing: {FNAME}...")

    if "idle" in FNAME:
        # idle tests were 24 minutes long - 48, 30s long CSVs
        num_breaks = NUM_IDLE_CSVS
    else:
        # walking tests were 2 minutes - 4, 30s long CSVs
        num_breaks = NUM_WALK_CSVS

    split_csv(FNAME,num_breaks)


    