$(document).ready(
    init()
)

function init(){
    $.ajaxSetup({
        headers : {"X-CSRFToken": $.cookie("csrftoken")}
    });
    $("#b").click(function(e){
            e.preventDefault();
            var data = {"u" : $("#u").val(), "e" : $("#e").val(), "p" : $("#p").val()};
            $.post("/api/signup", data, function(data){
                if (data.return == 0){
                    $.cookie('u', $("#u").val(), {path : "/"});
                    $.cookie('p', $("#p").val(), {path : "/"});
                    location.reload();
                }
                else{
                    alert(data.message);
                }
            });
        }
    );
}