class Telecision:
    def __init__(self, channel, volume, on):
        self.channel = channel
        self.volume = volume
        self.on = on
    def show(self):
        print(f"Channel {self.channel},Volume: {self.volume},on: {self.on}")
        def __str__(self):
            return f"Channel:{self.Channel}, Volume: {selfe.Volume}, On: {self.on}"

tv1 = Television(1, 10, True)
print(tv1)
tv1.show()
