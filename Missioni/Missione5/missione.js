document.addEventListener("DOMContentLoaded",()=>{ // caricare il testo
    fetchData("get-dialogue",setLines);
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

// funzione che aggiusta il formato dele linee passate dal database e le inserisce in una variabile
function setLines(data)
{
    let lines = data.flatMap(obj => obj.text); // prende ogni linea di testo per gli oggetti estratti e la mappa all'oggetto
    console.log (lines); // log del risultato per check e debug
    dialogLines = lines; // assegna le linee di dialogo alla variabile globale
    document.getElementById("dialog-box").textContent = lines[0];
}

// funzione che fa avanzare le linee di testo
function moveLines()
{}