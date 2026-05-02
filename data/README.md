#  Data

## Using our recorded data
The data we have collected is available from hugging faces (think github for training data).  
You must first make an account here:

Then, on command line, ensure hf is installed on your machine

curl -LsSf https://hf.co/cli/install.sh | bash

login with your key using this command

hf auth login

Once this is setup, you can execute our ./download_data.sh script, it will auto download the files we recorded onto your machine in the desired format.  Note that this can take some time, as the files are very large.

if you have a dataset that you would like to upload you can use the following command (must have access to repo to do this portion).

hf upload skantz-ksu/wifi-csi-sensing . --repo-type=dataset


## Using Your own Data

To use your own data, put the captured pcap files into the format described below

data
 -hf_dataset
  -raw_pcap
   -[Input folders with your desired pcap files here, named idle or walking, and 40 or 80 for bandwidth]
  -pcap_csvs
   -[put converted files here, once converted using our python scripts]

We have provided two scripts to help you with the parsing process, pcap_to_csv.py and split_file.py

### pcap_to_csv.py 
Use python to run this file from the "data" directory (where it lives).  It will search through for hf_dataset/raw_pcap/*.pcap and will convert to CSVs based on the filename (if 80_ assumes 80MHz bandwidth, else assumes 40MHz).  This will place the CSVs in the same location as the pcap files, you will have to manually move them to desired location from here.

### split_file.py
This will itereate through the CSVs in data/pcap_csvs/*.csv and split them accordingly.  THe variables at the top of the script can be updated depending on the length of your tests, but this assumes 2 minute intervals for walking tests, 24 minute intervals for idle tests, and a desired test length of 30s.  It will split the files accordingly and output them in the same location as the original csv.