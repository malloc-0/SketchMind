// struct.ts

// This file contains basic data structures used in nodes and maps.

// Copyright (c) 2018 "malloc(0)" Group. All rights reserved.

class Color {
    r: number;
    g: number;
    b: number;

    constructor(r: number, g: number, b: number) {
        this.r = r;
        this.g = g;
        this.b = b;
    }

    to_hex(i: number) {
        let s = i.toString(16);
        if (s.length == 1) {
            s = "0" + s;
        }
    }

    print_hex() {
        return "0x" + this.to_hex(this.r) + this.to_hex(this.g) + this.to_hex(this.b); 
    }
}

enum Size { small, medium, large };

class MapNode {
    static last_id: number = 0;
    // 静态类型变量，用来给出唯一的全局递增 id。

    id: number;
    // 每个节点的 id。

    content: [string];
    // 内容。多点内容以数组形式存储。

    color: Color;
    // 这一块儿的颜色

    size: Size;

    constructor (cont: [string], size: Size) {
        MapNode.last_id++;
        this.id = MapNode.last_id;
        this.content = cont;
        this.size = size;
    }
    // 构造器。传入节点的内容（数组形式）
}


class MindMap {

    title: string;
    // 图的标题

    nodes: [MapNode];
    // 结点数组

    node_count: number;
    // 结点计数器

    adj_mat: Array<Array<number>>;
    // 表示指向关系的邻接矩阵

    constructor(title: string) {
        this.title = title;
        this.node_count = 0;
    }

    add_node(node: MapNode) {
        this.nodes.push(node);
        // 先增加一个 node
        this.node_count++;
        // 增加图的 node count 计数
        for (let i: number = 0; i < this.adj_mat.length; ++i) {
            this.adj_mat[i].push(0);
            // 给每条边增加一个结点维度
        }
    }

    delete_node(id: number) {
        for (let i: number = 0; i < this.adj_mat.length; ++i) {
            // 遍历所有边
            if (this.adj_mat[i][id] != 0) {
                // 如果这条边和所要删除的点有交集（!= 0）
                this.adj_mat.splice(i);
                // 就从边矩阵里删掉此边
                break;
            }
            this.adj_mat[i].splice(id);
            // 如果这条边和所要删除的点没关系
            // 就只从边矩阵中删除点的维度
        }
        this.nodes[id] = undefined;
        // 清空 nodes 数组中的元素，但保留其索引位置
    }
    
    add_connection(from: number, to: number) {
        let new_mat: [number];
        for(let i = 0; i < this.node_count; ++i) {
            new_mat.push(0);
        }
        // 边矩阵里加入一个全 0 列

        new_mat[from] = -1;
        new_mat[to] = 1;
        // 设置 -1 1 表示指向关系

        this.adj_mat.push(new_mat);
        // 把新的边推入矩阵
    }

    cut_connection(from: number, to: number) {
        let new_mat: [number];
        for(let i = 0; i < this.node_count; ++i) {
            new_mat.push(0);
        }
        new_mat[from] = -1;
        new_mat[to] = 1;
        // 构造出 connection 的矩阵表示

        for (let i = 0; i < this.adj_mat.length; ++i) {
            if (this.adj_mat[i] == new_mat) {
                this.adj_mat.splice(i)
                // 找到符合条件的就删除整行
            }
        }
    }
}

