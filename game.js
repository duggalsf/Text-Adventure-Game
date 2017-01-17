/**
 * Created by Shelly on 1/16/17.
 */

var inventory,
    answer = $("#answer".value);

function start(){
    $("#story").html("You are on the road with the ruined city behind you. You really need to find a car, preferably something electric that can take you the 200 miles to your family. There is an intersection ahead.");
    $("#question").html("Do you go straight, right, or left?").addClass("start");
}

$("#submit").on("click", function(answer){
   switch(answer) {
       case $("#question").hasClass("start"):

   }
});