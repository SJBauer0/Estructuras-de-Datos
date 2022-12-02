import igraph as ig
import matplotlib.pyplot as plt

#---------------------------------------------------------

def plotGraph():
  fig, ax = plt.subplots(figsize=(6, 6))
  ig.plot(
    g,
    target=ax,
    layout="auto",  # print nodes in a circular layout
    vertex_size=0.1,
    vertex_frame_width=2.0,
    vertex_label=g.vs["name"],
    vertex_label_size=10.0,
    vertex_frame_color=[
      "blue" if start == True else "black" for start in g.vs["start"]
    ],
    vertex_color=[
      "green" if neighbor == True else "salmon"
      for neighbor in g.vs["neighbor"]
    ],
  )


#---------------------------------------------------------

NC = int(input("Ingresa la cantidad de conexiones:  "))
sublist = ()
list = []
formula = ""

while (NC != 0):
  conexion = str(input("Ingresa la puerto de salida: "))
  sublist = conexion.split(" ")
  formula += sublist[0] + "-" + sublist[1] + ","
  NC -= 1

g = ig.Graph.Formula(formula)

#---------------------------------------------------------

NQ = int(input("Ingresa la cantidad de Consultas: "))
totalvertex = g.vcount()
g.delete_vertices("")
respuesta = ()

while (NQ != 0):
  awns = str(input("Ingresa el puerto y la longitud de las conexiones: "))
  respuesta = awns.split(" ")
  num = int(respuesta[1])
  vertex = g.vs.find(name=respuesta[0])
  vertexid = (vertex.index)
  edges = g.neighborhood(respuesta[0], order=num)
  numedges = len(edges)
  g.vs[vertexid]["start"] = True
  i = numedges - 1
  while i != 0:
    g.vs[edges[i]]["neighbor"] = True
    i -= 1
  ports = (totalvertex - numedges - 1)
  print("Case ", NQ, " : ", ports, " ports not reachable from port ",
        (respuesta[0]), " with MNP = ", num, ".")
  plotGraph()
  NQ -= 1

plt.show()

#---------------------------------------------------------
