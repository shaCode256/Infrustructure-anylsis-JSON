import json
import sys

inFile = sys.argv[1]
outFile = sys.argv[2]
# Dependancy conflict tracker


def proccess_data(self):
    DependOn= {}
    DependOnMe= {}

    mining= []

    for project in json_data['Projects']:
        key= project['Name']
        for Dependency in project['Dependencies']:
            value= Dependency['Name']
            if project['Name'] not in DependOn:
                DependOn[key] = []
            DependOn[key].append(value)
        
        visited= []
        if key not in DependOn:
            mining= []
        else:
             mining= [DependOn[key]]
        while len(mining)>0: #get all indirect dependencies
            dep= mining.pop()
            for d in dep:
                for project in json_data['Projects']:
                    if project['Name']== d:
                        for Dependency in project['Dependencies']:
                            value= Dependency['Name']
                            if DependOn[key].count(value)==0:     # Avoid duplicate values in dictionary
                                DependOn[key].append(value)
                            if value not in visited: # to avoid getting in an infinite loop
                                mining.append(value)
                                visited.append(value)
                            
    
    

    for key in DependOn:
        for value in DependOn[key]:
            if value not in DependOnMe:
                DependOnMe[value]= [] 
            DependOnMe[value].append(key)

    for key in DependOn:#sort values
        DependOn[key].sort()
    for key in DependOnMe:#sort values
        DependOnMe[key].sort()    
    return (DependOn, DependOnMe)


with open(inFile,'r') as f:
    json_data = json.load(f)
    data=proccess_data(json_data)
    result= {"DependOn": data[0], "DependOnMe": data[1]}

            
with open(outFile,'w') as o:
    o.write(json.dumps(result, sort_keys=True))