/* Artist Scroll Animation */

const artistCards = document.querySelectorAll(".artist-card");

function revealArtists(){

artistCards.forEach(card => {

const cardTop = card.getBoundingClientRect().top;

if(cardTop < window.innerHeight - 100){

card.classList.add("show");

}

});

}

window.addEventListener("scroll", revealArtists);

revealArtists();



/* Artist Search */

const artistSearch = document.getElementById("artistSearch");

if(artistSearch){

artistSearch.addEventListener("keyup", function(){

let filter = artistSearch.value.toLowerCase();

artistCards.forEach(card => {

let name = card.querySelector(".artist-name").textContent.toLowerCase();

if(name.includes(filter)){

card.style.display = "block";

}else{

card.style.display = "none";

}

});

});

}