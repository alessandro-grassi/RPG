function caricaAbilita() {
    fetch("http://localhost:8080/broffoni/sm_abilita", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: "{}"
    })
    .then(response => {
        if (!response.ok) {
            throw new Error("Errore nella risposta");
        }
        return response.json();
    })
    .then(data => {
        mostraAbilita(data.abilita);
    })
    .catch(error => {
        console.error(error);
        alert("Errore nel caricamento abilità");
    });
}

function mostraAbilita(lista) {
    const container = document.getElementById("lista-abilita");
    lista.forEach(a => {
        const div = document.createElement("div");
        div.textContent = `${a.id} - ${a.Forza} - ${a.Destrezza} - ${a.Intelligenza}`;
        container.appendChild(div);
    });
}

window.onload = caricaAbilita;
