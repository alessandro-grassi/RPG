function updateMission(data) {
    if (!data || !data.description || !data.answers || !data.image) {
        console.error("Dati non validi:", data);
        return;
    }

    document.getElementById('description').textContent = data.description;

    const answersContainer = document.getElementById('answers');
    answersContainer.innerHTML = ''; // Puliamo le risposte precedenti

    data.answers.forEach((answer, index) => {
        const label = document.createElement('label');
        label.style.display = "block"; // Separiamo le risposte senza bisogno di `<br>`
        label.innerHTML = `<input type="radio" name="answer" value="${index + 1}"> ${answer}`;
        answersContainer.appendChild(label);
    });

    // Verifica se il bottone già esiste
    let submitButton = document.getElementById('submit');
    if (!submitButton) {
        submitButton = document.createElement('button');
        submitButton.id = 'submit';
        submitButton.textContent = 'Invia';
        answersContainer.appendChild(submitButton);
    }

    // Aggiorna l'immagine nello scenario
    const scenario = document.getElementById('scenario');
    scenario.innerHTML = ''; // svuota il contenuto del dom
    const img = document.createElement('img');
    img.src = data.image;
    img.alt = 'Scenario';
    scenario.appendChild(img);
}

// Esempio di dati ricevuti dal server, ancora da ridefinire le chiamate al server
const esempio = {
    description: "Sono il perfido Dr. Malvagio! Se non rispondi correttamente a questa domanda, ti trasformerò in un gatto! Quant'è 2 + 2?",
    answers: ["5", "4", "Cane", "134523"],
    image: "https://spacejockeyreviews.com/wp-content/uploads/2013/08/Dr.-Malvegio-011.jpg"
};

async function getData(){ 
    try{
        const response = await fetch("nome server");
        if (!response.ok){
            throw new Error(`Errore HTTP: ${responde.status}`);
        }
        const data = await response.json();
        console.log(data);
        updateMission(data); //dati ricevuti nel seguente moto:
        /*
        description: "descrizione",
        answers: ["risposta1", "risposta2"...],
        image: "url immagine"
        */
    } catch(error) {
        console.error("Errore durante la richiesta GET: ", error);
        logResult({error: error.message});
    }
}

async function inviaData(data){ //funzione per la POST della risposta selezionata dall'utente
    try{
        const response = await fetch("server name", {
            method : "POST",
            headers : { "Content-Type" : "application/json"},
            body : JSON.stringify(data)
        });
        if(!response.ok){
            throw new Error(`Errore HTTP: ${response.status}`);
        }
        const risposta = await response.json();
        console.log(risposta);

        if(risposta.result === 1){ //ricevo una risposta dal server con un JSON contenente il risultato, se è 1 allora è tutto corretto
            alert("Risposta corretta!");
            window.location.reload();
            //DA IMPLEMENTARE IL PASSAGGIO ALLA MISSIONE SUCCESSIVA
        }else if(risposta.result === 0){
            alert("No hai sbagliato!");
            window.location.reload();
        }else{
            alert("C'è stato un errore di comunicazione con il server!");
            window.location.reload();
        }
    } catch(error){
        console.error("Errore durante la richiesta POST: ", error);
    }
}


updateMission(esempio);
