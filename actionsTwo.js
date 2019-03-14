window.onload = runPythonTwo();

function runPythonTwo(){
    $(document).ready(function(){
        $('#openOne').click(function(){
            var a = new XMLHttpRequest();
            a.open("GET", "OpeningRackTwo");
            a.onreadystatechange=function(){
                    if (a.readyState == 4){
                        if (a.status == 200){
                            alert("SUCCESS")
                        } 
                        else if (a.status == 404){
                            alert("you goofed up")
                        }
                        else alert("HTTP ERROR")
                    }
            }
            a.send();
        });
    });
}