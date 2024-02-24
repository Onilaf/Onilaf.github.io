document.addEventListener('DOMContentLoaded', gererDessin);

function gererDessin() {

    // Création automatique d'un ensemble de 50 x 50 pixels
    creerLesPixels('#ex2 .zonedessin', 50, 50);

    // Complétez le programme ici

    // I. Echauffement:
    const pixel_ex1 = document.querySelector("#ex1 .pixel");
    //pixel_ex1.classList.add("pixel--coloré");

    // II. Traiter un pixel seul:
    const span_poids = document.querySelector(".poids");
    pixel_ex1.addEventListener("click",couleur); //ajoute un écouteur d'évènement
    function couleur(){
        this.classList.add("pixel--coloré"); //ajoute la classe pixel--coloré
        console.log(this.dataset.poids); //affiche la valeur de poids-data dans la console
        span_poids.innerText = this.dataset.poids; //affiche la valeur de poids-data dans le span
    };

    // III. Traiter tous les pixels:
    const pixels = document.querySelectorAll("#ex2 .pixel");
    pixels.forEach(element => {
        element.addEventListener("click",changerCouleur); //ajoute un écouteur d'évènement pour tous les pixels
    });
    function changerCouleur(event){
        if(event.button != 2){ //si autre bouton que clic droit
            this.classList.add("pixel--coloré"); //ajouter la classe pixel--coloré
        } else { //sinon (si c'est un clic droit)
            if(this.classList.contains("pixel--coloré")){ //si il possède la classe pixel--coloré
                this.classList.remove("pixel--coloré"); //la lui retirer
            };
        };

        // Question V.A:
        var newLi = document.createElement("li"); //créer un nouvelle élément "li"
        newLi.innerHTML = this.dataset.poids; //lui attribut la valeur de data-poids du pixel séléctionné
        liste.append(newLi); //rajoute le'élément' à la fin de la liste
    };

    // IV. Traiter tous les pixels:
    document.querySelector(".recommencer").addEventListener("click",recommencer); //ajoute un écouteur d'évènement
    function recommencer(){
        pixels.forEach(element => {
            element.classList.remove("pixel--coloré"); //enlève la classe pour tous les pixels
        });

        // Question V.B:
        liste.innerHTML = ""; //vide la liste des différents poids
    };

    // V. Gérer la liste des pixels:
    const liste = document.querySelector("#lesPoids");

    // VI. Travail sur la famille:
    const grands_freres = document.querySelectorAll(".grandFrere");
    grands_freres.forEach(element => {
        element.addEventListener("click",changerFrere); //ajoute un écouteur d'évènement pour les deux pixels grand frère
    });
    function changerFrere(event){
        const petit_frere = event.currentTarget.closest(".couplePixels").querySelector(".petitFrere"); //cherche le petit frère présent dans le même couple de pixel
        if(petit_frere.classList.contains("pixel--coloré")){ //si il possède la classe pixel--coloré
            petit_frere.classList.remove("pixel--coloré"); //la lui enlève
        } else { //sinon
            petit_frere.classList.add("pixel--coloré"); //la lui ajoute
        };
    };

    function creerLesPixels(lieu, nbLignes, nbColonnes) {
        const zoneDeDessin = document.querySelector(lieu);
        const largeur = 100 / nbColonnes;
        for (let i = 1; i <= nbColonnes * nbColonnes; i++) {
            const nouveauPixel = document.createElement('div');
            nouveauPixel.classList.add('pixel');
            nouveauPixel.setAttribute("style", "flex-basis:" + largeur + "%");
            const poids = getRandomIntInclusive(1, 3);
            nouveauPixel.setAttribute("data-poids", poids);
            zoneDeDessin.append(nouveauPixel);
        }
    } // creerLesPixels

    // Pour donner un poids aléatoire aux pixels
    function getRandomIntInclusive(min, max) {
        min = Math.ceil(min);
        max = Math.floor(max);
        return Math.floor(Math.random() * (max - min + 1)) + min;
    }

} // gererDessin