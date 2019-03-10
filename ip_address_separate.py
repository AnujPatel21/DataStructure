import ipaddress

fh = open("log.txt","r")
fhh = open("ipaddress.txt","w")

for line in fh:
    for part in line.split():
        try:
            a = ipaddress.ip_network(part)
        except ValueError:
            pass # not in the right format
        else:
            fhh.write("ip_address: " + repr(a) + '\n')

fh.close()
fhh.close()
