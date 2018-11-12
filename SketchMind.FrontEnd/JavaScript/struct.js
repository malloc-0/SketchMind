// struct.ts
// This file contains basic data structures used in nodes and maps.
// Copyright (c) 2018 "malloc(0)" Group. All rights reserved.
var Color = /** @class */ (function () {
    function Color(r, g, b) {
        this.r = r;
        this.g = g;
        this.b = b;
    }
    Color.prototype.to_hex = function (i) {
        var s = i.toString(16);
        if (s.length == 1) {
            s = "0" + s;
        }
    };
    Color.prototype.print_hex = function () {
        return "0x" + this.to_hex(this.r) + this.to_hex(this.g) + this.to_hex(this.b);
    };
    return Color;
}());
var Size;
(function (Size) {
    Size[Size["small"] = 0] = "small";
    Size[Size["medium"] = 1] = "medium";
    Size[Size["large"] = 2] = "large";
})(Size || (Size = {}));
;
var MapNode = /** @class */ (function () {
    function MapNode(cont, size) {
        MapNode.last_id++;
        this.id = MapNode.last_id;
        this.content = cont;
        this.size = size;
    }
    MapNode.last_id = 0;
    return MapNode;
}());
var MindMap = /** @class */ (function () {
    // 表示指向关系的邻接矩阵
    function MindMap(title) {
        this.title = title;
        this.node_count = 0;
    }
    MindMap.prototype.add_node = function (node) {
        this.nodes.push(node);
        // 先增加一个 node
        this.node_count++;
        // 增加图的 node count 计数
        for (var i = 0; i < this.adj_mat.length; ++i) {
            this.adj_mat[i].push(0);
            // 给每条边增加一个结点维度
        }
    };
    MindMap.prototype.delete_node = function (id) {
        for (var i = 0; i < this.adj_mat.length; ++i) {
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
    };
    MindMap.prototype.add_connection = function (from, to) {
        var new_mat;
        for (var i = 0; i < this.node_count; ++i) {
            new_mat.push(0);
        }
        // 边矩阵里加入一个全 0 列
        new_mat[from] = -1;
        new_mat[to] = 1;
        // 设置 -1 1 表示指向关系
        this.adj_mat.push(new_mat);
        // 把新的边推入矩阵
    };
    MindMap.prototype.cut_connection = function (from, to) {
        var new_mat;
        for (var i = 0; i < this.node_count; ++i) {
            new_mat.push(0);
        }
        new_mat[from] = -1;
        new_mat[to] = 1;
        // 构造出 connection 的矩阵表示
        for (var i = 0; i < this.adj_mat.length; ++i) {
            if (this.adj_mat[i] == new_mat) {
                this.adj_mat.splice(i);
                // 找到符合条件的就删除整行
            }
        }
    };
    return MindMap;
}());
