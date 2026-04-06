# WiFi Sensing Neural Net
A nexmon based system to capture CSI from a raspberry pi, train, and decode to determine if there is motion or no motion in a given room.

## Raspberry Pi Setup and data collection
To capture CSI data a raspberry pi 4 must be used, and set up as described in the nexmon repository found here.  https://github.com/seemoo-lab/nexmon_csi?tab=readme-ov-file#getting-started  Note that for most newer kernels, some commands vary slightly, and you should use this discussion post as a reference to get it up and running.  https://github.com/seemoo-lab/nexmon_csi/discussions/395

Once github tests have concluded, you should prepare a folder with necessary files, download the start_record.sh script found in raspberry_pi folder.  Next you should copy two files to the same location that the bash script lives: 1st the setup file (available at nexmon/setup_env.sh) and 2nd the makecsiparams executable (found at nexmon/patches/bcm43455c0/7_45_189/nexmon_csi/utils/makecsiparams).  Once these are all in the same repository you are good to procede.

From here, you can execute the bash script found in the raspberry_pi folder in two methods './start_record.sh' or './start_record.sh filename.pcap' to begin capture.  Providing no filename will be a test capture that prints data to screen but dows not record the output data.  Providing the filename for the pcap allows for the data to be captured and stored in a pcap format.  For both versions, ctrl-c can be used to end the capture of data.

## PCAP to CSV
Once the desired data has been captured in the various scenarios (walking, static, etc).  They should be copied from your raspberry pi to the pcap_conversion/pcap_files folder.  Once this step is ran you will have all the necessary CSVs needed for training and using the data.

## Processing and detection
The host system should use the CSI_WIFI_Sensing.ipynb to process and analyze for binary motion vs no motion.  Initially the CSI Dataset for WiFi based human detection from Qamar Zaman https://ieee-dataport.org/documents/csi-dataset-wifi-based-human-detection was used for training.  Download the dataset, place in repo and the logic should work out of the box.  Once that is in place, you are free to try your own captures and expiriment with own datasets.  Captures are left out of this git repo due to their size and restrictions (IEEEDataPort subscription required to download, own pcap files are too large).
