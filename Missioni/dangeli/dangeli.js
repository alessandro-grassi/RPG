function listaAbilita(){
fetch('http://localhost:8080/dangeli/listaAbilita')
    .then(response => {
    if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`);
    }
    return response.json(); // Decodifica la risposta JSON
    })
    .then(data => {
    // Mostra il messaggio nella pagina
    let abilita = data;
    let divApp = document.getElementById("container");

    abilita.forEach((ab)=> {
        let div = document.createElement("div");
        div.textContent=ab;
        divApp.appendChild(div);
        });
    })
    .catch(error => {
    console.error("Errore durante la chiamata REST:", error);
    alert("Errore di connesione, riprova più tardi!");
    });

}