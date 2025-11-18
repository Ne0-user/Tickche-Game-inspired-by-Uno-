from Node import Node

class CircularLinkedList:
    def __init__(self,data=None):
        self.__head = None
        
        if data:
            try:
                for d in data:
                    self.append(d)
            except TypeError:
                self.append(data)
                
    def get_head(self):
        return self.__head
        
    def append(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.__head = new_node
            self.__head.set_next(self.__head)
        else:
            current=self.__head
            while current.get_next() != self.__head:
                current = current.get_next()
            current.set_next(new_node)
            new_node.set_next(self.__head)
            
            pass
    def remove(self, index=None, value=None):
        if self.is_empty():
            raise Exception("removing from empty list")
            
        if index!=None and value!=None:
            raise Exception("idex and value must be given exclusively")
            
        elif index != None:
            if index < 0 or not isinstance(index, int):
                raise IndexError("index must be positive _int_")
            if index == 0:
                current = self.__head
                while current.get_next() != self.__head:
                    current = current.get_next()
                current.set_next(current.get_next())
                self.__head = current.get_next()
            
            else:
                current = self.__head
                for i in range(index-1):
                    current = current.get_next()
                    current.set_next(current.get_next())
                
            
        elif value != None:
            current=self.__head
            
    def merge(self,circularlinkedlist2):
        if not self.__head:
            self.__head=circularlinkedlist2.__head
        
        if not circularlinkedlist2.__head:
            return
        
        current=self.__head
        
        while current.get_next() !=self.__head:
            current=current.get_next()
        
        current.set_next(circularlinkedlist2.__head)
        
        current=circularlinkedlist2.__head
        
        while current.get_next()!=circularlinkedlist2.__head:
            current=current.get_next()
        
        current.set_next(self.__head)
    
    def len_lista(self):
        if self.is_empty():
            return 0
        
        i=0
        current=self.__head
        while current.get_next()!=self.__head:
            i=i+1
            current=current.get_next()
        
        return i
    
    def N_esimo(self,dato):
        n=self.len_lista()
        
        current=self.__head
        
        for i in range(n-dato+1):
            current=current.get_next()
        
        print(current.get_data())
    
    def copy(self):
        current=self.__head
        clist2=CircularLinkedList()
        
        while current.get_next()!=self.__head:
            clist2.append(current.get_data())
            current=current.get_next()
        
        clist2.append(current.get_data())
        return clist2
        
    def is_empty(self):
        return self.__head == None
    
    def eliminar_rep(self):
        current=self.__head
        vistos=[]
        prev=None
        
        while current.get_next()!=self.__head:
            if current.get_data() in vistos:
                prev.set_next(current.get_next())
                
            
            else:
                vistos.append(current.get_data())
                prev=current
            
            current=current.get_next()
        
    def sort(self,reverse=False):
        if not self.__head or not self.__head.get_next():
            return
        
        lista=[]
        current=self.__head
        
        while current.get_next()!=self.__head:
            lista.append(current.get_data())
            current=current.get_next()
        
        lista.append(current.get_data())
        
        self.__quick_sort(lista,0,len(lista)-1)
        self.__head=None
        
        if reverse:
            lista_invertida=lista[::-1]
            newlinklist=CircularLinkedList(lista_invertida)
        
        else:
            newlinklist=CircularLinkedList(lista)
            
        self.__head=newlinklist.__head
        
        
    def __particion(self,lista,pivote,izq,der):
        i=izq-1
        
        for j in range(izq,der):
            
            if lista[j]<lista[pivote]:
                i+=1
                aux=lista[i]
                lista[i]=lista[j]
                lista[j]=aux
        i+=1
        aux=lista[i]
        lista[i]=lista[pivote]
        lista[pivote]=aux
        return i
    
    def __quick_sort(self,lista,izq,der):
            
        if izq>=der:
            return
            
        piv=der
        p=self.__particion(lista, piv, izq, der)
        self.__quick_sort(lista, izq, p-1)
        self.__quick_sort(lista, p+1, der) 
    
    def __repr__(self):
        if self.is_empty():
            return "None"
        print(self.__head.get_data(), end=" -> ")
        current=self.__head.get_next()
        while current != self.__head:
            print(current.get_data(), end=" -> ")
            current = current.get_next()
        return "head"
