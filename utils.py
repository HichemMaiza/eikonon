import cv2

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
        parameters -- a dictionary of parameters 
        """

        cam_object = cv2.VideoCapture(camera_index)
        frame_per_second = cam_object.get(cv2.CAP_PROP_FPS) # Gets the frames per second
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