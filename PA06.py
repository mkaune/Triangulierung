class ngonTriang:

 def __init__(self, n, triangles):
    #triangles=[[0,1,5], [1,5,2], [2,3,5], [3,4,5]]
    #n>=4
    triangles.sort()
    self.n=n
    self.triangles=triangles
    liste=[]
    for dreiecke in triangles:
        liste+=dreiecke
        if len(set(dreiecke))!=3:
            raise ValueError("no triangulation")
    # anzahl Diagonales en polygon:
    walls=set()
    
    for dreieck in triangles:
        #for i,elem in enumerate(dreicke):
        if dreieck[0]+1!=dreieck[1]:
            walls.add((dreieck[0],dreieck[1]))
        if dreieck[1]+1!=dreieck[2]:
            walls.add((dreieck[1],dreieck[2]))
        if  dreieck[2]!=n-1 or dreieck[2]==n-1 and dreieck[0]!=0:
            walls.add((dreieck[0],dreieck[2]))
    #no triangulierung???
    # anzahl triangles+
    walls=[list(elem) for elem in walls]
    print(walls)
    if len(walls)!=n-3:
        raise ValueError("no triangulation")       
    if len(triangles)!=n-2:
        raise ValueError("no triangulation")
    #vereinigung
    if set(range(n))!= set(liste):
        raise ValueError("no triangulation")
    
    self.walls=walls
 def n_walls(self):
    return len(self.walls)
 def flip(self, wall):
     tri=self.triangles
     walls=self.walls
     #viereck=set()
     newwall=[]
     #newdreicks
     index=[]
     for i,dreieck in enumerate(tri):
         if set(wall).issubset(set(dreieck)):
             print(dreieck,"dre")
             elemento=list(set(dreieck)-set(wall))[0]
             print(elemento, "elemento")
             newwall.append(elemento)
             #tri[i]=[wall.pop()]
             index.append(i)
     for i in index:
         tri[i]=[wall.pop()]  +newwall
         tri[i].sort()
     newwall.sort()
     print(tri)
     print(self.triangles)
     print(newwall)
     
     S=ngonTriang(n, tri)
     return S
             
             #newwall.append()
             
             #viereck.add(dreieck)
             
         #if wall[0] in dreieck and wall[1] in dreieck:
             #viereck=dreieck
             
     
     #return example: S=T.flip(wall)
     #nueva position de diagonales
     #S.triangles: [[1,2,3], [3,4,6]]
     
    
triangles=[[0,1,5], [1,2,5], [2,3,5], [3,4,5]]
n=6
#triangles=[[0,1,2],[0,2,3]]
#n=4
#walls: [(3, 5), (1, 5), (2, 5)]
