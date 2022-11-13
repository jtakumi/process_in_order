import random,json,os
output = {}

def save_data(file_name):
    path = os.path.join('save_data','dataset.dat')
    with open(path,'w') as f:
        print(file_name,file=f)

def compose_data(data,fn):
    path = os.path.join('datasets',fn)
    with open(path,'w') as f:
        json.dump(data,f,indent=2,ensure_ascii=False)


def main():
    for i in range(3):
        data = []
        for j in range(50):
            val_seed = int(random.random() * 100)
            id_seed = random.randint(1,1000)
            data.append({'id':id_seed,'value':val_seed})
        output = {'file_number':i,'data':data}
        fn = "dataset_" + str(i) + ".json"
        compose_data(output,fn)
    save_data(fn)
    print("composed datas")

""" if i ==0 and j == 10:
                id_seed = 1100
            elif i ==2 and j ==20:
                id_seed = 1200
            else
:"""

if __name__ == '__main__':
    main()

    