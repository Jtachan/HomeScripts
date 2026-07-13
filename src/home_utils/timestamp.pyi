class Timestamp:
    """Class holding a timestamp as a set of three integers.

    When initializing the class, any overflown value is carried automatically
    to the next field. For example, initializing an instance with `seconds=3600`
    will return an instance equal to initializing to `hours=1`.

    Attributes
    ----------
    hours: int, default = 0
    minutes: int, default = 0
    seconds: int, default = 0
    """

    @classmethod
    def from_str(cls, timestamp: str) -> Timestamp:
        """Initialization from a string with format '(\d+)h (\d+)min (\d+)s'."""

    @property
    def all_seconds(self) -> int:
        """Returns the value of the timestamp as only seconds."""

    def calculate_mean(self, nof_timestamps: int) -> Timestamp:
        """Calculates the mean timestamp assuming X timestamps.

        This function assumes the current `Timestamp` instance is already the
        sum of as many timestamps as the provided at the input parameter.
        """
