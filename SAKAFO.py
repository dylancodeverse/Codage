# vary = 3200
# menaka = 1500
# laoka = 7000
# fraisSyGouterVo = 5000
# fraisSyGouterMi = 5000
# vovotsavony = 400
# siramamy = 800
# cafe = 700
# ronono =3000
# gouter = 6000


# print(f"{(40000 -1*( vary +menaka+laoka+fraisSyGouterVo+fraisSyGouterMi+vovotsavony+siramamy+cafe+ronono+gouter))*30:,}"+" AR")
# resteParMois = (40000 -1*( vary +menaka+laoka+fraisSyGouterVo+fraisSyGouterMi+vovotsavony+siramamy+cafe+ronono+gouter))*30
# print(f"{resteParMois*5 - 500000:,} fmg")


language = ['0', '10', '110', '111']


summ = 0
for element in language:
    summ+=2**-len(element)
if summ <=1:
    print( 1)
else:    
    print(0)