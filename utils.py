# Author : Hichem MAIZA 
# License : Feel free to use and/or modify the code

# import system librairies 
import os, sys

# import 3rd party librairies
import cv2
import numpy as np

def show_window(image, name = 'TestWindow', shape = (128,128)):

    """ function so we can confiugre our image window, so that's easy fo us even when we forget synatx 

    Args: 
    name -- the window name 
    shape -- the size of the window in pixel points

    returns:
    """

    cv2.namedWindow(name, cv2.WINDOW_NORMAL)
    cv2.resizeWindow(name, shape)
    cv2.imshow(name, image) 

def initialize_parameters(camera_index = 0 , seconds = 2):

        """ function to initialize parameters -- called at the beginning of the main code function 
        args 
        camera_index -- id of the opened video capturing device, usually equal to zero when using webcam 
        seconds  -- to choose number of frames per second to save

        returns 
        parameters -- a dictionary of parameters contains cam_object, frame_per_second, threshold
        """

        cam_object = cv2.VideoCapture(camera_index)
        frame_per_second = cam_object.get(cv2.CAP_PROP_FPS) 
        threshold = frame_per_second * seconds
         
        parameters = {
            'cam_object': cam_object,
            'frame_per_second': frame_per_second, 
            'threshold': threshold
        }

        return parameters
        
def write_to_folder(classId, numImage, image, shape = (64,64), folder_path = 'images'): 
    
    """ function to write images to a specific folder 
    
    args:
    classId -- class number, integer from 0-5 
    numImage -- image number 
    """
    if numImage == 10:
        numImage = 0
        classId +=1
    cv2.imwrite(folder_path + "/frame_{}_{}.jpg".format(classId, numImage), cv2.resize(image,shape))
    numImage+=1 

    parameters = {
        'classId' : classId, 
        'numImage': numImage
    }

    return parameters 

def save_images_to_array(list_folders = ['images-hichem', 'images-sami'], save_npy = False):

    """ list of folders -- every folder has some images which belongs to a specific person

    args 
    list_folders -- list of folders which contains images it has a default value 
    of ['images-hichem', 'images-sami'] which represent my folders 
    you have to change it so it fits your naming policy. 

    returns 
    parameters -- a dictionnary of parameters 
    parameters['X'] -- a numpy array of shape [n_example,64,64,3] 
    parameters['X'] -- a numpy array of shape [n_example,]

    """

    Y = []
    X = []

    for folder in list_folders:

        list_files = os.listdir(folder)
        for f in list_files:
            image = cv2.imread(os.path.join(folder,f))
            Y.append(f[6])
            X.append(image)

    if save_npy == True:

        np.save('X', X)
        np.save('Y', Y)

    parameters = {

        'X': np.array(X),
        'Y': np.array(Y) 
    }
    
    return parameters