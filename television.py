class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self):
        self._status = False
        self._muted = False
        self._volume = Television.MIN_VOLUME
        self._channel = Television.MIN_CHANNEL

    def turn_on(self):
        self._status = True

    def turn_off(self):
        self._status = False

    def mute(self):
        if self._status:
            self._muted = not self._muted

    def channel_up(self):
        if self._status:
            self._channel += 1
            if self._channel > Television.MAX_CHANNEL:
                self._channel = Television.MIN_CHANNEL

    def channel_down(self):
        if self._status:
            self._channel -= 1
            if self._channel < Television.MIN_CHANNEL:
                self._channel = Television.MAX_CHANNEL

    def volume_up(self):
        if self._status and not self._muted:
            if self._volume < Television.MAX_VOLUME:
                self._volume += 1

    def volume_down(self):
        if self._status and not self._muted:
            if self._volume > Television.MIN_VOLUME:
                self._volume -= 1

    def __str__(self):
        return f"TV status: {'On' if self._status else 'Off'}, Channel: {self._channel}, Volume: {self._volume}, Muted: {self._muted}"
