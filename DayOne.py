import Util

def getSlidingWindows(data, window_size):
    windows = []
    for i in range(len(data) - window_size + 1):
        if i+window_size > len(data):
            break
        windows.append(data[i:i+window_size])
    return windows

def getSumFromWindows(windows):
    window_sums = []
    for window in windows:
        window_sums.append(sum(window))
    return window_sums

def getNumberOfIncrements(data):
    count = 0
    prev_row = data[0]
    for row in data[1:]:
        if row > prev_row:
            count += 1
        prev_row = row
    return count

def main():
    # Part one test
    data = Util.getData('1-part-1-test')
    count = getNumberOfIncrements(data)
    assert count == 7

    # Part one
    data = Util.getData('1-part-1')
    count = getNumberOfIncrements(data)
    assert count == 1688
    print('Part one:', count)

    # Part two test
    window_size = 3
    data = Util.getData('1-part-1-test')
    windows = getSlidingWindows(data, window_size)
    windows = getSumFromWindows(windows)
    count = getNumberOfIncrements(windows)
    assert count == 5

    # Part two
    data = Util.getData('1-part-1')
    windows = getSlidingWindows(data, window_size)
    windows = getSumFromWindows(windows)
    count = getNumberOfIncrements(windows)
    assert count == 1728
    print('Part two:', count)

    return 0

if __name__ == '__main__':
    main()