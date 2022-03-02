from platform import machine


machine1= int(0)
machine2=0


w1=[30, 50]
w2=[0, 40]
w3=[20, 70]
w4=[30, 0]
w5=[50, 20]

   

def simulator(ranges,machinea,machineb):
    for m in range(ranges):
        if(machinea==0 and machineb==0):
            print('trabajo 1 iniciado por machine a1')
            print('trabajo 2 iniciado por machine a2')
        machinea+=1
        machineb+=1
        if(machinea==30):
         print('machine a1 ah finalizado trabajo 1 a1 terminado :',w1[0],'min de ejecucion')
         print('trabajo 3 iniciado por machine a1 ')
        if(machineb==40):
         print('machine a2 ah finalizado trabajo 2 con ',w2[1],'min de ejecucion')
         print('trabajo 1 a2  iniciado por machine a2')
        if(machinea==50):
            print('machine a1 ah finalizado trabajo 3 con',w3[0],'min ejecucion')
            print('trabajo 4 iniciado por machine a1')
        if(machinea==80):
            print('machine a1 ah finalizado trabajo 4 con',w4[0],'min ejecucion')
            print('trabajo 5 iniciado por machine a1')
        if(machineb==90):
             print('machine a2 ah finalizado trabajo 1 a2 con',w1[1],'min ejecucion')
             print('trabajo 3 a2 iniciado por machine a2')
        if(machinea==130):
          print('machine a1 ah finalizado trabajo  5 con',w5[0],'min ejecucion')
          print('la mauqina a1 ah finalizado')
        if(machineb==160):
            print('machine a2 ah finalizado trabajo  3 con',w3[1],'min ejecucion')
            print('trabajo 5 a2 iniciado por machine a2')
    if(machineb==180):
     print('machine a2 ah finalizado trabajo  5 con',w5[1],'min ejecucion')
     print('el trabajo ah finalizado')

        

simulator(180,machine1,machine2)



