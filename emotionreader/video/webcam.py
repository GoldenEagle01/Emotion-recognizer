import pickle
import cv2
import numpy as np
from frames import FrameHandler
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import plotly.plotly as py
from live_plot import plot
from live_plot import init

def record(filename, seconds, **kwargs):
   
    cap = cv2.VideoCapture(0)
    
    fourcc = kwargs.get('fourcc', ('X', 'V', 'I', 'D'))
    frame_size = kwargs.get('size', (640, 480))
    fps = kwargs.get('fps', 20)
    codec = cv2.cv.CV_FOURCC(*fourcc)
    
    cap.set(cv2.cv.CV_CAP_PROP_FPS, fps)
    out = cv2.VideoWriter(filename, codec, fps, frame_size)
    
    total_frames = int(fps * seconds)
    frame_count = 0
    while (cap.isOpened() and frame_count < total_frames):
        ret, frame = cap.read()
        if ret:
            out.write(frame)
            frame_count += 1
        else:
            break

    return frame_count


def get_webcam_video(width, height):
    vc = cv2.VideoCapture(0)
    vc.set(3, width)
    vc.set(4, height)
    
    while True:
        ret, frame = vc.read()
        
        if not ret:
            return
        
        yield frame


def predict_from_webcam(args):
    #init plot
    init()
    
    emotions = ['anger', 'disgust','happy', 'neutral', 'sadness', 'surprise']
    
    with open('models/trained_svm_model') as f:
         model = pickle.load(f)

    width, height = args.dimensions
    for frame in get_webcam_video(width, height):
        handler = FrameHandler(frame)
        array_data = np.array([])
        prediction_data = 0

        if args.landmarks:
            handler.draw_landmarks()
        
        faces = np.array([handler.get_vectorized_landmarks()])
        if faces[0] is not None:
            prediction = model.predict(faces)
            if len(prediction) > 0:
                text = emotions[prediction[0]]
                prediction_data = prediction[0]
                cv2.putText(handler.frame, text, (60, 60),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255),
                            thickness=2)
                array = model.predict_proba(faces)
                array_data = np.array(array[0])
        else:
            prediction_data = 6

        #plot data
        if array_data is not None:
            plot(array_data, prediction_data)

        cv2.imshow('image', handler.frame)
        cv2.moveWindow('image', 800, 30);

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
