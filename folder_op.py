# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 13:16:01 2021

@author: quann
"""

import os 

#Các hàm 

   # Hàm kiểm tra thư mục 
def kiem_tra_folder(path):
    os.chdir(path)                                      #Di chuển đến thư mục trong đường dẫn path
    check = os.listdir(path)                            #List các thư mục hiện có ở ổ C:\
    if 'Crawler' not in check:                          #Nếu chưa có thư mục CRAWLER thì tạo thư mục CRAWLER
        os.mkdir('Crawler')                             #Nếu chưa có thư mục Crawler thì tạo thư mục Crawler

   
   # Hàm tạo thư 
def tao_thu_muc(name):
    os.mkdir(name)
    os.chdir(name)
        

#Hàm này để lưu lại các đường dẫn đã lấy vào thư mục vừa tạo
def luu_file(data, name_folder):      
    path = "C:\\Crawler\\"                              #data là list chứa nội dung file html
    os.chdir(path + str(name_folder))                   #Di chuyển tới folder
    html = data[0]
    f = open('HTML_web.html', 'w', encoding='utf-8')    #Đường link tới trang web
    fs = open('ND_HTML.txt', 'w', encoding='utf-8')     #file ghi nội dung của html
    fs.write(str(html))
    f.write(str(html))
    f.close()
    
#Hàm này để lưu lại lịch sử các đường dẫn đã cào vào file History.txt
def luu_lich_su_dulieu_da_cao(url):
    path = "C:\\Crawler\\"
    os.chdir(path)
    file = open("History.txt", 'r+', encoding='utf-8')
    STT = len(file.readlines()) -   10  #bắt đầu ghi ở dòng thứ 10
    file.close()
    file = open("History.txt", 'a+', encoding='utf-8')
    content = str(STT) + "/ " + str(url) + "\n"
    file.write(content)
    file.close()