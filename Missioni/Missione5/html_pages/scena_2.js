document.addEventListener("DOMContentLoaded",()=>{ 
    fetchData("enemies-images-path", setImageEnemy)
    fetchData("enemies-list", setLifePoints)
    setName();
    setDialogue();
    setLifePointsPG();
    setButtonAttack();
    setButtonMagic();
    setButtonHeal();
    setButtonNext();
});

let client_index;

// Funzione per inviare dati al server
function sendToServer(request, data) {
    return fetch("http://localhost:8080/m5/" + request, {
        method: "POST", 
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data)
    });
}


// Funzione per prendere dati dal server
function fetchData(request, callback)
{
    fetch("http://localhost:8080/m5/" + request)
    .then(response => {
        if(!response.ok) 
            throw new Error(`response fetch error ${response.status}`);
        return response.json();
    })
    .then(data => { 
        console.log("GET body data: ");
        callback(data);
    })
    .catch(err => { 
        console.error('request error',err);
    });
}

// Variabili globali
const NAME = "Adepto immortale Cremisi";
let vita_corrente = 0;
let vita_corrente_pg = 500;
let attacco_pg = 10;
let danno_fisico_pg = attacco_pg * 10;
let forza = 10;
let danno_fisico = forza * 10;
let rand = 0;
let danno_magico_pg = attacco_pg * 15;
let vita_max_pg = 500;
let enemyAlive = true;
let path = "";

// Imposta immagine nemico
function setImageEnemy(json){
    json.forEach(element => {
        if (element['enemy_name'] == NAME)
            path = element['image']; 
    });
    document.getElementById('image_mage').setAttribute('src', "http://localhost:8080/m5/get-image/"+ path);
}

// Imposta vita nemico
function setLifePoints(json){
    json.forEach(enemy =>{
        if(enemy['name'] == NAME){
            vita_corrente = enemy['stats'].vita;
            document.getElementById('vita').value = vita_corrente;
            document.getElementById('vita').max = vita_corrente;
            document.getElementById('vita-text').innerHTML = "PV:"+vita_corrente;
        }
    })
}

// Imposta nome nemico
function setName(){
    document.getElementById('name-text').innerHTML = NAME;
}

// Imposta dialogo iniziale
function setDialogue(){
    document.getElementById('text').innerHTML = "Adepto immortale cremisi ti osserva...";
}

// Bottone ATTACCO fisico
function setButtonAttack(){
    document.getElementById('attack_button').addEventListener("click", function(){
        if (!enemyAlive) return;
        let variabile_danno = Math.floor(danno_fisico_pg * (Math.random() * 0.4 + 0.8));

        vita_corrente -= variabile_danno;

        let enemyImage = document.getElementById('image_mage');
        enemyImage.classList.add('hit-effect');

        setTimeout(() => {
            enemyImage.classList.remove('hit-effect');
        }, 300);

        if(vita_corrente <= 0){
            enemyDefeated();
            return;
        }
        else{
            document.getElementById('vita').value = vita_corrente;
            document.getElementById('vita-text').innerHTML = "PV:"+ vita_corrente;
            document.getElementById('text').innerHTML = "Hai inflitto "+variabile_danno+" danni fisici!";
        }

        document.getElementById('next_button').style = "visibility: visible;"; 
        this.style = "visibility: hidden";
        toggleActionButtons(false);
    })
}

// Bottone MAGIA
function setButtonMagic() {
    document.getElementById('magic_button').addEventListener("click", function() {
        if (!enemyAlive) return;

        let variabile_danno = Math.floor(danno_magico_pg * (Math.random() * 0.4 + 0.8));

        vita_corrente -= variabile_danno;

        const enemyImage = document.getElementById('image_mage');
        enemyImage.classList.add('magic-effect');

        setTimeout(() => {
            enemyImage.classList.remove('magic-effect');
        }, 400);

        if (vita_corrente <= 0) {
            enemyDefeated();
            return;
        } else {
            document.getElementById('vita').value = vita_corrente;
            document.getElementById('vita-text').innerHTML = "PV:" + vita_corrente;
            document.getElementById('text').innerHTML = "Hai lanciato una magia! Danno: " + variabile_danno;
        }

        document.getElementById('next_button').style = "visibility: visible;";
        this.style = "visibility: hidden";
        toggleActionButtons(false);
    });
}

