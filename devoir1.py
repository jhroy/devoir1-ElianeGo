# coding: utf-8


url = "https://montrealcampus.ca?p="

print(url[url.rfind("=")+1:])

liste = list(range(20000,30151))

n = 0
for num in range(20000,30151):
    num1=str(num)
    url1=url+num1
    n += 1
    print(n, url1)
    
print(len(liste))

liste = list 
print(liste)
