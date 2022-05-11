from typing import List

from .base import BTBaseRow
from .enums import Alignment


class MetaData(BTBaseRow):
    def __init__(self, table, row: List):
        for i in row:
            self.validate(i)
        super(MetaData, self).__init__(table, row)

    def __setitem__(self, key: int, value: int):
        self.validate(value)
        super(MetaData, self).__setitem__(key, value)

    def validate(self, value):
        pass


class AlignmentMetaData(MetaData):
    def validate(self, value: Alignment):
        if not isinstance(value, Alignment):
            allowed = (f"{type(self).__name__}.{i.name}" for i in Alignment)
            error_msg = (
                "allowed values for alignment are: "
                + ", ".join(allowed)
                + f", was {value}"
            )

            raise TypeError(error_msg)


class NonNegativeIntegerMetaData(MetaData):
    def validate(self, value):
        if isinstance(value, int) and value >= 0:
            pass
        else:
            raise TypeError(
                ("Value must a non-negative integer, " "was {}").format(value)
            )
