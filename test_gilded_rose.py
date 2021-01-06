# -*- coding: utf-8 -*-
import pytest
import mock

from python.gilded_rose import Item, GildedRose


def test_item():  # line 46
    items = [Item("foo", 0, 0)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert ("foo" == items[0].name)


def test_items_value_decreases_by_one_everyday():  # line 12-13
    items = [Item("foo", 1, 0)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].quality == 0


def test_items_value_does_not_drop_below_zero():  # line 12-13
    items = [Item("foo", 0, 0)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].quality == 0


def test_aged_brie_value_increases_twice_faster_when_sell_in_below_zero():  # line 35-36
    items = [Item("Aged Brie", 0, 8)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].quality == 10


def test_aged_brie_quality_increases_when_sell_in_decreases():
    items = [Item("Aged Brie", 10, 10)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].quality == 11
    assert items[0].sell_in == 9


def test_items_quality_is_never_more_than_50():
    items = [Item("Aged Brie", 0, 50),
             Item("Aged Brie", 0, 49)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].quality == 50
    assert items[1].quality == 50


def test_sulfuras_never_sold_or_decreases_in_quality():
    items = [Item("Sulfuras, Hand of Ragnaros", 10, 10)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].quality == 10
    assert items[0].sell_in == 10


def test_aged_brie_and_backstage_quality_increases_when_sell_in_decreases():  # line 15-16
    items = [Item("Aged Brie", 10, 10),
             Item("Backstage passes to a TAFKAL80ETC concert", 20, 20),
             Item("Backstage passes to a TAFKAL80ETC concert", 8, 20),
             Item("Backstage passes to a TAFKAL80ETC concert", 2, 20)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].quality == 11
    assert items[0].sell_in == 9
    assert items[1].quality == 21
    assert items[1].sell_in == 19
    assert items[2].quality == 22
    assert items[2].sell_in == 7
    assert items[3].quality == 23
    assert items[3].sell_in == 1


# def test_aged_brie_value_increases_by_one_everyday():  # line 35-36
#     items = [Item("Aged Brie", 10, 9)]
#     gilded_rose = GildedRose(items)
#     gilded_rose.update_quality()
#     assert items[0].quality == 10
#
#
# def test_backstage_quality_zeroed_when_sell_in_drops_below_zero():  # line 33
#     items = [Item("Backstage passes to a TAFKAL80ETC concert", 0, 0)]
#     gilded_rose = GildedRose(items)
#     gilded_rose.update_quality()
#     assert items[0].quality == 0
#
#
# def test_items_quality_decreases_twice_faster_when_sell_in_below_zero():  # line 30-31
#     items = [Item("foo", 0, 10)]
#     gilded_rose = GildedRose(items)
#     gilded_rose.update_quality()
#     assert items[0].quality == 8


# def test_backstage_quality_increases_when_it_is_below_50_sell_in_below_11():  # lines 17-18-19-20


# def test_backstage_quality_increases_when_it_is_below_50_sell_in_below_6():  # lines 21-22-23

