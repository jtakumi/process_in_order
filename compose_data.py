import random,json,os
from datetime import timedelta,timezone,datetime
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
    for i in range(100):
        data = []
        for j in range(50):
            val_seed = int(random.random() * 100)
            id_seed = random.randint(1,1000)
            data.append({'id':id_seed,'value':val_seed})
        JST = timezone(timedelta(hours=+9), 'JST')
        time_seed = datetime.now(JST)
        time = time_seed.strftime('%Y%m%dT%H%M%S+09:00')
        output = {'file_number':i,'time':time,'data':data}
        fn = "dataset_" + str(i) + ".json"
        compose_data(output,fn)
    save_data(fn)
    print("composed datas")

if __name__ == '__main__':
    main()

    