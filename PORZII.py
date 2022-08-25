
print("Formula de ejemplo :> 11-22-43-13-")
form = input("insertar Formula: ")
t=0
x=0
y=0
while x < len(form):
    if y < 2:y+=1
    else:
        t+=int(form[x-2])*int(form[x-1])
        y=0
    x+=1
marca=""
x=0
while x < t/2:
    marca+="."
    x+=1
print("<",t,">")
print("                    <|"+marca+"|>")
par2 = input("insertar parametro 2: ")
par1 = input("insertar parametro 1: ")

resultado=""

x=0
y=0
s=False
z1=0
z2=0
while x < len(form):
    if y < 2:y+=1
    else:
        z=0
        while z < int(form[x-2]):
            if s==False:
                P=z1
                while z1 < int(form[x-1])+P:
                    if len(par1) > z1:
                        resultado+=str(par1[z1])
                    else:
                        while z2 < len(par2):
                            resultado+=str(par2[z2])
                            z2+=1
                    z1+=1
                print("#")
                s=True
            else:
                P=z2
                while z2 < int(form[x-1])+P:
                    if len(par2) > z2:
                        resultado+=str(par2[z2])
                    else:
                        while z1 < len(par1):
                            resultado+=str(par1[z1])
                            z1+=1
                    z2+=1
                print("%")
                s=False
                print("[",x,"]",form[x], s, " >> ", resultado)
            z+=1
        y=0
        print("[",x,"]",form[x], s, " >> ", resultado)
    x+=1


print(">>>>>> ",resultado)
