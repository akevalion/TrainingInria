class Timer:
    """
    Declare a timer
    a = Timer(1)

    """
    def __init__(self, initial: int = 0) -> None:
        self._count = initial

    # @property
    def current(self) -> int:
        # return the value
        return self._count
    
    def next(self) -> None:
        if self._count > 0:
            self._count -= 1