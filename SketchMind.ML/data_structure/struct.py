#!/usr/bin/env python

import const
import json


class MapNode:

    id = 0
    # 每个节点的 id。

    parent_id = 0
    # 父节点的 id。根节点的 parent_id 设置为 0。

    content = ""
    # 内容。

    expand_right = True
    # 是否向右展开。默认为 yes。
    # 目前不想用它

    def __init__(self, content):
        const.last_id += 1
        self.id = const.last_id
        self.content = content
        self.parent_id = -1
    # 构造器。传入节点的内容


class MindMap:
    title = ""
    # 图的标题

    nodes = []
    # 结点数组

    node_count = 0
    # 结点计数器

    adj_mat: [[]]
    # 表示指向关系的邻接矩阵

    def __init__(self, title):
        self.title = title
        self.node_count = 0

    def add_node(self, node):
        self.nodes.append(node)
        # 先增加一个 node

        self.node_count += 1
        # 增加图的 node count 计数

        for i in self.adj_mat:
            i.append(0)

    def delete_node(self, id):
        for i in self.adj_mat:
            if i[id] != 0:
                self.adj_mat.remove(i)
            else:
                i.remove(i[id])
                # 如果这条边和所要删除的点没关系
                # 就只从边矩阵中删除点的维度
        self.nodes[id] = None
        # 清空 nodes 数组中的元素，但保留其索引位置

    def add_connection(self, from_where, to_where):
        new_mat = []
        for i in self.nodes:
            new_mat.push(0)
        # 边矩阵里加入一个全 0 列

        new_mat[from_where] = -1
        new_mat[to_where] = 1
        # 设置 - 1 1 表示指向关系

        self.adj_mat.append(new_mat)
        # 把新的边推入矩阵

        self.nodes[to].parent_id = self.nodes[from].id

    def cut_connection(self, from_where, to_where) {
        new_mat = []
        for i in self.nodes:
            new_mat.push(0)

        new_mat[from_where] = -1
        new_mat[to_where] = 1
        # 构造出 connection 的矩阵表示

        for i in self.adj_mat
            if (self.adj_mat[i] == new_mat):
                self.adj_mat.remove(i)

        self.nodes[to].parent_id = -1

        def generate_minddata():
        mind = {
            # 元数据，定义思维导图的名称、作者、版本等信息
            "meta": {
                "name": this.title,
                "author": "malloc(0)",
                "version": utils.VERSION,
            },
            # 数据格式声明
            "format": "node_array",
            # 数据内容
            "data": []
        }

        for node in this.nodes:
            if (node.parent_id == -1):
                # 是根节点。开始往里扔
                mind["data"].append({
                    "id": str(node.id),
                    "isroot": true,
                    "topic": node.content,
                })
            else:
                # 不是根节点。要设置爹
                mind["data"].push({
                    "id": str(node.id),
                    "parentid": str(node.parent_id),
                    "topic": node.content,
                })

        return json.dump(mind)

        def get_example_minddata(self):
            return const.EXAMPLE_MIND
