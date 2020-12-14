#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import requests

url = 'http://localhost:5000/results'

r = requests.post(url,json={"duration":0,
                            "src_bytes":491,
                            "dst_bytes":0,
                            "land":0,
                            "wrong_fragment":0,
                            "urgent":0,
                            "hot":0,
                            "num_failed_logins":0,
                            "logged_in":0,
                            "num_compromised":0,
                            "root_shell":0,
                            "su_attempted":0,
                            "num_root":0,
                            "num_file_creations":0,
                            "num_shells":0,
                            "num_access_files":0,
                            "is_host_login":0,
                            "is_guest_login":0,
                            "count":2,
                            "srv_count":2,			 
            			    "serror_rate":0.0, 
             			    "srv_serror_rate":0.0,
             			    "rerror_rate":0.0
             			    "srv_rerror_rate":0.0, 
             			    "same_srv_rate":1.0, 
             			    "diff_srv_rate":0.0, 
             			    "srv_diff_host_rate":0.0, 
             			    "dst_host_count":150, 
             			    "dst_host_srv_count":25,
             			    "dst_host_same_srv_rate":0.17,
             			    "dst_host_diff_srv_rate":0.03,
             			    "dst_host_same_src_port_rate":0.17, 
             			    "dst_host_srv_diff_host_rate":0.00,
             			    "dst_host_serror_rate":0.00,
             			    "dst_host_srv_serror_rate":0.0,
             			    "dst_host_rerror_rate":0.05,
             			    "dst_host_srv_rerror_rate":0.0,
             			    "protocol_type":1,
             			    "service":45,
             			    "flag":1
                            })

print(r.json())

