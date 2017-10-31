import sys
import cv2
import glob

def progress(count, total, status=''):
    bar_len = 100
    filled_len = int(round(bar_len * count / float(total)))
    
    percents = round(100.0 * count / float(total), 1)
    bar = '=' * filled_len + '-' * (bar_len - filled_len)
    
    sys.stdout.write('%s   [%s]%s %s\r' % (status, bar, percents, '%'))
    sys.stdout.flush()

def detect_faces(emotion, face_detectors):
    i = 0
    print('\nworking on %s' % emotion)
    files = glob.glob("data/sorted_set/%s/*.jpg" % emotion)
    files += glob.glob("data/sorted_set/%s/*/*.jpg" % emotion)
    total = len(files)
    print('%s has %d files' % (emotion, total))

    for num, f in enumerate(files):
        frame = cv2.imread(f)
        if frame is not None: gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Try to detect a face, using 4 different face detectors.
        faces = [det.detectMultiScale(
                 gray, scaleFactor=1.1, minNeighbors=10, minSize=(5, 5),
                 flags=cv2.CASCADE_SCALE_IMAGE)
                 for det in face_detectors]

        # Go over detected faces, stop at the first one.
        facefeatures = next((f for f in faces if len(f) == 1), None)
        if facefeatures is None:
            continue

        # Cut and save face
        for (x, y, w, h) in facefeatures:
            i = i + 1
            progress (i,total,status=' Loading')
            #print("face found in file: %s" % f)
            gray = gray[y:y+h, x:x+w]  # Cut the frame to size

            try:
                out = cv2.resize(gray, (350, 350))
                cv2.imwrite("data/%s/%s.jpg" % (emotion, num), out)
            except Exception as e:
                print('error occured: ', e)


def prepare_dataset(args):
    emotions = ["anger", "disgust",
                "fear", "happy", "neutral", "sadness", "surprise"]
    face_detectors = [
        cv2.CascadeClassifier('models/haarcascade_frontalface_default.xml'),
        cv2.CascadeClassifier('models/haarcascade_frontalface_alt.xml'),
        cv2.CascadeClassifier('models/haarcascade_frontalface_alt2.xml'),
        cv2.CascadeClassifier('models/haarcascade_frontalface_alt_tree.xml')
    ]
        
    for emotion in emotions:
        detect_faces(emotion, face_detectors)
