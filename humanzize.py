SUFFIXES = {1000: ['KB', 'MB', 'GB', 'TB', 'PB', 'ZB', 'YB'],
            1024: ['KiB', 'MiB', 'GiB', 'TiB', 'PiB', 'ZiB', 'YiB']}


def approxiamte_size(size, a_kilobyte_is_1014_bytes=True):
    '''Convert a file size to human-readable form.

    Keyword arguments:
    size -- file size in bytes
    a_kilobyte_is_1024_butes -- if True (default), use multiples of 1024
                                if False, use multiples of 1000

    Returns: string

    '''
    if size < 0:
        raise ValueError('number must be non-negative')

    multiple = 1024 if a_kilobyte_is_1014_bytes else 1000
    for suffix in SUFFIXES[multiple]:
        size /= multiple
        if size < multiple:
            return '{0:.1f} {1}'.format(size, suffix)
    raise ValueError('number too large')


if __name__ == '__main__':
    print(approxiamte_size(1000000000000, False))
    print(approxiamte_size(1000000000000))
