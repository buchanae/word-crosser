def passing_window(passing, window_size):
    parts = []

    for i in range(1, window_size + len(passing)):
        if i <= len(passing):
            part_length = i
            part = passing[-part_length:]
            padding = 0
        elif i > window_size:
            part_length = i - window_size
            part = passing[:-part_length]
            padding = window_size
        else:
            part = passing
            padding = i

        if len(part) > window_size:
            part = part[:window_size]

        part = part.rjust(padding)
        parts.append(part)

    return parts


def debug(window, passing):

    s = set()
    for view in passing_window(passing, len(window)):
        for a, b in zip(view, window):
            if a != ' ':
                p = a + b
                s.add(p)

                p = b + a
                s.add(p)

    return s

if __name__ == '__main__':

    A = 'XYZ'
    B = 'LMNOPQR'

    a = debug(A, B)
    b = debug(B, A)

    assert a == b
