if __name__ == '__main__':
    s = input()
    
    print(any(c.isalnum()for c in s))
    print(any(c.isalpha()for c in s))
    print(any(c.isdigit()for c in s))
    print(any(c.islower()for c in s))
    print(any(c.isupper()for c in s))

#okunabilirliği az ama tek satırda.....
s = input().strip()
print(*(any(f(s) for f in [str.isalnum, str.isalpha, str.isdigit, str.islower, str.isupper])), sep='\n')

"""
f(s) for f in [str.isalnum, str.isalpha, str.isdigit, str.islower, str.isupper]

Burada bir generator expression var.

[str.isalnum, str.isalpha, str.isdigit, str.islower, str.isupper] ----> bir liste, içinde fonksiyonlar var.

for f in [...] ----> listedeki her fonksiyonu sırayla f olarak al.

f(s) → her fonksiyonu string s üzerinde uygula.

Örneğin, s = "qA2" için:

str.isalnum(s) → True (çünkü en az bir alfanümerik karakter var)

str.isalpha(s) → True (en az bir alfabetik var)

str.isdigit(s) → True (en az bir rakam var)

str.islower(s) → True (en az bir küçük harf var)

str.isupper(s) → True (en az bir büyük harf var)

any(...)

any() fonksiyonu, içindeki iterable’da en az bir True varsa True döner.

Burada her fonksiyon için True/False dönen bir generator var.

Yani any(f(s) for f in [...]) ----> bu şekilde her kontrol için tek tek uygulayıp sonucu True/False döndürür.

(unpacking operator)

"*" listenin veya tuple’ın elemanlarını ayrı argümanlar olarak print fonksiyonuna veriyor.

Örneğin:

results = [True, True, True, True, True]
print(*results, sep='\n')


Bu, şunu yapar:

True
True
True
True
True

sep='\n'

print’te sep argümanı, birden fazla argümanı yazarken aralarına konacak karakteri belirler.

sep='\n' -> her sonucu yeni satıra yazdırır.

 Özet Akış

---- Listeyi oluştur -> içinde fonksiyonlar var [isalnum, isalpha, ...]

---- Her fonksiyonu string üzerinde çalıştır -> f(s)

---- any() ile en az bir karakter eşleşiyor mu kontrol et -> True/False

---- * ile sonuçları print’e gönder

---- sep='\n' ile her satırı ayrı yazdır


"""