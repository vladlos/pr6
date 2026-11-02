"""Операції з бронюваннями системи «Аудиторний фонд»."""


def end_minute(start_minute, duration, ofset):
    """Повертає хвилину завершення бронювання."""
    return start_minute + duration + ofset


def overlaps(start_a, end_a, start_b, end_b):
    """Перевіряє, чи перетинаються два бронювання в часі."""
    return start_a < end_b and start_b < end_a
