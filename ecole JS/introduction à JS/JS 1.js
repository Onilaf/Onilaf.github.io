function jeuneOuVieuxLog(age){
    if (age<40){
        console.log("Jeune");
    } else {
        console.log("Vieux");
    }

}

function jeuneOuVieux(age){
    if (age<40){
        return "Jeune";
    } else {
        return "Vieux";
    }

}

function majeure(annee){
    const dateActuelle = new Date();
    const anneeActuelle = dateActuelle.getFullYear();
    if (anneeActuelle-annee>17){
        return true;
    }
    return false;
    
}

class Personne {
    constructor(nom,prenom,annee,permis) {
        this.nom = nom;
        this.prenom = prenom;
        this.anneeNaiss = annee;
        this.permisB = permis;
    }
}

moi = new Personne("Duminy","Quentin",2003,true);
pierre = new Personne("Dragono","Pierre",1999,false);
milly = new Personne("Racnier","Milly",2005,false);
fred = new Personne("Penjiska","Fred",2002,true);
arthur = new Personne("Enyope","Arthur",2000,true);
monEquipe = [moi,pierre,milly,fred,arthur];

function estMajeure(personne){
    return majeure(personne.anneeNaiss);
}

function nbPermisB(groupe){
    nb=0;
    for (let i = 0; i<groupe.length;i++){
        if (groupe[i].permisB){
            nb+=1;
        }
    }
    return nb;
}

function nbMajeure(groupe){
    nb=0;
    for (let i = 0; i<groupe.length;i++){
        if (estMajeure(groupe[i])){
            nb+=1;
        }
    }
    return nb;
}

function tousMajeure(groupe){
    tab=[];
    for (let i = 0; i<groupe.length;i++){
        if (estMajeure(groupe[i])){
            tab.push(groupe[i]);
        }
    }
    return tab;
}

jeuneOuVieuxLog(50);
console.log(jeuneOuVieux(34));
console.log(majeure(1977));
console.log(estMajeure(moi));
console.log(nbPermisB(monEquipe));
console.log(nbMajeure(monEquipe));
console.log(tousMajeure(monEquipe));