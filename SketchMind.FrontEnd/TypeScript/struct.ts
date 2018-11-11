
class MindMap {
    title: string;
    nodes: [MapNode];

    node_count: number;

    adj_mat: Array<Array<number>>;

    constructor(title: string) {
        this.title = title;
        this.node_count = 0;
    }

    add_node(node: MapNode) {
        this.nodes.push(node);
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

    cut_connection(from: number, to: number) {
        let new_mat: [number];
        for(let i = 0; i < this.node_count; ++i) {
            new_mat.push(0);
        }
        new_mat[from] = -1;
        new_mat[to] = 1;
        for (let i = 0; i < this.adj_mat.length; ++i) {
            if (this.adj_mat[i] == new_mat) {
                this.adj_mat.splice(i)
            }
        }
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

