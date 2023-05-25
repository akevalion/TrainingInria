from mytimer import Timer
# test for classes
# 1. a timer without initia value is set to 0
# 2. A timer next method decrese the timer stat

def test_timer_is_zero_by_default():
    timer = Timer()
    assert timer.current() == 0

def test_timer_can_be_initialized():
    timer = Timer(10)
    assert timer.current() == 10

def test_timer_next_decreases_timer_state():
    timer = Timer(10)
    timer.next()
    assert timer.current() == 9

def test_timer_decreases_only_to_zero():
    # setup
    timer = Timer(0)
    # exercise
    timer.next()
    # check expectations
    assert timer.current() == 0