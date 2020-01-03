function showMore(id) {
   var truncateReviews = document.getElementsById("{{ opinion._id }}_truncated");
  var fullReviews = document.getElementById("{{ opinion._id }}_full");
document.getElementById("{{ opinion._id}}_show").click();
 if (truncateReviews.style.display == "block") {
   fullReviews.style.display == "none";
    
 } else if ( fullReviews.style.display == "block"){
   truncateReviews.style.display =="none";  
 
 } else {
  truncateReviews.style.display == "block";
 
}

 }