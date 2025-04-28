# test_tv.py

import pytest
from television import Television

def test_initial_state():
    tv = Television()
    assert tv._Television__status == False
    assert tv._Television__muted == False
    assert tv._Television__volume == 5
    assert tv._Television__channel == 0

def test_power():
    tv = Television()
    tv.power()
    assert tv._Television__status == True
    tv.power()
    assert tv._Television__status == False

def test_mute():
    tv = Television()
    tv.power()
    tv.mute()
    assert tv._Television__muted == True
    tv.mute()
    assert tv._Television__muted == False

def test_channel_up_wrap():
    tv = Television()
    tv.power()
    tv._Television__channel = Television.MAX_CHANNEL
    tv.channel_up()
    assert tv._Television__channel == Television.MIN_CHANNEL

def test_channel_down_wrap():
    tv = Television()
    tv.power()
    tv._Television__channel = Television.MIN_CHANNEL
    tv.channel_down()
    assert tv._Television__channel == Television.MAX_CHANNEL

def test_volume_up_max():
    tv = Television()
    tv.power()
    tv._Television__volume = Television.MAX_VOLUME
    tv.volume_up()
    assert tv._Television__volume == Television.MAX_VOLUME

def test_volume_down_min():
    tv = Television()
    tv.power()
    tv._Television__volume = Television.MIN_VOLUME
    tv.volume_down()
    assert tv._Television__volume == Television.MIN_VOLUME

def test_str_muted_volume():
    tv = Television()
    tv.power()
    tv.mute()
    assert "Volume = 0" in str(tv)
