import json

# s_json = {'key1': 1, "key2" : 2}
# print(s_json['key2'])

# py_obj = '{"a":1,"a": 2, "a": 3, "b": 1, "b": 2}'
# json_obj = json.loads(py_obj)
# print(json_obj)

# mylist = ['apple', 'orange']
# json_obj = json.dumps(mylist)
# print(json_obj)

# mylist = ('apple', 'orange')
# json_obj = json.dumps(mylist)
# print(json_obj)
with open('st.json') as f:
    students = json.load(f)
    for name in students:
        del name["Info"]
    with open('new_students.json', 'w')as f:
        print(name)
        json.dump(students,f,indent = 2)
