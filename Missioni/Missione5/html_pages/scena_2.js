document.addEventListener("DOMContentLoaded",()=>{ 
    fetchData("enemies-images-path", setImageEnemy)
    fetchData("enemies-list", setLifePoints)
    setName();
    setDialogue();
    setLifePointsPG();
    setButtonAttack();
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
    const NAME = "Adepto immortale Cremisi";
    let vita_corrente = 0;
    let vita_corrente_pg = 500;
    let attacco_pg = 10;
    let danno_fisico_pg = attacco_pg * 10;

function setImageEnemy(json){
    json.forEach(element => {
    if (element['enemy_name'] == NAME)
        path = element['image']; 
    });
    document.getElementById('image_mage').setAttribute('src', "http://localhost:8080/m5/get-image/"+ path);
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
    document.getElementById('text').innerHTML = "Adepto immortale cremisi sta aspettando...";
}

function setButtonAttack(){
    document.getElementById('attack_button').addEventListener("click", function(){
        vita_corrente -= danno_fisico_pg;
        if(vita_corrente <= 0){
            document.getElementById('image_mage').remove();
            document.getElementById('vita').remove();
            document.getElementById('vita-text').remove();
            document.getElementById('overlay').remove();
            document.getElementById('text').innerHTML = "HAI VINTO!!";
            this.removeEventListener();
        }
        else{
            document.getElementById('vita').value = vita_corrente;
            document.getElementById('vita-text').innerHTML = "PV:"+ vita_corrente;
            document.getElementById('text').innerHTML = "'Hai inflitto "+danno_fisico_pg+" danni magici!'";
        }
    })
}

function setLifePointsPG(){
    document.getElementById('vita-text-pg').innerHTML = "PV:"+vita_corrente_pg;
}