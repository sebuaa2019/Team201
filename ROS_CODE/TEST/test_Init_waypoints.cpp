#include<iostream>
#include <ros/ros.h> 
#include <std_msgs/String.h>
#include <vector>
#include "action_manager.h"
#include <sound_play/SoundRequest.h>
#include <move_base_msgs/MoveBaseAction.h>
#include <actionlib/client/simple_action_client.h>
#include <waterplus_map_tools/GetWaypointByName.h>

using namespace std;

static vector<string> arWaypoint;

static void Init_waypoints()
{
    arWaypoint.push_back("1");
    arWaypoint.push_back("2");
    arWaypoint.push_back("3");
    arWaypoint.push_back("4");
    arWaypoint.push_back("5");
    arWaypoint.push_back("6");
    arWaypoint.push_back("7");
    arWaypoint.push_back("8");
    arWaypoint.push_back("9");
    arWaypoint.push_back("10");
    arWaypoint.push_back("11");
    arWaypoint.push_back("12");
	arWaypoint.push_back("13");
    arWaypoint.push_back("14");
    arWaypoint.push_back("15");
    arWaypoint.push_back("16");
    arWaypoint.push_back("17");
    arWaypoint.push_back("18");
    arWaypoint.push_back("19");
    arWaypoint.push_back("20");
}

int main(){
	Init_waypoints();
	if(sizeof(arWaypoint)==20){
		printf("right"); 
		return 0
	}
	else {
		return 1;
	}
}
