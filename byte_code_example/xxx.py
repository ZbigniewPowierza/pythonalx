program = """
x = 1
y = 2
print(x+y)

"""

import dis
print(dis.dis(program))

# wynik dzałania
#   2           0 LOAD_CONST               0 (1)
#               2 STORE_NAME               0 (x)
#
#   3           4 LOAD_CONST               1 (2)
#               6 STORE_NAME               1 (y)
#
#   4           8 LOAD_NAME                2 (print)
#              10 LOAD_NAME                0 (x)
#              12 LOAD_NAME                1 (y)
#              14 BINARY_ADD
#              16 CALL_FUNCTION            1
#              18 POP_TOP
#              20 LOAD_CONST               2 (None)
#              22 RETURN_VALUE
# None

