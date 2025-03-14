function get_missioni() {
    fetch("http://localhost:8080/sm_missioni")
    .then((respsonse) => {
        if(!respsonse.ok) {
            throw new Error("Errore di connessione")
        }
        return respsonse.json();
    })
    .then((data) => {
        loadMis(data.missioni);
    })
    .catch((e) => {
        alert("Errore");
        console.error(e);
    })
}

function loadMis(missioni) {
    let div = document.getElementById("missioni");

    missioni.forEach((missione) => {
        let mis = document.createElement("div");
        let btn = document.createElement("button");

        mis.innerHTML = "<h3>" + missione.nome + "</h3><br>" + missione.descrizione;
        btn.click = goToUrl(mis.url);
        btn.innerHTML = Partecipa;

    });
}

function goToUrl(url) {
    window.location.href = url;
}

get_missioni();