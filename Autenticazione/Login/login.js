var k=0;

function changeVisibility(){
  if(k == 0){
    document.getElementById("registrazione").style.visibility = 'visible';
    document.getElementById("accesso").style.visibility = "hidden";
    k=1;
  }else if(k == 1){
    document.getElementById("registrazione").style.visibility = 'hidden';
    document.getElementById("accesso").style.visibility = "visible";
    k=0;
  }
}

function registrazione(){
  const username= document.getElementById('n_username').value;
  const password= document.getElementById('n_password').value;
  const email= document.getElementById('n_email').value;
 
  
  if(username=="" || password == "" || email == ""){
    alert("Non hai compilato tutti i campi")
  }else{
    const message={
      user : username, 
      pw : password,
      mail : email
    };
    fetch('http://localhost:8080/login/registrazione', {
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
          else alert("Registrazione effettuata con successo");
      }
    })
    .catch(error => {
      console.error("Errore:", error);

    });
  }

}

function accedi(){
  const username= document.getElementById('username').value;
  const password= document.getElementById('password').value;
  if(username == "" || password == ""){
    alert("Non hai compilato tutti i campi")
  }else{
    const message={
      user : username, 
      pw : password
    };
    fetch('http://localhost:8080/login/accesso', {
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
        if (data=="errore") alert("Errore nelle credenziali")
        else {
        alert("Accesso effettuato con successo");
          document.cookie="utente="+username;
          window.location="http://localhost:8080/personaggio";
        };
      }
    })
    .catch(error => {
      console.error("Errore:", error);

    });
  }
}



