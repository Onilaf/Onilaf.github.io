//exercice 1

var liste1 = document.querySelectorAll("#ex1 ul li");
document.querySelector("#ex1 span").addEventListener("click",supprlst);

function supprlst(){
    liste1[0].remove();
    liste1 = document.querySelectorAll("#ex1 ul li");
};

//exercice 2

var liste2 = document.querySelectorAll("#ex2 ul li");
var ul2 = document.querySelector("#ex2 ul");
document.getElementById("boutonDeplacerEx2").addEventListener("click",deplace);
document.getElementById("boutonCreerEx2").addEventListener("click",creer); 

function deplace(){
    ul2.append(liste2[0]);
    liste2 = document.querySelectorAll("#ex2 ul li");
};

function creer(){
    var sauv = document.createElement("li");
    sauv.innerHTML = "nouveau";
    ul2.append(sauv);
};

//exercice 3

const liste3 = document.querySelectorAll("#ex3 ul li");
document.querySelector("#ex3 span").addEventListener("click",afficher3);
liste3.forEach(element => {
    element.addEventListener("click",invisible3);
});

function invisible3(){
    liste3[0].classList.add("invisible");
};

function afficher3(){
    liste3[0].classList.remove("invisible");
};

//exercice 4

const liste4 = document.querySelectorAll("#ex4 ul li");
document.querySelector("#ex4 span").addEventListener("click",afficher4);
liste4.forEach(element => {
    element.addEventListener("click",invisible4);
});

function invisible4(){
    this.classList.add("invisible");
};

function afficher4(){
    liste4.forEach(element => {
        element.classList.remove("invisible");
    });
};

//exercice 5

var liste5 = document.querySelectorAll("#ex5 ul li");
var ul5 = document.querySelector("#ex5 ul");
liste5.forEach(element => {
    element.addEventListener("click",descend);
});

function descend(){
    ul5.append(this);
    liste5 = document.querySelectorAll("#ex5 ul li");
};

//exercice 6

const liste6 = document.querySelectorAll("#ex6 ul li");
document.querySelector("#ex6 span").addEventListener("click",reAfficher);
liste6.forEach(element => {
    element.addEventListener("click",tousInvisible);
});

function tousInvisible(){
    var classe = this.classList[0]
    var memeClasse = document.querySelectorAll("."+classe);
    memeClasse.forEach(element => {
        element.classList.add("invisible");
    });
};

function reAfficher(){
    liste6.forEach(element => {
        element.classList.remove("invisible");
    });
};