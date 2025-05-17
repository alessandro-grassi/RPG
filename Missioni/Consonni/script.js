window.onload = function() {
    fetch('http://localhost:8080/')  
        .then(response => response.json())
        .then(data => {
            const container = document.getElementById('abilita-container');
            data.forEach(item => {
                const div = document.createElement('div');
                div.innerHTML = `
                    <p>ID: ${item.id}</p>
                    <p>Forza: ${item.Forza}</p>
                    <p>Destrezza: ${item.Destrezza}</p>
                    <hr>
                `;
                container.appendChild(div);
            });
        })
        .catch(error => {
            console.error('Errore:', error);
        });
};
