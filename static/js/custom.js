$('#nasa').click(function(){
  var nasaAPI = "https://api.nasa.gov/planetary/apod"
  $.ajax({
    method: "GET",
    url: nasaAPI,
    data: { api_key: "DEMO_KEY" }
  }).done(function(data) {
    $.ajax({
      method: "POST",
      url: "/images",
      data: data
    })
  })
})
