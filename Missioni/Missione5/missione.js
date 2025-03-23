document.addEventListener("DOMContentLoaded",()=>{ // caricare il testo
    fetchData("get-dialogue",setLines); // prende le linee di testo
    fetchData("dialog-index",moveLines); // aggiorna l'index per le linee correnti e le prossime
});

let dialogLines; // variabile globale per lo store delle linee di dialogo da scorrere

// funzione usata per fare il fetch dei dati dal server e passarli a una funione data come parametro
function fetchData(request,callback)
{
    fetch("http://localhost:8080/m5/" + request) // fetch url con richiesta
    .then(response => {
        if(!response.ok) // check stato risposta
            throw new Error(`response fetch error ${response.status}`); // in caso di errore stampa lo stato a console
        return response.json(); // ritorna la risposta codificata in json
    })
    .then(data => { // prende i dati ottenuti
        callback(data); // chiama la funzione di callback a cui passare i dati ottenuti
    })
    .catch(err => { // catch dell'errore in modo da stamparlo a console
        console.error('request error',err); // log dell'errore a console
    });
}

// funzione per impostare le linee di dialogo in base all'index preso dal server e far avanzare le immagini
function updateLines()
{
    fetchData("dialog-index",moveLines); // fa un fetch dell'index
}

// funzione che fa avanzare le linee di testo e aggiorna l'index lato server
function moveLines(index)
{
    const data = {"current_index": index + 1}; // dati con index da inviare
    sendToServer("update-index",data); // invia il nuovo index al server
}

// funzione che aggiusta il formato dele linee passate dal database e le inserisce in una variabile
function setLines(data)
{
    let lines = data.flatMap(obj => obj.text); // prende ogni linea di testo per gli oggetti estratti e la mappa all'oggetto
    console.log (lines); // log del risultato per check e debug
    dialogLines = lines; // assegna le linee di dialogo alla variabile globale
}

// funzione che manda i dati al server
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