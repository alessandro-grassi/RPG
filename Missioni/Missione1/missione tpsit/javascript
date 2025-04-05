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
    description: "Sono il perfido Dr. Malvagio! Se non rispondi correttamente a questa domanda, ti trasformerò in un gatto! Quant'è 2 + 2?",
    answers: ["5", "4", "Cane", "134523"],
    image: "https://spacejockeyreviews.com/wp-content/uploads/2013/08/Dr.-Malvegio-011.jpg"
};

updateMission(esempio);