import time
import random
import start
import statsandprint
import control
import sys
#def recieve_send_detect(numberofbits, error, feedbacktime, seed, doparity):
def recieve_send_detect(numberofbits, error,R, doparity, Seed):


    #random.seed(Seed)
    instaerror = float(error)
    instaerrorcount = 0
    
    #Commenting out lines here-------
    
    #instadelay = int(feedbacktime)
    
    #-------------------------------
    
    numberofpacketerror = 0

    paritycounter = 0
    checkflagcounter = 1
    while((checkflagcounter == 1) and (doparity != 0)):
        #find the parity bits needed
        if(numberofbits >= 2**paritycounter):
            paritycounter=paritycounter + 1
        else:
            checkflagcounter = 0
            doparity = 0
    

    #rnd = random.Random(seed)
    '''
    for x in range(0,numberofbits+paritycountchecker):        
        p = rnd.uniform(0,1)
        #p = random.uniform(0,1)
        if p > instaerror:
            numberofpacketerror = numberofpacketerror + 1
    '''
    
    #numberofbits was interpreted as a float leading to error so converted to int
    counter=0
    while (counter<int(numberofbits)+paritycounter):        
        p = random.random()  #returns floating point number between 0 and 1
        #print(str(p))
        #p = random.uniform(0,1)
        if p < instaerror:
            numberofpacketerror = numberofpacketerror + 1  
        counter+=1
        #print(counter)
        #print(paritycounter)
    
    #sys.exit()
    '''
    for x in range(0,int(numberofbits)+paritycounter):        
        p = random.random()  #returns floating point number between 0 and 1
        #print(str(p))
        #p = random.uniform(0,1)
        if p > instaerror:
            numberofpacketerror = numberofpacketerror + 1 
    '''     
    
    #------------------------------
    
    #time.sleep(instadelay)
    
    #--------------------------------
    
    if numberofpacketerror > 1:
    #returns 0 to retransmit the whole frame when this block fails
        return 0

    else:
    #block sent successfully
        return 1


