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
        label.style.display = "flex"; // Allineamento orizzontale delle risposte
        label.innerHTML = `<input type="radio" name="answer" value="${index + 1}"> ${answer}`;
        answersContainer.appendChild(label);
    });

    // Verifica se il bottone già esiste
    let submitButton = document.getElementById('submit');
    if (!submitButton) {
        submitButton = document.createElement('button');
        submitButton.id = 'submit';
        submitButton.textContent = 'Invia Risposta';
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

// Esempio di dati ricevuti dal server
const esempio = {
    description: "Sono la strega cattiva, rispondi correttamente o ti ridurrò in polvere! Ho città, ma non case. Ho montagne, ma non alberi. Ho acqua, ma non pesce. Che cosa sono?",
    answers: ["Una mappa", "Un castello", "L'Italia", "Una valigia"],
    image: "https://www.onestoespietato.com/wp-content/uploads/2014/06/maleficent.jpg"
};

updateMission(esempio);
function Sconfitta(){
    window.location.href="../Missione5/Missione_Finale/pagina_boss_finale/sconfitta.html";
}
function MissioneSuccessiva(){
    window.location.href="../Missione5/Missione2/memory/index.html";
}

function invia() {
    const risposta = document.querySelector('input[name="answer"]:checked');
    if (!risposta) {
        alert("Seleziona una risposta!");
        return;
    }

    const rispostaCorretta = 1; // Indice corretto (1 = "Una mappa")
    if (parseInt(risposta.value) === rispostaCorretta) {
        alert("Risposta corretta!");
        MissioneSuccessiva();
    } else {
        alert("Risposta sbagliata!");
        Sconfitta();
    }
}