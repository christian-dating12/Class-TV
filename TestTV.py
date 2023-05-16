# CHRISTIAN M. DATING | BSCPE 1-5

from TV import Television

# Two objects
tv_1 = Television
tv_2 = Television

# PSEUDOCODES

def main():
    tv_1 = Television(30, 3, True)
    tv_2 = Television(3, 2, True)

    # display tv_1 channel and volume, display tv_2 channel and volume
    print("tv_1's channel is", tv_1.get_channel, "and volume level is", tv_1.get_volume)
    print("tv_2's channel is", tv_2.get_channel, "and volume level is", tv_2.get_volume)

    # Set tv_1 channel and volume level
    tv_1.set_channel(18)
    print("New Channel tv_1:", tv_1.get_channel)
    tv_1.set_volume(9)
    print("The new current volume for tv_1 is", tv_1.get_volume,".")


    # Set tv_2 channel and volume level
    tv_2.set_channel(169)
    print("New Channel tv_2:", tv_2.get_channel)
    tv_2.set_volume(-5)
    print("The new current volume for tv_2 is", tv_2.get_volume, ".")

    # tv_1 channel_up and channel_down
    tv_1.channel_up()
    print("Channel Up tv_1:",tv_1.get_channel)
    tv_1.channel_down()
    print("Channel Down tv_1:",tv_1.get_channel)

    # tv_2 channel_up and channel_down
    tv_2.channel_up()
    print("Channel Up tv_2:",tv_2.get_channel)
    tv_2.channel_down()
    print("Channel Down tv_2:",tv_2.get_channel)

# tv_1 volume_up and volume_down