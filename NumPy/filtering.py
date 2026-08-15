import numpy as np

ages = np.array([[44, 18, 12, 9, 10],
                 [43, 33, 15, 19, 65]])

# teenagers = ages[ages < 18]
# # print(teenagers)

# adults = ages[(ages >= 18) & (ages < 60)]
# others = ages[(ages < 18) | (ages >= 60)]

# seniors = ages[ages >= 60]
# even = ages[ages % 2 == 0]
# odd = ages[ages % 2 != 0]

# print(adults)
# print(others)
# print(seniors)
# print(even)
# print(odd)

adults = np.where(ages >= 18 , ages, 0)
others = np.where((ages < 18 & ages > 60), ages, -1)

print(adults)