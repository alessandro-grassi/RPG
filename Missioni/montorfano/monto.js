function getDati()
{
    fetch('http://localhost:8080/esercitazione-montorfano/getDati', 
    { method: 'GET' })
    .then(response => response.json())
    .then(data => 
    {
        //ricavo p
        const p = document.getElementById("dataContainer");
        p.textContent = data;
    })
    .catch(error => {
        console.error("Si è verificato un errore:", error);
        document.getElementById('lista-indizi').innerHTML = '<li>Errore nel caricamento degli indizi. Riprova più tardi.</li>';
    });
}