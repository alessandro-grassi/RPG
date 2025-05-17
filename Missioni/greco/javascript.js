document.addEventListener("DOMContentLoaded",()=>{ 
    fetchFromServer("classi").then(data=>{ 
        console.log(data);
     });
});

function fetchFromServer(request)
{
    return fetch("http://localhost:8080/greco/" + request)
    .then((response) => {
        if(!response.ok)
            throw new Error(`response fetch error ${response.status}`);
        return response.json();
    })
    .then((data) => {
        console.log("fetched data:",data);
        return data;
    })
    .catch((err) => {
        console.error('request error: ',err);
        throw err;
    })
}