const menu = document.getElementById("ouverture_menu");
menu.addEventListener("click",ouvrirMenu);
const croix = document.getElementById("fermeture_menu");
croix.addEventListener("click",fermerMenu);

function ouvrirMenu(){
    menu.classList.add("invisible");
    croix.classList.remove("invisible");
    document.querySelector(".menu-principal").classList.add("ouvert");
};

function fermerMenu(){
    menu.classList.remove("invisible");
    croix.classList.add("invisible");
    document.querySelector(".menu-principal").classList.remove("ouvert");
};