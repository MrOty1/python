import random

# sar = []
# kiek = random.randint(5, 25)
# for i in range(kiek):
#     paz = random.randint(2, 10)
#     sar.append(paz)

sar = [random.randint(2, 10) for _ in range(random.randint(5, 25))]

print(sar)