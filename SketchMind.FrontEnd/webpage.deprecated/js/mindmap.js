
var mind = {
    /* 元数据，定义思维导图的名称、作者、版本等信息 */
    "meta": {
        "name": "Example",
        "author": "malloc(0)",
        "version": "0.1.0"
    },
    /* 数据格式声明 */
    "format": "node_array",
    /* 数据内容 */
    "data": [
        { "id": "1", "isroot": true, "topic": "Microsoft" },
        { "id": "2", "parentid": "1", "topic": "Windows", "direction": "left" },
        { "id": "3", "parentid": "1", "topic": "Office" },
        { "id": "4", "parentid": "1", "topic": "Visual Studio" },
        { "id": "5", "parentid": "1", "topic": "Visual Studio Code" },
        { "id": "6", "parentid": "1", "topic": "Xbox" },
        { "id": "7", "isroot": true, "topic": "Apple", "expanded": false, "direction": "right" },
        { "id": "8", "parentid": "7", "topic": "macOS" },
        { "id": "9", "parentid": "7", "topic": "iOS" },
        { "id": "10", "parentid": "7", "topic": "tvOS", "direction": "right" },
        { "id": "11", "parentid": "7", "topic": "watchOS" },
    ]
};

var options = {
    container: 'jsmind_container',
    editable: true,
    theme: 'orange'
};


function init_Mind() {
    let jm = new jsMind(options);
    jm.show(mind);
}