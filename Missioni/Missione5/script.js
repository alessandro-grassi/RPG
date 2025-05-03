
document.addEventListener("DOMContentLoaded", function(){ //esegue il codice solo dopo che la pagina è stata completamente caricata

    function caricaMissione(){
        
        let missione = {
            testo: "Qual è il colore del cielo di giorno?", // Testo della domanda
            opzioni: ["Rosso", "Blu", "Azzurro", "Giallo"], // Opzioni di risposta
            immagine: "/image" // Percorso dell'immagine da mostrare
        };

        
        document.getElementById("description").textContent = missione.testo; //imposta il testo della domanda

        
        let risposte = document.getElementById("answers");
        risposte.innerHTML = ""; //pulisco eventuali risposte precedenti

        
        missione.opzioni.forEach((opzione) => {
            let label = document.createElement("label");
            //radio button
            label.innerHTML = `<input type='radio' name='risposta' value='${opzione}'> ${opzione}`;
            risposte.appendChild(label); 
            risposte.appendChild(document.createElement("br")); 
        });

        document.getElementById("scenario").innerHTML = `<img src="${missione.immagine}" alt="Scenario">`;
    }
//quando la pagina è pronta carico la massione
    caricaMissione();
});
function Sconfitta(){
    window.location.href="/pagina_sconfitta"; 
}
function MissioneSuccessiva(){
    window.location.href="/missione2";
}

function invia(){
    let risposta = document.querySelector('input[name="risposta"]:checked');
    console.log(risposta.value); 
    if (!risposta) {
        alert("Seleziona una risposta!");
        return;
    }
    let rispostaCorretta = "Blu"; //risposta corretta
    if (risposta.value === rispostaCorretta) { //se la risposta è corretta
        alert("Risposta corretta!"); //messaggio di successo
        MissioneSuccessiva(); //passa alla missione successiva
    } else {
        alert("Risposta sbagliata!"); //messaggio di errore
        Sconfitta(); //passa alla schermata di sconfitta
    }
}
