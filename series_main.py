import pandas as pd
import numpy as np

data = [10, 20, np.nan, 40, 50, 60, np.nan, 80, 90, 100]
index = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
s = pd.Series(data, index=index)


print("Original Series:\n", s)
print("\nAccess by index label 'a':", s['a'])
print("Access by position 2:", s.iloc[2])
print("\nValues greater than 50:\n", s[s > 50])
print("\nFill NaN with 0:\n", s.fillna(0))
print("Drop NaN values:\n", s.dropna())

print("\nSum:", s.sum())
print("Mean:", s.mean())
print("Median:", s.median())
print("Standard Deviation:", s.std())
print("Minimum value:", s.min())
print("Maximum value:", s.max())

print("\nIndex values:", s.index)
print("Is 'e' in index?:", 'e' in s)

print("\nSquared values using apply:\n", s.apply(lambda x: x**2))

s_str = pd.Series(['cat', 'dog', 'rabbit', 'snake'])
print("\nString Series:\n", s_str)
print("Uppercase strings:\n", s_str.str.upper())
print("Strings containing 'a':\n", s_str.str.contains('a'))

print("\nSorted by values:\n", s.sort_values())
print("Sorted by index:\n", s.sort_index())
print("Rank of values:\n", s.rank())

print("\nAggregated stats:\n", s.agg(['sum', 'min', 'max', 'mean']))

new_index = ['a', 'b', 'c', 'x', 'y', 'z']
print("\nReindexed Series:\n", s.reindex(new_index, fill_value=0))

s2 = pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e'])
print("\nAddition with another Series:\n", s + s2)

print("\nCumulative Sum:\n", s.cumsum())

s_copy = s.copy()
print("\nCopied Series:\n", s_copy)

print("\nConvert to list:", s.tolist())
print("Convert to dictionary:", s.to_dict())
print("Convert to numpy array:", s.to_numpy())

#OUTPUT
Original Series:
a     10.0
b     20.0
c      NaN
d     40.0
e     50.0
f     60.0
g      NaN
h     80.0
i     90.0
j    100.0
dtype: float64

Access by index label 'a': 10.0
Access by position 2: nan

Values greater than 50:
 f     60.0
h     80.0
i     90.0
j    100.0
dtype: float64

Fill NaN with 0:
 a     10.0
b     20.0
c      0.0
d     40.0
e     50.0
f     60.0
g      0.0
h     80.0
i     90.0
j    100.0
dtype: float64
Drop NaN values:
 a     10.0
b     20.0
d     40.0
e     50.0
f     60.0
h     80.0
i     90.0
j    100.0
dtype: float64

Sum: 450.0
Mean: 56.25
Median: 55.0
Standard Deviation: 32.486260832190936
Minimum value: 10.0
Maximum value: 100.0

Index values: Index(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'], dtype='object')
Is 'e' in index?: True

Squared values using apply:
 a      100.0
b      400.0
c        NaN
d     1600.0
e     2500.0
f     3600.0
g        NaN
h     6400.0
i     8100.0
j    10000.0
dtype: float64

String Series:
 0       cat
1       dog
2    rabbit
3     snake
dtype: object
Uppercase strings:
 0       CAT
1       DOG
2    RABBIT
3     SNAKE
dtype: object
Strings containing 'a':
 0     True
1    False
2     True
3     True
dtype: bool

Sorted by values:
 a     10.0
b     20.0
d     40.0
e     50.0
f     60.0
h     80.0
i     90.0
j    100.0
c      NaN
g      NaN
dtype: float64
Sorted by index:
 a     10.0
b     20.0
c      NaN
d     40.0
e     50.0
f     60.0
g      NaN
h     80.0
i     90.0
j    100.0
dtype: float64
Rank of values:
 a    1.0
b    2.0
c    NaN
d    3.0
e    4.0
f    5.0
g    NaN
h    6.0
i    7.0
j    8.0
dtype: float64

Aggregated stats:
 sum     450.00
min      10.00
max     100.00
mean     56.25
dtype: float64

Reindexed Series:
 a    10.0
b    20.0
c     NaN
x     0.0
y     0.0
z     0.0
dtype: float64

Addition with another Series:
 a    11.0
b    22.0
c     NaN
d    44.0
e    55.0
f     NaN
g     NaN
h     NaN
i     NaN
j     NaN
dtype: float64

Cumulative Sum:
 a     10.0
b     30.0
c      NaN
d     70.0
e    120.0
f    180.0
g      NaN
h    260.0
i    350.0
j    450.0
dtype: float64

Copied Series:
 a     10.0
b     20.0
c      NaN
d     40.0
e     50.0
f     60.0
g      NaN
h     80.0
i     90.0
j    100.0
dtype: float64

Convert to list: [10.0, 20.0, nan, 40.0, 50.0, 60.0, nan, 80.0, 90.0, 100.0]
Convert to dictionary: {'a': 10.0, 'b': 20.0, 'c': nan, 'd': 40.0, 'e': 50.0, 'f': 60.0, 'g': nan, 'h': 80.0, 'i': 90.0, 'j': 100.0}
Convert to numpy array: [ 10.  20.  nan  40.  50.  60.  nan  80.  90. 100.]
