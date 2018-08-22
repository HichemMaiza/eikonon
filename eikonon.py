# Author: Hichem MAIZA 
# License: you can use and/or modify the code :) 

import cv2
import math
import sys
from utils import *

def main() :

    """main function 
    to execute the code: 
    python eikonon <number of seconds> <path to save images> 
    
    examples 1 -- take pictures every "2 seconds" and save to "images" folder in the same directory: 
    python eikonon 2 images
    
    example 2 -- take pictures every "5 seconds" and save to "test" folder in the same directory: 
    python eikonon 5 test
    
    """

    if sys.argv[1]: 
        seconds = int(sys.argv[1]) 
    else: 
        seconds = 2

    if sys.argv[2]:
        folder_path = sys.argv[2]
    else:
        folder_path = 'images'

    parameters = initialize_parameters(camera_index = 0 , seconds = seconds)

    cam_object = parameters['cam_object']
    threshold = parameters['threshold']

    frameId = 1
    numImage = classId =  0 

    while(cam_object.isOpened()): 
        
        passed, image = cam_object.read() 
        
        if passed == True:
            
            show_window(image)
            frameId+=1
            
            if int(frameId % threshold) == 0:         
                
                parameters = write_to_folder(classId, numImage, image, folder_path = folder_path)
                numImage = parameters['numImage'] 
                classId = parameters['classId']
            
            if (cv2.waitKey(1) & 0xFF == ord('q')): 
                break 
        else:
            break 

    cam_object.release()
    cv2.destroyAllWindows()
    print("It's done ! dataset created successfully")

if __name__ == "__main__":
    main()