# coding: utf-8
# vim:sw=4:ts=4:et:
"""Neos utils."""


def round_size(value):
    """Return value rounded to 2 decimal places"""
    value=round(value, 2)
    return value

def humanize_bytes(value, unit='B'):
    """Return humanized value from bytes."""
    if unit == 'KB':
        value=value / 1024
        return round_size(value)
    if unit == 'MB':
        value=value / 1024 / 1024
        return round_size(value)
    elif unit == 'GB':
        value=value / 1024 / 1024 / 1024
        return round_size(value)
    return round_size(value)

