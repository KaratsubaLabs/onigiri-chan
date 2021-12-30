import speech_recognition as sr

keywords = None

if __name__ == '__main__':
    r = sr.Recognizer()

    raw = sr.AudioFile('test.wav')
    with raw as source:
        r.adjust_for_ambient_noise(source)
        audio = r.record(source)
        print(r.recognize_sphinx(audio, keyword_entries=keywords))

