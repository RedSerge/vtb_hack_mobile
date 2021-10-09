from random import randint, triangular

avg = lambda values: sum(values) / len(values)
sign_pos = lambda num: int(abs(num) / num) if num != 0 else 1
random_sign = lambda: -1 + 2 * randint(0, 1)


def gen_stock_price(value_base, value_delta, value_decay, timestamp):
    value_current = value_base
    for _ in range(timestamp):
        if value_decay > 0:
            current_value_decay = triangular(value_delta) * value_base / value_current
        else:
            current_value_decay = triangular(value_delta) * value_current / value_base
        value_current -= current_value_decay - value_decay
        yield value_current
