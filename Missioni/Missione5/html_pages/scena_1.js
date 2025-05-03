document.addEventListener("DOMContentLoaded",()=>{ 
    fetchData("enemies-images-path", setImageEnemy)
    fetchData("enemies-list", setLifePoints)
    setName();
    setDialogue();
    setLifePointsPG();
    setButtonAttack();
    setButtonHeal();
    setButtonUlti();
    setButtonMagic();
    setButtonNext();
    setUltiCharge();
});

let PREFIX_API = '/m5/api/';

function sendToServer(request,data)
{
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
    const NAME = "Guardiano di Rocciascura";
    let vita_corrente = 0;
    
    let vigore=5;
    let vita_corrente_pg = vigore * 100;

    let forza_pg = 10;
    let danno_fisico_pg = forza_pg * 10;
    
    let intelligenza_pg = 8;
    let danno_magico_pg = intelligenza_pg *15;

    let forza = 10;
    let danno_fisico = forza * 10;

    let rand = 0;
    let tempChance = 0;

    let carica_ulti = 0;
    let client_index;


function setImageEnemy(json){
    json.forEach(element => {
    if (element['enemy_name'] == NAME)
        path = element['image'];
        console.log(path);
    });
    document.getElementById('image_guardian').setAttribute('src', "http://localhost:8080/m5/get-image/"+ path);
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

function setUltiCharge(){
    document.getElementById('ulti').value = carica_ulti;
    document.getElementById('ulti').max = 3;
}

function setName(){
    document.getElementById('name-text').innerHTML = NAME;
}

function setDialogue(){
    document.getElementById('text').innerHTML = "Il Guardiano è infuriato...";
}

function setButtonAttack(){
    document.getElementById('attack_button').addEventListener("click", function(){

        //effetti visivi
        const boss = document.getElementById('image_guardian');
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
        carica_ulti += 1;
        if(vita_corrente <= 0){

            victory();
            this.removeEventListener();
        }
        else{
            document.getElementById('vita').value = vita_corrente;
            document.getElementById('ulti').value = carica_ulti;
            document.getElementById('vita-text').innerHTML = "PV:"+ vita_corrente;
            document.getElementById('text').innerHTML = "'Hai inflitto "+danno_fisico_pg+" danni!'";
        }

        document.getElementById('ulti_button').style = "visibility: hidden;";
        document.getElementById('next_button').style = "visibility: visible;"; 
        document.getElementById('heal_button').style = "visibility: hidden;";
        document.getElementById('magic_button').style = "visibility: hidden;";
        document.getElementById('ulti').style = "visibility: hidden;";
        this.style = "visibility: hidden";

        void boss.offsetWidth; // Trigger reflow to restart animation
    })
}

function victory(){
    document.getElementById('image_guardian').remove();
    document.getElementById('vita').remove();
    document.getElementById('ulti').remove();
    document.getElementById('vita-text').remove();
    document.getElementById('overlay').remove();
    document.getElementById('attack_button').remove();
    document.getElementById('heal_button').remove();
    document.getElementById('ulti_button').remove();
    document.getElementById('magic_button').remove();
    document.getElementById('text').innerHTML = "HAI VINTO!!";
    document.getElementById('next_button').style = "visibility: visible;"; 
}

function setButtonMagic() {
    document.getElementById('magic_button').addEventListener("click", function() {

        //Audio ed Effetti
        const boss = document.getElementById('image_guardian');
        const magic_sound = document.getElementById('magical_sound');

        boss.classList.add('shake_boss');
        boss.classList.add('hit');
    
        magic_sound.currentTime = 0;
        magic_sound.play();

        setTimeout(() => {
            boss.classList.remove('shake_boss');
            boss.classList.remove('hit');
        }, 1300);

        //Attacco magico fa variare il danno
        let variabile_danno = Math.floor(danno_magico_pg * (Math.random() * 0.4 + 0.8));

        vita_corrente -= variabile_danno;

        if (vita_corrente <= 0) {
            //Sconfitta del boss
            victory();
        } else {
            //Magia del player
            document.getElementById('vita').value = vita_corrente;
            document.getElementById('vita-text').innerHTML = "PV:" + vita_corrente;
            document.getElementById('text').innerHTML = "'Hai inflitto " + variabile_danno + " danni magici!'";
        }

        document.getElementById('next_button').style = "visibility: visible;";
        document.getElementById('attack_button').style = "visibility: hidden;";
        document.getElementById('heal_button').style = "visibility: hidden;";
        document.getElementById('ulti').style = "visibility: hidden;";
        document.getElementById('ulti_button').style = "visibility: hidden;";
        this.style = "visibility: hidden";

        void boss.offsetWidth;
    });
}

function setButtonHeal(){
    document.getElementById('heal_button').addEventListener("click", function(){

        const heal_sound = document.getElementById('heal_sound');

        heal_sound.currentTime = 0;
        heal_sound.play();

        if(vita_corrente <= 0){
            this.removeEventListener();
        }

        vita_corrente_pg += 150;

        if(vita_corrente_pg > 500){
            vita_corrente_pg = 500;
            document.getElementById('vita-text-pg').innerHTML = "PV:"+ vita_corrente_pg;
            document.getElementById('vita_pg').value = vita_corrente_pg;
            document.getElementById('text').innerHTML = "'Non puoi curarti oltre i 500 PV!'";
        }
        else{
            document.getElementById('vita-text-pg').innerHTML = "PV:"+ vita_corrente_pg;
            document.getElementById('vita_pg').value = vita_corrente_pg;
            document.getElementById('text').innerHTML = "'Ti sei curato di 150 PV!'";
        }

        document.getElementById('ulti_button').style = "visibility: hidden;";
        document.getElementById('next_button').style = "visibility: visible;"; 
        document.getElementById('attack_button').style = "visibility: hidden;";
        document.getElementById('magic_button').style = "visibility: hidden;";
        document.getElementById('ulti').style = "visibility: hidden;";
        this.style = "visibility: hidden";

    })
}

function setButtonUlti(){
    document.getElementById('ulti_button').addEventListener("click", function(){

        //effetti visivi
        const boss = document.getElementById('image_guardian');
        const ulti_sound = document.getElementById('ulti_sound');

        boss.classList.add('shake_boss');
        boss.classList.add('hit');
    
        ulti_sound.currentTime = 0;
        ulti_sound.play();
    
        setTimeout(() => {
            boss.classList.remove('shake_boss');
            boss.classList.remove('hit');
        }, 200);

        vita_corrente -= danno_fisico_pg * 2;
        carica_ulti = 0;

        if(vita_corrente <= 0){
            victory();
            this.removeEventListener();
        }
        else{
            document.getElementById('vita').value = vita_corrente;
            document.getElementById('ulti').value = carica_ulti;
            document.getElementById('vita-text').innerHTML = "PV:"+ vita_corrente;
            document.getElementById('text').innerHTML = "'Hai inflitto "+danno_fisico_pg*2+" danni!'";
        }

        document.getElementById('attack_button').style = "visibility: hidden;";
        document.getElementById('next_button').style = "visibility: visible;"; 
        document.getElementById('heal_button').style = "visibility: hidden;";
        document.getElementById('magic_button').style = "visibility: hidden;";
        document.getElementById('ulti').style = "visibility: hidden;";
        this.style = "visibility: hidden";

        void boss.offsetWidth; // Trigger reflow to restart animation
    })
}

function setButtonNext(){
    document.getElementById('next_button').addEventListener("click", function(){
        if(vita_corrente > 0) {
            fetchData("random-chance", getRand)
            fetchData("enemies-list", enemyAttack)
            document.getElementById('attack_button').style = "visibility: visible;";
            document.getElementById('heal_button').style = "visibility: visible;";
            document.getElementById('ulti_button').style = "visibility: visible;";
            document.getElementById('magic_button').style = "visibility: visible;";
            document.getElementById('ulti').style = "visibility: visible;";
            if(carica_ulti >=3){
                document.getElementById('ulti_button').disabled = false;
            }
            else{
                document.getElementById('ulti_button').disabled = true;
            }
            this.style = "visibility: hidden";
        }
        else {
            window.location.replace("http://localhost:8080/m5/mission-start");
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

// Funzione per inviare dati al server
function sendToServer(request, data) {
    return fetch("http://localhost:8080/m5/" + request, {
        method: "POST", 
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data)
    });
}

function getRand(json){
    rand = parseInt(json['result']);
}

function enemyAttack(json){
    json.forEach(enemy =>{
        if(enemy['name'] == NAME){
            tempChance = 0;
            enemy['moves'].forEach(moves =>{
                tempChance += moves['chance'];
                if(tempChance >= rand){
                    document.getElementById('text').innerHTML = moves['description'];
                    if(moves['move_type'] == 'attack'){
                        if(moves['damage_type'] == 'fisico'){
                            danno_enemy = danno_fisico + Math.floor((vita_corrente_pg * (moves['damage_fis_perc']/100)));
                            vita_corrente_pg -= danno_enemy;
                            document.getElementById('vita-text-pg').innerHTML = "PV:" + vita_corrente_pg;
                        }
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
                    tempChance -= 100;

                    /*fetch(PREFIX_API+"enemy-attack/provaM5")                 
                    .then(response => response.json())
                    .then(data => console.log(data));

                    fetch(PREFIX_API+"get_enemy_life/provaM5")
                    .then(response=>response.json())
                    .then(data=>{
                            vita_corrente = data
                        })*/

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
    document.getElementById('heal_button').remove();
    document.getElementById('ulti_button').remove();
    document.getElementById('next_button').remove();
    document.getElementById('magic_button').remove();
    document.getElementById('ulti').remove();
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
