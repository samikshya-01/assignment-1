import numpy as np
import time

np.random.seed(7)
cities = np.array(["Kathmandu", "Pokhara", "Biratnagar", "Lalitpur", "Birgunj"])
days = np.array([f"D{i:02d}" for i in range(1, 15)])

temps = np.random.randint(14, 36, size=(5, 14)).astype(float)                 # °C, 5 cities × 14 days
humidity = np.random.randint(40, 95, size=(5, 14)).astype(float)              # %

temps[2, 5] = np.nan          # sensor outage
temps[4, 11] = np.nan

# ---------- B1: Array anatomy and reshaping ----------
print("B1 shape:", temps.shape, "| ndim:", temps.ndim, "| dtype:", temps.dtype, "| size:", temps.size)
a = np.arange(70)
r1 = a.reshape(5, 14)
r2 = a.reshape(5, -1)
print("B1 explicit vs -1 identical:", np.array_equal(r1, r2))
print("B1 flattened back, shape:", r1.ravel().shape)
##What -1 means?
#Suppose you have a single row of 70 objects and you want to divide them into 5 rows which means each row gets 14 objects
# because 70/5 = 14 and that is what -1 do like i will give you the rows and you figure out the rest.
# Just like how I wrote (5, -1) in the code and numpy gave me 14.

##Why reshape doesn't copy?
#Reshape doesn't copy because in memory, data is stored in a continuous line and reshaping is just a way of changing how
# we view it not change the actual data or copy it. And it is more efficient because it takes less memory.

# ---------- B2: Indexing and slicing ----------
print("B2a Pokhara day 3:", temps[1, 2], "shape:", temps[1, 2].shape)
print("B2b every city, last day:", temps[:, -1], "shape:", temps[:, -1].shape)
print("B2c Biratnagar fortnight:", temps[2], "shape:", temps[2].shape)
print("B2d first 3 cities, days 4-8:\n", temps[:3, 3:8], "shape:", temps[:3, 3:8].shape)
print("B2e Lalitpur every other day:", temps[3, ::2], "shape:", temps[3, ::2].shape)
print("B2f Kathmandu reversed:", temps[0, ::-1], "shape:", temps[0, ::-1].shape)

# ---------- B3: Boolean masks ----------
hot = temps > 30
print("B3a readings above 30 per city:", hot.sum(axis=1))
print("B3b days Kathmandu exceeded 30:", days[hot[0]])
##What is a mask and why temps[temps > 30] can't keep the 2D shape?
#A mask is a True/False grid which returns the only two possible outcomes and temps goes flat because Kathmandu has 1 hot
# day while Birgunj has 6 so numpy cannot keep it as rows since every row should be same length within the grid which
# is not possible with two different values so it cannot keep the 2D shapeand gives a simple list.

# ---------- B4: Views vs copies ----------
demo = temps.copy()          # work on a copy so the real temps stays untouched for B5-B10
view = demo[0, :3]
view[0] = 999
print("B4 original after changing the VIEW:", demo[0, :3])      # 999 appears

demo = temps.copy()
cp = demo[0, :3].copy()
cp[0] = 999
print("B4 original after changing the COPY:", demo[0, :3])      # unchanged
##Why NumPy defaults to a view, and what bug this causes if you forget?
#Numpy defaults to a view because it saves memory and you can change the original data without having to copy it and
# if you forget that it is a view and accidentally change the original data, then it causes bugs in the code.
# So, I only recommend this when you actually know what to change and how will it work and if not then just use a copy to
# avoid errors.