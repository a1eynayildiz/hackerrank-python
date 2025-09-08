import textwrap

def wrap(string, max_width):
    return textwrap.fill(string, max_width)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)

#Dokumanda textwrap için 2 adet method verilmişti wrap ve fill.Bu soruda uygun çözüm fill ile sağlandı.
#Çünkü wrap kullansaydık bir liste döndürürdük.Fill kullanarak metindeki tek bir paragrafı çıktı olarak paragrafı içeren tek bir string döndürdük.