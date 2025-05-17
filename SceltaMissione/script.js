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

        mis.innerHTML = `<h3>${missione.nome}</h3>${missione.descrizione}<br>`;             //aggiorna contenuto HTML di un elemento div creato dinamicamente
        btn.onclick = () => {
            goToUrl(missione.url);
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
        mis.style.backgroundSize = "100% 100%";
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

function setup()
{
    let personaggio = get_personaggio();
    document.getElementById('uid').value = personaggio;
}

setup();
function do_get() {
    fetch("http://localhost:8080/m1_get_generica")
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

    fetch("http://localhost:8080/m2_post_generica", {
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
