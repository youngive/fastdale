$("form").submit(function(e){
    e.preventDefault();

	$.post("/api/external/cabinet/handler", $("form").serialize(), function(data){
       $(".message").html(data);
	});
});