import json

def add():
    ask=str(input('create a To-Do list? :'))
    if ask=='yes'or 'yeah' or 'okay':
            create()
def create():
        tit=input('title: ')
        des=input('description: ')
        data={'title':tit,'description':des}

        op=open('work.json','r')
        with open('work.json','a') as f:
            search=json.load(op,strict=False)
            if search:
                f.write(',\n')
            else:
                f.write('\n')

            json.dump(data,f,indent=4)

     
add()