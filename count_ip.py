#parse a webserver log file and count the number of ip's and its hits

import re
from collections import Counter

def apache_log_reader()
  regex = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'

  with open("samplelog") as f:
          log = f.read()
          my_iplist = re.findall(regex,log)
          ipcount = Counter(my_iplist)
          for k,v in ipcount.items():
                 print k,v
                 
                 
                 
 if __name__ == "__main__":
        apache_log_reader("access_log")
