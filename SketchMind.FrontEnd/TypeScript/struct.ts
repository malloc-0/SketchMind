// struct.ts

// This file contains basic data structures used in nodes and maps.

// Copyright (c) 2018 "malloc(0)" Group. All rights reserved.

import * as utils from "./utils";

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

    parent_id: number;
    // 父节点的 id。根节点的 parent_id 设置为 0。

    content: string;
    // 内容。

    expand_right: boolean = true;
    // 是否向右展开。默认为 yes。
    // 目前不想用它

    size: Size;

    constructor (cont: string, size: Size) {
        MapNode.last_id++;
        this.id = MapNode.last_id;
        this.content = cont;
        this.size = size;
        this.parent_id = -1;
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

    accent: Color;
    // 确定整体主题色。

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

        this.nodes[to].parent_id = this.nodes[from].id;
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
        this.nodes[to].parent_id = -1;
    }

    generate_minddata() {
        let mind = {
            /* 元数据，定义思维导图的名称、作者、版本等信息 */
            "meta":{
                "name": this.title,
                "author": "malloc(0)",
                "version": utils.VERSION,
            },
            /* 数据格式声明 */
            "format": "node_array",
            /* 数据内容 */
            "data": []
        };

        for (let node of this.nodes) {
            if (node.parent_id == -1) {
                // 是根节点。开始往里扔
                mind["data"].push({
                    "id": node.id.toString(),
                    "isroot": true,
                    "topic": node.content,
                })
            } else {
                mind["data"].push({
                    "id": node.id.toString(),
                    "parentid": node.parent_id.toString(),
                    "topic": node.content,
                })
            }
        }
        return mind;
    }
}