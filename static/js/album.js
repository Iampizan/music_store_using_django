/* Album Scroll Animation */

const albumCards = document.querySelectorAll(".album-card");

function revealAlbums(){

albumCards.forEach(card => {

const cardTop = card.getBoundingClientRect().top;

if(cardTop < window.innerHeight - 100){

card.classList.add("show");

}

});

}

window.addEventListener("scroll", revealAlbums);
revealAlbums();



/* Album Search Filter */

const searchInput = document.getElementById("albumSearch");

if(searchInput){

searchInput.addEventListener("keyup", function(){

let filter = searchInput.value.toLowerCase();

albumCards.forEach(card => {

let title = card.querySelector(".album-title").textContent.toLowerCase();
let artist = card.querySelector(".artist-name").textContent.toLowerCase();

if(title.includes(filter) || artist.includes(filter)){

card.style.display = "block";

}else{

card.style.display = "none";

}

});

});

}