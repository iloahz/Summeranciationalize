$(document).ready(
    init()
)

function init(){
    $.ajaxSetup({
        headers : {"X-CSRFToken": $.cookie("csrftoken")}
    });
    $("#b").click(function(e){
            e.preventDefault();
            var data = {"u" : $("#u").val(), "p" : $("#p").val()};
            $.post("/api/signin", data, function(data){
                if (data.return == 0){
                    $.cookie("u", $("#u").val(), {expires: 30, path: "/"});
                    $.cookie("p", $("#p").val(), {expires: 30, path: "/"});
                    location.reload();
                }
                else{
                    alert(data.message);
                }
            });
        }
    );
}