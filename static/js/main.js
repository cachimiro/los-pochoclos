function showMore(id) {
   var truncateReviews = document.getElementById(id+"_truncated"); 
  var fullReviews = document.getElementById(id+"_full");
  var show = document.getElementById(id+"_show");
document.getElementById(id+"_show");
 if (truncateReviews.style.display =="block") {
   fullReviews.style.display = "block";
   truncateReviews.style.display = "none";
   show.innerText = "Show Less";
   
    
 } else{
   truncateReviews.style.display ="block"; 
   fullReviews.style.display ="none";
   show.innerText = "show More";
 
 }

 }
 
 function showMores(ids) {
   var truncateReviewss = document.getElementById(ids+"_truncateded"); 
  var fullReviewss = document.getElementById(ids+"_fulls");
  var shows = document.getElementById(ids+"_shows");
document.getElementById(ids+"_show");
 if (truncateReviewss.style.display =="block") {
   fullReviewss.style.display = "block";
   truncateReviewss.style.display = "none";
   shows.innerText = "show less";
   
    
 } else{
   truncateReviewss.style.display ="block"; 
   fullReviewss.style.display ="none";
   shows.innerText = "show More";
 
 }

 }
 
 var video = document.getElementById("myVideo");
var btn = document.getElementById("myBtn");

function myFunction() {
  if (video.paused) {
    video.play();
    btn.innerHTML = "Pause";
  } else {
    video.pause();
    btn.innerHTML = "Play";
  }
}


