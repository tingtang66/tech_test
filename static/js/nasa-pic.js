var current_date = $("#selector option:first").val()
$.ajax({
	type: "POST",
	url: "nasa",
	data: { date: current_date }
}).done(function(data){
	$("#daily").append("<img id='pic' src='"+ data +"'style='max-height:150%; max-width:150%'>")
})
$("#selector").change(function(){
	var changed_date = $("#selector option:selected").text()
	$.ajax({
	    type: "POST",
	    url: "nasa",
	    data: { date: current_date }
    }).done(function(data){
    	$("#pic").remove()
	    $("#daily").append("<img id='pic' src='"+ data +"'style='max-height:150%; max-width:150%'>")
    })
})