# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 12:06:12 2021

@author: quann
"""
import folder, web.op


# Nhập đường link, giới hạn page tải về
url_first = input("Nhập đường link:")
w = int(input("Nhập giới hạn page: "))

# Tạo các danh sách
url_list = []                                          # Chứa các link chưa duyệt
url_list_limit = 3000                                  #Quy định số lượng trang web được tải về
history = []                                           # Chứa các link đã duyệt
max_pages = w                                          #Giới han page tải về  
folder.kiem_tra_folder("C:\\")                         #Kiểm tra và tạo thư mục Crawler để lưu trữ
data_folder = 'C:\\Users\\Public\\Crawler\\'           #Lưu vào ổ C thư mục Crawler 
count = 0                                              #Đếm số lượng trang web tải về 
url_list.append(url_first)                             # Thêm url vào hàng chờ

#Kịch bản tải các trang web khác 
folder.kiem_tra_folder(data_folder)                    # Tạo một Folder

while count < max_pages:
    url = url_list.pop(0)
    url_new = []                                       # danh sách những đường link vừa tìm được
    url_new_limit = 1000
    content = web.op.doc_noi_dung(url)                      # Đọc nội dung
    item = web.op.lay_duong_dan(content)                    # Lấy tất cả đường link 
    for k in item:                                          #Duyệt từng đường link thu được để kiểm tra tính hợp lệ
        if web.op.kiem_tra_duong_dan(k) == False:           # Kiểm tra đường link
            k = web.op.chinh_sua_duong_dan(url_first, k)    #Chỉnh sửa nếu thiếu phần https://...   
        if (k not in history) and (k not in url_list):      #Nếu đường link chưa hề được duyệt và chưa có trong hàng đợi
            if web.op.kiem_tra_url_da_duyet(k) == True:
                continue    
            else:    
                url_new.append(k)                           #Thêm đường link mới vào danh sách url_new
    url_list = url_list + url_new                           # Lưu lại các url hợp lệ vào url_list
    count += 1                                              # đếm số đường link đã duyệt
    folder.luu_lich_su_du_lieu_da_cai(url)                  # Lưu lại đường link vừa lấy từ web về vào lịch sử
    history.append(url)
    data_array = [content, url_new, url, url_new_limit]     #data_array là một list gồm nội dung file html...
    name_folder = folder.tao_ten_folder()                   #Tạo thư mục tự động và kết quả trả về là tên thư mục vừa tạo
    w = folder.luu_file(data_array, name_folder)
    
    # Sau khi hoàn tất 
    print("ĐÃ DUYỆT", url)