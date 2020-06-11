# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.

import random

import simplepackage


def test_plus_one():
    random.seed()
    a = random.randrange(1000000)
    assert a + 1 == simplepackage.plus_one(a)


def test_plus_two():
    random.seed()
    a = random.randrange(1000000)
    assert a + 2 == simplepackage.plus_two(a)