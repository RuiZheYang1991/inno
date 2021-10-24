# import multiprocessing
#
# def spawn_process(i):
#    print ('This is process: %s' %i)
#    import time
#    time.sleep(100)
#    return
#
# if __name__ == '__main__':
#     Process_jobs = []
#     for i in range(3):
#         p = multiprocessing.Process(target = spawn_process, args = (i,))
#         Process_jobs.append(p)
#         p.start()
#     p.join()
import numpy as np
import pandas as pd
a=np.array([5])
b=np.array([2])
c=np.append(arr=a,values=b)
print(c[0])