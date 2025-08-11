import pytest
from television import *

from television import Television


class Test:
    def setup_method(self):
        self.tv1 = Television()
        self.tv2 = Television()

    def teardown_method(self):
        del self.tv1
        del self.tv2

    def test_init(self):
        assert self.tv1.__str__() == "Power = False, Channel = 0, Volume = 0"
        assert self.tv2.__str__() == "Power = False, Channel = 0, Volume = 0"

    def test_power(self):
        self.tv1.power()
        assert self.tv1.__str__() == "Power = True, Channel = 0, Volume = 0"
        assert self.tv2.__str__() == "Power = False, Channel = 0, Volume = 0"
        self.tv1.power()
        assert self.tv1.__str__() == "Power = False, Channel = 0, Volume = 0"
        assert self.tv2.__str__() == "Power = False, Channel = 0, Volume = 0"

    def test_mute(self):
        self.tv1.power()
        self.tv1.volume_up()
        self.tv1.mute()
        assert self.tv1.__str__() == "Power = True, Channel = 0, Volume = 0"
        assert self.tv2.__str__() == "Power = False, Channel = 0, Volume = 0"
        self.tv1.mute()
        assert self.tv1.__str__() == "Power = True, Channel = 0, Volume = 1"
        assert self.tv2.__str__() == "Power = False, Channel = 0, Volume = 0"
        self.tv1.power()
        self.tv1.mute()
        assert self.tv1.__str__() == "Power = False, Channel = 0, Volume = 1"
        assert self.tv2.__str__() == "Power = False, Channel = 0, Volume = 0"
        self.tv1.mute()
        assert self.tv1.__str__() == "Power = False, Channel = 0, Volume = 1"
        assert self.tv2.__str__() == "Power = False, Channel = 0, Volume = 0"

    def test_channel_up(self):
        self.tv1.channel_up()
        assert self.tv1.__str__() == "Power = False, Channel = 0, Volume = 0"
        assert self.tv2.__str__() == "Power = False, Channel = 0, Volume = 0"
        self.tv1.power()
        self.tv1.channel_up()
        assert self.tv1.__str__() == "Power = True, Channel = 1, Volume = 0"
        assert self.tv2.__str__() == "Power = False, Channel = 0, Volume = 0"
        self.tv1.channel_up()
        self.tv1.channel_up()
        self.tv1.channel_up()
        assert self.tv1.__str__() == "Power = True, Channel = 0, Volume = 0"
        assert self.tv2.__str__() == "Power = False, Channel = 0, Volume = 0"

    def test_channel_down(self):
        self.tv1.channel_down()
        assert self.tv1.__str__() == "Power = False, Channel = 0, Volume = 0"
        assert self.tv2.__str__() == "Power = False, Channel = 0, Volume = 0"
        self.tv1.power()
        self.tv1.channel_down()
        assert self.tv1.__str__() == "Power = True, Channel = 3, Volume = 0"
        assert self.tv2.__str__() == "Power = False, Channel = 0, Volume = 0"

    def test_volume_up(self):
        self.tv1.volume_up()
        assert self.tv1.__str__() == "Power = False, Channel = 0, Volume = 0"
        assert self.tv2.__str__() == "Power = False, Channel = 0, Volume = 0"
        self.tv1.power()
        self.tv1.volume_up()
        assert self.tv1.__str__() == "Power = True, Channel = 0, Volume = 1"
        assert self.tv2.__str__() == "Power = False, Channel = 0, Volume = 0"
        self.tv1.mute()
        self.tv1.volume_up()
        assert self.tv1.__str__() == "Power = True, Channel = 0, Volume = 2"
        assert self.tv2.__str__() == "Power = False, Channel = 0, Volume = 0"
        self.tv1.volume_up()
        assert self.tv1.__str__() == "Power = True, Channel = 0, Volume = 2"
        assert self.tv2.__str__() == "Power = False, Channel = 0, Volume = 0"

    def test_volume_down(self):
        self.tv1.volume_down()
        assert self.tv1.__str__() == "Power = False, Channel = 0, Volume = 0"
        assert self.tv2.__str__() == "Power = False, Channel = 0, Volume = 0"
        self.tv1.power()
        self.tv1.volume_up()
        self.tv1.volume_up()
        self.tv1.volume_down()
        assert self.tv1.__str__() == "Power = True, Channel = 0, Volume = 1"
        assert self.tv2.__str__() == "Power = False, Channel = 0, Volume = 0"
        self.tv1.volume_up()
        self.tv1.mute()
        self.tv1.volume_down()
        assert self.tv1.__str__() == "Power = True, Channel = 0, Volume = 1"
        assert self.tv2.__str__() == "Power = False, Channel = 0, Volume = 0"
        self.tv1.volume_down()
        self.tv1.volume_down()
        assert self.tv1.__str__() == "Power = True, Channel = 0, Volume = 0"
        assert self.tv2.__str__() == "Power = False, Channel = 0, Volume = 0"


if __name__ == '__main__':
    pytest.main()