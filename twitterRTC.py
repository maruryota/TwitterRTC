#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- Python -*-

"""
 @file TwitterRTC.py
 @brief ModuleDescription
 @date $Date$


"""
import sys
import time
sys.path.append(".")

# Import RTM module
import RTC
import OpenRTM_aist

from twitter_action.get_timeline import get_timeline
from twitter_action.post import post_tweet

import json, config #標準のjsonモジュールとconfig.pyの読み込み
from requests_oauthlib import OAuth1Session #OAuthのライブラリの読み込み


# Import Service implementation class
# <rtc-template block="service_impl">

# </rtc-template>

# Import Service stub modules
# <rtc-template block="consumer_import">
# </rtc-template>


# This module's spesification
# <rtc-template block="module_spec">
TwitterRTC_spec = ["implementation_id", "TwitterRTC", 
		 "type_name",         "TwitterRTC", 
		 "description",       "ModuleDescription", 
		 "version",           "1.0.0", 
		 "vendor",            "maruryota", 
		 "category",          "Category", 
		 "activity_type",     "STATIC", 
		 "max_instance",      "1", 
		 "language",          "Python", 
		 "lang_type",         "SCRIPT",
		 ""]
# </rtc-template>

##
# @class TwitterRTC
# @class TwitterRTC
# @brief ModuleDescription
# 
# 
class TwitterRTC(OpenRTM_aist.DataFlowComponentBase):
	
	##
	# @brief constructor
	# @param manager Maneger Object
	# 
	def __init__(self, manager):
		OpenRTM_aist.DataFlowComponentBase.__init__(self, manager)

		self.url = "https://api.twitter.com/1.1/statuses/update.json"

		tweet_arg = [None] * int((len(RTC._d_TimedString) - 4) / 2)
		self._d_tweet = RTC.TimedPose2D(*tweet_arg)
		"""
		"""
		self._tweetIn = OpenRTM_aist.InPort("tweet", self._d_tweet)

		


		# initialize of configuration-data.
		# <rtc-template block="init_conf_param">
		
		# </rtc-template>


		 
	##
	#
	# The initialize action (on CREATED->ALIVE transition)
	# formaer rtc_init_entry() 
	# 
	# @return RTC::ReturnCode_t
	# 
	#
	def onInitialize(self):
		# Bind variables and configuration variable
		
		# Set InPort buffers
		self.addInPort("tweet",self._tweetIn)

		# Set OutPort buffers
		
		# Set service provider to Ports
		
		# Set service consumers to Ports
		
		# Set CORBA Service Ports
		
		return RTC.RTC_OK
	
	###
	## 
	## The finalize action (on ALIVE->END transition)
	## formaer rtc_exiting_entry()
	## 
	## @return RTC::ReturnCode_t
	#
	## 
	#def onFinalize(self):
	#
	#	return RTC.RTC_OK
	
	###
	##
	## The startup action when ExecutionContext startup
	## former rtc_starting_entry()
	## 
	## @param ec_id target ExecutionContext Id
	##
	## @return RTC::ReturnCode_t
	##
	##
	#def onStartup(self, ec_id):
	#
	#	return RTC.RTC_OK
	
	###
	##
	## The shutdown action when ExecutionContext stop
	## former rtc_stopping_entry()
	##
	## @param ec_id target ExecutionContext Id
	##
	## @return RTC::ReturnCode_t
	##
	##
	#def onShutdown(self, ec_id):
	#
	#	return RTC.RTC_OK
	
	##
	#
	# The activated action (Active state entry action)
	# former rtc_active_entry()
	#
	# @param ec_id target ExecutionContext Id
	# 
	# @return RTC::ReturnCode_t
	#
	#
	def onActivated(self, ec_id):
		CK = config.CONSUMER_KEY
		CS = config.CONSUMER_SECRET
		AT = config.ACCESS_TOKEN
		ATS = config.ACCESS_TOKEN_SECRET
		self.twitter = OAuth1Session(CK, CS, AT, ATS) #認証処理
		
	
		return RTC.RTC_OK
	
	###
	##
	## The deactivated action (Active state exit action)
	## former rtc_active_exit()
	##
	## @param ec_id target ExecutionContext Id
	##
	## @return RTC::ReturnCode_t
	##
	##
	#def onDeactivated(self, ec_id):
	#
	#	return RTC.RTC_OK
	
	##
	#
	# The execution action that is invoked periodically
	# former rtc_active_do()
	#
	# @param ec_id target ExecutionContext Id
	#
	# @return RTC::ReturnCode_t
	#
	#
	def onExecute(self, ec_id):
		print("行いたい行動を入力してください。 'post' 'timeline'")
		action = input()

		if action == "post":
			print("tweet 内容を入力してください：")
			tweet = input()
			post(self.url, self.twitter, tweet)


		elif action == "timeline":
			print("タイムライン取得数を入力してください：")
			timeline_count = input()
			get_timeline(self.url, self.twitter, int(timeline_count))

		else:
			print("行動は 'post' 'timeline'が選択可能です。")
	
		return RTC.RTC_OK
	
	###
	##
	## The aborting action when main logic error occurred.
	## former rtc_aborting_entry()
	##
	## @param ec_id target ExecutionContext Id
	##
	## @return RTC::ReturnCode_t
	##
	##
	#def onAborting(self, ec_id):
	#
	#	return RTC.RTC_OK
	
	###
	##
	## The error action in ERROR state
	## former rtc_error_do()
	##
	## @param ec_id target ExecutionContext Id
	##
	## @return RTC::ReturnCode_t
	##
	##
	#def onError(self, ec_id):
	#
	#	return RTC.RTC_OK
	
	###
	##
	## The reset action that is invoked resetting
	## This is same but different the former rtc_init_entry()
	##
	## @param ec_id target ExecutionContext Id
	##
	## @return RTC::ReturnCode_t
	##
	##
	#def onReset(self, ec_id):
	#
	#	return RTC.RTC_OK
	
	###
	##
	## The state update action that is invoked after onExecute() action
	## no corresponding operation exists in OpenRTm-aist-0.2.0
	##
	## @param ec_id target ExecutionContext Id
	##
	## @return RTC::ReturnCode_t
	##

	##
	#def onStateUpdate(self, ec_id):
	#
	#	return RTC.RTC_OK
	
	###
	##
	## The action that is invoked when execution context's rate is changed
	## no corresponding operation exists in OpenRTm-aist-0.2.0
	##
	## @param ec_id target ExecutionContext Id
	##
	## @return RTC::ReturnCode_t
	##
	##
	#def onRateChanged(self, ec_id):
	#
	#	return RTC.RTC_OK
	



def TwitterRTCInit(manager):
    profile = OpenRTM_aist.Properties(defaults_str=TwitterRTC_spec)
    manager.registerFactory(profile,
                            TwitterRTC,
                            OpenRTM_aist.Delete)

def MyModuleInit(manager):
    TwitterRTCInit(manager)

    # Create a component
    comp = manager.createComponent("TwitterRTC")

def main():
	mgr = OpenRTM_aist.Manager.init(sys.argv)
	mgr.setModuleInitProc(MyModuleInit)
	mgr.activateManager()
	mgr.runManager()

if __name__ == "__main__":
	main()

