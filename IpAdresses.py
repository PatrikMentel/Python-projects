def ipsBetween(ip1, ip2):
    ip1 = ip1.split(".").reverse()
    ip2 = ip2.split(".").reverse()
    num = 0
    for i in range(3):
        if ip1[i] >= ip2[i]: num += (int(ip1[i])-int(ip2[i]))*255**i
        if ip1[i] < ip2[i]: num += (int(ip2[i])-int(ip1[i]))*255**i
    return num
print(ipsBetween("10.0.0.0", "10.0.0.50"))