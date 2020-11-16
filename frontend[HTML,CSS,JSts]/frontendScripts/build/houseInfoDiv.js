"use strict";
var houseCard = document.getElementsByClassName("card");
var houseDiv = document.getElementsByClassName("houseInfoDiv");
var i;
for (i = 0; i < houseCard.length; i++) {
    houseCard[i].addEventListener("click", cardClick);
}
function cardClick() {
    houseDiv[0].style.display = "grid";
}
// adding an event listener to the close button of the houseInfoDiv
var closeHouseDiv = document.getElementsByClassName("closeHouseBtn");
closeHouseDiv[0].addEventListener("click", closeTheHouseDiv);
function closeTheHouseDiv() {
    houseDiv[0].style.display = "none";
}
