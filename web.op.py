# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 10:40:05 2021

@author: quann
"""

#Các thư viên cần thiết

import requests
import re
from bs4 import BeautifulSoup
import os

#Các hàm cần thiết

   #Hàm đọc nội dung của trang web theo url chỉ định
   #Kết quả trả về là 1 văn bản dạng chuỗi trong đường dẫn 
def doc_noi_dung(url):
    pageee = requests.get(url)                            # Gửi yêu cầu truy cập url
    rabbit = BeautifulSoup(pageee.text,'html.parser')     #.........................
    return rabbit                                         #.........................


#Hàm lấy các đường link web trong nội dung đọc về
#Kết quả trả về là 1 list chứa các đường link
def lay_cac_duong_dan(rabblit):
    url_list = []
    problem  = []
    raw = rabblit.find_all("a")                           #Lọc các thẻ có đầu <a>
    for item in raw:                                      #
        link = item.get("href")                           #Lấy ra các đường dẫn trong href
        url_list.append(link)                             #
    for item in url_list:                                 # Lọc các đường dẫn trong url_list
        item = str(item)                                  #
        if (item.find("http", 0, 4)):                     # Giữ lại các đường dẫn như https và vn
         if (item.find("java", 0, 4)):                    #       
          if (item.find("#", 0, 4)):                      #   
           if (item.find("None", 0, 4)):                  #  
            if len(item) > 2:                             #
             problem.append(item)                         #  Rồi sau đó thêm vào list problem
        
        if not(item.find("http", 0, 4)):
            problem.append(item)
    return problem 


#Hàm kiểm tra tính hợp lệ của 1 đường link 
#Kết quả trả về: True nếu hợp lệ, False nếu không hợp lệ
 

def kiem_tra_link(url):                                   #
    kt = re.search("http", url)                           #
    try:                                                  #
        if url == kt.string:                              #
            return True                                   #
    except:                                               #                       
        return False                                      #
    
#Hàm chỉnh sửa đường link nếu đường link là không đầy đủ hoặc chưa hợp lệ 
#Kết quả trả về là một đường link đầy đủ 


def chinh_sua_link(url, item): 
    item = str(url) + item                                #Thêm https://... vào
    return item


def kiem_tra_url_da_duyet(url):                           #Kiểm tra lại các url đã duyệt 
    path = "C:\\CRAWLER\\"                                #
    os.chdir(path)                                        #
    file = open("History.txt", 'r+', encoding='utf-8')    #
    ds_da_duyet = file.readlines()                        #
    for i in ds_da_duyet:                                 #
        if url in i:                                      #
            return True                                   #
    file.close()                                          #
    return False                                          #









