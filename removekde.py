import os


#kdebloat.txt contains the output of 
#apt list --installed | grep kscreen
#apt list --installed | grep kwin
#apt list --installed | grep plasma
#apt list --installed | grep kde
#lines having lockdev were removed 

f = open("kdebloat.txt","r")
#print(f)
lines = f.read()
lines = lines.split("\n")
bloats = []
for line in lines:
    line0 = line.split("/")
    bloats.append(line0[0])



for bloat in bloats:
    rembloatcmd = "sudo apt-get autoremove "+bloat+" -y"
    print(rembloatcmd)
    os.system(rembloatcmd)

