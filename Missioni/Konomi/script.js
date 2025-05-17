function caricaIndizi() {
    fetch('http://localhost:8080/konomi/caricatutto', { method: 'GET' })
        .then(response => response.json())
        .then(data => {
            const spazio = document.getElementById('spazio');

            spazio.innerHTML = data;
        })
        .catch(error => {
            console.error("Si è verificato un errore:", error);
        });
}