import ipaddress

x = input('input an ip :')
while True:
    try:
        ip = ipaddress.ip_address(x)
        print("valid")
        break
    except:
        print("Invalid")
        break
