# -*- coding: utf-8 -*-
# libPostfixLog plugin from modules Python Class v0.1-20091018
# Copyright (c) 2009 - Reinaldo de Carvalho <reinaldoc@gmail.com>

import re
from libTemplate import TemplateLog

class PostfixLog(TemplateLog):
	re_postfixLog = re.compile(r"^(?P<date_syslog>[A-Za-z]{3} \d{1,2} {1,2}\d\d:\d\d:\d\d) (?P<hostname>.*?) (?P<process>.*?): (?P<queue_id>.*?):.*?Subject: (?P<subject>.*) from (?P<client_ip_hostname>.*)\[(?P<client_ip>.*)\]; from=<(?P<mail_from>.*?)> to=<(?P<rcpts>.*?)> .*? helo=<(?P<helo>.*?)>")

	def __init__(self):
		pass

	def __del__(self):
		pass

	def insert(self, dbHandle, data):
		try:
			match = PostfixLog.re_postfixLog.match(data)
			result = self._match2dict(match)
			result = self._prepareSQL(result)
			if dbHandle.insert("INSERT INTO PostfixLog (date_now, date_syslog, hostname, process, queue_id, subject, client_ip_hostname, client_ip, mail_from, rcpts, helo) VALUES (now(), %(date_syslog)s, %(hostname)s, %(process)s, %(queue_id)s, %(subject)s, %(client_ip_hostname)s, %(client_ip)s, %(mail_from)s, %(rcpts)s, %(helo)s)" % result):
				return True
			else:
				return False
		except:
			return False
