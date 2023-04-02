names = {}
def first(name:str, good_marks):
    names[name] = good_marks

def second(name:str):
    print(names[name])
first('Violetta' , 5)
second ('Violetta')
