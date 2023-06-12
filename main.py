


# bir db de bulunan çalışanlara ait isim ve maas bilgilerini çekip hızlı bir şekilde arama gerçekleştirecek BST algoritması ..


import sqlite3 as sql



# tablo
with sql.connect("veriler.db") as vt:
    cursor = vt.cursor()

    cursor.execute("create table if not exists veriler (isim text, maas int)")

    vt.commit()

# ekle
def vt_ekle(isim, maas):
    with sql.connect("veriler.db") as vt:
        cursor = vt.cursor()

        cursor.execute("INSERT INTO veriler (isim, maas) VALUES (?, ?)", (isim, maas))

        vt.commit()

# getir
def vt_getir():
    with sql.connect("veriler.db") as vt:
        cursor = vt.cursor()

        cursor.execute("SELECT * FROM veriler")

        data = cursor.fetchall()

        return data

     



class employees_Node:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
        self.left = None
        self.right = None



class employees_BST:
    def __init__(self):
        self.root = None



    def add_employe(self,name,salary):
        new_employe = employees_Node(name,salary)
        if self.root is None:
            self.root = new_employe
        else:
            self._add_helper(self.root,new_employe)


    def _add_helper(self,current_node,new_employe):
        if new_employe.name < current_node.name:
            if current_node.left is None:
                current_node.left = new_employe
            else:
                self._add_helper(current_node.left,new_employe)
        elif new_employe.name > current_node.name:
            if current_node.right is None:
                current_node.right = new_employe
            else:
                self._add_helper(current_node.right, new_employe)

    def search_employe(self,name):
        return self._search_helper(self.root, name)

    def _search_helper(self,current_node,name):
        if current_node is None or current_node.name == name:
            return current_node  
        elif name < current_node.name:
            return self._search_helper(current_node.left, name)
        else:
            return self._search_helper(current_node.right, name)
          

# örnek çalışan listesi
calisanlar = [   
                 ["halis", 5000],
                 ["john", 6000],
                 ["emily", 5500],
                 ["michael", 7000],
                 ["jessica", 4500],
                 ["david", 8000],
                 ["sophia", 4000],
                 ["daniel", 6500],
                 ["olivia", 5500],
                 ["andrew", 7500]
            ]


# db e veri girişi
# for i in calisanlar:
#     vt_ekle(i[0],i[1])


# ağaç oluşturma ve veri girme
tree_of_employe = employees_BST()

data = vt_getir()

for i in data:
    tree_of_employe.add_employe(i[0],i[1])


# arama işlemi
name = input("çalışan ismi: ")

result = tree_of_employe.search_employe(name)
print(f"\nçalışan ismi: {result.name}\nçalışan maaşı: {result.salary} TL")



# :)
