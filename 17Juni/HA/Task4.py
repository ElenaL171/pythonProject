a1 = int(input ())
a2 = int(input ())
a3 = int(input ())
if a1!=a2 and a2!=a3 and a1!=a3: print(0)
if (a1==a2 and a2!=a3) or (a1==a3 and a2!=a3): print(2)
if a1==a2 and a2==a3: print(3)
