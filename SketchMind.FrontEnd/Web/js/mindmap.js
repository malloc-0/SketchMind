import "struct"

var mind = { /* jsMind 数据，详见下一节的说明 */ };

var options = {
    container: 'jsmind_container',
    editable: true,
    theme: 'orange'
};

function loadDefault() {
    mind = MindMap.prototype.get_example_minddata()
    updateMind()
}

function updateMind() {
    var jm = new jsMind(options);
    // 让 jm 显示这个 mind 即可
    jm.show(mind);
}