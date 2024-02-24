console.log("Exécution du programme principal")

//exercice 1
const liste = document.querySelectorAll("#ingredients li") //récupération les ingrédients
console.log("J'ai trouvé "+liste.length+" ingrédients"); //affichage du nombre d'ingrédient

//exercice 2
const elem = document.getElementById("elemEx2"); //récupération de l'élément
console.log(elem.classList); //affichage de ses classes
elem.classList.remove("control"); //suppression de la classe control
elem.classList.add("inverse"); //rajout de la classe inverse

//exercice 3
document.getElementById("reussite").textContent = "ha ok, j'ai compris !"; //changement du texte
const image = document.getElementById("dog"); //récupération de l'élément
console.log(image.getAttribute("alt")); //affichage de l'attribut alt
document.getElementById("legendeDog").textContent = image.getAttribute("alt"); //placement du texte dans le figcaption

//exercice 4
//effacer
document.getElementById("boutonEffacerEx4").addEventListener("click",detectionsuppr); //création de l'écouteur d'évènement
function detectionsuppr(){ //création de la fonction
    console.log("Evénement détecté !"); //affichage du message
    textbouton.textContent = "Afficher"; //change le text du bouton
    document.querySelector("#figureEx4 img").classList.add("invisible"); //rend l'image invisible
}
//afficher
document.getElementById("boutonAfficherEx4").addEventListener("click",detectionaffich); //création de l'écouteur d'évènement
function detectionaffich(){ //création de la fonction
    textbouton.textContent = "Effacer"; //change le text du bouton
    document.querySelector("#figureEx4 img").classList.remove("invisible"); //rend l'image visible
}
//afficher ou supprimer
document.getElementById("boutonDoubleEx4").addEventListener("click",detection); //création de l'écouteur d'évènement
let textbouton = document.getElementById("boutonDoubleEx4");
textbouton.textContent = "Effacer";
function detection(){ //création de la fonction
    document.querySelector("#figureEx4 img").classList.toggle("invisible"); //change la visibilité de l'image
    if(textbouton.textContent=="Effacer"){ //regarde le texte actuel
        textbouton.textContent = "Afficher"; //change le text du bouton
    } else {
        textbouton.textContent = "Effacer"; //change le text du bouton
    }
}

//exercice 5
const imageTete = document.querySelectorAll("#ex5 .liste_tetes img"); //récupération des 4 images
imageTete.forEach(element =>{ //pour chaques images...
    element.classList.add("penche"); //rajout de la classe penche
});
const h2 = document.querySelectorAll("h2"); //récupération de tous les titres h2
h2.forEach(element =>{ //pour chaques titres h2...
    element.classList.add("elargi"); //rajout de la classe elargi
});

//exercice 6
document.querySelector("#ex6 p img").addEventListener("click", pencher); //création de l'écouteur d'évènement
function pencher(){ //création de la fonction
        this.classList.toggle("penche"); //rajout de la classe pencher
};
const imageTete2 = document.querySelectorAll("#ex6 .liste_tetes img"); //récupération des 4 images
imageTete2.forEach(element =>{ //pour chaques images...
    element.addEventListener("click", pencher); //rajout d'un écouteur d'évènement
    element.addEventListener("mouseenter", enter); //création de l'écouteur d'évènement quand souris entre dans l'image
    element.addEventListener("mouseleave", leave); //création de l'écouteur d'évènement quand souris sort de l'image
});

function enter(){ //création de la fonction
    this.classList.add("penche"); //rajout de la classe pencher
};
function leave(){ //création de la fonction
    this.classList.remove("penche"); //suppression de la classe pencher
};