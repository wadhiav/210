class graph():
    def __init__(self):
        self.dict = {}

    def add_node(self, node):
        if node not in self.dict:
            self.dict[node] = []

    def add_edge(self,node,node2):
        self.dict[node2].append(node)
        self.dict[node].append(node2)

    def prt_graph(self):
        print (self.dict)


if __name__=='__main__':

    create = graph()

    create.add_node("A")
    create.add_node("B")
    create.add_node("C")
    create.add_node("D")
    create.add_node("E")
    create.add_node("F")
    create.add_node("G")
    create.add_node("H")
    create.add_node("I")

    create.add_edge("A","B")
    create.add_edge("A","C")
    create.add_edge("B","D")
    create.add_edge("C","E")
    create.add_edge("D","F")
    create.add_edge("E","G")
    create.add_edge("F","H")
    create.add_edge("G","I")



    create.prt_graph()
