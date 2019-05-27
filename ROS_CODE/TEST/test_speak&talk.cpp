#include <iostream>
#include <ros/ros.h>
#include <std_msgs/String.h>
#include "wpb_home_tutorials/Follow.h"
#include <geometry_msgs/Twist.h>
#include <sound_play/SoundRequest.h>
#include <tf/transform_listener.h>
#include <geometry_msgs/PoseStamped.h> 
#include <string>

static std_msg::String msg;

void Speak(string inStr)
{
    spk_msg.arg = inStr;
    spk_pub.publish(spk_msg);
}

void KeywordCB(const std_msgs::String::ConstPtr & msg)
{
    ROS_WARN("------ Keyword = %s ------",msg->data.c_str());
    if(nState == STATE_FOLLOW)
    {
        // 从识别结果句子中查找物品（航点）关键词
        string strKeyword = FindKeyword(msg->data);
        int nLenOfKW = strlen(strKeyword.c_str());
        ROS_WARN("length of keyword is: %d",nLenOfKW);
        if(nLenOfKW > 0)
        {
            // 发现物品（航点）关键词
            
            //AddNewWaypoint(strKeyword);
            string strSpeak = strKeyword + " . OK. I have memoried. Next one , please";
            Speak(strSpeak);
        }

        // 停止跟随的指令
        int nFindIndex = msg->data.find("top follow");
        ROS_WARN("index is: %d",nFindIndex);
        if(nFindIndex >= 0)
        {
        	ROS_WARN("recognize stop following!");
            //FollowSwitch(false, 0);
            //AddNewWaypoint("master");
            //nState = STATE_ASK;
            //nDelay = 0;
            Speak("OK. What do you want me to fetch?");
        }
    }
}



int main(){
	ros::init(argc, argv, "wpb_home_shopping");

    ros::NodeHandle n;
    ros::Subscriber sub_sr = n.subscribe("/xfyun/iat", 10, KeywordCB);
    
    spk_pub = n.advertise<sound_play::SoundRequest>("/robotsound", 20);
    spk_msg.sound = sound_play::SoundRequest::SAY;
    spk_msg.command = sound_play::SoundRequest::PLAY_ONCE;
    
    while(ros::Ok()){
    	ros::spinOnce();
	}
    return 0;
}

