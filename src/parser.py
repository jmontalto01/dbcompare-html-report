import json
import pandas as pd

def parse_file():
    with open('log_json_detailed.txt') as json_file:
        for i in json_file.readlines():
            data =json.loads(i)
            df = pd.DataFrame.from_records(data)
            print(df)
    
if __name__ == "__main__":
    parse_file()

# create table


   


    #print(data[0].values())
    #print(data[0].keys())
    #for index in range(len(data)):
        #for key in data[index]:
            #print(type(data[index][key]))
            #if type(key) in [str]:
                #print(key)

        #for v in data[0].values():
         #   print("{col}, {vals}".format(col=k,vals=v))