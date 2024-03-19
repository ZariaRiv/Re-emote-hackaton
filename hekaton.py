from naoqi import ALProxy
import argparse
import qi
import sys
import time

ROBOT_IP="169.254.81.197"  # change to correct IP

tts = ALProxy("ALTextToSpeech", ROBOT_IP, 9559)
gesture = ALProxy("ALAnimatedSpeech", ROBOT_IP, 9559)
navigationProxy = ALProxy("ALNavigation", ROBOT_IP, 9559)
motionProxy     = ALProxy("ALMotion", ROBOT_IP, 9559)
postureProxy    = ALProxy("ALRobotPosture", ROBOT_IP, 9559)
animationProxy = ALProxy("ALAnimationPlayer", ROBOT_IP, 9559)
ledProxy = ALProxy("ALLeds", ROBOT_IP, 9559)

#tts.say("UwU")
#animationProxy.run("animations/Stand/Gestures/Enthusiastic_4")
#gesture.post.say(" ^mode(disabled) ^start({}/behavior_1) \\rspd=50\\ \\emph=1\\ {} \\pau=500\\ \\rspd=80\\ means \\emph=1\\ {} ^mode(disabled)\\pau=10000\\".format(gesture,message1,message2))
#gesture.post.say(" ^mode(disabled) ^start({}/behavior_1) \\rspd=50\\ \\emph=1\\ {} \\pau=500\\".format(gesture,'I hope this works'))

value=0

names1=["LeftFaceLedsGreen","RightFaceLedsGreen"]
names2=["LeftFaceLedsBlue","RightFaceLedsBlue"]
names3=["LeftFaceLedsRed","RightFaceLedsRed"]
ledProxy.createGroup("MyGroup1",names1)
ledProxy.createGroup("MyGroup2",names2)
ledProxy.createGroup("MyGroup3",names3)

#animationProxy.run("animations/Stand/Gestures/Enthusiastic_4")

def bored():
	ledProxy.setIntensity("MyGroup1",0)
	ledProxy.setIntensity("MyGroup2",1)
	ledProxy.setIntensity("MyGroup3",0)
	#animationProxy.run("animations/Stand/Gestures/BodyTalk_7")
	tts.setParameter('pitchShift', 1)
	tts.setParameter("speed", 50)
	tts.say("nao booored")
	#gesture.post.say(" ^mode(disabled) ^start({}/behavior_1) \\rspd=50\\ \\emph=1\\ {} \\pau=500\\".format(gesture,'nao saaaad'))
	postureProxy.goToPosture("Crouch", 0.5)

def happy():
	#tts.setParameter('pitchShift',1.w1)
	#tts.say("UwU")
	ledProxy.setIntensity("MyGroup1",0.3)
	ledProxy.setIntensity("MyGroup2",1)
	ledProxy.setIntensity("MyGroup3",1)
	tts.setParameter('pitchShift', 1.3)
	tts.setParameter("speed", 70)
	tts.say("Hurrah!")
	#gesture.post.say(" ^mode(disabled) ^start({}/behavior_1) \\rspd=50\\ \\emph=1\\ {} \\pau=500\\".format(gesture, 'Hurrah!'))
	postureProxy.goToPosture("StandInit", 0.5)
	animationProxy.run("animations/Stand/Gestures/Enthusiastic_5")
	#animationProxy.run("animations/Stand/Gestures/Hey_1")

def disgust():
	print('disgust')
	ledProxy.setIntensity("MyGroup1",1)
	ledProxy.setIntensity("MyGroup2",0)
	ledProxy.setIntensity("MyGroup3",0)
	tts.setParameter('pitchShift', 0.6)
	tts.setParameter("speed", 100)
	tts.say("Terrible!")
	#gesture.post.say(" ^mode(disabled) ^start({}/behavior_1) \\rspd=50\\ \\emph=1\\ {} \\pau=500\\".format(gesture, 'horrible'))
	postureProxy.goToPosture("StandInit", 3)
	animationProxy.run("animations/Stand/Gestures/No_3")
	#animationProxy.run("animations/Stand/Gestures/No_8")
	#animationProxy.run("animations/Stand/Gestures/No_9")

while value!=3:
	value=int(input('mood:'))
	print(value)
	if value==0:
		print('bored')
		bored()
	elif value==1:
		print('happy')
		happy()
	elif value==2:
		print('disgusted')
		disgust()