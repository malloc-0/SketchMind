"use strict";
// struct.ts
export const __esModule = true;
// This file contains basic data structures used in nodes and maps.
// Copyright (c) 2018 "malloc(0)" Group. All rights reserved.
var utils = require("./utils");
var Style;
(function (Style) {
    Style[Style["primary"] = 0] = "primary";
    Style[Style["warning"] = 1] = "warning";
    Style[Style["danger"] = 2] = "danger";
    Style[Style["success"] = 3] = "success";
    Style[Style["info"] = 4] = "info";
    Style[Style["greensea"] = 5] = "greensea";
    Style[Style["nephrite"] = 6] = "nephrite";
    Style[Style["belizehole"] = 7] = "belizehole";
    Style[Style["wisteria"] = 8] = "wisteria";
    Style[Style["asphalt"] = 9] = "asphalt";
    Style[Style["orange"] = 10] = "orange";
    Style[Style["pumpkin"] = 11] = "pumpkin";
    Style[Style["pomegranate"] = 12] = "pomegranate";
    Style[Style["clouds"] = 13] = "clouds";
    Style[Style["asbestos"] = 14] = "asbestos";
})(Style = exports.Style || (exports.Style = {}));
var MapNode = /** @class */ (function () {
    // 是否向右展开。默认为 yes。
    // 目前不想用它
    function MapNode(cont) {
        // 内容。
        this.expand_right = true;
        MapNode.last_id++;
        this.id = MapNode.last_id;
        this.content = cont;
        this.parent_id = -1;
    }
    MapNode.last_id = 0;
    return MapNode;
}());
var MindMap = /** @class */ (function () {
    // 确定整体主题色。
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
        this.nodes[to].parent_id = this.nodes[from].id;
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
        this.nodes[to].parent_id = -1;
    };
    MindMap.prototype.generate_minddata = function () {
        var mind = {
            /* 元数据，定义思维导图的名称、作者、版本等信息 */
            "meta": {
                "name": this.title,
                "author": "malloc(0)",
                "version": utils.VERSION
            },
            /* 数据格式声明 */
            "format": "node_array",
            /* 数据内容 */
            "data": []
        };
        for (var _i = 0, _a = this.nodes; _i < _a.length; _i++) {
            var node = _a[_i];
            if (node.parent_id == -1) {
                // 是根节点。开始往里扔
                mind["data"].push({
                    "id": node.id.toString(),
                    "isroot": true,
                    "topic": node.content
                });
            }
            else {
                mind["data"].push({
                    "id": node.id.toString(),
                    "parentid": node.parent_id.toString(),
                    "topic": node.content
                });
            }
        }
        return mind;
    };
    MindMap.prototype.get_example_minddata = function () {
        return utils.EXAMPLE_MIND;
    };
    return MindMap;
}());
exports.MindMap = MindMap;
