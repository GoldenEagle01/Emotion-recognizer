import glob
import random
import pickle
from sklearn.svm import LinearSVC
from sklearn.calibration import CalibratedClassifierCV
from sklearn import datasets
import numpy as np
from sklearn.svm import SVC

from emotionreader.video import ImageHandler


emotions = ['anger', 'disgust','happy', 'neutral', 'sadness', 'surprise']

def get_files(emotion):
    files = glob.glob('data/%s/*.jpg' % emotion)
    #files += glob.glob('data/googleset/%s/*' % emotion)
    random.shuffle(files)
    training = files[:int(len(files) * 0.8)]
    prediction = files[-int(len(files) * 0.2):]
    return training, prediction


def _handle_subset(emotion, emotion_index, files, data, labels):
    for item in files:
        handler = ImageHandler(item)
        # We know the dataset has 1 face in the correct size,
        # so no resizing is necessary
        landmarks = handler.get_vectorized_landmarks(resized=False)
        if not landmarks:
            continue
        data.append(landmarks)
        labels.append(emotion_index)


def make_sets():
    training_data = []
    training_labels = []
    prediction_data = []
    prediction_labels = []

    for index, emotion in enumerate(emotions):
        print('working on %s' % emotion)
        training, prediction = get_files(emotion)
        _handle_subset(emotion, index, training,
                       training_data, training_labels)
        _handle_subset(emotion, index, prediction,
                       prediction_data, prediction_labels)

    return training_data, training_labels, prediction_data, prediction_labels


def make_model():
    #model = SVC(kernel='linear', probability=True)
    model = LinearSVC()
    (training_data, training_labels,
     prediction_data, prediction_labels) = make_sets()
    model = CalibratedClassifierCV(model,method='sigmoid',cv=3)
    npar_train = np.array(training_data)
    model.fit(npar_train, training_labels)
    print ('Linear accuracy: ', model.score(np.array(prediction_data), prediction_labels))
    return model


def measure_accuracy():
    #clf = SVC(kernel='linear', probability=True)
    clf = LinearSVC()
    accur_lin = []
    for i in range(0, 10):
        print('Making sets %s' % i)
        (training_data, training_labels,
         prediction_data, prediction_labels) = make_sets()

        npar_train = np.array(training_data)
        print('training SVM linear %s' % i)
        clf = CalibratedClassifierCV(clf,method='sigmoid',cv=3)
        clf.fit(npar_train, training_labels)
        print('getting accurary')
        npar_pred = np.array(prediction_data)
        pred_lin = clf.score(npar_pred, prediction_labels)
        print('linear: ', pred_lin)
        accur_lin.append(pred_lin)

    print('mean value lin svm: %s' % np.mean(accur_lin))


def save_trained_model():
    model = make_model()
    print "save trainer"
    with open('models/trained_svm_model', 'wb') as f:
        pickle.dump(model, f)


def train_model(args):
    if args.measure:
        measure_accuracy()
    else:
        save_trained_model()
