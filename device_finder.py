import pyaudio

audio = pyaudio.PyAudio()
numDevices = audio.get_host_api_info_by_index(0).get('deviceCount')

print ('----------Input Devices----------')

for i in range (0,numDevices):
    if (audio.get_device_info_by_host_api_device_index(0,i)).get('maxInputChannels') > 0:
        print(f"Input Device Index: {i} - {audio.get_device_info_by_host_api_device_index(0,i).get('name')}")
print ('---------------------------------\n\n')

print ('----------Output Devices----------')
for i in range (0,numDevices):
    if (audio.get_device_info_by_host_api_device_index(0,i)).get('maxOutputChannels') > 0:
        print(f"Output Device Index: {i} - {audio.get_device_info_by_host_api_device_index(0,i).get('name')}")
print ('---------------------------------')