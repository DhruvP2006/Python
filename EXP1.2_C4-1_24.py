a ="Python programming"
print(a[a.find("i")])
print(len(a))
print(a[slice(0,6)])
print(a[slice(7,14)])
print(a[slice(2,4)]+a[slice(15,18)])
print(a.upper())
b= "is interesting."
print(a,b, sep=" ")
#Table Methods
b = a.replace("programming", "language")
print(b)
print(a.count("m"))
print(a.startswith("P"))
print(a.endswith("n"))
print(a.swapcase())
print(a.rstrip("ming"))
print(a.islower())
print(a.zfill(10))
b = "Python Prgramming {0} {1}".format("is", "fun")
print(b)
print(a.split("n"))