import pickle
import bz2

big_list = [(x, y) for x in range(1, 1000) for y in range(1, 1000)]

listfile = bz2.open('testpickle.bz', 'wb')
pickle.dump(big_list, listfile)
listfile.close()

print("Finished saving.")