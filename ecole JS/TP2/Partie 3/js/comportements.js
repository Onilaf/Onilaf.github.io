document.getElementById("saisieNbTS").addEventListener("input",dire);
const zone = document.getElementById("zoneRetourClient")


function dire(){
    var shirt = "s";
    var frais = " + 5€ de frais de port";
    if (this.value==1){
        shirt = "";
    };
    if (this.value*15>50){
        frais = " (frais de port offerts)";
    }
    if (this.value<1){
        zone.textContent = "Veuillez rentrer une valeur correcte !";
    } else {
    zone.textContent = "Vous avez choisi de commander "+this.value+" t-shirt"+shirt+", pour un montant de "+this.value*15+"€"+frais;
    };
};