document.addEventListener('DOMContentLoaded', () => {
    // Funzione per recuperare i dati delle classi
    async function recuperaClassi() {
        try {
            // Chiamata al backend per ottenere i dati delle classi
            const response = await fetch('http://localhost:8080/personaggio/classi'); // Cambia l'URL in base al tuo backend
            if (!response.ok) {
                throw new Error('Errore nella chiamata al backend');
            }
            
            // Decodifica la risposta JSON
            const classi = await response.json();
            
            // Trova la tabella
            const tableBody = document.getElementById('classi-table').getElementsByTagName('tbody')[0];
            
            // Aggiungi le righe alla tabella
            classi.forEach(classe => {
                const row = tableBody.insertRow();
                row.insertCell(0).textContent = classe.ID;        // Assumendo che l'ID sia nella proprietà 'ID'
                row.insertCell(1).textContent = classe.VIGORE;    // Assumendo che 'VIGORE' sia un campo
                row.insertCell(2).textContent = classe.FORZA;     // Assumendo che 'FORZA' sia un campo
            });
        } catch (error) {
            console.error('Errore durante il recupero delle classi:', error);
            alert('Si è verificato un errore durante il recupero dei dati.');
        }
    }

    // Chiamata della funzione
    recuperaClassi();
});
