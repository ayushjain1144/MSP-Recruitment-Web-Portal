var timer = null;

function loadFunction() {
    
    if (window.localStorage.getItem("sec_rem") === null) {
        var start_time_str = document.getElementById("start_time").value + " GMT+0530 (India Standard Time)"; // Hardcoding it to be for India only. Can change later.        
        var start_time = Math.floor(Date.parse(start_time_str) / 1000);
        var curr_time_str = document.getElementById("curr_time").value + " GMT+0530 (India Standard Time)"; // Hardcoding it to be for India only. Can change later.
        var curr_time = Math.floor(Date.parse(curr_time_str) / 1000);
        window.localStorage.setItem("sec_rem", 3600 - (curr_time - start_time));   // Hardcoding it for 1 hour
    }
    
    var qnum = document.getElementById("qnum").innerHTML;
    var count_q = document.getElementById("qnum-count").innerHTML;
    var round = "1";
           
    if (window.localStorage.getItem("round") === null) {
        window.localStorage.setItem("count_1", count_q);
        window.localStorage.setItem("round", round);
    }
    else if (window.localStorage.getItem("round") == "2" && window.localStorage.getItem("count_2") === null) {
            window.localStorage.setItem("count_2", count_q);
    }

    round = window.localStorage.getItem("round");
    
    if (document.getElementById("hidden_round").value != round) {
        document.getElementsByName("Finish")[0].click();
    }
    
    if (qnum <= 1) {
        var element = document.getElementsByClassName("nav-arrow")[0].getElementsByTagName("button")[0];
        element.disabled = true;
        element.style.visibility = "hidden";
    }
    if (qnum >= count_q) {
        var element = document.getElementsByClassName("nav-arrow")[1].getElementsByTagName("button")[0];
        element.disabled = true;
        element.style.visibility = "hidden";
    }
    
    /*
    0 - (Yet to attempt) Default
    1 - (Attempted) Success
    2 - (Not Attempted) Danger
    3 - (Current Question) Info
    */

    if (window.localStorage.getItem("btnMapping") === null) {
        btnMapping = ["btn-default", "btn-success", "btn-danger", "btn-info"];
        window.localStorage.setItem("btnMapping", JSON.stringify(btnMapping));
    }
    if (window.localStorage.getItem("btnStatus_" + round) === null) {
        btnStatus = new Array(count_q);
        for (var i = 0; i < btnStatus.length; ++i) {
            btnStatus[i] = Number(0);
        }
        window.localStorage.setItem("btnStatus_" + round, JSON.stringify(btnStatus));
    }
    btnStatus = JSON.parse(window.localStorage.getItem("btnStatus_" + round));
    btnStatus[qnum-1] = 3;
    window.localStorage.setItem("btnStatus_" + round, JSON.stringify(btnStatus));
    
    btnMapping = JSON.parse(window.localStorage.getItem("btnMapping"));
    var element = document.getElementById("button-set").getElementsByTagName("button");
    for (var i = 0; i < btnStatus.length; ++i) {
        element[i].className = "btn ";
        element[i].className += btnMapping[btnStatus[i]];
    }
    
    start_timer();

}

function start_timer() {
    timer = setInterval(timer_helper, 1000);
}

function timer_helper() {
    var sec_rem = parseInt(window.localStorage.getItem("sec_rem"));
    --sec_rem;
    var mins = Math.floor(sec_rem / 60);
    var secs = sec_rem % 60;
    var mins_str = mins, secs_str = secs;
    if(mins < 10){
        mins_str = "0" + mins;
    }
    if(secs < 10){
        secs_str = "0" + secs;
    }    
    document.getElementById("timer-mins").innerHTML = mins_str;
    document.getElementById("timer-secs").innerHTML = secs_str;
    window.localStorage.setItem("sec_rem", sec_rem);
    if (sec_rem <= 0) {
        clearInterval(timer);
        document.getElementsByName("Finish")[0].click();   
    }
}

function proceedRound2() {            
    btnClickMCQ();
    window.localStorage.setItem("round", "2");
}

function goBackRound1() {
    btnClickDes();
    window.localStorage.setItem("round", "1");
}

function finishTest() {
    var conf;
    var round = window.localStorage.getItem("round");
    var sec_rem = parseInt(window.localStorage.getItem("sec_rem"));
    if (sec_rem <= 1) {
        conf = true;   
    }
    else if (document.getElementById("hidden_round").value != round) {
        conf = true;
        alert("You have already completed the test!");
    }
    else {
        conf = confirm("Are you sure you want to finish the test? You cannot return back!");
        if (conf == true) {        
            btnClickDes();
            window.localStorage.setItem("round", "3");
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

    btnStatus = JSON.parse(window.localStorage.getItem("btnStatus_2"));
    btnMapping = JSON.parse(window.localStorage.getItem("btnMapping"));
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

    window.localStorage.setItem("btnStatus_2", JSON.stringify(btnStatus));
    window.localStorage.setItem("btnMapping", JSON.stringify(btnMapping));
}

function btnClickMCQ() {
    var qnum = document.getElementById("qnum").innerHTML;
    
    /*
    0 - (Yet to attempt) Default
    1 - (Attempted) Success
    2 - (Not Attempted) Danger
    3 - (Current Question) Info
    */

    btnStatus = JSON.parse(window.localStorage.getItem("btnStatus_1"));
    btnMapping = JSON.parse(window.localStorage.getItem("btnMapping"));

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

    window.localStorage.setItem("btnStatus_1", JSON.stringify(btnStatus));
    window.localStorage.setItem("btnMapping", JSON.stringify(btnMapping));
}

window.onload = loadFunction;
