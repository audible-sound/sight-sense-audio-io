# sight-sense-audio-io
Backend to manage audio input and output for the Sightsense glasses.\
Built for Jetson Nano.
### Installation Guide
---
Prequisites:
- Ubuntu 20.04
- Python version **3.9.X**

Install Python dependencies:\
`pip install -r requirements.txt`

Update Ubuntu Packages:\
`sudo apt-get update`\
`sudo apt-get -y upgrade`

Install PortAudio:\
`sudo apt install portaudio19-dev`

Install PyAudio:\
`sudo apt-get install python3-pyaudio`

Install Synthesizer:\
`sudo apt-get install espeak -y`

Install FLAC:\
`sudo apt-get install flac`
