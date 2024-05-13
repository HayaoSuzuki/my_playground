# SPDX-FileCopyrightText: 2024-present Hayao Suzuki <hayao.math@gmail.com>
#
# SPDX-License-Identifier: MIT

import collections.abc
import math
import typing

PHI: typing.Final[float] = (1 + math.sqrt(5)) / 2


class FibonacciSized(collections.abc.Sized):

    def __init__(self, data: typing.Optional[collections.abc.Iterable] = None):
        if data is not None:
            self._data = [v for v in data]
        else:
            self._data = []

    def __repr__(self) -> str:
        return repr(self._data)

    def __str__(self) -> str:
        return str(self._data)

    def __len__(self) -> int:
        return math.floor((1 / math.sqrt(5)) * pow(PHI, len(self._data)) + (1 / 2))
