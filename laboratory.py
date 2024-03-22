taskList = {'sunday': [], 'monday': [], 'tuesday': [], 'wednesday': ['funcionou', 'perfeito'], 'thursday': [], 'friday': [], 'saturday': []}
name = "wednesday"
copy = {}
for key in taskList:
    print(key)
    if name == key:
        #self.name is the name of the curent screen given on the "taskmanager.kv" file
        copy = taskList[key]
        print(copy)