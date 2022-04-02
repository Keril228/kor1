from mcpi.minecraft import Minecraft
mc = Minecraft.create("217.182.203.129",28813)
uid = mc.getPlayerEntityId("aabbcc")
pos = mc.entity.getPos(uid)
x = pos.x
y = pos.y
z = pos.z
#нос корабля
def nose(spisok,n):
    ass = 0
    for i in range(8):
        for j in range(7):
            mc.setBlock(x + i, y+n, z + j + 3, spisok[ass])
            ass += 1
def stupenki(n):
    fig=0
    for i in range(4):
        fig+=1
        for w in range(4):
            for j in range(2):
                mc.setBlock(x+i+22,y+fig+5,z+1+j+n,164)
plate = 126,5
d_o=0
stup = 164,4
dub = 17
decor_1=     [0,0,0,0,0,0,plate,0,0,0,0,0,0, #14 по x 13 по y
             0,0,0,0,0,0,0,0,0,0,0,0,0,
             0,0,0,0,0,0,0,0,0,0,0,0,0,
             0,0,0,0,0,188,0,188,0,0,0,0,0,
             0,0,0,0,0,188,d_o,188,0,0,0,0,0,
             0,0,0,0,188,dub,d_o,dub,188,0,0,0,0,
             0,0,0,188,188,d_o,d_o,0,188,188,0,0,0,
             0,0,0,188,d_o,d_o,d_o,0,d_o,188,0,0,0,
             0,0,188,188,dub,d_o,d_o,d_o,0,188,188,0,0,
             0,0,188,d_o,d_o,d_o,d_o,d_o,d_o,d_o,188,0,0,
             0,0,188,dub,d_o,d_o,d_o,d_o,d_o,dub,188,0,0,
             0,188,d_o,d_o,d_o,d_o,d_o,d_o,d_o,d_o,d_o,188,0,
             188,0,d_o,d_o,d_o,d_o,d_o,d_o,d_o,d_o,d_o,dub,0,
             188,d_o,d_o,d_o,d_o,d_o,d_o,d_o,d_o,d_o,d_o,d_o,188]


d_o=5,5


osnovanie = [0,0,0,0,0,0,d_o,0,0,0,0,0,0,
             0,0,0,0,0,0,d_o,0,0,0,0,0,0,
             0,0,0,0,0,0,d_o,0,0,0,0,0,0,
             0,0,0,0,0,d_o,d_o,d_o,0,0,0,0,0,
             0,0,0,0,0,d_o,d_o,d_o,0,0,0,0,0,
             0,0,0,0,d_o,d_o,d_o,d_o,d_o,0,0,0,0,
             0,0,0,0,d_o,d_o,d_o,d_o,d_o,0,0,0,0,
             0,0,0,d_o,d_o,d_o,d_o,d_o,d_o,d_o,0,0,0,
             0,0,0,d_o,d_o,d_o,d_o,d_o,d_o,d_o,0,0,0,
             0,0,d_o,d_o,d_o,d_o,d_o,d_o,d_o,d_o,d_o,0,0,
             0,0,d_o,d_o,d_o,d_o,d_o,d_o,d_o,d_o,d_o,0,0,
             0,d_o,d_o,d_o,d_o,d_o,d_o,d_o,d_o,d_o,d_o,d_o,0,
             0,d_o,d_o,d_o,d_o,d_o,d_o,d_o,d_o,d_o,d_o,d_o,0,
             d_o,d_o,d_o,d_o,d_o,d_o,d_o,d_o,d_o,d_o,d_o,d_o,d_o,
             d_o,d_o,d_o,d_o,d_o,d_o,d_o,d_o,d_o,d_o,d_o,d_o,d_o,
             d_o,d_o,d_o,d_o,d_o,d_o,d_o,d_o,d_o,d_o,d_o,d_o,d_o,
             d_o,d_o,d_o,d_o,d_o,d_o,d_o,d_o,d_o,d_o,d_o,d_o,d_o,
             d_o,d_o,d_o,d_o,d_o,d_o,d_o,d_o,d_o,d_o,d_o,d_o,d_o,
             d_o,d_o,d_o,d_o,d_o,d_o,d_o,d_o,d_o,d_o,d_o,d_o,d_o,
             d_o,d_o,d_o,d_o,d_o,d_o,d_o,d_o,d_o,d_o,d_o,d_o,d_o,
             d_o,d_o,d_o,d_o,d_o,d_o,d_o,d_o,d_o,d_o,d_o,d_o,d_o,
             d_o,d_o,d_o,d_o,d_o,d_o,d_o,d_o,d_o,d_o,d_o,d_o,d_o,
             d_o,d_o,d_o,d_o,d_o,d_o,d_o,d_o,d_o,d_o,d_o,d_o,d_o,
             d_o,d_o,d_o,d_o,d_o,d_o,d_o,d_o,d_o,d_o,d_o,d_o,d_o,
             d_o,d_o,d_o,d_o,d_o,d_o,d_o,d_o,d_o,d_o,d_o,d_o,d_o,
             d_o,d_o,d_o,d_o,d_o,d_o,d_o,d_o,d_o,d_o,d_o,d_o,d_o,
             d_o,d_o,d_o,d_o,d_o,d_o,d_o,d_o,d_o,d_o,d_o,d_o,d_o,
             0,d_o,d_o,d_o,d_o,d_o,d_o,d_o,d_o,d_o,d_o,d_o,0,
             0,0,0,d_o,d_o,d_o,d_o,d_o,d_o,d_o,0,0,0]
