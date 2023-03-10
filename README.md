import math

arr =["Arsel", "Avivah", "Daiva", ["Wahyu", "Wibi"]]
list1 = ["Arsel", "Avivah", "Daiva"]
list2 = ["Wahyu", "Wibi"]

def jumpSearch(arr, x, n ):
    step = math.sqrt(n)
    prev = 0
    while arr[int(min(step, n)-1)] < x:
        prev = step
        step += math.sqrt(n)
        if prev >= n:
            return -1
    while arr[int(prev)] < x:
        prev += 1
        if prev == min(step, n):
            return -1
    if arr[int(prev)] == x:
        return prev
    return -1

x = "Arsel"
n = len(arr)
index = jumpSearch(arr, x, n)
print(x, "berada di indeks" ,"%.0f"%index)

x = "Avivah"
n = len(arr)
index = jumpSearch(arr, x, n)
print(x, "berada di indeks" ,"%.0f"%index)

print(list2[0], "berada di indeks 3 pada kolom 0")
print(list2[1], "berada di indeks 3 pada kolom 1")
