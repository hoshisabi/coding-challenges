import pickle
import time
import bz2


for n in range(1, 200):
    start = time.perf_counter()
    listfile = bz2.open('testpickle.bz', 'rb')
    big_list = pickle.load(listfile)
    #print(len(big_list))
    listfile.close()
    end = time.perf_counter()
    print(f"One loop took: {end - start:0.4f} seconds")
    time.sleep(1)
