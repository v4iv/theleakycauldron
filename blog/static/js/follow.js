$(document).ready(function(){
var curTop = parseInt($('.follow').css('top'));
$('.follow').fadeIn(1000);
$(window).scroll(function(){
var top = $(window).scrollTop();
$('.follow').css('top', top + curTop);
});
});