# Assume that a function called compute() has already been defined for you. This function is very computationally intensive, and can create quite a lot of overhead in programs. Your task is to profile this function (aka measure how long it takes for it to run). Save the value in a float variable called runtime. Your measurement must be in seconds.
import time
start = time.process_time()
compute()
end = time.process_time()
runtime = start - end