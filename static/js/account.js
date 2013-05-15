$(document).ready(function(){
        init();
    }
)

function init(){
    $.ajaxSetup({
        headers : {"X-CSRFToken": $.cookie("csrftoken")}
    });
    $("#button-add-fav").click(function(e){
        e.preventDefault();
        var data = {"u" : $.cookie("u"), "p" : $.cookie("p"), "url" : $("#url-add-fav").val()};
        $.post("/api/favorite/add", data, function(data){
            if (data.return == 0){
                location.reload();
            }
        });
    });
    if ($("#button-follow").text().trim() == "unfollow"){
        $("#button-follow").addClass("disabled");
//        $("#button-follow").attr("disabled", "disabled");
    }
    else{
        $("#button-follow").click(function(e){
            e.preventDefault();
            var data = {"u" : $.cookie("u"), "p" : $.cookie("p"), "target" : $("#username").text()};
            $.post("/api/relation/follow", data, function(data){
                if (data.return == 0){
                    location.reload();
                }
            });
        });
    }
    $("#favorite ul li i").click(function(){
        var a = $(this).parent().children('a');
        var data = {"u" : $.cookie("u"), "p" : $.cookie("p"), "url" : a.attr('href')};
        $.post("/api/favorite/del", data, function(data){
            if (data.return == 0){
                location.reload();
//                a.parent().hide();
            }
            else{
                alert(data.message);
            }
        });
    });
    $("#favorite ul li i").hover(function(){
        var a = $(this).parent().children('a');
        a.css('text-decoration', 'line-through');
    },
    function(){
        var a = $(this).parent().children('a');
        a.css('text-decoration', '');
    });
}