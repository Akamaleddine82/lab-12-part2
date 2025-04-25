from television import Television

def test_power_toggle():
    tv = Television()
    assert not tv._status
    tv.turn_on()
    assert tv._status
    tv.turn_off()
    assert not tv._status

def test_channel_wraparound_up():
    tv = Television()
    tv.turn_on()
    tv._channel = Television.MAX_CHANNEL
    tv.channel_up()
    assert tv._channel == Television.MIN_CHANNEL

def test_volume_blocked_when_muted():
    tv = Television()
    tv.turn_on()
    tv.volume_up()
    tv.mute()
    tv.volume_up()
    assert tv._volume == 1  

def test_channel_down_wrap():
    tv = Television()
    tv.turn_on()
    tv._channel = Television.MIN_CHANNEL
    tv.channel_down()
    assert tv._channel == Television.MAX_CHANNEL

def test_str_output():
    tv = Television()
    expected = "TV status: Off, Channel: 0, Volume: 0, Muted: False"
    assert str(tv) == expected
