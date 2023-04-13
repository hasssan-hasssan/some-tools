import os
import time
# path="E:/PIC/self/WIN_20200406_11_57_32_Pro.jpg"
# filename = os.path.basename(path).split('/')[-1]
# print(filename)

num_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
num_dict = {'۰':'0','۱':'1','۲':'2','۳':'3','۴':'4','۵':'5','۶':'6','۷':'7','۸':'8','۹':'9',}
path = input('Enter your pictures of folder: ')
print(path)
folder = path.replace('\'', '/')
l = list(folder)
l.append('/')
folder = "".join(l)
print("New Search==============================================")
for file in os.listdir(folder):
    
    
    new_file_name = ''
    for i in file:
        if i in num_list:
            new_file_name += i

        if i in num_dict:
            new_file_name += num_dict[i]

    old_name = folder + file 
    new_name = folder + new_file_name + "." +file.split('.')[1]
    if new_name.endswith('.mp4'):
        l = list(new_name)
        del(l[-5])
        new_name = "".join(l)
    print(old_name)
    print(new_name)
    print("="*len(new_name))
    os.rename(old_name, new_name)
    print(new_name)
    print('='*len(new_name))