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
        //let img = document.createElement("img");

        mis.innerHTML = "<h3>" + missione.nome + "</h3>" + missione.descrizione + "<br>";
        btn.onclick = () => {
            goToUrl(mis.url);
        }
        btn.innerHTML = "Partecipa";
        //img.src = missione.img;

        if(missione.completata) {
            mis.classList.add("completato");
        }
        else {
            mis.classList.add("missione");
        }
        //mis.appendChild(img);
        //mis.innerHTML += "<br>"
        mis.style.backgroundImage = `url('${missione.img}')`;
        mis.style.backgroundSize = "contain";
        mis.style.backgroundRepeat = "no-repeat";  
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