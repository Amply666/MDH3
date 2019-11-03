#!/usr/bin/python
#coding=utf-8

import time
import MySQLdb

timeSleep = 5

def executeReaddata():
    conn = MySQLdb.connect(host="192.168.1.2", user="mdh_user", passwd="Pa55w0rd", db="mydomhome")
    x = conn.cursor()
    try:
        now = time.strftime('%Y-%m-%d %H:%M:%S')
        x.execute("select intero from mdh_aux where string = %s ", ["seth_alive"])
        myresult = x.fetchall()
        for xxx in myresult:
            val = xxx[0]
        if val > 4294967294:
            val = 0
        x.execute("update mdh_aux set intero=%s, datetime_val=%s  where string = %s", [val+1,now,"seth_alive"])
        conn.commit()
        #print val
    except MySQLdb.Error, e:
        try:
            print "MySQL Error [%d]: %s" % (e.args[0], e.args[1])
        except IndexError:
            print "MySQL Error: %s" % str(e)

    time.sleep(timeSleep)

while True:
    executeReaddata()
