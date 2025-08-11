class Television:
    """
    A class representing details about a television object.
    """
    MIN_VOLUME: int = 0
    MAX_VOLUME: int = 2
    MIN_CHANNEL: int = 0
    MAX_CHANNEL: int = 3

    def __init__(self) -> None:
        """
        Method to set default values for a television object.
        """
        self.__status: bool = False
        self.__muted: bool = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL

    def power(self) -> None:
        """
        Method to set power status of television object.
        """
        if self.__status:
            self.__status = False
        else:
            self.__status = True

    def mute(self) -> None:
        """
        Method to set mute status of television object.
        """
        if self.__status:

            if self.__muted:
                self.__muted = False
            else:
                self.__muted = True

    def channel_up(self) -> None:
        """
        Method to set channel of television object one higher.
        """
        if self.__status:

            target_up_channel = self.__channel + 1

            if target_up_channel > Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL
            else:
                self.__channel = target_up_channel

    def channel_down(self) -> None:
        """
        Method to set channel of television object one lower.
        """
        if self.__status:

            target_down_channel = self.__channel - 1

            if target_down_channel < Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL
            else:
                self.__channel = target_down_channel

    def volume_up(self) -> None:
        """
        Method to set volume level of television object one higher.
        """
        if self.__status:

            if self.__muted:
                self.__muted = False

            if self.__volume == Television.MAX_VOLUME:
                pass
            else:
                self.__volume = self.__volume + 1

    def volume_down(self) -> None:
        """
        Method to set volume level of television object one lower.
        """
        if self.__status:

            if self.__muted:
                self.__muted = False

            if self.__volume == Television.MIN_VOLUME:
                pass
            else:
                self.__volume = self.__volume - 1

    def __str__(self) -> str:
        """
        Method to return string containing a television object's current details.
        :return: A string containing a television object's current details.
        """
        if self.__muted:
            return f"Power = {self.__status}, Channel = {self.__channel}, Volume = 0"
        else:
            return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}"
