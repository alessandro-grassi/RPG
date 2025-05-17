document.addEventListener("DOMContentLoaded",()=>{ 
    fetch("http://localhost:8080/es/api/get-abilita")
    .then(response => {
        if (!response.ok) {
            throw new Error(`Errore HTTP! Status: ${response.status}`);
        }
        return response.json();
    })
    .then(data => {
        console.log("Dati ricevuti:", data);
        document.getElementById("output").innerText = JSON.stringify(data, null, 2);
    })
    .catch(error => {
        console.error("Si è verificato un errore:", error);
    });
});