for wewe in range(6):
    count = 0
    for i in range(29):
        for j in range(13):
            mc.setBlock(x+i,y+wewe,z+j,osnovanie[count])
            count+=1
count = 0
for i in range(14):
    for j in range(13):
        mc.setBlock(x + i+1, y + 6, z + j,decor_1[count])
        count += 1

count = 0



nos_1 =[0,0,0,stup,0,0,0,
       0,0,0,d_o,0,0,0,
       0,0,0,d_o,0,0,0,
       0,0,0,d_o,0,0,0,
       0,0,d_o,d_o,d_o,0,0,
       0,0,d_o,d_o,d_o,0,0,
       0,d_o,d_o,d_o,d_o,d_o,0,
       d_o,d_o,d_o,d_o,d_o,d_o,d_o]
nos_2 = [0,0,0,0,0,0,0,
         0,0,0,0,0,0,0,
         0,0,0,0,0,0,0,
         0,0,0,stup,0,0,0,
         0,0,d_o,d_o,d_o,0,0,
         0,0,d_o,d_o,d_o,0,0,
         0,d_o,d_o,d_o,d_o,d_o,0,
         d_o,d_o,d_o,d_o,d_o,d_o,d_o]
nos_3 = [0,0,0,0,0,0,0,
         0,0,0,0,0,0,0,
         0,0,0,0,0,0,0,
         0,0,0,0,0,0,0,
         0,0,stup,stup,stup,0,0,
         0,0,d_o,d_o,d_o,0,0,
         0,d_o,d_o,d_o,d_o,d_o,0,
         d_o,d_o,d_o,d_o,d_o,d_o,d_o]
nos_4= [0,0,0,0,0,0,0,
        0,0,0,0,0,0,0,
        0,0,0,0,0,0,0,
        0,0,0,0,0,0,0,
        0,0,0,0,0,0,0,
        0,0,stup,stup,stup,0,0,
        0,d_o,d_o,d_o,d_o,d_o,0,
        d_o,d_o,d_o,d_o,d_o,d_o,d_o]
nos_5= [0,0,0,0,0,0,0,
        0,0,0,0,0,0,0,
        0,0,0,0,0,0,0,
        0,0,0,0,0,0,0,
        0,0,0,0,0,0,0,
        0,0,0,0,0,0,0,
        0,stup,stup,stup,stup,stup,0,
        d_o,d_o,d_o,d_o,d_o,d_o,d_o]
nos_6=[0,0,0,0,0,0,0,
        0,0,0,0,0,0,0,
        0,0,0,0,0,0,0,
        0,0,0,0,0,0,0,
        0,0,0,0,0,0,0,
        0,0,0,0,0,0,0,
        0,0,0,0,0,0,0,
        stup,stup,stup,stup,stup,stup,stup]

#низ корабля 11
for i in range(4):
    mc.setBlocks(x + 13 + i, y - 1 - i, z + i, x + 25 - i, y - i-1, z - i + 11,d_o)
#нос корабля
nose(nos_1,5)
nose(nos_2,4)
nose(nos_3,3)
nose(nos_4,2)
nose(nos_5,1)
nose(nos_6,0)
for i in range(3):
    mc.setBlock(x+i-1,y+6,z+6,plate)

#основание палубы
mc.setBlocks(x+22,y+6,z+3,x+29,y+9,z+9,d_o)
stupenki(0)
stupenki(9)
mc.setBlocks(x+22,y+6,z,x+26,y+9,z,d_o)
mc.setBlocks(x+22,y+6,z+12,x+26,y+9,z+12,d_o)
mc.setBlocks(x+27,y+6,z+1,x+27,y+9,z+2,d_o)
mc.setBlocks(x+27,y+6,z+10,x+27,y+9,z+11,d_o)
mc.setBlocks(x+26,y+9,z+1,x+26,y+9,z+2,d_o)
mc.setBlocks(x+26,y+9,z+10,x+26,y+9,z+11,d_o)

#забор
mc.setBlocks(x+13+1,y+6,z,x+21,y+6,z,188)
mc.setBlocks(x+13+1,y+6,z+12,x+21,y+6,z+12,188,2)
bl = 35,15
wh = 35
gr = 35,7
#Парус
parus = [bl,bl,bl,bl,bl,bl,bl,bl,bl,
         bl,bl,gr,bl,bl,bl,bl,gr,bl,
         bl,bl,gr,gr,bl,bl,gr,gr,bl,
         bl,bl,bl,wh,wh,wh,gr,bl,bl,
         bl,bl,bl,bl,wh,bl,wh,bl,bl,
         bl,bl,gr,wh,bl,wh,gr,bl,bl,
         gr,gr,bl,bl,bl,bl,bl,gr,gr,
         bl,bl,bl,bl,bl,bl,bl,bl,bl]
count=0
for s in range(8):
    for i in range(9):
        for j in range(8):
            mc.setBlock(x+13,y-s,z+j,parus[count])
            count+=1
mc.setBlocks(x+12,y+6,z+6,x+12,y+13,z+6,dub)
mc.setBlocks(x+17,y+6,z+6,x+17,y+17,z+6,dub)


