function sendToServer(request,data)
{
    fetch("http://localhost:8080/m5/" + request,{
        method:"POST", 
        headers:{'Content-Type':'application/json'},
        body: JSON.stringify(data)
    })
    .then((response)=>{ 
        if(!response.ok) 
        {
            alert('operazione fallita, riprovare o ricaricare la pagina'); 
            throw new Error(`error posting content to server: ${response.status}`); 
        }
        return response.json(); 
    })
    .then((result)=>{
        console.log(result); 
    })
    .catch((err)=>{ 
        console.error('error POST data: ',err);
        alert('operazione fallita, riprovare o ricaricare la pagina.\n\ncodice di errore: '+ err); 
    });
}

function fetchData(request,callback)
{
    fetch("http://localhost:8080/m5/" + request)
    .then(response => {
        if(!response.ok) 
            throw new Error(`response fetch error ${response.status}`);
        return response.json();
    })
    .then(data => { 
        console.log("GET body data: ");
        console.log(data) 
        callback(data);
    })
    .catch(err => { 
        console.error('request error',err);
    });
}
