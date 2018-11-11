
class MindMap {

    title: string;

    map: Map<number, MapNode>;

    add_node(node: MapNode) {
        this.map[node.id] = node
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

