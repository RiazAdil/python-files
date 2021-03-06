import speech_recognition as sr  

# get audio from the microphone                                                                       
r = sr.Recognizer()                                                                                   
with sr.Microphone() as source:
	r.adjust_for_ambient_noise(source,duration=5)
	r.dynamic_energy_threshold=True 
	print("Speak:")
	audio = r.listen(source)
	try:
		print("You said " + r.recognize_google(audio))
	except sr.UnknownValueError:
		print("Could not understand audio")
	except sr.RequestError as e:
		print("Could not request results; {0}".format(e))