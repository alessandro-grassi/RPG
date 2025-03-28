document.addEventListener("DOMContentLoaded",()=>{ // caricare il testo
    fetchFromServer("get-dialog").then(data=>{ // fetch dei dialoghi dal server
        let lines = data.flatMap(obj => obj.text); // prende ogni linea di testo per gli oggetti estratti e la mappa all'oggetto
        dialogLines = lines; // assegna le linee di dialogo alla variabile globale});
     });
    fetchFromServer("dialog-index").then(index=>{
        document.getElementById("dialog-box").textContent = dialogLines[index.current_index]; // imposta index corrente
    });
    setButton();
});

let dialogLines; // variabile globale per lo store delle linee di dialogo da scorrere
let imageMapping; // variabile usata per salvare la mappatura delle immagini
let index; // variabile globale per lo store lato client dell'index a cui si trova il dialogo e le immagini
// funzione usata per impostare l'evento legato al bottone per far avanzare il testo
function setButton(){
    document.getElementById("next-button").addEventListener("click",function(){
        fetchData("dialog-index",moveLines) // fa un fetch dell'index
    });
}

// funzione che fa avanzare le linee di testo in base all'index ricevuto e aggiorna l'index lato server
function moveLines(index)
{
    console.log("index:");
    console.log(dialogLines[index]);
    document.getElementById("dialog-box").textContent = dialogLines[index.current_index];
    const data = {"current_index": index.current_index + 1}; // dati con index da inviare
    sendToServer("update-index",data); // invia il nuovo index al server
}

// funzione che manda i dati al server prende in input la richiesta da fare e i dati da mandare come oggetto
function sendToServer(request,data)
{
    fetch("http://localhost:8080/m5/" + request,{
        method:"POST", // metodo richiesta
        headers:{'Content-Type':'application/json'},
        body: JSON.stringify(data) // dati da inviare in formato json
    })
    .then((response)=>{ // prende la risposta del server
        if(!response.ok) // in caso di errore manda stato risposta a console
        {
            alert('operazione fallita, riprovare o ricaricare la pagina'); // in caso di fallimento post
            throw new Error(`error posting content to server: ${response.status}`); 
        }
        return response.json(); // restituisce la risposta data dal server
    })
    .then((result)=>{
        console.log(result); // log risposta per debug
    })
    .catch((err)=>{ // catch errori
        console.error('error sending data: ',err); // fa un log a console dell'errore
        alert('operazione fallita, riprovare o ricaricare la pagina.\n\ncodice di errore: '+ err); // manda un alert con il codice di errore
    });
}

// funzione usata per fare il fetch dei dati dal server e passarli a una funzione data come parametro
function fetchData(request,callback)
{
    fetch("http://localhost:8080/m5/" + request) // fetch url con richiesta
    .then(response => {
        if(!response.ok) // check stato risposta
            throw new Error(`response fetch error ${response.status}`); // in caso di errore stampa lo stato a console
        return response.json(); // ritorna la risposta codificata in json
    })
    .then(data => { // prende i dati ottenuti
        console.log("fetched data: ");
        console.log(data) // log dati per debug
        callback(data); // chiama la funzione di callback a cui passare i dati ottenuti
    })
    .catch(err => { // catch dell'errore in modo da stamparlo a console
        console.error('request error',err); // log dell'errore a console
    });
}

// funzione che controlla se al dialogo corrente è associata un immagine
function checkImage(index)
{
    imageMapping.forEach(mapping => { // controlla se a ogni dialogo corrisponde un immagine
        if(mapping.dialog == dialogLines[index]) // se trova un mapping per il dialogo
            return mapping.image; // ritorna nome immagine da recuperare
        else 
            return false // ritorna falso
    })
}


// funzione di fetch a server a scopo generico
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