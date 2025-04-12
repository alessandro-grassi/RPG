document.addEventListener("DOMContentLoaded",()=>{ 
    fetchData("enemies-images-path", setImageEnemy)
    fetchData("enemies-list", setLifePoints)
    setName();
    setDialogue();
    setLifePointsPG();
    setButtonAttack();
    setButtonNext();
});



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
    const NAME = "Il Re Eterno";
    let vita_corrente = 0;
    let vita_corrente_pg = 500;
    let attacco_pg = 10;
    let danno_fisico_pg = attacco_pg * 10;
    let forza = 10;
    let danno_fisico = forza * 10;
    let rand = 0;

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
        vita_corrente -= danno_fisico_pg;
        if(vita_corrente <= 0){
            document.getElementById('image_king').remove();
            document.getElementById('vita').remove();
            document.getElementById('vita-text').remove();
            document.getElementById('overlay').remove();
            document.getElementById('text').innerHTML = "HAI VINTO!!";
            this.removeEventListener();
        }
        else{
            document.getElementById('vita').value = vita_corrente;
            document.getElementById('vita-text').innerHTML = "PV:"+ vita_corrente;
            document.getElementById('text').innerHTML = "'Hai inflitto "+danno_fisico_pg+" danni fisici!'";
        }
        document.getElementById('next_button').style = "visibility: visible;"; 
        this.style = "visibility: hidden";
    })
}

function setButtonNext(){
    document.getElementById('next_button').addEventListener("click", function(){
        fetchData("random-chance", getRand)
        fetchData("enemies-list", enemyAttack)
        document.getElementById('attack_button').style = "visibility: visible;"; 
        this.style = "visibility: hidden";
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
            enemy['moves'].forEach(moves =>{
                console.log(moves);
                console.log(moves['chance']);
                tempChance += moves['chance'];
                console.log(tempChance);
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
                    }
                    if(vita_corrente_pg < 0){
                        vita_corrente_pg = 0;
                        gameover();
                    }
                    tempChance -= 100
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