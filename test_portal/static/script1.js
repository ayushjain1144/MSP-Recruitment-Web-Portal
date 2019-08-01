function loadFunction() {
    
    var start_time;
    if (window.sessionStorage.getItem("start_time") === null) {
        var start_time_str = document.getElementById("start_time").value;
        //TODO : parse the Django based "Y n j H i s" datetime to JS Date
        window.sessionStorage.setItem("start_time", start_time);
    }
    else {
        start_time_str = window.sessionStorage.getItem("start_time");
        start_time = new Date(start_time_str);
    }
    
    var qnum = document.getElementById("qnum").innerHTML;
    var count_q = document.getElementById("qnum-count").innerHTML;
    var round = "1";
           
    if (window.sessionStorage.getItem("round") === null) {
        window.sessionStorage.setItem("count_1", count_q);
        window.sessionStorage.setItem("round", round);
    }
    else if (window.sessionStorage.getItem("round") == "2" && window.sessionStorage.getItem("count_2") === null) {
            window.sessionStorage.setItem("count_2", count_q);
    }

    round = window.sessionStorage.getItem("round");
    
    if (document.getElementById("hidden_round").value != round) {
        document.getElementsByName("Finish")[0].click();
    }
    
    if (qnum <= 1) {
        document.getElementsByClassName("nav-arrow")[0].getElementsByTagName("button")[0].disabled = true;
    }
    if (qnum >= count_q) {
        document.getElementsByClassName("nav-arrow")[1].getElementsByTagName("button")[0].disabled = true;
    }
    
    /*
    0 - (Yet to attempt) Default
    1 - (Attempted) Success
    2 - (Not Attempted) Danger
    3 - (Current Question) Info
    */

    if (window.sessionStorage.getItem("btnMapping") === null) {
        btnMapping = ["btn-default", "btn-success", "btn-danger", "btn-info"];
        window.sessionStorage.setItem("btnMapping", JSON.stringify(btnMapping));
    }
    if (window.sessionStorage.getItem("btnStatus_" + round) === null) {
        btnStatus = new Array(count_q);
        for (var i = 0; i < btnStatus.length; ++i) {
            btnStatus[i] = Number(0);
        }
        window.sessionStorage.setItem("btnStatus_" + round, JSON.stringify(btnStatus));
    }
    btnStatus = JSON.parse(window.sessionStorage.getItem("btnStatus_" + round));
    btnStatus[qnum-1] = 3;
    window.sessionStorage.setItem("btnStatus_" + round, JSON.stringify(btnStatus));
    
    btnMapping = JSON.parse(window.sessionStorage.getItem("btnMapping"));
    var element = document.getElementById("button-set").getElementsByTagName("button");
    for (var i = 0; i < btnStatus.length; ++i) {
        element[i].className = "btn ";
        element[i].className += btnMapping[btnStatus[i]];
    }
    
    //TODO
    start_timer();

}

function start_timer() {
    //TODO   
}

function proceedRound2() {            
    btnClickMCQ();
    window.sessionStorage.setItem("round", "2");
}

function goBackRound1() {
    btnClickDes();
    window.sessionStorage.setItem("round", "1");
}

function finishTest() {
    var conf;
    round = window.sessionStorage.getItem("round");    
    if (document.getElementById("hidden_round").value != round) {
        conf = true;
        alert("You have already completed the test!");
    }
    else {
        conf = confirm("Are you sure you want to finish the test? You cannot return back!");
        if (conf == true) {        
            btnClickDes();
            window.sessionStorage.setItem("round", "3");
        }
    }
    return conf; 
}

function btnClickDes() {
    var qnum = document.getElementById("qnum").innerHTML;
    
    /*
    0 - (Yet to attempt) Default
    1 - (Attempted) Success
    2 - (Not Attempted) Danger
    3 - (Current Question) Info
    */

    btnStatus = JSON.parse(window.sessionStorage.getItem("btnStatus_2"));
    btnMapping = JSON.parse(window.sessionStorage.getItem("btnMapping"));
    textarea = document.getElementById("comment");

    var element = document.getElementById("button-set").getElementsByTagName("button");
    element[qnum-1].className = "btn ";
    if (textarea.value.trim() == "") {
        element[qnum-1].className += btnMapping[2];
        btnStatus[qnum-1] = 2;
    }
    else {
        element[qnum-1].className += btnMapping[1];
        btnStatus[qnum-1] = 1;
    }

    window.sessionStorage.setItem("btnStatus_2", JSON.stringify(btnStatus));
    window.sessionStorage.setItem("btnMapping", JSON.stringify(btnMapping));
}

function btnClickMCQ() {
    var qnum = document.getElementById("qnum").innerHTML;
    
    /*
    0 - (Yet to attempt) Default
    1 - (Attempted) Success
    2 - (Not Attempted) Danger
    3 - (Current Question) Info
    */

    btnStatus = JSON.parse(window.sessionStorage.getItem("btnStatus_1"));
    btnMapping = JSON.parse(window.sessionStorage.getItem("btnMapping"));

    var btnSelected = false;
    
    var b1 = (document.getElementById("id_response1").checked == true);
    var b2 = (document.getElementById("id_response2").checked == true);
    var b3 = (document.getElementById("id_response3").checked == true);
    var b4 = (document.getElementById("id_response4").checked == true);
    if (b1 || b2 || b3 || b4) {
        btnSelected = true;
    }

    var element = document.getElementById("button-set").getElementsByTagName("button");
    element[qnum-1].className = "btn ";
    if (btnSelected) {
        element[qnum-1].className += btnMapping[1];
        btnStatus[qnum-1] = 1;
    }
    else {
        element[qnum-1].className += btnMapping[2];
        btnStatus[qnum-1] = 2;
    }

    window.sessionStorage.setItem("btnStatus_1", JSON.stringify(btnStatus));
    window.sessionStorage.setItem("btnMapping", JSON.stringify(btnMapping));
}

window.onload = loadFunction;
