# -*- coding: utf-8 -*-
import time
def dec(funk):
    def a():
        start_time = time.time()
        funk()
        print(time.time() - start_time)
    return a
@dec
def func_to_decor():
    for i in range(1000):
        print(i)
func_to_decor()