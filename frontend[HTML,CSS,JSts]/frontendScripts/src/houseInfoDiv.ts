var houseCard=document.getElementsByClassName("card")
let houseDiv=document.getElementsByClassName("houseInfoDiv")

let i:number

for (i=0;i<houseCard.length;i++){
    houseCard[i].addEventListener("click",cardClick)

}

function cardClick(){

    houseDiv[0].style.display="grid"
}

// adding an event listener to the close button of the houseInfoDiv

let closeHouseDiv=document.getElementsByClassName("closeHouseBtn")
closeHouseDiv[0].addEventListener("click",closeTheHouseDiv)
function closeTheHouseDiv(){

    houseDiv[0].style.display="none"
}
