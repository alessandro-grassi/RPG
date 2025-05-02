document.addEventListener("DOMContentLoaded",()=>{ // caricare il testo
    fetchFromServer("get-dialog").then(data=>{ // fetch dei dialoghi dal server
        dialogLines = data;// assegna le linee di dialogo alla variabile globale});
     });
    fetchFromServer("dialog-index").then(index=>{
        document.getElementById("dialog-box").textContent = formatDialog(dialogLines[index.current_index]); // imposta index corrente
        client_index = index.current_index; // salva index su index globale
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

//funzione che formatta il blocco di dialogo e controlla se ci sono immagini
function formatDialog(dialogLines)
{
    let finalDialog = "" // crea una variabile in cui fare lo store delle linee
    dialogLines.forEach(line =>{ // itera ogni linea della cella di dialogo
        if(line.fight != null) // controlla se ci sono reindirizzamenti a pagine di combattimento
        {
            sendToServer("update-index", { current_index: client_index });
            window.location.replace("http://localhost:8080/m5/" + line.fight); // redirect in modo che non si possa fare back alla pagina precedente
        }
        else
        {
            if(line.image == null) // nel caso non ci siano immagini da cambiare
                finalDialog += line + "\n"; // aggiunge le linee di testo al dialogo finale
            updateImage(line.image); // fa un update delle immagini
        }
    })
    return finalDialog; // restituisce dialogo finale
}

// funzione che permette di modificare l'index dei dialoghi
function movelines(step)
{
    if(client_index + step < dialogLines.length)
    {
        client_index += step; // incrementa index di quanto indicato dallo step
        const data = {"current_index": client_index}; // crea oggetto da inviare al server
        sendToServer("update-index",data); // invia al server l'index nuovo in modo da aggiornarlo
    }
    document.getElementById("dialog-box").textContent = formatDialog(dialogLines[client_index]); // imposta i dialoghi all' index corrente
    updateImage();
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

// funzione per aggiornare le immagini in base al dialogo
function updateImage(current_image)
{
    if(current_image != null)
    {
        document.getElementById("background-image").setAttribute("src", "http://localhost:8080/m5/get-image/" + current_image); // cambia l'attributo del tag con il percorso per l'immagine necessaria
        const data = {"last_image": current_image}; // crea oggetto da inviare al server
        sendToServer("update-last_image", data);
    }
    else
        fetchFromServer("dialog-index").then((image)=>{ // in caso non ci siano immagini da impostare prende l'ultima salvata
            document.getElementById("background-image").setAttribute("src","http://localhost:8080/m5/get-image/" + image.last_image); // carica ultima immagine salvata su progress.json
        });
}