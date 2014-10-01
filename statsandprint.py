
import math
import start
import blockreciever
import control
import sys 
def standard_dev(lists):
    
    if len(lists) == 0:
        return 0
    
    x = len(lists)
    if(x == 0):
        x = 1
    avg = float(sum(lists))/x
    #print(avg)
    dev = []
    for x in lists:
        dev.append(x - avg)
        #print(dev)
    sqr = []
    
    for x in dev:
        sqr.append(x * x)
        
    #print(sqr)
    mean = sum(sqr)/len(sqr)
    #print(mean)
    standard_deviation = math.sqrt(sum(sqr)/(len(sqr)-1))    
    return standard_deviation

#array_of_frames is total number of frames
#array of thoroughput is self explanatory
#array of seeds is ?
#array of input is just command line arguments
def getandprintstats(array_of_frames,array_of_correct,array_of_thoroughput, array_of_seeds, array_of_input ):

    T = 5
    #Thoroughputstddev is probably correct
    
    #Framestddev = standard_dev(array_of_frames)
    #Framestddev = numpy.std(arrayofframes)
    
    avg_frame_transmission=[]
    
    for i in range(0,len(array_of_frames)):
        if(array_of_correct[i]!=0):  #Since the array_of_correct can have 0 values- avoid division by zero error
            temp=array_of_frames[i]//array_of_correct[i]
            avg_frame_transmission.append(temp)
        else:
            continue
    
    Framestddev=standard_dev(avg_frame_transmission)
    Thoroughputstddev = standard_dev(array_of_thoroughput)
    #Thoroughputstddev = numpy.stdev(arrayofthoroughput)   
    
    #standard deviation
    #standard deviation end
    
    
    #Framesum=0
    #for numofframes in (array_of_frames):
        #Framesum = Framesum+numofframes
    
    Frame_total=sum(array_of_frames)
    Frame_correct=sum(array_of_correct)
    if (Frame_correct==0):
        Frame_correct=1
    Frameavg = Frame_total/Frame_correct    
    Frameavg = Frame_total/Frame_correct

    Thoroughputsum = 0
    for athoroughput in (array_of_thoroughput):
        Thoroughputsum = Thoroughputsum + athoroughput
    
    Thoroughputavg = Thoroughputsum/(len(array_of_thoroughput))

    Framec1 = float((Frameavg)-(2.776*(Framestddev/(math.sqrt(T)))))
    Framec2 = float((Frameavg)+(2.776*(Framestddev/(math.sqrt(T)))))

    Thoroughc1 = float((Thoroughputavg)-(2.776*(Thoroughputstddev/(math.sqrt(T)))))
    Thoroughc2 = float((Thoroughputavg)+(2.776*(Thoroughputstddev/(math.sqrt(T)))))
    
    #Thoroughc1 = float((Thoroughputavg)+(2.776*(Framestddev/(math.sqrt(len(T))))))
    #Thoroughc2 = (Thoroughputavg) + (2.776(float(Thoroughputstddev)/(math.sqrt(len(T)))))
  # Framestdev =  statistics.stdev(arrayofframes)

   #Throughputstdev =  statistics.stddev(arrayofthroughput)
    #print(array_of_input)
    
    contain = ""
    for x in array_of_input:
        contain = contain + x + " "
    print(contain)
    print("Frame std deviation: ",Framestddev)
    print("Thoroughput std deviation: ", Thoroughputstddev)
    print("Frame stats:"+str(Frameavg)+" "+"("+ str(Framec1)+ "," + str(Framec2)+")")
    print("Thoroughput stats: "+str(Thoroughputavg)+" "+"("+ str(Thoroughc1)+ "," + str(Thoroughc2)+")")
    #sys.exit()
