# CHRISTIAN M. DATING | BSCPE 1-5

class Television:

# Define self, channel, volume, status_TV.
    def __init__(self, channel, volume, status_TV):
        self.get_channel = channel
        self.get_volume = volume 
        self.status_TV = status_TV

        # channel (1-120)
        if self.get_channel > 120:
            self.get_channel = 120
        elif self.get_channel < 1:
            self.get_channel = 1
        # volume (1-7)  
        if self.get_volume > 7:
            self.get_volume = 7
        elif self.get_volume < 1:
            self.get_volume = 1

# If true, turn on tv
    def turn_on(self):
        self.status_TV = True
# If false, turn off tv
    
# set new channel between 1-120
# set new volume between 1-7
# Increase the channel number by 1
# Decrease the channel number by 1
# Increase the volume level by 1
# Decrease the volume level by 1