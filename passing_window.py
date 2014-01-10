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


#stationary = 'XYZ'
#passing = 'LMNOPQR'

window = 'LMNOPQR'
passing = 'XYZ'

for view in passing_window(passing, len(window)):
    print window
    print view
    print
