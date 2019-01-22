# import numpy as np
# a = np.arange(1,10,2.5)     # Here 2 in brackets is third argument which is optional and called as step value
# # and step value can be integer as well as float too.
#
# print(a)
#
# # 1 Dimensional array
# import numpy as np
# a = np.array([2,4,4,5,6,67,2])
#
# # 2 Dimensional arrays
# # 3 x 3 Arrays
# b = np.array([
#     [1,2,3],
#     [1,2,3],
#     [1,2,3]
# ])
#
#
# # 3 Dimensional arrays
# # 3 x 3 x 3
#
# import numpy as np
# a = np.arange(1,10,2.5)     # Here 2 in brackets is third argument which is optional and called as step value
# # and step value can be integer as well as float too.
#
# print(a)
#
# # 1 Dimensional array
# import numpy as np
# a = np.array([2,4,4,5,6,67,2])
#
# # 2 Dimensional arrays
# # 3 x 3 Arrays
# b = np.array([
#     [1,2,3],
#     [1,2,3],
#     [1,2,3]
# ])
#
#
# # 3 Dimensional arrays
# # 3 x 3 x 3
#
# c = np.array([
#     [[1,2,3],[1,2,3],[1,2,3],
#     [1,2,3],[1,2,3],[1,2,3],
#     [1,2,3],[1,2,3],[1,2,3]
#      ]])
#
# print(c)
# print(c.shape)

# zeros function in numpy
import numpy as np
b = np.zeros((4,4), dtype=np.int16)
print(b)