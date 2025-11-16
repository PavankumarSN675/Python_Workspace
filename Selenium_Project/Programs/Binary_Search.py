
class binary_search:
    def binary_search(self, list, key):
        low = 0
        high = len(list)-1
        mid = 0
        while low <= high:
            mid = (low+high)//2
            if list[mid] > key:
                high = mid - 1
            elif list[mid] < key:
                low = mid + 1
            else:
                return mid

        return -1


binary_search = binary_search()
# ele_list = [12, 24, 32, 39, 45, 50, 54]
ele_list = [12, 24, 32, 39, 45, 50, 54, 24, 37, 15, 48]
ele_list = sorted(ele_list)
print(ele_list)
key = 15
result = binary_search.binary_search(ele_list, key)
if result != -1:
    print("The key is present in the list")
else:
    print("The key is not present in the list")