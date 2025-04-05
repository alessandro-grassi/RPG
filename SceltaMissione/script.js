function get_missioni() {
    let uid = document.getElementById("uid").value;
    fetch("http://localhost:8080/sm_missioni", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({uid})
    }
    )
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
        let img = document.createElement("img");

        mis.innerHTML = "<h3>" + missione.nome + "</h3>" + missione.descrizione + "<br>";
        btn.onclick = () => {
            goToUrl(mis.url);
        }
        btn.innerHTML = "Partecipa";
        encoded_img = missione.img.split(",")[1];
        console.log(atob(encoded_img));
        img.src = atob(encoded_img);

        if(missione.completata) {
            mis.classList.add("completato");
        }
        else {
            mis.classList.add("missione");
        }
        mis.appendChild(img);
        mis.appendChild(btn);
        div.appendChild(mis);
    });
}

function goToUrl(url) {
    window.location.href = url;
}

setTimeout(() => {
    get_missioni();
}, 100);