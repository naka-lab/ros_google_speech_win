#!/usr/bin/env python
import os
import sys

# 環境に合わせてIPを設定
os.environ["ROS_MASTER_URI"] = "http://192.168.0.157:11311"
os.environ["ROS_IP"] = "192.168.0.150"

# パスを通す
sys.path.append("../ros_portable/python_package")

import rospy
from std_msgs.msg import String
import yaml
import time


grammar = """
[GRAMMAR]
greeding : $slot_greeding
bring_known_obj : $slot_drink * $slot_person * <持って行って|届けて|取って>
bring_unknown_obj : $slot_any を $slot_person * <持って行って|届けて|取って>



[SLOT]
$slot_greeding
hello : こんにちは|ハロー
bye : さようなら|バイ
morning : おはよう

$slot_drink
drink1 : ジュース
drink2 : コーラ|コーク
drink3 : お茶|緑茶

$slot_person
person1 : 中村|中村さん
person2 : 田中
person3 : 太郎

"""


def main():
    rospy.init_node("gspeech_example2")
    pub_grammar = rospy.Publisher(
        "grammar_lu/grammar", String, queue_size=10, latch=True
    )
    pub_synthesis = rospy.Publisher("google_speech/utterance", String, queue_size=10)

    time.sleep(2)
    pub_grammar.publish(grammar)

    while not rospy.is_shutdown():
        msg = rospy.wait_for_message("grammar_lu/results", String)
        results = yaml.safe_load(msg.data)

        print(results["text"])
        print(results["gram_id"])
        print(results["slot_id"])
        print(results["slot_str"])
        print("--------")

        if results["gram_id"] == "greeding":
            if results["slot_id"][0] == "hello":
                pub_synthesis.publish("ごきげんよう")
            elif results["slot_id"][0] == "bye":
                pub_synthesis.publish("さようなら")
            elif results["slot_id"][0] == "morning":
                pub_synthesis.publish("早起きは苦手です")


if __name__ == "__main__":
    main()
