# -*- coding: utf-8 -*-
import pytest

from python.gilded_rose import Item, GildedRose


def test_item():
    items = [Item("foo", 0, 0)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert ("foo" == items[0].name)


def test_items_value_decreases_by_one_everyday():
    items = [Item("foo", 1, 0)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].quality == 0


def test_items_value_does_not_drop_below_zero():
    items = [Item("foo", 0, 0)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].quality == 0


