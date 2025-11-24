from task import Task

class TaskManager:
    def __init__(self):
        self.tasks = {1: [], 2: [], 3: []}  # Priority levels 1 (high), 2 (medium), 3 (low)

    def add(self, task: Task):
        if task.priority > 3 or task.priority < 1:
            return False
        for i in self.tasks:
            if task.priority == i:
                self.tasks[i].append(task)
                return True
    
    def remove(self, name: str):
        for i in self.tasks:
            index = 0
            for j in self.tasks[i]:
                if j.name.lower().replace(' ', '') == name.lower().replace(' ', ''):
                    self.tasks[i].pop(index)
                    return True
                index += 1
        else:
            return False
    
    def complete(self, name: str):
        for i in self.tasks:
            index = 0
            for j in self.tasks[i]:
                if j.name.lower().replace(' ', '') == name.lower().replace(' ', ''):
                    j.completion = True
                    return True
                index += 1
        else:
            return False
    
    def save_json(self):
        import json
        data = {1: [], 2: [], 3: []}
        for i in self.tasks:
            for j in self.tasks[i]:
                data[i].append(j.to_dict())
        with open('tasks.json', 'w') as f:
            json.dump(data, f, indent=4)
    
    def import_json(self):
        import json
        try:
            with open('tasks.json', 'r') as f:
                data = json.load(f)
            for i in data:
                for j in data[i]:
                    task = Task.from_dict(j)
                    self.tasks[int(i)].append(task)
        except FileNotFoundError:
            pass

    
    def __str__(self):
        text = '-------------------------\n'
        text += 'High Priority Tasks:\n'
        for i in self.tasks[1]:
            text += "[x] " + i.name + '\n' if i.completion == True else "[ ] " + i.name + '\n'

        text += "\n"
        text += 'Medium Priority Tasks:\n'
        for i in self.tasks[2]:
            text += "[x] " + i.name + '\n' if i.completion == True else "[ ] " + i.name + '\n'

        text += "\n"
        text += 'Low Priority Tasks:\n'
        for i in self.tasks[3]:
            text += "[x] " + i.name + '\n' if i.completion == True else "[ ] " + i.name + '\n'
        
        text += '-------------------------'
        return text