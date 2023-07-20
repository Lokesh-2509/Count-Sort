def count_sort(arr):
    max_element = max(arr)
    count_arr = [0] * (max_element + 1)
    for num in arr:
        count_arr[num] += 1
    sorted_arr = []
    for i in range(len(count_arr)):
        if count_arr[i] > 0:
            sorted_arr.extend([i] * count_arr[i])
    return sorted_arr
if __name__ == "__main__":
    input_str = input("Enter the elements of the array (separated by space): ")
    A = list(map(int, input_str.split()))
    result = count_sort(A)
    print("Sorted array:", result)
