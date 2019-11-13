# import random

# def generate_device_token():
#   rands = []
#   for i in range(0,16):
#     r = random.random()
#     rand = 4294967296.0 * r
#     rands.append((int(rand) >> ((3 & i) << 3)) & 255)

#   hexa = []
#   for i in range(0,256):
#     hexa.append(str(hex(i+256)).lstrip("0x").rstrip("L")[1:])

#   id = ""
#   for i in range(0,16):
#     id += hexa[rands[i]]

#     if (i == 3) or (i == 5) or (i == 7) or (i == 9):
#       id += "-"

#   return id
