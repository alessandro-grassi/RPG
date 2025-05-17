fetch('http://localhost:8080')
    .then(res => res.json())
    .then(data => {
        const container = document.getElementById('output');
        data.forEach(row => {
            const p = document.createElement('p');
            p.textContent = `ID: ${row.ID}, VIGORE: ${row.VIGORE}, FORZA: ${row.FORZA}`;
            container.appendChild(p);
        });
    })
    .catch(err => {
        console.error('Errore nel recupero dati:', err);
    });

