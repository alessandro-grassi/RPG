document.addEventListener("DOMContentLoaded",()=>{ // caricare il testo
    fetchFromServer("get-dialog").then(data=>{ // fetch dei dialoghi dal server
        let lines = data.flatMap(obj => obj.text); // prende ogni linea di testo per gli oggetti estratti e la mappa all'oggetto
        dialogLines = lines; // assegna le linee di dialogo alla variabile globale});
     });
    // fetch mapping immagini testo
    fetchFromServer("get-mapping").then(data=>{ 
        imageMapping = data; // salva il mapping dell'immagine in un file json
    });
    fetchFromServer("dialog-index").then(index=>{
        document.getElementById("dialog-box").textContent = dialogLines[index.current_index]; // imposta index corrente
        client_index = index.current_index; // salva index su index globale
        updateImage(); // imposta l'immagine
        console.log(checkImage()); // preso il mapping controlla se alle linee di testo sono associate immagini
    });
    setButton();
});

let dialogLines; // variabile globale per lo store delle linee di dialogo da scorrere
let imageMapping; // variabile usata per salvare la mappatura delle immagini
let client_index; // variabile globale per lo store lato client dell'index a cui si trova il dialogo e le immagini

// funzione usata per impostare l'evento legato al bottone per far avanzare o tornare indietro il testo
function setButton(){
    document.getElementById("next-button").addEventListener("click",function(){
        movelines(1); // imposta incremento linee
    });
}

// funzione che permette di modificare l'index dei dialoghi
function movelines(step)
{
    client_index += step; // incrementa index di quanto indicato dallo step
    document.getElementById("dialog-box").textContent = dialogLines[client_index]; // imposta i dialoghi all' index corrente
    const data = {"current_index": client_index}; // crea oggetto da inviare al server
    //sendToServer("update-index",data); // invia al server l'index nuovo in modo da aggiornarlo
    console.log(checkImage()); // log immagini corrispondenti
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

// funzione di fetch

// funzione che controlla se al dialogo corrente è associata un immagine
function checkImage()
{
    let  match =  false; // restituisce null se non vengono trovati match 
    imageMapping.forEach(mapping => { // controlla se a ogni dialogo corrisponde un immagine
        if(mapping.dialog.normalize("NFC").trim() === dialogLines[client_index].normalize("NFC").trim()) // se trova un mapping per il dialogo
            match = mapping.image; // ritorna nome immagine da recuperare
    });
    return match; // fa il return del match
}

// funzione per aggiornare le immagini in base al dialogo
function updateImage()
{
    const matchFound = checkImage(); // recupera il nome dell'immagine
    if(matchFound)
        document.getElementById("background-image").setAttribute("src", "http://localhost:8080/m5/get-image/" + matchFound); // cambia l'attributo del tag con il percorso per l'immagine necessaria
}