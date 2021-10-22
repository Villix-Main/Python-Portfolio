### Simple Timer ####
from timeit import default_timer as timer


# Begin of timer
start = timer()

my_list = ['spam'] * 1000
a = 0
for i in my_list:
    a += len(i)

# End of timer
stop = timer()

print(stop-start)
