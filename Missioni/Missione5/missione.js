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
    const container = document.getElementById("dialog-container"); // prende container per bottone
    const nextButton = document.createElement("button"); // crea bottone next
    nextButton.className = "dialog-button";
    nextButton.id = "next-button"; // aggiunge id bottone
    nextButton.textContent = "next"; // imposta text content
    nextButton.addEventListener("click",()=>{
            movelines(1); // imposta incremento linee
    });
    container.appendChild(nextButton); // appende bottone a container
    skipButton(); // aggiunge skip button assieme a next-button
}

//funzione che formatta il blocco di dialogo e controlla se ci sono immagini
function formatDialog(dialogLines)
{
    let finalDialog = "" // crea una variabile in cui fare lo store delle linee
    dialogLines.forEach(line =>{ // itera ogni linea della cella di dialogo
        if(line.fight != null) // controlla se ci sono reindirizzamenti a pagine di combattimento
        {
            sendToServer("update-index", { current_index: client_index + 1}).then(function(){
                window.location.replace("http://localhost:8080/m5/" + line.fight); // redirect in modo che non si possa fare back alla pagina precedente
            });
            return "";
        }
        if(line.choice == "end") // caso in cui si arriva alla fine della missione
        {
            if(line.image == null) // nel caso non ci siano immagini da cambiare
                finalDialog += line + "\n"; // aggiunge le linee di testo al dialogo finale
            updateImage(line.image); // fa un update delle immagini
            endChoice(); // aggiunge bottone di restart missione
            endMission(); // tasto per uscire dalla missione
            removeNext(true); // rimuove tasto next
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

// funzione che genera due button per ricominciare la missione
function endChoice()
{
    const container = document.getElementById("dialog-container"); // prende container dove mettere bottoni
    const newRun = document.createElement("button"); // crea bottone di restart missione
    newRun.textContent = "nuova run"; // imposta text content bottone
    newRun.id = "new-run-button"; // imposta id al bottone incaso servisse
    newRun.className = "dialog-button"; // classe per styling
    newRun.onclick = function() { // event handler per click bottone
        const data = {"current_index":0}; // setta index a 0 per far ricominciare la missione
        sendToServer("update-index",data).then(function(){// invia dati al server
            window.location.reload(); // ricarica la pagina a nuovo index
        }); 
    }
    container.appendChild(newRun); // appende il bottone al div container
}

// funzione che fa uscire dalla missione
function endMission()
{
    const container = document.getElementById("dialog-container");
    const endRun = document.createElement("button");
    endRun.textContent = "termina missione";
    endRun.id = "exit-run";
    endRun.className = "dialog-button";
    endRun.onclick = function() {
        console.log("aggiungere parte che rimanda a selezione missioni");
    }
    container.appendChild(endRun);
}

// sotto funzione che rimuove il button next
function removeNext(flag)
{
    if(flag) // se flag true rimuove next-button
    {
        document.getElementById("next-button").remove();
        document.getElementById("skip-button").remove();
    }
    else // rimuove tasti di fine missione
    {
        document.getElementById("new-run-button").remove(); // rimuove bottone 
        document.getElementById("exit-run").remove(); // rimuove bottone
        setButton(); // imposta bottone next
    }
}

// funzione che crea il tasto skip
function skipButton()
{
    const container = document.getElementById("dialog-container"); // prende container
    const skipButton = document.createElement("button"); // crea bottone di skip
    skipButton.textContent = "salta dialoghi"; // textcontent bottone
    skipButton.id = "skip-button"; // setta id
    skipButton.className = "dialog-button"; // classe per styling
    skipButton.onclick = function() {
        moveToFight(); // sposta al primo fight trovato
    }
    container.appendChild(skipButton); // aggiunge bottone skip a container
}

// sotto funzione che recuperar gli index che fanno partire i fight
function moveToFight()
{
    let flag = false; // indica se è stata trovata una fight
    let i = client_index;
    while( i+1 < dialogLines.length && flag == false) // while itera i blocchi di dialogo a partire da quello corrente
    {
        dialogLines[i].forEach(line => { // itera ogni linea del blocco
            if(line.image != null)
            {
                const data = {"last_image": current_image}; // crea oggetto da inviare al server
                sendToServer("update-last_image", data);
            }
            else if(line.fight != null || line.choice != null) // caso in cui trova una linea che avvia un fight
            {
                flag = true; // fa terminare loop
                movelines(i-client_index); // sposta la pagina allo start della boss fight
            }
        });
        i ++; // incrementa i per andare al prossimo blocco di dialogo
    }
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
    return fetch("http://localhost:8080/m5/" + request,{
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