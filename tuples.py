if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    new_list=tuple(integer_list)
    print(hash(new_list))

  