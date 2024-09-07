#!/usr/bin/python3
""" UTF-8 Validation """


def validUTF8(data):
    """
    Determines if given data set represents valid UTF-8 encoding.
    """
    number_bytes = 0

    data_1 = 1 << 7
    data_2 = 1 << 6

    for i in data:

        data_byte = 1 << 7

        if number_bytes == 0:

            while data_byte & i:
                number_bytes += 1
                data_byte = data_byte >> 1

            if number_bytes == 0:
                continue

            if number_bytes == 1 or number_bytes > 4:
                return False

        else:
            if not (i & data_1 and not (i & data_2)):
                    return False

        number_bytes -= 1

    if number_bytes == 0:
        return True

    return False
