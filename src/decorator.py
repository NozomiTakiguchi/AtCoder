import time
import psutil
import datetime

def trace_perf(func):
    def trace_perf(*args, **kwargs):
        name = func.__name__
        s_mem = psutil.virtual_memory().percent
        s_time = time.time()
        func(*args, **kwargs)
        e_time = time.time()
        e_mem = psutil.virtual_memory().percent

        #TODO impl logger
        print('[PERFORMANCE INFO][{}] function=[{}], latency=[{}], memory=[{}]'.format(datetime.datetime.now(), name, e_time - s_time, e_mem - s_mem))
    return trace_perf
