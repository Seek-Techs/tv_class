class TV:
    def __init__(self):
        self.channel = list(range(1, 121))[0]
        self.volume = list(range(1, 8))[0]
        self.on = bool

    # def __repr__(self):
    #     return TV

    def turnOn(self):
        # self.on = True
        return 'TV is turning on'#, self.on

    def turnOff(self):
        # self.on = False
        return 'TV is turning off'#, self.on

    def getChannel(self):
        print('Current Channel: ', self.channel)
    
    #current channel (1 to 120)
    def setChannel(self, channel):
        self.channel = channel
        
    def getVolume(self):
        print('Current volume level: ', self.volume)

    def setVolume(self, volume):
        self.volume = volume

    def channelUp(self):
        channel = 1
        self.channel += channel
        print('Channel Increased: ', self.channel)

    def channelDown(self):
        channel = 1
        self.channel -= channel
        print('Channel Decreased: ', self.channel)

    def volumeUp(self):
        volume = 1
        self.volume += volume
        print('Volume Increased: ', self.volume)

    def volumeDown(self):
        volume = 1
        self.volume -= volume
        print('Volume Decreased: ', self.volume)

# Instance of TV class
tv = TV()

# Method operations on the instance
print(tv.turnOn())
print(tv.turnOff())
tv.setChannel(12)
tv.getChannel()
tv.setVolume(23)
tv.getVolume()
tv.channelUp()
tv.channelUp()
tv.channelUp()
tv.channelDown()
tv.volumeUp()
tv.volumeDown()
