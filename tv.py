class TV:
    def __init__(self):
        self.__channel = 1
        self.__volume = 1
        self.is_on = False

    # def __repr__(self):
    #     return TV

    def turnOn(self):
        print('TV is turning on...')
        self.is_on = True
        # return self.is_on

    def turnOff(self):
        # self.on = False
        print('TV is turning off')
        self.is_on = False
        # return self.is_on

    def getChannel(self):
        print('Current Channel: ', self.__channel)
    
    #current channel (1 to 120)
    def setChannel(self, channel):
        if channel in range(1, 121):
            self.__channel = channel

        else:
            print('Invalid Channel')
        
    def getVolume(self):
        print('Current volume level: ', self.__volume)

    def setVolume(self, volume):
        if volume in range(1, 8):
            self.__volume = volume

        else:
            print('Invalid Volume')

    def channelUp(self):
        channel = 1
        if self.__channel != 120:
            self.__channel += channel
            print('Channel Increased: ', self.__channel)

        else:
            print('Maximum Channel Level Reached: ', self.__channel)

    def channelDown(self):
        if self.__channel >= 1:
            channel = 1
            self.__channel -= channel
            print('Channel Decreased: ', self.__channel)

        else:
            print('Lowest Channel Level Reached')

    def volumeUp(self):
        if self.__volume in range(1, 8):
            volume = 1
            self.__volume += volume
            print('Volume Increased: ', self.__volume)

        else:
            print('Maximum Volume Level Reached')

    def volumeDown(self):
        if self.__volume >= 1:
            volume = 1
            self.__volume -= volume
            print('Volume Decreased: ', self.__volume)

        else:
            print('Lowest Volume Reached')

# Instance of TV class
tv = TV()

# Method operations on the instance
tv.turnOn()
tv.turnOff()
tv.setChannel(119)
tv.getChannel()
tv.setVolume(7)
tv.getVolume()
tv.channelUp()
tv.channelUp()
tv.channelUp()
tv.channelDown()
tv.volumeUp()
tv.volumeUp()
tv.volumeUp()
tv.getVolume()
tv.volumeDown()
tv.volumeDown()
tv.volumeDown()
