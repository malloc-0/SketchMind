
class MindMap {
    title: string;
    map: Map<number, MapNode>;

    node_count: number;

    adj_mat: Array<Array<number>>;

    constructor(title: string) {
        this.title = title;
        this.node_count = 0;
    }

    add_node(node: MapNode) {
        this.map[node.id] = node
        this.node_count++;
        for (let i: number = 0; i < this.adj_mat.length; ++i) {
            this.adj_mat[i].push(0);
        }
    }
    
    add_connection(from: number, to: number) {
        let new_mat: [number];
        for(let i = 0; i < this.node_count; ++i) {
            new_mat.push(0);
        }
        new_mat[from] = -1;
        new_mat[to] = 1;
        this.adj_mat.push(new_mat);
    }
}

class MapNode {
    static last_id: number = 0;
    id: number;
    content: string;

    constructor (cont: string) {
        MapNode.last_id++;
        this.id = MapNode.last_id;
        this.content = cont;
    }
}

