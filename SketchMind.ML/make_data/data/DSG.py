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
Node_dic={"输出":[300,300],"物理输出":[200,200],"魔法输出":[400,200],"黑暗游侠":[100,100],"恐怖利刃":[200,100],
          "混沌骑士":[300,100],"莱恩":[400,100],"痛苦女王":[500,100]  }
#我们识别了所有的edge及其角度，长度（切割图片对角线的长度），位置
Edge_dic={"E1":[0.8,70,[250,250]],"E2":[2.4,70,[350,250]],"E3":[0.8,70,[150,150]],"E4":[1.6,70,[200,150]],
"E5":[2.4,70,[250,150]],"E6":[1.6,70,[400,150]],"E7":[2.4,70,[450,150]],
}

mistake = 20
Tree_data_json=""

def round(p1,p2):
    if(abs(p1[0]-p2[0]) < mistake  and abs(p1[1]-p2[1]) < mistake):
        return True
    return False
class MindMapping:
    relationship=[]       #[[A,b],[b,c]]
    R_table={}        #A:[b,c,d]
    root=""
    def __init__(self, node_l, edge_l):
        self.node_l = node_l
        self.edge_l = edge_l
    def generate(self):
        self.get_relationship()
        self.get_table()
        self.get_root()    
    def get_relationship(self):
        for edge in self.edge_l:
            A=self.edge_l[edge][0]
            L=self.edge_l[edge][1]
            pos=self.edge_l[edge][2]
            start_e=[]
            end_e=[]
            start_e.append( pos[0] + L*cos(A))
            start_e.append( pos[1] + L*sin(A))
            end_e.append( pos[0] - L*cos(A))
            end_e.append( pos[1] - L*sin(A))
            start ="None"
            end = "None"
            for node in self.node_l:
                # mistake=20
                if(round(self.node_l[node],start_e) and start == "None"):
                    start=node
                if(round(self.node_l[node],end_e) and end == "None"):
                    end=node
            if(start != [0,0] and end != [0,0]):
                self.relationship.append([start,end])
    def get_table(self):
        for N in self.node_l:
            self.R_table[N]=[]
            for R in self.relationship:
                if(R[0] == N ):
                    self.R_table[N].append(R[1])
    def get_root(self):
        for N in self.node_l:
            isRoot=True
            for List in self.R_table.values():
                if N in List:
                    isRoot=False
                if(not(isRoot)):
                    break
            if(isRoot):
                self.root = N
                return
    def Print(self):
        #找到root                 T
        #深度优先遍历              T
        #把自己的名字打出来           T
        #把{},[]打出来        T
        temp=self.root
        global Tree_data_json
        Tree_data_json=Tree_data_json+"{\"name\":\""+self.root+"\""
        # Tree_data_json=s
        # Tree_data_json=Tree_data_json+"{"
        if(len(self.R_table[self.root])!=0):
            Tree_data_json=Tree_data_json+",\"children\":"
            Tree_data_json=Tree_data_json+"["
            temp_l=self.R_table[self.root]
            for name in temp_l:
                self.root=name
                self.Print()
                if(len(temp_l)>=1):
                    Last=temp_l[len(temp_l)-1]      
                    if name != Last:
                        Tree_data_json+=","
                self.root=temp
            Tree_data_json=Tree_data_json+"]"
            Tree_data_json=Tree_data_json+"}"
        else:
            Tree_data_json+="}"
        return

A=MindMapping(Node_dic,Edge_dic)
A.generate()
A.Print()
json_data="data:[\n                  "+Tree_data_json+"\n]"
json_before='''option = {
    title : {
        text: '冰桶挑战'
    },
    toolbox: {
        show : true,
        feature : {
            mark : {show: true},
            dataView : {show: true, readOnly: false},
            restore : {show: true},
            saveAsImage : {show: true}
        }
    },
    series : [
        {
            name:'树图',
            type:'tree',
            orient: 'horizontal',  // vertical horizontal
            rootLocation: {x: 100,y: 230}, // 根节点位置  {x: 100, y: 'center'}
            nodePadding: 8,
            layerPadding: 200,
            hoverable: false,
            roam: true,
            symbolSize: 6,
            itemStyle: {
                normal: {
                    color: '#4883b4',
                    label: {
                        show: true,
                        position: 'right',
                        formatter: "{b}",
                        textStyle: {
                            color: '#000',
                            fontSize: 5
                        }
                    },
                    lineStyle: {
                        color: '#ccc',
                        type: 'curve' // 'curve'|'broken'|'solid'|'dotted'|'dashed'

                    }
                },
                emphasis: {
                    color: '#4883b4',
                    label: {
                        show: false
                    },
                    borderWidth: 0
                }
            },
            '''
json_after='''
        }
    ]
};'''
final_json=json_before+json_data+json_after        
print (final_json)

       



