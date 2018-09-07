data ={"cat":"xiaobai","dog":"erhei","fish":"jinli"}
for k,v in data.items():
    print (k,v)

for k in data:
    v = data.get(k)
    print (k,v)