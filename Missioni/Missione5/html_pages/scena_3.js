document.addEventListener("DOMContentLoaded",()=>{ 
    fetchData("enemies-images-path", setImageEnemy)
    fetchData("enemies-list", setLifePoints)
    setName();
    setDialogue();
    setLifePointsPG();
    setButtonAttack();
    setButtonNext();
});



// Funzione per inviare dati al server
function sendToServer(request, data) {
    return fetch("http://localhost:8080/m5/" + request, {
        method: "POST", 
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data)
    });
}

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

//GLOBAL
    const NAME = "Il Re Eterno";
    let vita_corrente = 0;
    let vita_corrente_pg = 500;
    let attacco_pg = 10;
    let danno_fisico_pg = attacco_pg * 10;
    let forza = 10;
    let danno_fisico = forza * 10;
    let rand = 0;
    let tempChance = 0;

function setImageEnemy(json){
    json.forEach(element => {
    if (element['enemy_name'] == NAME)
        path = element['image']; 
    });
    document.getElementById('image_king').setAttribute('src', "http://localhost:8080/m5/get-image/"+ path);
}

function setLifePoints(json){
    json.forEach(enemy =>{
        if(enemy['name'] == NAME){
            vita_corrente = enemy['stats'].vita;
            document.getElementById('vita').value = vita_corrente;
            document.getElementById('vita').max = vita_corrente;
            document.getElementById('vita-text').innerHTML = "PV:"+vita_corrente;
            document.getElementById('vita_pg').value = vita_corrente_pg;
            document.getElementById('vita_pg').max = vita_corrente_pg;
        }
    })
}

function setName(){
    document.getElementById('name-text').innerHTML = NAME;
}

function setDialogue(){
    document.getElementById('text').innerHTML = "Il Re sta aspettando...";
}

function setButtonAttack(){
    document.getElementById('attack_button').addEventListener("click", function(){

        //effetti visivi
        const boss = document.getElementById('image_king');
        const hit_sound = document.getElementById('hit_sound');

        boss.classList.add('shake_boss');
        boss.classList.add('hit');
    
        hit_sound.currentTime = 0;
        hit_sound.play();
    
        setTimeout(() => {
            boss.classList.remove('shake_boss');
            boss.classList.remove('hit');
        }, 200);

        vita_corrente -= danno_fisico_pg;
        if(vita_corrente <= 0){
            document.getElementById('image_king').remove();
            document.getElementById('vita').remove();
            document.getElementById('vita-text').remove();
            document.getElementById('overlay').remove();
            document.getElementById('text').textContent = "HAI VINTO!!";
            document.getElementById('next_button').style = "visibility: visible;";
            this.removeEventListener('click', setButtonAttack);
        }
        else{
            document.getElementById('vita').value = vita_corrente;
            document.getElementById('vita-text').textContent = "PV:"+ vita_corrente;
            document.getElementById('text').textContent = "'Hai inflitto "+danno_fisico_pg+" danni fisici!'";
        }
        document.getElementById('next_button').style = "visibility: visible;"; 
        this.style = "visibility: hidden";

        void boss.offsetWidth; // Trigger reflow to restart animation
    })
}

function setButtonNext(){
    document.getElementById('next_button').addEventListener("click", function(){
        if(vita_corrente > 0){
            fetchData("random-chance", getRand)
            fetchData("enemies-list", enemyAttack)
            document.getElementById('attack_button').style = "visibility: visible;";
            this.style = "visibility: hidden";
        }
        else {
            window.location.replace("http://localhost:8080/m5/mission-start"); // rimanda a mission start
        }
    })
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

// funzione che manda i dati al server prende in input la richiesta da fare e i dati da mandare come oggetto
function sendToServer(request,data)
{
    fetch("http://localhost:8080/m5/" + request,{
        method:"POST", // metodo richiesta
        headers:{'Content-Type':'application/json'},
        body: JSON.stringify(data) // dati da inviare in formato json
    })

}

function getRand(json){
    rand = parseInt(json['result']);
    console.log(rand);
}

function enemyAttack(json){
    json.forEach(enemy =>{
        if(enemy['name'] == NAME){
            tempChance = 0;
            console.log(tempChance);
            enemy['moves'].forEach(moves =>{
                tempChance += moves['chance'];
                console.log(tempChance);
                console.log(moves['chance']);
                if(tempChance >= rand){
                    document.getElementById('text').innerHTML = moves['description'];
                    if(moves['move_type'] == 'attack'){
                        if(moves['damage_type'] == 'fisico'){
                            danno_enemy = danno_fisico + Math.floor((vita_corrente_pg * (moves['damage_fis_perc']/100)));
                            vita_corrente_pg -= danno_enemy;
                            document.getElementById('vita-text-pg').innerHTML = "PV:" + vita_corrente_pg;
                        }
                    }
                    else if(moves['move_type'] == 'buff'){
                        if(moves['move_name'] == 'Aura immortale'){
                            vita_corrente_pg -= danno_fisico;
                            document.getElementById('vita-text-pg').innerHTML = "PV:" + vita_corrente_pg;
                        }
                        if(moves['move_name'] == 'Corona Indistruttibile'){
                            document.getElementById('image_king').style = "filter: brightness(150%);";
                            vita_corrente_pg -= danno_fisico;
                            document.getElementById('vita-text-pg').innerHTML = "PV:" + vita_corrente_pg;
                        }
                    }
                    else if(moves['move_type'] == 'Unique'){
                        document.getElementById("img-Throne").style = "filter: invert(100%)"
                        vita_corrente_pg -= danno_fisico;
                        document.getElementById('vita-text-pg').innerHTML = "PV:" + vita_corrente_pg;
                    }
                    else{
                        vita_corrente_pg -= danno_fisico;
                        document.getElementById('vita-text-pg').innerHTML = "PV:"+ vita_corrente_pg;
                        document.getElementById('vita_pg').value = vita_corrente_pg;
                    }
                    if(vita_corrente_pg <= 0){
                        vita_corrente_pg = 0;
                        gameover();
                    }
                    tempChance -= 100

                    document.getElementById('boss_sound').setAttribute('src', "http://localhost:8080/m5/get-audio/"+ moves['audio']);

                    const combat_box = document.getElementById('combat-box');
                    const boss_sound = document.getElementById('boss_sound');

                    combat_box.classList.add('shake_player');
                    combat_box.classList.add('hit');
                    combat_box.classList.add('flash');
                    
                    boss_sound.load();
                    boss_sound.currentTime = 0;
                    boss_sound.play().catch(err => console.error("Errore riproduzione audio:", err));
                
                    setTimeout(() => {
                        combat_box.classList.remove('shake_player');
                        combat_box.classList.remove('hit');
                        combat_box.classList.remove('flash');
                    }, 4000);

                    void combat_box.offsetWidth; // Trigger reflow to restart animation
                }
            })
        }
    })
}

function gameover(){
    document.getElementById('vita-text-pg').innerHTML = "PV:"+vita_corrente_pg;
    document.getElementById('text').innerHTML = "GAME OVER";
    document.getElementById('attack_button').remove();
    document.getElementById('next_button').remove();
    retry = document.createElement('button');
    retry.textContent = "Retry";
    retry.className = "dialog-button";
    retry.addEventListener("click", function(){
        location.reload();
    });
    document.getElementById('dialog-box').appendChild(retry);
}

function setLifePointsPG(){
    document.getElementById('vita-text-pg').innerHTML = "PV:"+vita_corrente_pg;
}