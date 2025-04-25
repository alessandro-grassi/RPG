document.addEventListener("DOMContentLoaded",()=>{ 
    // Carica i dati iniziali dal server al caricamento della pagina
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

function sendToServer(request,data)
{
    // Funzione per inviare dati al server (POST)
    fetch("http://localhost:8080/m5/" + request,{
        method:"POST", 
        headers:{'Content-Type':'application/json'},
        body: JSON.stringify(data)
    })
    .then((response)=>{ 
        if(!response.ok) 
        {
            alert('operazione fallita, riprovare o ricaricare la pagina'); 
            throw new Error(`error posting content to server: ${response.status}`); 
        }
        return response.json(); 
    })
    .then((result)=>{
        console.log(result);
        return result;
    })
    .catch((err)=>{ 
        console.error('error POST data: ',err);
        alert('operazione fallita, riprovare o ricaricare la pagina.\n\ncodice di errore: '+ err); 
    });
}

function fetchData(request, callback)
{
    // Funzione per ottenere dati dal server (GET)
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

// Variabili globali del gioco
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
let enemyAlive = true; // variabile che indica se il nemico è ancora vivo

function setImageEnemy(json){
    // Imposta l'immagine del nemico
    json.forEach(element => {
    if (element['enemy_name'] == NAME)
        path = element['image']; 
    });
    document.getElementById('image_mage').setAttribute('src', "http://localhost:8080/m5/get-image/"+ path);
}

function setLifePoints(json){
    // Imposta i punti vita del nemico
    json.forEach(enemy =>{
        if(enemy['name'] == NAME){
            vita_corrente = enemy['stats'].vita;
            document.getElementById('vita').value = vita_corrente;
            document.getElementById('vita').max = vita_corrente;
            document.getElementById('vita-text').innerHTML = "PV:"+vita_corrente;
        }
    })
}

function setName(){
    // Imposta il nome del nemico sullo schermo
    document.getElementById('name-text').innerHTML = NAME;
}

function setDialogue(){
    // Imposta il testo iniziale di dialogo
    document.getElementById('text').innerHTML = "Adepto immortale cremisi ti osserva...";
}

function setButtonAttack(){
    // Azione quando si preme il pulsante di attacco
    document.getElementById('attack_button').addEventListener("click", function(){
        vita_corrente -= danno_fisico_pg;

        let enemyImage = document.getElementById('image_mage');
        enemyImage.classList.add('hit-effect'); // Effetto di attacco sul nemico

        setTimeout(() => {
            enemyImage.classList.remove('hit-effect');
        }, 300);

        if(vita_corrente <= 0){
            // Il nemico è morto: rimuovi immagine, barra vita, testo, mostra solo "Next"
            enemyAlive = false;
            document.getElementById('image_mage').remove();
            document.getElementById('vita').remove();
            document.getElementById('vita-text').remove();
            document.getElementById('overlay').remove();
            document.getElementById('text').innerHTML = "HAI VINTO!!";
        
            toggleActionButtons(false); // Nasconde i pulsanti
            document.getElementById('next_button').style = "visibility: visible;";
        
            return;
        }
        else{
            // Il nemico è ancora vivo: aggiorna vita
            document.getElementById('vita').value = vita_corrente;
            document.getElementById('vita-text').innerHTML = "PV:"+ vita_corrente;
            document.getElementById('text').innerHTML = "'Hai inflitto "+danno_fisico_pg+" danni magici!'";
        }

        // Mostra solo "Next", nasconde altri
        document.getElementById('next_button').style = "visibility: visible;"; 
        this.style = "visibility: hidden";
        toggleActionButtons(false);
    })
}

function setButtonMagic() {
    // Azione del pulsante Magia
    document.getElementById('magic_button').addEventListener("click", function() {
        vita_corrente -= danno_magico_pg;

        const enemyImage = document.getElementById('image_mage');
        enemyImage.classList.add('magic-effect'); // Effetto magico differente

        setTimeout(() => {
            enemyImage.classList.remove('magic-effect');
        }, 400);

        if (vita_corrente <= 0) {
            // Nemico ucciso con magia
            document.getElementById('image_mage').remove();
            document.getElementById('vita').remove();
            document.getElementById('vita-text').remove();
            document.getElementById('overlay').remove();
            document.getElementById('text').innerHTML = "HAI VINTO CON LA MAGIA!";
        } else {
            // Nemico colpito ma non morto
            document.getElementById('vita').value = vita_corrente;
            document.getElementById('vita-text').innerHTML = "PV:" + vita_corrente;
            document.getElementById('text').innerHTML = "Hai lanciato una magia! Danno: " + danno_magico_pg;
        }

        toggleActionButtons(false); 
    });
}


function setButtonHeal() {
    // Azione del pulsante Cura
    document.getElementById('heal_button').addEventListener("click", function() {
        const healedAmount = 100;
        if (vita_corrente_pg >= vita_max_pg) {
            // Se sei già al massimo della vita, non perdi il turno
            document.getElementById('text').innerHTML = "Hai già tutta la vita!";
            return; 
        }

        // Cura del personaggio
        vita_corrente_pg += healedAmount;
        if (vita_corrente_pg > vita_max_pg) vita_corrente_pg = vita_max_pg;

        setLifePointsPG();
        document.getElementById('text').innerHTML = "Ti sei curato di " + healedAmount + " PV!";
        greenFlash(); // Schermata verde per feedback visivo
        toggleActionButtons(false); 
    });
}

function setButtonNext(){
    // Azione del pulsante Next
    document.getElementById('next_button').addEventListener("click", function(){
        console.log("Bottone Cliccato"); // Stampa in console come richiesto

        if (!enemyAlive) return; // Se il nemico è morto, non si fa nulla

        // Attacco del nemico
        fetchData("random-chance", getRand);
        fetchData("enemies-list", enemyAttack);
        this.style = "visibility: hidden";
    });
}

function getRand(json){
    // Ottiene un numero casuale dal server
    rand = parseInt(json['result']);
    console.log(rand);
}

function enemyAttack(json){
    // Azione dell'attacco nemico
    if (!enemyAlive) return; // Il nemico non può attaccare se è morto

    json.forEach(enemy =>{
        if(enemy['name'] == NAME){
            tempChance = 0;
            enemy['moves'].forEach(moves =>{
                console.log(moves);
                console.log(moves['chance']);
                tempChance += moves['chance'];
                console.log(tempChance);
                if(tempChance >= rand){
                    document.getElementById('text').innerHTML = moves['description'];

                    if(moves['move_type'] == 'attack'){
                        if(moves['damage_type'] == 'fisico'){
                            danno_enemy = danno_fisico;
                            vita_corrente_pg -= danno_enemy;
                            document.getElementById('vita-text-pg').innerHTML = vita_corrente_pg;
                        }
                    }
                    else{
                        vita_corrente_pg -= danno_fisico;
                        document.getElementById('vita-text-pg').innerHTML = vita_corrente_pg;
                    }                    
                    if(vita_corrente_pg < 0){
                        // Il PG è morto
                        vita_corrente_pg = 0;
                        gameover();
                    }
                    tempChance -= 100
                }
            })
            setLifePointsPG();
            flashScreen(); // Schermata rossa per danno
            toggleActionButtons(true); // I pulsanti riappaiono dopo l'attacco (ma non se il nemico è morto)
        }
    })
}

function gameover(){
    // Quando il PG muore
    document.getElementById('vita-text-pg').innerHTML = vita_corrente_pg;
    document.getElementById('text').innerHTML = "GAME OVER";
    document.getElementById('attack_button').remove();
    document.getElementById('next_button').remove();
}

function setLifePointsPG(){
    // Aggiorna la barra della vita del PG
    const pgText = document.getElementById('vita-text-pg');
    const pgBar = document.getElementById('vita-pg');

    pgText.innerHTML = "PV: " + vita_corrente_pg;
    pgBar.value = vita_corrente_pg;
    pgBar.max = vita_max_pg;
}

function flashScreen() {
    // Effetto rosso quando si prende danno
    const flash = document.getElementById('screen-flash');
    flash.classList.add('active');
    setTimeout(() => {
        flash.classList.remove('active');
    }, 200);
}

function toggleActionButtons(show) {
    // Mostra o nasconde i pulsanti di azione
    const visibility = show ? "visible" : "hidden";
    document.getElementById('attack_button').style.visibility = visibility;
    document.getElementById('magic_button').style.visibility = visibility;
    document.getElementById('heal_button').style.visibility = visibility;
    document.getElementById('next_button').style.visibility = show ? "hidden" : "visible";
}

function greenFlash() {
    // Effetto verde quando ci si cura
    const flash = document.getElementById('screen-flash');
    flash.classList.add('green', 'active');
    setTimeout(() => {
        flash.classList.remove('green', 'active');
    }, 200);
}
