# 我们需要的数据结构
# option = {
#     title : {
#         text: '冰桶挑战'
#     },
#     toolbox: {
#         show : true,
#         feature : {
#             mark : {show: true},
#             dataView : {show: true, readOnly: false},
#             restore : {show: true},
#             saveAsImage : {show: true}
#         }
#     },
#     series : [
#         {
#             name:'树图',
#             type:'tree',
#             orient: 'horizontal',  // vertical horizontal
#             rootLocation: {x: 100,y: 230}, // 根节点位置  {x: 100, y: 'center'}
#             nodePadding: 8,
#             layerPadding: 200,
#             hoverable: false,
#             roam: true,
#             symbolSize: 6,
#             itemStyle: {
#                 normal: {
#                     color: '#4883b4',
#                     label: {
#                         show: true,
#                         position: 'right',
#                         formatter: "{b}",
#                         textStyle: {
#                             color: '#000',
#                             fontSize: 5
#                         }
#                     },
#                     lineStyle: {
#                         color: '#ccc',
#                         type: 'curve' // 'curve'|'broken'|'solid'|'dotted'|'dashed'

#                     }
#                 },
#                 emphasis: {
#                     color: '#4883b4',
#                     label: {
#                         show: false
#                     },
#                     borderWidth: 0
#                 }
#             },
            
#             data: [
#                    {"name":"第一级1","children":[{"name":"第二级1"},{"name":"第二级2"},{"name":"第二级3"}]}
#                   ]
#         }
#     ]
# };

from math import cos,sin

#假装识别出了一切（想要啥有啥），生成一个图
#我们识别了所有的node及其内容，位置
Node_dic={"string1":[x1,y1],"string2":[x2,y2],"string3":[x3,y3]}
#我们识别了所有的edge及其角度，长度（切割图片对角线的长度），位置
Edge_dic={"E1":[A1,L1,[x1,y1]],"E2":[A2,L2,[x2,y3]]}

mistake = 20

def round(p1,p2,mistake):
    if(abs(p1[0]-p2[0]) < mistake  and abs(p1[1]-p2[1]) < mistake):
        return True
    return False
    


class Node:
    root=None
    def __init__(self,father=None,data=None,children=None):
        self.father=father
        self.data=data
        self.children=children
    def Generate(self,A,inroot):
        self.root.father=None
        self.root.children=A[inroot]
        self.root.data=inroot
        Queue=[]
        Queue += A[inroot]
        
        while Queue.size()!=0:
            temp_name=Queue[0]
            del Queue[0]
            temp = Node(None,temp_name,A[temp_name])
            Queue += A[temp_name]




class MindMapping:
    
    relationship=[]
    R_table={}
    def __init__(self, node_l, edge_l):
        self.node_l = node_l
        self.edge_l = edge_l
    def get_relationship(self):
        for edge in self.edge_l:
            # L=edge[2]
            A=self.edge_l[edge][0]
            L=self.edge_l[edge][1]
            pos=self.edge_l[edge][2]
            start_e = pos + [L*cos(A),L.sin(A)]
            end_e = pos - [L*cos(A),L.sin(A)]
            start,end =[0,0]
            for node in self.node_l:
                # mistake=20
                if(round(self.node_l[node],start_e) and start == [0,0]):
                    start=node
                if(round(self.node_l[node],end_e) and end == [0,0]):
                    end=node
            if(start != [0,0] and end != [0,0]):
                self.relationship.append([start,end])
 
    def get_table(self):
        for N in range(self.node_l):
            self.R_table[N]=[]
            for R in self.relationship:
                if(R[0] == N ):
                    self.R_table[N].append(R[1])
    def get_root(self):
        for N in self.node_l:
            isRoot=True
            for List in self.R_table:
                if N in List:
                    isRoot=False
                if(not(isRoot)):
                    break
            if(isRoot):
                return N

               
    def generate_DS(self):
        root=self.get_root()

        # print "Name : ", self.name,  ", Salary: ", self.salary
