##Basics which are important

class BinarySearch:
    def FindThroughBSRecursive(low,high,arr,target):
        if (low <= high):
            mid = low + (high -low)//2
            if(arr[mid] == target):
                return mid
            elif(target > arr[mid]):
                return BinarySearch.FindThroughBSRecursive(mid+1,high,arr,target)
            else:
                return BinarySearch.FindThroughBSRecursive(low,high-1,arr,target)
        else:
            return -1

    def FindThroughBSIterative(arr,target):
        low = 0
        high = len(arr) -1
        while(high >= low):
            mid = low + (high-low)//2
            if(arr[mid] == target):
                return mid
            elif(arr[mid] < target):
                low = mid + 1
            else :
                high = mid - 1
        return -1
                

if __name__ == "__main__":
    nums = [-1,0,3,5,9,12]
    target = 9
    print("Recursive Test",BinarySearch.FindThroughBSRecursive(0,len(nums),nums,target))
    print("Iterative Test",BinarySearch.FindThroughBSIterative(nums,target))
