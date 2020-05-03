


import math


print([int(i) for i in range(-5, 4, (3+5)//3)])     # -5 ~ 3
print([int(i) for i in range(-10, 11, int(math.ceil(10+11+3)/5))])     # -5 ~ 3
# print([int(i) for i in range(1, 11, int(math.ceil(1+11+2)/5))])     # 1 ~ 10
# print([int(i) for i in range(0, 11, int(math.ceil(0+11+2)/2))])     # 1 ~ 10


# print([int(i) for i in range(-10, 11, int((10+11+2)/6))]) # -10 ~ 10
# print([int(i) for i in range(1, 11, int((1+11+2)/5))])    #  1 ~ 10
#
# print(int((1+11+2)/5))
# print((1+11) / 5)