import random,os,json

def main():
   data = [[random.randint(1,100),random.randint(1,100)] for i in range(100)]
   with open('./array_test/test.txt',"w") as f:
    print(data,file=f)

if __name__ == "__main__":
    main()