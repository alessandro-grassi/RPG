function get_data() {
    fetch("http://localhost:8080/demo_getData")
    .then((response) => {
        if(!response.ok) {
            throw new Error("errore di connessione");
        }
        return response.json()
    })
    .then((data) => {
        fill(data.dati);
    })
    .catch((e) => {
        alert("errore");
        console.error(e);
    })
}

function fill(data) {
    let div = document.getElementById("div");
    data.forEach(row => {
        div.innerHTML += row + "<br>";
    });
}

get_data();