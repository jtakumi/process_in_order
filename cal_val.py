import json,os

def load_file_name(datname):
    with open(os.path.join("save_data",datname),"r") as f:
        save_data = f.readline()
    save_data = save_data.replace('\n','')
    return save_data

def write_file_name(file_name,dat_name):
    with open(os.path.join("save_data",dat_name),"w") as f:
        print(file_name,file=f)

def json_r(file_name):
    with open(os.path.join("datasets",file_name),"r") as f:
        d = json.load(f)
    return d

def json_w(data,f_num):
    f_name = './outputs/output_' + str(f_num) + '.json'
    with open(f_name,"w") as f:
        json.dump(data,f,indent=2,ensure_ascii=False)
    write_file_name(f_name,'output.dat')
    if f_num >=99:
        f_num =1
    else:
        f_num +=1
    next_dataset = 'dataset_' + str(f_num) + '.json'
    with open(os.path.join("save_data","dataset.dat"),"w") as f:
        print(next_dataset,file=f)


def main():
    output = {}
    data =[]
    id = {}
    value ={}
    before_id = {}
    before_value = {}
    delta = {}
    file_name = load_file_name('dataset.dat')
    f_num = file_name.replace('.json','')
    idx = f_num.find('_')
    f_num = f_num[idx+1:]
    d = json_r(file_name)
    f_num =int(f_num)
    if f_num <=0:
        bf_num =99
    else:
        bf_num= f_num-1
    b_file_name= 'dataset_' + str(bf_num) + '.json'
    before_d =json_r(b_file_name)
    n=0
    for i in d:
        value[n] = d['data'][n]['value']
        id[n] = d['data'][n]['id']
        before_value[n] = before_d['data'][n]['value']
        before_id[n] = before_d['data'][n]['id']
        if id[n] in before_id:
            delta[n] = value[n] - before_value[n]
        else:
            delta[n]  = value[n]
        data.append({'id':id[n],'value':value[n],'before_value':before_value[n],'delta':delta[n]})
        n+=1
    data.sort(key=lambda x:x['id'])
    output = {'current_data':file_name,'before_data':b_file_name,'data':data}
    json_w(output,f_num)

if __name__ == '__main__':
    main()


