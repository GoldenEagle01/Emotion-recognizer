import glob
from shutil import copyfile


emotions = ["neutral", "anger", "fear", "disgust"
            "happy", "sadness", "surprise"]


def sorted_glob(pattern):
    return sorted(glob.glob(pattern))


def handle_file(filepath, session):
    with open(filepath, 'r') as f:
        emotion = int(float(f.readline()))
        session_files = sorted_glob('data/source_images/%s/*' % session)
        src_emotion = session_files[-1]
        src_neutral = session_files[0]
        dest_emotion = 'data/sorted_set/%s/%s' % (
            emotions[emotion], src_emotion[29:])
        dest_neutral = 'data/sorted_set/neutral/%s' % src_neutral[29:]
        copyfile(src_neutral, dest_neutral)
        copyfile(src_emotion, dest_emotion)


def sort_ck(args):
    # Returns a list of all folders with participant numbers
    participants = sorted_glob('data/source_emotions/*')

    for x in participants:
        ls_sessions = sorted_glob('%s/*' % x)
        for sessions in ls_sessions:
            ls_files = sorted_glob('%s/*' % sessions)
            for files in ls_files:
                current_session = files[21:-30]
                handle_file(files, current_session)
