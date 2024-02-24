const logo = document.getElementById("le-logo");
console.log(logo);
console.log(logo.classList);
logo.classList.remove("clair");

const lien = document.querySelector(".menu-principal a");
lien.classList.add("actuel");

const equipe = document.querySelectorAll(".equipier");
console.log(equipe.length);
equipe.item(1).classList.add("expert");


const footer = document.querySelector(".footer-principal");
console.log(footer.textContent);

logo.textContent = "Top !";

footer.textContent += "L1 info";

console.log(equipe.item(1).textContent);


console.log(equipe.item(1).getAttribute("data-prenom"));

logo.setAttribute("href","index.html");

equipe.item(2).querySelector(".equipier__nom").textContent = equipe.item(2).getAttribute("data-nom");

console.log(equipe.item(0).dataset.prenom);


equipe.forEach(personne =>{
    console.log(personne.getAttribute("data-nom"));
    personne.querySelector(".equipier__nom").textContent = personne.dataset.prenom+" "+personne.dataset.nom;
});