
/* Admin */
$('.cancle_button').click(function() {
   window.location = '/admin/';
});


function gotoOutLink(url){
	window.open(url, "_blank");
}

function gotoLink(url){
	document.location.href = url;
}


/* Main page search form */
$(document).ready(function(){ 
	$('#gosearch').click(function(){
		if ($('#searchterm').val()==""){
			alert("Please, insert search term.");
		}else{
			// document.location.href =$('#searchurl').val() + $('#searchterm').val();
			document.location.href ='/main/query_manager/?q=' + $('#searchterm').val();
		}
	})

	$("#searchterm").keydown(function (e) {
		if (e.keyCode == 13) {
			$('input[name = butAssignProd]').click();
			// document.location.href =$('#searchurl').val() + $('#searchterm').val();
			document.location.href ='/main/query_manager/?q=' + $('#searchterm').val();
			
		}
	});


	$(function() {
		function log( message ) {
		  $( "<div>" ).text( message ).prependTo( "#log" );
		  $( "#log" ).scrollTop( 0 );
		}

		$( "#searchterm" ).autocomplete({
		  source: function( request, response ) {
			$.ajax({
				type: "GET",
				url: "/main/autocomplete",
				dataType: "json",
				data: {
					/*csrfmiddlewaretoken: "{{ csrf_token }}",*/
					maxRows: 12,
					term: request.term
				},
			error:function(){alert("Sorry, Search error, Please contact administrator.");},
			  success: function( data ) {
				response( $.map( data.genenames, function( item ) {
				  return {
					label: item.gene, value: item.gene
				  }
				}));
			  }
			});
		  },
		  minLength: 1,
		  select: function( event, ui ) {
			  /*
			log( ui.item ?
			  "Selected: " + ui.item.label :
			  "Nothing selected, input was " + this.value);
			  */
		  },
		  open: function() {
			$( this ).removeClass( "ui-corner-all" ).addClass( "ui-corner-top" );
		  },
		  close: function() {
			$( this ).removeClass( "ui-corner-top" ).addClass( "ui-corner-all" );
		  }
		});
	});
})


