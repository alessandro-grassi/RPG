var k=1;
var j=0;

function changeVisibility(){
  if(k == 0){
    document.getElementById("scegli").style.visibility = 'visible';
    document.getElementById("crea").style.visibility = "hidden";
    k=1;
  }else if(k == 1){
    document.getElementById("scegli").style.visibility = 'hidden';
    document.getElementById("crea").style.visibility = "visible";
    k=0;
  }
}

function cambiaImmagine() {
    var selezione = document.getElementById("choice").value;
    var class_image = document.getElementById("class-image");
    var image_1 = "http://localhost:8080/personaggio/magoblu"
    var image_2 = "http://localhost:8080/personaggio/magorosso"
    var default_image = "https://cdn.pixabay.com/photo/2016/09/28/02/14/user-1699635_1280.png"

    if (selezione == "opzione1") {
        class_image.src = image_1;
    } else if (selezione == "opzione2") {
        class_image.src = image_2;
    } else {
        class_image.src = default_image;  // Non mostrare nulla altrimenti
    }
}


function listaClassi(){
  fetch('http://localhost:8080/personaggio/listaClassi')
    .then(response => {
      if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`);
      }
      return response.json(); // Decodifica la risposta JSON
    })
    .then(data => {
      // Mostra il messaggio nella pagina
      let classi = data;
      let select = document.getElementById("choice");

      classi.forEach((classe)=> {
        let option = document.createElement("option");
        option.textContent=classe;
        option.value=classe;
        select.appendChild(option);
        });
    })
    .catch(error => {
      console.error("Errore durante la chiamata REST:", error);
      alert("Errore di connesione, riprova più tardi!");
    });

}


async function cerca_personaggi(){
  let resp = await fetch('http://localhost:8080/personaggio/listaPersonaggi',{
    "method":"POST",
    "body": '"'+get_utente()+'"'
  });
  json = await resp.json();
  str="";
  json.forEach(
    data=>{
        str+="<option value='"+data[0]+"'>"+data[1]+"</option>";
    }
  )
  document.getElementById("my_pers").innerHTML=str;
	  
}


async function statistics() {
  const A = document.getElementById("A");
  const B = document.getElementById("B");
  const C = document.getElementById("C");
  const D = document.getElementById("D");
  const E = document.getElementById("E");


    const response = await fetch('http://localhost:8080/personaggio/statistiche', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({classe: document.getElementById("choice").value})
    });

    if (!response.ok)
      throw new Error(`HTTP error! Status: ${response.status}`);
    
    const data = await response.json();

    A.textContent = 'Vigore: ' + data[0];
    B.textContent = 'Forza: ' + data[1];
    C.textContent = 'Destrezza: ' + data[2];
    D.textContent = 'Intelligenza: ' + data[3];
    E.textContent = 'Fede: ' + data[4];

}



function mostraAbilita(){
  document.getElementById("ab1").style.visibility = 'visible';
  document.getElementById("ab2").style.visibility = 'visible';
  document.getElementById("ab3").style.visibility = 'visible';
  j=1;

}
function fillAb(json){
  str = "<option value='default'>Seleziona abilita'</option>"
  json.forEach(a =>{
    if (a!="default")
    str+="<option value='"+a+"'>"+a+"</option>";
  })
  document.getElementById("ab1").innerHTML=str;
  document.getElementById("ab2").innerHTML=str;
  document.getElementById("ab3").innerHTML=str;
}
async function listaAbilita(){
  if(j!=0){
    let classe = document.getElementById("choice").value;
    const message={
      class : classe
    };
    let resp = await fetch('http://localhost:8080/personaggio/listaAbilita', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(message)
    });
    if (resp.ok){
      json = await resp.json();
      console.log(json);
      fillAb(json);
    }
    
  j=0;
    
  }
}


function next_page(){
  document.cookie="personaggio="+document.getElementById("my_pers").value;
  window.location="http://localhost:8080/sm_home";
}


function crea_personaggio(){
  const nome = document.getElementById("name").value;
  const classe = document.getElementById("choice").value;
  const ab1 = document.getElementById("ab1").value;
  const ab2 = document.getElementById("ab2").value;
  const ab3 = document.getElementById("ab3").value;
  const usname = get_utente();
  const message={
    username: usname,
    name: nome,
    class: classe,
    ability1 : ab1,
    ability2 : ab2,
    ability3 : ab3
  };
  fetch('http://localhost:8080/personaggio/crea_personaggio', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(message)
  })
  .then(response => {
    if (!response.ok) {
      throw new Error('Errore nella risposta del server.');
    }
    return response.json();
  })
  .then(data => {
    if (data.error) {
      alert("Errore di connessione, riprova più tardi!")
    } else {
      if (data=="errore") alert("Errore Client")
        else alert("Personaggio registrato con successo");
    }
  })
  .catch(error => {
    console.error("Errore:", error);

  });
}