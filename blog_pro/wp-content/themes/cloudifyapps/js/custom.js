$(document).ready(function () {

    // Navigation scrolls
    $(".navbar-nav li a").on('click', function(event) {
        $('.navbar-nav li').removeClass('active');
        $(this).closest('li').addClass('active');
        var $anchor = $(this);
        var nav = $($anchor.attr('href'));
        if (nav.length) {
        $('html, body').stop().animate({				
            scrollTop: $($anchor.attr('href')).offset().top				
        }, 1500, 'easeInOutExpo');
        
        event.preventDefault();
        }
    });
    
    // Add smooth scrolling to all links in navbar
    $("a.mouse-hover, a.get-quote").on('click', function(event) {
      var hash = this.hash;
      if( hash ) {
        event.preventDefault();
        $('html, body').animate({
            scrollTop: $(hash).offset().top
        }, 1500, 'easeInOutExpo');
      }
    });


     $("#course-search-box").on('keyup', function(event) {
			var input, filter, ul, li, a, i;
			input = document.getElementById("course-search-box");
			filter = input.value.toUpperCase();
			coursediv = document.getElementById("course-div");
			courseitem = coursediv.getElementsByClassName("course-item");
			for (i = 0; i < courseitem.length; i++) {
				a = courseitem[i].getElementsByTagName("h4")[0];
				if (a.innerHTML.toUpperCase().indexOf(filter) > -1) {
					courseitem[i].style.display = "";
				} else {
					courseitem[i].style.display = "none";

				}
			}
		});


	function toggleIcon(e) {
        $(e.target)
            .prev('.panel-heading')
            .find(".more-less")
            .toggleClass('glyphicon-plus glyphicon-minus');
    }
    $('.panel-group').on('hidden.bs.collapse', toggleIcon);
    $('.panel-group').on('shown.bs.collapse', toggleIcon);




    //Check to see if the window is top if not then display button
	$(window).scroll(function(){
		if ($(this).scrollTop() > 100) {
			$('.scrollToTop').fadeIn();
		} else {
			$('.scrollToTop').fadeOut();
		}
	});

	//Click event to scroll to top
	$('.scrollToTop').click(function(){
		$('html, body').animate({scrollTop : 0},800);
		return false;
	});


	/* Type-1 */
$('#myCarousel').carousel({
  interval: 4000
})

$('.carousel .item').each(function(){
  var next = $(this).next();
  if (!next.length) {
    next = $(this).siblings(':first');
  }
  next.children(':first-child').clone().appendTo($(this));

  for (var i=0;i<2;i++) {
    next=next.next();
    if (!next.length) {
    	next = $(this).siblings(':first');
  	}

    next.children(':first-child').clone().appendTo($(this));
  }
});

$(".tabs li").on("click", function(){
    $("html,body").animate({scrollTop:0},"slow");
});





/////  next-prev for materials

$("#btnNext").on("click",function(){

var currIndex = $(".tab-pane.active.text-style").index();
var nextIndex = currIndex + 1;

if(currIndex==0){
$("#btnPrev").attr('disabled','disabled');
}else{
$("#btnPrev").removeAttr('disabled');
}

var tabLen = $(".tab-pane.text-style").length;

if((tabLen-1) == nextIndex){
$("#btnNext").attr('disabled','disabled');
}

$(".tab-pane.text-style").removeClass("active");
$(".tab-pane.text-style").eq(nextIndex).addClass("active");
$("html,body").animate({scrollTop:0},"slow");

});


$("#btnPrev").on("click",function(){

var currIndex = $(".tab-pane.active.text-style").index();
var prevIndex = currIndex - 1;

var tabLen = $(".tab-pane.text-style").length;


$(".tab-pane.text-style").removeClass("active");
$(".tab-pane.text-style").eq(prevIndex).addClass("active");
$("html,body").animate({scrollTop:0},"slow");

});




// get the content of the editor

$("#txtEditor").Editor();





}); //end of document.ready()


filterSelection("all")
function filterSelection(c) {
  var x, i;
  x = document.getElementsByClassName("filterDiv");
  if (c == "all") c = "";
  for (i = 0; i < x.length; i++) {
    w3RemoveClass(x[i], "show");
    if (x[i].className.indexOf(c) > -1) w3AddClass(x[i], "show");
  }
}

function w3AddClass(element, name) {
  var i, arr1, arr2;
  arr1 = element.className.split(" ");
  arr2 = name.split(" ");
  for (i = 0; i < arr2.length; i++) {
    if (arr1.indexOf(arr2[i]) == -1) {element.className += " " + arr2[i];}
  }
}

function w3RemoveClass(element, name) {
  var i, arr1, arr2;
  arr1 = element.className.split(" ");
  arr2 = name.split(" ");
  for (i = 0; i < arr2.length; i++) {
    while (arr1.indexOf(arr2[i]) > -1) {
      arr1.splice(arr1.indexOf(arr2[i]), 1);
    }
  }
  element.className = arr1.join(" ");
}

