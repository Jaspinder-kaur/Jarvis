import openai
import pyttsx3
import speech_recognition as sr
import time
import pyaudio

openai.api_key = "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"

engine = pyttsx3.init()

def transcribe_audio_to_text(filename):
    recognizer = sr.Recognizer()
    with sr.Audiofile(filename) as source:
        audio = recognizer.record(source)

    try:
        return recognizer.recognize.google(audio)
    except:
        print("Unknown Error!")

def generate_response(prompt):
    response = openai.Completion.create(
        engine = "text-davinci-003",
        prompt = prompt,
        max_tokens = 4000,
        n = 1,
        stop = None,
        temperature = 0.5,
    )
    return response ["Choices"] [0] ["Text"]

def spech_to_text(text):
    engine.say(text)
    engine.runAndWait()


def main():
    while True:

        print("Say 'Jarvis' to start recording your question")
        with sr.Microphone() as source:
            recognizer = sr.Recognizer()
            audio = recognizer.listen(source)
            try:
                transcription = recognizer.recognize_google(audio)
                if transcription.lower() == "jarvis":
                    filename = "input.wav"
                    print("Say your question...")
                    with sr.Microphone() as source:
                        recognizer = sr.Recognizer()
                        source.pause_threshold = 1
                        audio = recognizer.listen(source, phrase_time_limit = None, timeout = None)
                        with open(filename,"wb") as f:
                            f.write(audio.get_wav_data)

                    text = transcribe_audio_to_text(filename)
                    if text :
                        print("You said...{text}")

                        response = generate_response(text)
                        print("Jarvis :{response}")


                        spech_to_text(response)

            except Exception as e:
                print("An error occurred: {} ".format(e))
if __name__ == "__main__":
    main()
