
function onStartFrameLoad() {
    document.getElementById("frame0").height = 0;
    document.getElementById("frame0").height = document.getElementById("frame0").contentWindow.document.body.scrollHeight;
    console.log("start frame to " + document.getElementById("frame0").height);
}

function onEditFrameLoad() {
    let element = document.getElementById("frame1");

    console.log("edit frame to " + document.getElementById("frame1").height);
}

function onAboutFrameLoad() {
    document.getElementById("frame2").height = 0;
    document.getElementById("frame2").height = document.getElementById("frame2").contentWindow.document.body.scrollHeight;
    console.log("about frame to " + document.getElementById("frame2").height);
}


function switchTab(id) {
    for (let i=0; i<3; i++)
    {
        document.getElementById("tab"+i).style.display="none";
    }
    document.getElementById("tab"+id).style.display="block";
    switch (id) {
        case 0:
            onStartFrameLoad();
            break;
        case 1:
            onEditFrameLoad();
            break;
        case 2:
            onAboutFrameLoad();
            break;
    }
}
