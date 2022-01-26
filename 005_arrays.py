# Arrays
# Find sum of an array and display the output . Example [10,4,5,2,5,6,9].
def arrSum(arr):
    result = 0
    for i in arr:
        result += i
    return result
# print(arrSum([10,4,5,2,5,6,9]))

# Find average of an array and display the output.
def arrAvg(arr):
    totalSum = 0
    for i in arr:
        totalSum += i
    avg = totalSum / len(arr)
    return avg
# print(arrAvg([10,4,5,2,5,6,9]))

# Find maximum and minimum of an array.
def minMax(arr):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i] 
    minVal,maxVal = arr[0], arr[-1]       
    return minVal,maxVal
    
    # arr.sort()
    # return arr[0], arr[-1]
# print(minMax([10,4,5,2,5,6,9]))

# Find Median and Mode of an array.
#     Median : (N+1/2)th term.
#     Mode : Most repeating term
from statistics import mode
def medMode(arr):
    median = (len(arr)+1)/2
    modeVal = mode(arr)
    return modeVal,median
# print(medMode([10,4,5,2,5,6,9]))

# Find sum of two arrays.
#     [3,5,2,9,4] = 3+5+2+9+4 = 23
#     [6,2,8,1,3] = 6+2+8+1+3 = 20
#     Final Output : 20+23 = 43
def twoSumArr(arr1, arr2):
    result = 0
    for i in range(len(arr1)):
        result += arr1[i] + arr2[i]
    return result
# print(twoSumArr([3,5,2,9,4], [6,2,8,1,3]))

# Shift an array by X to right.
#     Example [1,2,3,4,5] after shifting to right [5,1,2,3,4]
def shiftArr(arr):
    return arr[-1:]+arr[:-1]
# print(shiftArr([1,2,3,4,5]))

# Find the sum of two matrix.
X = [[1,2,3],
    [4 ,5,6],
    [7 ,8,9]]
 
Y = [[9,8,7],
    [6,5,4],
    [3,2,1]]
result = [[0,0,0],
         [0,0,0],
         [0,0,0]]

for i in range(len(X)):
    for j in range(len(X[i])):
        result[i][j] = X[i][j]+Y[i][j]
# print(result)
# for r in result:
#     print(r)

# Transpose
X = [[1,2],
    [3,4]]
print(X)
for i in X:
    print(i)
for i in range(len(X)):
    for j in range(len(X[i])):
        x_trans = X[i][j]