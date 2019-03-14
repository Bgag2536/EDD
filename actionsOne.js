window.onload = runPythonOne();

function runPythonOne(){
    $(document).ready(function(){
        $('#openOne').click(function(){
            var a = new XMLHttpRequest();
            a.open("GET", "OpeningRackOne");
            a.onreadystatechange=function(){
                    if (a.readyState == 4){
                        if (a.status == 200){
                            alert("SUCCESS")
                        } 
                        else if (a.status == 404){
                            alert("you fucked up")
                        }
                        else alert("HTTP ERROR")
                    }
            }
            a.send();
        });
    });
}