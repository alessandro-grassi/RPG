document.getElementById('register-form').addEventListener('submit', function(event) {
    event.preventDefault();
    const newUser = {
        username: document.getElementById('username').value,
        nome: document.getElementById('nome').value,
        cognome: document.getElementById('cognome').value,
        data_nascita: document.getElementById('data_nascita').value,
        password: document.getElementById('password').value,
    };
    fetch('http://localhost:8080/users', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(newUser)
    }).then(response => response.json())
      .then(() => {
          document.getElementById('register-form').reset();
          fetchUsers();
      });
});

function fetchUsers() {
    fetch('http://localhost:8080/users')
        .then(response => response.json())
        .then(users => {
            const userList = document.getElementById('user-list');
            userList.innerHTML = '';
            users.forEach(user => {
                const li = document.createElement('li');
                li.textContent = `User: ${user.username} | Nome: ${user.nome} | Cognome: ${user.cognome}`;
                userList.appendChild(li);
            });
        });
}

document.getElementById('toggle-users').addEventListener('click', function() {
    testo = document.getElementById('toggle-users')
    const userList = document.getElementById('user-list');
    if (userList.style.display === 'none') {
        userList.style.display = 'block';
        testo.textContent = 'Nascondi utenti registrati'
        fetchUsers();
    } else {
        userList.style.display = 'none';
        testo.textContent = 'Mostra utenti registrati'
    }
});