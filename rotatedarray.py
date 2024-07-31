arr=[1,2,3,4,5]
print("original array: ",arr)
arr1=arr[2:]+arr[:2]
print("rotated array: ",arr1)


#OR
def rotate(arr,pos):
    pos=pos%len(arr)
    return arr[pos:]+arr[:pos]
arr=[6,7,8,9,10]
print("original array: ",arr)
pos=2
print("Rotated array:",rotate(arr,pos))
