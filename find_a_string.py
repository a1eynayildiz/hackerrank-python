def count_substring(string, sub_string):
  count=0
  for i in range(len(string)-len(sub_string)+1):#kaç aralığı kontrol edeceğini buradan kontrol etmesi lazım
    if string[i:i+len(sub_string)] == sub_string:#stringin içinde sub_stringe kadar dolaşır eğer sub_stringle eşleşen bir ifade bulursa countu 1 artırır.
        count +=1
    
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)