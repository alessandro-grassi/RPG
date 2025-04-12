document.addEventListener('DOMContentLoaded', () => {
  const DIM = 10;
  const PERCORSO = ['9-0','8-0','7-0','7-1','7-2','6-2','5-2','5-3','5-4','4-4','3-4','3-5','3-6','2-6','1-6','1-7','1-8','0-8','0-9'];
  
  const stato = {
    x: 9,
    y: 0,
    vite: 3,
    punti: 0,
    attivo: true,
    fuori: false
  };

  // Inizializza trappole casuali
  const trappole = [];
  while(trappole.length < 5) {
    const x = Math.floor(Math.random() * DIM);
    const y = Math.floor(Math.random() * DIM);
    const key = `${x}-${y}`;
    
    if(!PERCORSO.includes(key) && !(x === 9 && y === 0) && !(x === 0 && y === 9)) {
      trappole.push(key);
    }
  }

  function aggiornaMappa() {
    let html = '';
    
    for(let x = 0; x < DIM; x++) {
      for(let y = 0; y < DIM; y++) {
        const key = `${x}-${y}`;
        let classi = ['cella'];
        let contenuto = '';
        
        if(x === stato.x && y === stato.y) {
          classi.push('giocatore');
          contenuto = 'G';
        } else if(x === 9 && y === 0) {
          classi.push('partenza');
          contenuto = 'S';
        } else if(x === 0 && y === 9) {
          classi.push(stato.fuori ? 'porta-chiusa' : 'porta');
          contenuto = 'P';
        } else {
          classi.push('cespuglio');
          const visibile = Math.abs(x - stato.x) <= 1 && Math.abs(y - stato.y) <= 1;
          
          if(visibile) {
            classi.push('visibile');
            if(trappole.includes(key)) classi.push('trappola');
            if(PERCORSO.includes(key)) classi.push('percorso');
          }
        }
        
        html += `<div class="${classi.join(' ')}">${contenuto}</div>`;
      }
    }
    
    document.getElementById('mappa').innerHTML = html;
    document.getElementById('vite').textContent = stato.vite;
    document.getElementById('punti').textContent = stato.punti;
  }

  function muovi(dx, dy) {
    if(!stato.attivo) return;
    
    const nx = stato.x + dx;
    const ny = stato.y + dy;
    
    // Controlla confini
    if(nx < 0 || nx >= DIM || ny < 0 || ny >= DIM) return;
    
    // Blocca porta se fuori percorso
    if(nx === 0 && ny === 9 && stato.fuori) {
      document.getElementById('messaggio').textContent = 'Porta chiusa! Torna al percorso';
      return;
    }
    
    // Aggiorna posizione
    stato.x = nx;
    stato.y = ny;
    stato.punti++;
    
    // Controlla trappole
    if(trappole.includes(`${stato.x}-${stato.y}`)) {
      stato.vite--;
      document.getElementById('messaggio').textContent = 'Trappola! -1 vita';
      
      if(stato.vite <= 0) {
        stato.attivo = false;
        document.getElementById('messaggio').textContent = 'GAME OVER!';
        document.getElementById('reset').classList.remove('hidden');
      }
    }
    
    // Controlla percorso
    stato.fuori = !PERCORSO.includes(`${stato.x}-${stato.y}`);
    
    // Vittoria
    if(stato.x === 0 && stato.y === 9 && !stato.fuori) {
      stato.attivo = false;
      document.getElementById('messaggio').textContent = `VITTORIA! Punti: ${stato.punti}`;
      document.getElementById('reset').classList.remove('hidden');
    }
    
    aggiornaMappa();
  }

  // Event listeners
  document.addEventListener('keydown', (e) => {
    const movimenti = {
      'ArrowUp': [-1, 0],
      'ArrowDown': [1, 0],
      'ArrowLeft': [0, -1],
      'ArrowRight': [0, 1]
    };
    
    if(movimenti[e.key]) {
      muovi(...movimenti[e.key]);
    }
  });

  document.getElementById('reset').addEventListener('click', () => {
    location.reload();
  });

  // Inizializzazione
  aggiornaMappa();
});