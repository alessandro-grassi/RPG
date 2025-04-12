function completion() {
    //campi nell'header della pagina
    let uid = document.getElementById("uid").value;     //uid e' un campo hidden che specifica l'id del personaggio utilizzato
    let mid = document.getElementById("mid").value;     //mid e' un campo hidden che specifica l'id della missione svolta

    fetch("http://localhost:8080/cm_complete",{
        method : "POST",
        headers : {"Content-Type" : "application/json"},
        body :JSON.stringify({uid,mid}) 
    })
    .then((response) => {
        if(!response.ok) {
            throw new Error("Errore di connessione: impossibile inviare dati al server");
        }
        return response.json()
    })
    .then((data) => {
        if(data.error != null) {
            alert(data.error)
        }
        else {
            alert(data.success)
        }
    })
    .catch((e) => {
        console.error(e);
        alert("Errore di connessione");
    })

}

completion()