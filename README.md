# WiFi Sensing Neural Net
A nexmon based system to capture CSI from a raspberry pi, train, and decode to determine if there is motion or no motion in a given room.  The create_venv.sh bash can be used to generate a virtual environment and pip install necessary python dependencies, the start_notebook.sh will source this environment and start the jupyter notebook.

## Raspberry Pi Setup and data collection
To capture CSI data a raspberry pi 4 must be used, and set up as described in the nexmon repository found here.  https://github.com/seemoo-lab/nexmon_csi?tab=readme-ov-file#getting-started  Note that for most newer kernels, some commands vary slightly, and you should use this discussion post as a reference to get it up and running.  https://github.com/seemoo-lab/nexmon_csi/discussions/395

Once raspberry pi tests have concluded, you should prepare a folder with necessary files, download the start_record.sh scripts found in raspberry_pi folder.  Next you should copy two files to the same location that the bash script lives: 1st the setup file (available at nexmon/setup_env.sh) and 2nd the makecsiparams executable (found at nexmon/patches/bcm43455c0/7_45_189/nexmon_csi/utils/makecsiparams).  Once these are all in the same repository you are good to procede.

From here, you can execute the bash script found in the raspberry_pi folder in two methods './start_record.sh' or './start_record.sh filename.pcap' to begin capture.  Providing no filename will be a test capture that prints data to screen but dows not record the output data.  Providing the filename for the pcap allows for the data to be captured and stored in a pcap format.  For both versions, ctrl-c can be used to end the capture of data.

## PCAP to CSV
Once the desired data has been captured in the various scenarios (walking, static, etc).  They should be copied from your raspberry pi to the pcap_conversion/pcap_files folder.  Once this step is ran you will have all the necessary CSVs needed for training and using the data.

## Processing and detection
The host system should use the CSI_WIFI_Sensing.ipynb to process and analyze for binary motion vs no motion.  Follow steps in data folder to download our data and play around with yourself.  

### CSI_WiFi_Sensing.ipynb
This is the core model of our system and the main file to review.  Open up and you will find that it is documented with instructions for how to use, once hugginf face data is downloaded it should be plug and play / easy to use

### Analyze_CSI.ipynb
This is a helper file to analyze the CSI data recorded.  It generates graphs to help better understand how the datasets differ test by test and room by room.

### Inference_CSI.ipynb
This is a helper file to use the models we created over individual cases.  It is mostly use for post test analysis.

## Models

3 models are saved for ease of testing.  As their name suggests, they are used for the 20MHz, 40MHz, and 80MHz bandwidths respectively.

1. Base_ch011_20MHz_3.keras
2. Base_ch157_40MHz_3.keras
3. Base_ch157_80MHz_3.keras