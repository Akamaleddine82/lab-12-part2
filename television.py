# television.py

"""
Television Class
"""

class Television:
    """
    A class representing a Television.
    """

    
    MIN_VOLUME = 0
    MAX_VOLUME = 10
    MIN_CHANNEL = 0
    MAX_CHANNEL = 10

    def __init__(self) -> None:
        """
        Initialize the Television with default values.
        """
        self.__status = False
        self.__muted = False
        self.__volume = 5
        self.__channel = 0

    def power(self) -> None:
        """
        Turn the TV on or off.
        """
        self.__status = not self.__status

    def mute(self) -> None:
        """
        Mute or unmute the TV.
        """
        if self.__status:
            self.__muted = not self.__muted

    def channel_up(self) -> None:
        """
        Increase the channel by 1. Wrap around if at max channel.
        """
        if self.__status:
            if self.__channel == self.MAX_CHANNEL:
                self.__channel = self.MIN_CHANNEL
            else:
                self.__channel += 1

    def channel_down(self) -> None:
        """
        Decrease the channel by 1. Wrap around if at min channel.
        """
        if self.__status:
            if self.__channel == self.MIN_CHANNEL:
                self.__channel = self.MAX_CHANNEL
            else:
                self.__channel -= 1

    def volume_up(self) -> None:
        """
        Increase the volume by 1 unless muted or at max volume.
        """
        if self.__status and not self.__muted:
            if self.__volume < self.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self) -> None:
        """
        Decrease the volume by 1 unless muted or at min volume.
        """
        if self.__status and not self.__muted:
            if self.__volume > self.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self) -> str:
        """
        Return a string representation of the TV status.
        """
        return (f"Power = {self.__status}, "
                f"Channel = {self.__channel}, "
                f"Volume = {self.__volume if not self.__muted else 0}")

