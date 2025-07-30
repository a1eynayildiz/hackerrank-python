if __name__ == '__main__':
    n = int(input())
    arr =list( map(int, input().split()))
    
    maximum=max(arr)
    new_arr=[x for x in arr if x !=maximum]
    
    print(max(new_arr))
    
   