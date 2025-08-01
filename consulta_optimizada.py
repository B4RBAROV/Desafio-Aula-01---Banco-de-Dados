from time import perf_counter as time 

class Tree:
    def __init__(self):
        self.root = None
        
        
    def add_user(self, id, name, phone):
        if self.root is None:
            self.root = No(name, None)
        
        return self.root.add_user(id, name, phone)
    
    
    def find_name(self, name):
        start = time()
        if self.root is not None:
            system_return = self.root.find_name(name)
            end = time()
            
            print('Time Total: {:.4f} seg'.format(end - start))
            return system_return
        
        return False
    
    
    def in_order(self):
        if self.root is not None:
            return self.root.in_order()
        
        return False
            
        
    def balance(self):
        list = self.in_order()
        
        if list:
            self.root = No.balance(0, len(list) - 1, list)
            return True
        
        return False
    
    def test(self):
        print(self.root.info)
            


class No:
    def __init__(self, name, users):
        self.info = name
        if users is not None:
            self.users = users
        else:
            self.users = {}
        self.left = self.right = None
        
    def add_user(self, id, name, phone):
        if name == self.info:
            if id in self.users:
                return False
            
            self.users[id] = {
                "Name": name,
                "Phone": phone
            }
            return True
        
        if name < self.info:
            if self.left is None:
                self.left = No(name, None)
            
            return self.left.add_user(id, name, phone)
                
        if self.right is None:
            self.right = No(name, None)
            
        return self.right.add_user(id, name, phone)
    
    
    def find_name(self, name):
        if name == self.info:
            for id in self.users:
                print('Name: {}; id: {}; Phone: {}'.format(name, id, phone))
            return True
        
        if name < self.info:
            if self.left is not None:
                return self.left.find_name(name)
            
            return False
        
        if self.right is not None:
            return self.right.find_name(name)
        
        return False
    
    
    def in_order(self):
        list = []
        if self.left is not None:
            list.extend(self.left.in_order())
            
        list.append(self)
        
        if self.right is not None:
            list.extend(self.right.in_order())
        
        return list
    
    @staticmethod
    def balance(start, end, list):
        if start > end:
            return None 
        
        mid = int((start + end) / 2)
        node = list[mid]
        new_node = No(node.info, node.users)
        
        new_node.left = No.balance(start, mid - 1, list)
        new_node.right = No.balance(mid + 1, end, list)
        
        return new_node
        
        
            


tree = Tree()

start = time()
with open('dados_clientes.dbf', 'r') as db:
    
    line = db.readline().strip()
    while line != '':
         date = line.split(';')
         
         id = date[0]
         name = date[1]
         phone = date[2]
         
         tree.add_user(id, name, phone)
         line = db.readline()

tree.balance()

name = input('Name: ')
tree.find_name(name)

end = time()
print('Time to Create Tree and Find Name: {:.4f} seg'.format(end - start))
