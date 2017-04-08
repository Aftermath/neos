# coding: utf-8
# vim:sw=4:ts=4:et:
"""Neos utils."""


def humanize_bytes(value, unit='KB'):
    """Return humanized value from kilobytes."""
    if unit == 'MB':
        return value / 1024
    elif unit == 'GB':
        return value / 1024 / 1024
    return value
