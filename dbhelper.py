import mysql.connector
from tverketresponse import *


class DbHelper(object):

    def __init__(self,obj):
        self.obj= obj

    def push_data(self):
        cnx = mysql.connector.connect(user='stbt', database='trafikverket')
        cursor = cnx.cursor()
        print(self.obj.sql)
        print(self.obj.values)
        cursor.execute(self.obj.sql, self.obj.values)
        cnx.commit()
        cnx.close()