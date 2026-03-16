
// 3D tilt effect

const cards = document.querySelectorAll(".card3d");

cards.forEach(card => {

card.addEventListener("mousemove", (e) => {

const rect = card.getBoundingClientRect();

const x = e.clientX - rect.left;
const y = e.clientY - rect.top;

const centerX = rect.width / 2;
const centerY = rect.height / 2;

const rotateX = -(y - centerY) / 15;
const rotateY = (x - centerX) / 15;

card.style.transform =
`rotateX(${rotateX}deg) rotateY(${rotateY}deg) scale(1.05)`;

});

card.addEventListener("mouseleave", () => {

card.style.transform = "rotateX(0) rotateY(0)";

});

});



// Scroll animation

const cardsFeature = document.querySelectorAll(".feature-card");

window.addEventListener("scroll", () => {

cardsFeature.forEach(card => {

const cardTop = card.getBoundingClientRect().top;

if(cardTop < window.innerHeight - 100){

card.classList.add("show");

}

});

});



// Floating gramophone animation

const gramophone = document.querySelector(".hero-image img");

let float = 0;

function floatAnimation(){

float += 0.02;

gramophone.style.transform =
`translateY(${Math.sin(float)*10}px)`;

requestAnimationFrame(floatAnimation);

}

floatAnimation();