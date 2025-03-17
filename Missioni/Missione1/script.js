function do_get() {
    fetch("http://localhost:8080/missione1/get_generica")
    .then((response) => {
        if(!response.ok) {
            throw new Error("Errore connessione"); 
        }
        return response.json();
    })
    .then((data) => {
        alert(data);
    })
    .catch((e) => {
        console.error(e);
        alert("Errore");
    })
}

function do_post() {
    let nome = document.getElementById("nome").value;
    if(nome == "") {
        alert("manca il nome");
        return;
    }

    fetch("http://localhost:8080/missione1/post_generica", {
        method: "POST",
        headers: {"Content-Type" : "application/json"},
        body: JSON.stringify({nome})
    })
    .then((response) => {
        if(!response.ok) {
            throw new Error("Errore connessione"); 
        }
        return response.json();
    })
    .then((data) => {
        alert(data);
    })
    .catch((e) => {
        console.error(e);
        alert("Errore");
    })
}