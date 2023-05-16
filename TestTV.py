# CHRISTIAN M. DATING | BSCPE 1-5

input("\n\033[93mPress Any Key to Start...\033[0m\n")
print("\033[90m=" *100)
print("\033[93m ------------------------- WELCOME! ------------------------- \033[0m".center(105))
print("\033[90m=" *100)

from TV import Television

# Two objects
tv_1 = Television
tv_2 = Television

# PSEUDOCODES

def main():
    tv_1 = Television(30, 3, True)
    tv_2 = Television(3, 2, True)

    # display tv_1 channel and volume, display tv_2 channel and volume
    print("\n\033[94mtv_1's channel is", tv_1.get_channel, "and volume level is", tv_1.get_volume)
    print("\033[94mtv_2's channel is", tv_2.get_channel, "and volume level is", tv_2.get_volume)

    # Set tv_1 channel and volume level
    tv_1.set_channel(18)
    print("\n\033[95mNew Channel tv_1:", tv_1.get_channel)
    tv_1.set_volume(9)
    print("\033[95mThe new current volume for tv_1 is", tv_1.get_volume,".")


    # Set tv_2 channel and volume level
    tv_2.set_channel(169)
    print("\n\033[92mNew Channel tv_2:", tv_2.get_channel)
    tv_2.set_volume(-5)
    print("\033[92mThe new current volume for tv_2 is", tv_2.get_volume, ".")

    # tv_1 channel_up and channel_down
    tv_1.channel_up()
    print("\n\033[91mChannel Up tv_1:",tv_1.get_channel)
    tv_1.channel_down()
    print("\033[91mChannel Down tv_1:",tv_1.get_channel)

    # tv_2 channel_up and channel_down
    tv_2.channel_up()
    print("\n\033[96mChannel Up tv_2:",tv_2.get_channel)
    tv_2.channel_down()
    print("\033[96mChannel Down tv_2:",tv_2.get_channel)

    # tv_1 volume_up and volume_down
    tv_1.volume_up()
    print("\n\033[94mVolume Up tv_1:",tv_1.get_volume)
    tv_1.volume_down()
    print("\033[94mVolume Down tv_1:",tv_1.get_volume)

    tv_2.volume_up()
    print("\n\033[95mVolume Up tv_2:",tv_2.get_volume)
    tv_2.volume_down()
    print("\033[95mVolume Down tv_2:",tv_2.get_volume,"\n")


main()

print("\033[90m=" *100)
print("\033[90m=" *100)

