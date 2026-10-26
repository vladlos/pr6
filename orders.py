"""Операції із замовленнями системи «КіберМаркет»."""


def free_stock(quantity, reserved):
    """Повертає вільний залишок: кількість мінус резерв."""
    return quantity - reserved


def can_order(requested, quantity, reserved):
    """Перевіряє, чи вистачає вільного залишку на замовлення."""
    return free_stock(quantity, reserved) >= requested
