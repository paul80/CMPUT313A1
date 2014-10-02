import sys
import argparse
import blockreciever
import control
import statsandprint
import startatrial

#start program here

def main():
    #prints what we want from the user
    print ("enter A K e R t respectively without commas separated by spaces +\n")
    print("A is feedback time in bit times")
    print("K is blocks\n")
    print("F is size of frame and K must be divisible by it\n")
    print("e is error in float \n")
    print("R is length of simulations +\n")
    print("t is trials +\n")
    print("any wrong input will ask you to reenter the inputs")
    
    y = 0
    x = 0
    while( y ==0):
        command_arguments=[]
        
        while (x ==0):            
            #parser = argparse.ArgumentParser()
            #parser.add_argument("start", nargs = 6 )

            if ((len(sys.argv)>=7)and(int(sys.argv[2])==0)):
                for arg in sys.argv:
                    command_arguments.append(arg)
                print(command_arguments)   
                print('is this correct? ')
                user_input= int(input("enter 1 for true and 0 to re- enter new input: "))
                if (user_input==1):
                    x=1 
                else:
                    continue
                
            elif ((len(sys.argv)>=7)and((int(sys.argv[3])%(int(sys.argv[2])))==0)):
                #print(str(sys.argv[1]) +str(sys.argv[2])+str(sys.argv[3]) +str(sys.argv[4]) +str(sys.arg[5]) +str(sys.arg[6])
                #Print out the command line arguments to console in a list
                #command_arguments=str(sys.argv).strip
                
                #command_arguments=[]
                #use the for loop because just using str(sys.argv) is trippy 
                for arg in sys.argv:
                    command_arguments.append(arg)
                print(command_arguments)
                #print(command_arguments[0])
                print('is this correct? ')
                user_input= int(input("enter 1 for true and 0 to re- enter new input: "))
                
                #parser1 = argparse.ArgumentParser() 
                #parser1.add_argument('start',  type=int,  nargs=1 )
                #if(int(sys.argv[1]))==1:
                #exits while loop that asks for user input
                if (user_input==1):
                    x=1
                else:
                #stays in while loop that asks for user input
                    continue
                      
            else:
                #stays in while loop that asks for user input
                print("your arguments does not match our criteria please try again \n")
                y=1
                x=1
                #break

        #inside a while loop that starts a sample with 5 tests
        #these containers are for information regarding the output needed
        frame_counter_container=[]
        successful_frame_container = []
        thoroughput_container=[]
        seed_instance_container=[]
            
        #x = int(sys.argv[6])
        #this is a sample iterating through instances of tests
        for testinstance in range(0, int(sys.argv[6])):
            seed = int(sys.argv[6+testinstance+1])
            #seed=testinstance
            #framecounter, succesfulframecount, thoroughputinstance, seed = startatrial.instancetrial(sys.argv, seed)
            frame_counter, successful_frame_count, thoroughput_instance, seed = startatrial.instancetrial(sys.argv, seed)
            
            
            
            #adds information to the containers
            #framecountercontainer.append(framecounter)
            #succesfulframecontainer.append(succesfulframecount)
            #throughputcontainer.append(thoroughputinstance)
            #seedinstancecontainer.append(seed)
            
            frame_counter_container.append(frame_counter)
            successful_frame_container.append(successful_frame_count)
            thoroughput_container.append(thoroughput_instance)
            seed_instance_container.append(seed)

        #prints stats needed
        #statsandprint.getandprintstats(frameinstancecontainer, thoroughputcontainer, seedinstancecontainer, sys.argv)
        statsandprint.getandprintstats(frame_counter_container,successful_frame_container, thoroughput_container, seed_instance_container, sys.argv[1:])
        
        print('\n would you like to do a new test? \n')
        print('enter 0 for no and 1 for yes')
        #to string
        if(int(sys.argv[1]))==1:
            y = 0
        else:
            y = 1

        #youve indented these lines above
        #call divider here
        #start time here
        #convert bit time to seconds


if __name__ == "__main__":
    main()