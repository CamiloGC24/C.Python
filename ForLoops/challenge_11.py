print("Welcome to the Binary/Hexadecimal Converter App")
decimales = int(input("Compute binary and hexadecimal values up to the following decimal number:"))
start =int(input("What decimal number would you like to start at: ")) 
stop =int(input("What decimal number would you like to stop at: "))
print("Decimal values from", start , "to", N1,":")

for i in range(start ,stop +1):
    print(i)
print("Binary values from",start ,"to", stop  ,": ")
for x in range(start ,stop +1):
    print(bin(x))
    
print("Hexadecimal values from ",start ,"to", stop  ,": ")
for x in range(start ,stop +1):
    print(hex(x))


print("Press Enter to see all values from 1 to", decimales)
print("Decimal --- Binary --- Hecadecimal")
for n in range(1,decimales + 1):
    print(n,"--",bin(n),"--",hex(n))
