async function caricaAbilita() {
    try {
        const response = await fetch('/abilita');
        if (!response.ok) throw new Error('Errore: ' + response.status);
        const dati = await response.json();
        document.getElementById('jsonOutput').textContent = JSON.stringify(dati, null, 2);
    } catch (e) {
        document.getElementById('jsonOutput').textContent = 'Errore: ' + e.message;
    }
}

window.addEventListener('DOMContentLoaded', caricaAbilita);
