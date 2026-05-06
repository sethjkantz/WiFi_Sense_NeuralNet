# Raspberry Pi Data

## Setup
Copy each of these files over to your raspberry pi.  It is assumed that the pi / nexmon config is already on your system (see link in above repo for instructions).  Once these are on the configured pi, copy the makecsiparams and setup_env.sh (both from the configured nexmon firmware, see link again for further details) to the same folder as these scripts.  These script should handle all logic for configuring your network, starting nexmon and recording.  Start each individual script to record on the desired setting.  If you provide no filename, it will just output to terminal.  This is useful for verifying that your firmware is configured correctly.  if you provide a filename after (IE ./start_record_20.sh test.pcap) the data will be stored in there.  You can end the capture by hitting ctrl-c.

### start_record_20.sh
ch11 - 20MHz bandwidth


### start_record_40.sh
ch157 - 20MHz bandwidth


### start_record_80.sh
ch157 - 20MHz bandwidth