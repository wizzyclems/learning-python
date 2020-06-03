#!/usr/bin/env python3

import os
import re
import csv
import operator


def parseSysLog():
  errorCount = {}
  userEntryCount = {}

  with open(os.path.expanduser('~') + '/syslog.log', mode='r',encoding='UTF-8') as file:
    for log in  file.readlines():
      pattern = r"[\w \.\:]* ([A-Z]{4,}) ([\w \']*) [\w \[\]\#]*\(([\w\.]*)\)"
      result = re.search(pattern, log)
    
      if result[3] not in userEntryCount :
          userEntryCount[result[3]] = [0,0]

      if result[1] == 'ERROR' :

         if result[2] not in errorCount :
           errorCount[result[2]] = 1
           userEntryCount[result[3]][1] = 1
           continue

         errorCount[result[2]] = errorCount[result[2]] + 1
         userEntryCount[result[3]][1] = userEntryCount[result[3]][1] + 1

      if result[1] == 'INFO' :
          userEntryCount[result[3]][0] = userEntryCount[result[3]][0] + 1

      #user_error_dict = userEntryCount[result[3]]
      #user_error_dict[result[1]] = user_error_dict[result[1]] + 1

    file.close()


  sortedErrorCount = sorted(errorCount.items(),key=operator.itemgetter(1), reverse=True)
  sortedErrorCount.insert(0,("Error","Count"))
  
  with open(os.path.expanduser('~') + '/error_message.csv', mode='w',encoding='UTF-8') as error_file :
      writer = csv.writer(error_file)
      writer.writerows(sortedErrorCount)
      error_file.close()

  #print(userEntryCount)
  #print("===========================")
  sortedUserEntryCount = sorted(userEntryCount.items(),key=operator.itemgetter(0))
  #print(sortedUserEntryCount)
  transformed_user_list = []

  for user_row in sortedUserEntryCount :
      transformed_user_list.append((user_row[0], user_row[1][0], user_row[1][1]))

  #print("===========================")
  transformed_user_list.insert(0,("Username", "INFO", "ERROR"))
  #print(transformed_user_list)

  with open(os.path.expanduser('~') + '/user_statistics.csv', mode='w',encoding='UTF-8') as user_file :
      writer = csv.writer(user_file)
      writer.writerows(transformed_user_list)
      user_file.close()



parseSysLog()

