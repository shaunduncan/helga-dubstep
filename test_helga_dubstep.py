import time

from functools import partial

from helga_dubstep import dubstep


def test_dubstep_gives_wubs():
    assert 'wubwub' in dubstep('', '', '', '', '')


def test_dubstep_stops_after_max():
    dubstep._last = time.time()
    dubstep._counts['#bots'] = 0

    run = partial(dubstep, '', '#bots', '', '', '')

    assert 'wubwub' in run()
    assert 'wubwub' in run()
    assert 'wubwub' in run()
    assert 'STOP' in run()

    # Should start over now
    assert 'wubwub' in run()


def test_dubstep_after_timeout_resets_count():
    dubstep._last = time.time() - 30
    dubstep._counts['#bots'] = 10
    dubstep('', '#bots', '', '', '')
    assert dubstep._counts['#bots'] == 1
