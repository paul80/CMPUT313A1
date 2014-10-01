import time
import random
import start
import blockreciever
import statsandprint
import sys

def organizercontroll(A,K,F,e,R, seed):

    #global blockfail - not needed
    #ADD SEED LATER
    
    sizeofpacket = int(F)
    numberofblock = int(K)
    biterrorprobability = float(e)
    correct_frames=0
    
    #-----------------------------------Old stuff_------------------------------
    #the bit time is converted into seconds
    #instadelay = int(A*(10**(-7)))
    
    #---------------------------------------------------------------------------
    
    #New stuff------------------------------------------------------------------
    
    time_receive=0        #Time to receive correct frame
    correct_frame_times=[] #array that holds times to correctly receive frames
    

    framecounter = 0
    successful_block_count = 0
    
    total_frames=0  #includes retransmissions/failed frames
    correct_frames=0
    startinstancetime = time.time()

    #here we separate the frame into K blocks
    #if one of the blocks fails re-transmit the whole frame
    
    count=R%F
    #frames is number of times to go through for loop R/F, amount of frames to send
    frames=R//F
    
    #print(R,F,frames)
    if (count!=0):
        frames+=1
    #print(frames)
    for i in range(frames):
        #blockfail checks if any of the blocks failed
        blockfail = 0
        #iterate through all of the blocks of a frame
        for instanceblock in range(0,numberofblock):
            if(K == 0):
                #successfully_send = blockreciever.recieve_send_detect(F, biterrorprobability, instadelay, R, 0)
                successfully_send = blockreciever.recieve_send_detect(F, biterrorprobability, R, 0, seed)
                
                framecounter = framecounter + 1
                if (succesfully_send == 1):
                    successful_block_count = successful_block_count + 1
                else:
                    #if any of the block fails the whole frame is resent so blockfail is set to 1
                    blockfail = 1
            else:
                #print(framesentfailed)
                #successfully_send = blockreciever.recieve_send_detect((F/K), biterrorprobability,instadelay,R,1)
                
                successfully_send = blockreciever.recieve_send_detect((F/K), biterrorprobability,R,1, seed)
                
                framecounter = framecounter + 1
                #print("successfullysend"+str(successfullysend)) == 0
                if(successfully_send != 0):
                    successful_block_count = successful_block_count + 1
                else:
                    #if any of the block fails the whole frame is resent                    
                    blockfail = 1
                    
        total_frames+=1
        if (blockfail == 0):
            #if all of the blocks are succefully sent exit the while loop and increment total frames by 1
            correct_frames+=1
            #If the frame is correctly received, add the time it took for a correct frame to correct_frame_times
            #and reset receiving time to 0
            correct_frame_times.append(time_receive)
            time_receive=0
            
        if (blockfail==1):
            time_receive+=500      #Increment the time to receive a correct frame

    #ok we have an instance of a test
    #we start returning values
    
    #Old stuff here----------------------------------------------------------------
    
    #endinstancetime= time.time()
    #theinstancetime = endinstancetime - startinstancetime
    
    #End here------------------------------------------------------------------------
    
    theinstancetime=sum(correct_frame_times)
    if (K==0):
        K=1
        
    if (theinstancetime == 0):
        theinstancetime =1
    thoroughputinstance = (F*correct_frames)/(theinstancetime)
    print(thoroughputinstance)
   # print(frames)
   
    #print(correct_frames, frames, correct_frames/frames)
    #return total_frames, correct_frames/frames, thoroughputinstance,R
    return total_frames,correct_frames,thoroughputinstance,R

                    
