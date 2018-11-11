var MindMap = /** @class */ (function () {
    function MindMap(title) {
        this.title = title;
        this.node_count = 0;
    }
    MindMap.prototype.add_node = function (node) {
        this.nodes.push(node);
        this.node_count++;
        for (var i = 0; i < this.adj_mat.length; ++i) {
            this.adj_mat[i].push(0);
        }
    };
    MindMap.prototype.add_connection = function (from, to) {
        var new_mat;
        for (var i = 0; i < this.node_count; ++i) {
            new_mat.push(0);
        }
        new_mat[from] = -1;
        new_mat[to] = 1;
        this.adj_mat.push(new_mat);
    };
    MindMap.prototype.cut_connection = function (from, to) {
        var new_mat;
        for (var i = 0; i < this.node_count; ++i) {
            new_mat.push(0);
        }
        new_mat[from] = -1;
        new_mat[to] = 1;
        for (var i = 0; i < this.adj_mat.length; ++i) {
            if (this.adj_mat[i] == new_mat) {
                this.adj_mat.splice(i);
            }
        }
    };
    return MindMap;
}());
var MapNode = /** @class */ (function () {
    function MapNode(cont) {
        MapNode.last_id++;
        this.id = MapNode.last_id;
        this.content = cont;
    }
    MapNode.last_id = 0;
    return MapNode;
}());
