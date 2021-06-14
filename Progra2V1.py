import cv2
from random import randrange

notas1=[]
notas2=[]
notas3=[]

def fitness(imageName):
    #Se abre la imagen
    image = cv2.imread('Silueta3.jpg')
    image2= cv2.imread('a'+str(imageName)+'.jpg')

    ejeX=[[0,300],[0,300],[300,600]]
    ejeY=[[0,300],[300,600],[0,600]]
    for a in range(3):
        exe=5000
        aciertos=0
        for z in range(exe):
            #se generan coordenas aleatorias
            x=randrange(ejeX[0][0],ejeX[0][1])
            y=randrange(ejeY[0][0],ejeY[0][1])

            #Canales de color de la imagen
            b, g, r = image[x,y]
            b1,g1,r1= image2[x,y]

            "Implementación #1"
    ##
    ##        if(b<100 and b1<100 and g<100 and g1<100 and r<100 and r1<100):
    ##            aciertos+=2
    ##        elif((b<100 and g<100 and r<100) or (b1<100 and g1<100 and r1<100)):
    ##            aciertos+=1
    ##        else:
    ##            aciertos+=0

            "Implementación #2"

    ##        if(b<100 and b1<100):
    ##            if(g<100 and g1<100):
    ##                if(r<100 and r1<100):
    ##                    aciertos+=1
            
            "Implementación #3"

            if(b==b1 and g==g1 and r==r1):
                aciertos+=1

        if(a==0):    
            notas1.append([a,aciertos/exe*100,'a'+str(imageName)])
        elif(a==1):
            notas2.append([a,aciertos/exe*100,'a'+str(imageName)])
        else:
            notas3.append([a,aciertos/exe*100,'a'+str(imageName)])
            
        ejeX.pop(0)
        ejeY.pop(0)

    

def imprimirNotasM():
    notas1.sort(reverse=True, key=lambda x: x[1])
    print("Mitad 1: ",notas1)
    notas2.sort(reverse=True, key=lambda x: x[1])
    print("Mitad 2: ",notas2)
    notas2.sort(reverse=True, key=lambda x: x[1])
    print("Mitad 3: ",notas2)

def main():
    for i in range(0,101):
        fitness(i)
    
