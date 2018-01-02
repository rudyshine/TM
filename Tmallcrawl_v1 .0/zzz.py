import random

sumpage="23"
n =6
if int(sumpage) >= n:
    m = int(sumpage) // n
    print("m",m)
    ran_num = range(int(sumpage))
    print("ran_num:",ran_num)
    print(type(ran_num))
    for i in range(m):
        print("i:",i)
        s = set(ran_num)
        print("s:",s)
        ran1 = range(n)
        print("ran1:",ran1)
        s1 = set(ran1)
        print("s1:",s1)
        s2 = s - s1
        print("s2:",s2)
        ran_num = list(s2)
        print("ran_num:",ran_num)
    ran_num = range(len(ran_num))
    # crawlpage(ran_num, url1, proxies)
else:
    # ip_list = get_ip_list(url_ip, headers_ip=headers_ip)
    # proxies = get_random_ip(ip_list)
    # print("proxies:", proxies)
    ran_num0 = range(0, int(sumpage), int(sumpage))
    print("ran_num0:",ran_num0)
