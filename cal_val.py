import json,os

def load_file_name():
    with open(os.path.join("save_data","dataset.dat"),"r") as f:
        save_data = f.readline()
    save_data = save_data.replace('\n','')
    return save_data

def json_r(file_name):
    with open(os.path.join("datasets",file_name),"r") as f:
        d = json.load(f)
    return d

def main():
    output = {}
    val = {}
    data =[]


if __name__ == '__main__':
    main()


