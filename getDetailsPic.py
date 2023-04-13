import os, datetime

# Get file's path and change each backslash "\" to forward slash "/" and add a forward the end of path
def getPath():
    path = input('Enter your path: ')
    path = path.replace('\'', '/')
    l = list(path)
    l.append('/')
    path = "".join(l)
    return path


def getCreateTimeFile(file_path):
    timestamp = os.path.getctime(file_path)
    date_create = datetime.datetime.fromtimestamp(timestamp).isoformat()
    date_create = date_create.replace("-","").replace("T","").replace(":","").replace(".","")
    l = list(date_create)
    del(l[14:])
    date_create = "".join(l)
    return date_create

def main():
    path = getPath()
    for filename in os.listdir(path):
        file_path = path + filename
        new_name = path + getCreateTimeFile(file_path) + "." + file_path.split('.')[1]
        print(file_path)
        print(new_name)
        print("="*len(new_name))
        os.rename(file_path, new_name)
        print(new_name)
        print('='*len(new_name))     
        




if __name__ == "__main__":
    main()