// Bottone CURA
function setButtonHeal() {
    document.getElementById('heal_button').addEventListener("click", function() {
        if (!enemyAlive) return;
        const healedAmount = Math.floor(Math.random() * 50) + 75; // Cure tra 75 e 125

        if (vita_corrente_pg >= vita_max_pg) {
            document.getElementById('text').innerHTML = "Hai già tutta la vita!";
            return;
        }

        vita_corrente_pg += healedAmount;
        if (vita_corrente_pg > vita_max_pg) vita_corrente_pg = vita_max_pg;

        setLifePointsPG();
        document.getElementById('text').innerHTML = "Ti sei curato di " + healedAmount + " PV!";
        greenFlash();

        document.getElementById('next_button').style = "visibility: visible;";
        toggleActionButtons(false);
    });
}

// Bottone NEXT
function setButtonNext(){
    document.getElementById('next_button').addEventListener("click", function(){        
        if (!enemyAlive)
        {
            window.location.replace("http://localhost:8080/m5/mission-start"); // rimanda a mission start
        }
        else {
        fetchData("random-chance", getRand);
        fetchData("enemies-list", enemyAttack);
        this.style = "visibility: hidden";
        }
    });
}

// Prendi il numero casuale per attacco nemico
function getRand(json){
    rand = parseInt(json['result']);
    console.log(rand);
}

// Funzione attacco nemico
function enemyAttack(json){
    if (!enemyAlive) return;
    json.forEach(enemy =>{
        if(enemy['name'] == NAME){
            let tempChance = 0;
            enemy['moves'].forEach(moves =>{
                tempChance += moves['chance'];
                if(tempChance >= rand){
                    document.getElementById('text').innerHTML = moves['description'];

                    if(moves['move_type'].toLowerCase() == 'attack'){
                        let damage = Math.floor(enemy['stats'].danno_mag_base * (Math.random() * 0.4 + 0.8));
                        vita_corrente_pg -= damage;
                        flashScreen();
                        setLifePointsPG();
                    }
                    tempChance = 0; // reset per sicurezza
                }
            })
            toggleActionButtons(true);
        }
    })
}

// Quando nemico è morto
function enemyDefeated(){
    enemyAlive = false;
    document.getElementById('image_mage').remove();
    document.getElementById('vita').remove();
    document.getElementById('vita-text').remove();
    document.getElementById('overlay').remove();
    document.getElementById('text').innerHTML = "HAI VINTO!!";
    toggleActionButtons(false);
    document.getElementById('next_button').style.visibility = "visible";
}

// Se il giocatore muore
function gameover(){
    document.getElementById('vita-text-pg').innerHTML = vita_corrente_pg;
    document.getElementById('text').innerHTML = "GAME OVER";
    document.getElementById('attack_button').remove();
    document.getElementById('next_button').remove();
}

// Imposta barra vita PG
function setLifePointsPG(){
    const pgText = document.getElementById('vita-text-pg');
    const pgBar = document.getElementById('vita-pg');

    pgText.innerHTML = "PV: " + vita_corrente_pg;
    pgBar.value = vita_corrente_pg;
    pgBar.max = vita_max_pg;
}

// Flash rosso quando subisci danni
function flashScreen() {
    const flash = document.getElementById('screen-flash');
    flash.classList.add('active');
    setTimeout(() => {
        flash.classList.remove('active');
    }, 200);
}

// Flash verde quando ti curi
function greenFlash() {
    const flash = document.getElementById('screen-flash');
    flash.classList.add('green', 'active');
    setTimeout(() => {
        flash.classList.remove('green', 'active');
    }, 200);
}

// Mostra o nasconde bottoni azione
function toggleActionButtons(show) {
    const visibility = show ? "visible" : "hidden";
    document.getElementById('attack_button').style.visibility = visibility;
    document.getElementById('magic_button').style.visibility = visibility;
    document.getElementById('heal_button').style.visibility = visibility;
    document.getElementById('next_button').style.visibility = show ? "hidden" : "visible";
}

function movelines(step) {
    client_index += step;
    const data = { "current_index": client_index };
    return sendToServer("update-index", data);
}


function fetchFromServer(request)
{
    return fetch("http://localhost:8080/m5/" + request)
    .then((response) => { // check risposta 
        if(!response.ok)
            throw new Error(`response fetch error ${response.status}`); // in caso di errore stampa lo stato a console
        return response.json(); // ritorna la risposta codificata in json
    })
    .then((data) => {
        console.log("fetched data:",data);
        return data; // return data
    })
    .catch((err) => {
        console.error('request erro: ',err); //log errore a console
        throw err;
    })
}