set ROS_MASTER_URI=http://192.168.0.157:11311
set ROS_HOSTNAME=192.168.0.150
set PYTHONPATH=%PYTHONPATH%;roslib

start python ros_google_speech/scripts/grammar_lang_understanding.py
python ros_google_speech/scripts/google_speech.py