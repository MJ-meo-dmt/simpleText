#!/usr/bin/env python

import ConfigParser


class ConfigHandler():

	@staticmethod
	def writeCfg():
		config = ConfigParser.RawConfigParser()

		config.add_section('Settings')
		config.set('Settings', 'username', 'no-username')


		# Writing configuration file
		with open('config.cfg', 'wb') as configfile:
			config.write(configfile)


	@staticmethod
	def readCfg():
		config = ConfigParser.RawConfigParser()
		config.read('config.cfg')

		username = config.get('Settings', 'username')

		return username
