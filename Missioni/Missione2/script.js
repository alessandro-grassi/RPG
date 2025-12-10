// script.js

document.addEventListener('DOMContentLoaded', () => {
  const DIM = 10;
  let livello = 0;
  let vite = 3, punti = 0, mosse = 0;
  let gameActive = true;
  let player, percorsoDisabilitato, trappole, indizi;
  let layoutIce, currentStep, timerId, timeLeft;

  // Livello 3 (Vulcano)
  let mapA, mapB, nextToggle;

  const plateOrder = ['3-3','6-5','5-7'];
  const startC = { x:9, y:0 }, goalC = { x:0, y:9 };
  const percorsoC = [
    '9-0','8-0','7-0','7-1','7-2','6-2',
    '5-2','5-3','5-4','4-4','3-4','3-5','3-6',
    '2-6','1-6','1-7','1-8','0-8','0-9'
  ];
  const startG = { x:9, y:0 }, goalG = { x:0, y:9 };
  const layoutGhiaccio = [
    ['N','N','N','N','N','N','N','N','N','N'],
    ['N','I','I','I','I','I','I','I','I','N'],
    ['N','I','N','N','N','N','N','N','I','N'],
    ['N','I','N','T1','I','I','I','N','I','N'],
    ['N','I','N','I','N','N','N','N','I','N'],
    ['N','I','I','I','N','I','T2','I','I','N'],
    ['N','N','N','I','N','N','N','I','I','N'],
    ['S','I','I','I','N','T3','N','N','I','N'],
    ['N','N','N','N','N','N','N','N','N','N'],
    ['N','N','N','N','N','N','N','N','N','N']
  ];

  const mappa   = document.getElementById('mappa');
  const msgEl   = document.getElementById('messaggio');
  const viteEl  = document.getElementById('vite');
  const puntiEl = document.getElementById('punti');
  const mosseEl = document.getElementById('mosse');
  const reset   = document.getElementById('reset');
  reset.addEventListener('click', () => location.reload());

  function genMap() {
    const m = Array.from({ length: DIM }, () => Array(DIM).fill('E'));
    let cnt = 0;
    while (cnt < 40) {
      const x = Math.floor(Math.random() * DIM);
      const y = Math.floor(Math.random() * DIM);
      if (m[y][x] === 'E' && !(x === 0 && y === 0) && !(x >= 8 && y <= 1)) {
        m[y][x] = 'L';
        cnt++;
      }
    }
    return m;
  }

  function startTimer() {
    timeLeft = 20;
    timerId = setInterval(() => {
      timeLeft--;
      if (timeLeft <= 0) {
        clearInterval(timerId);
        gameActive = false;
        msgEl.textContent = 'TIME OUT! Game Over';
        reset.classList.remove('hidden');
      } else if (livello === 1) {
        msgEl.textContent = `Secondo livello: premi piastre in ordine! Tempo: ${timeLeft}s`;
      } else if (livello === 2) {
        msgEl.textContent = `Terzo livello: evita la lava! Tempo: ${timeLeft}s`;
        draw();
      }
    }, 1000);
  }

  function initLivello() {
    vite = 3; punti = 0; mosse = 0; gameActive = true;
    clearInterval(timerId);
    reset.classList.add('hidden');

    if (livello === 0) {
      // Livello 1
      player = { ...startC };
      percorsoDisabilitato = false;
      trappole = new Set();
      while (trappole.size < 5) {
        const x = Math.floor(Math.random() * DIM);
        const y = Math.floor(Math.random() * DIM);
        const c = `${x}-${y}`;
        if (!percorsoC.includes(c) && c !== `${startC.x}-${startC.y}` && c !== `${goalC.x}-${goalC.y}`) {
          trappole.add(c);
        }
      }
      indizi = {};
      percorsoC.forEach(c => {
        if (c !== `${startC.x}-${startC.y}` && c !== `${goalC.x}-${goalC.y}`) {
          const [x, y] = c.split('-').map(Number);
          const dirs = [];
          if (percorsoC.includes(`${x-1}-${y}`)) dirs.push('SU');
          if (percorsoC.includes(`${x+1}-${y}`)) dirs.push('GIU');
          if (percorsoC.includes(`${x}-${y-1}`)) dirs.push('SINISTRA');
          if (percorsoC.includes(`${x}-${y+1}`)) dirs.push('DESTRA');
          indizi[c] = dirs.join(' o ');
        }
      });
      viteEl.textContent = vite;
      puntiEl.textContent = punti;
      mosseEl.textContent = mosse;
      msgEl.textContent = 'Primo livello: evita i cespugli-trappola!';
    }
    else if (livello === 1) {
      // Livello 2
      player = { ...startG };
      layoutIce = layoutGhiaccio;
      currentStep = 0;
      viteEl.textContent = '';
      puntiEl.textContent = '';
      mosseEl.textContent = mosse;
      msgEl.textContent = 'Secondo livello: premi piastre in ordine!';
      startTimer();
    }
    else {
      // Livello 3
      player = { x: 9, y: 9 };
      mapA = genMap();
      mapB = genMap();
      nextToggle = Date.now() + 3000;  // <--- 3 secondi
      viteEl.textContent = vite;
      msgEl.textContent = 'Terzo livello: evita la lava!';
      startTimer();
    }

    draw();
  }

  function draw() {
    const now = Date.now();
    const phase = now % 3000;
    const inTrans = phase >= 2000;
    let html = '';

    for (let y = 0; y < DIM; y++) {
      for (let x = 0; x < DIM; x++) {
        const cls = ['cella'];
        let content = '';

        if (livello === 0) {
          // draw livello 1
          const c = `${x}-${y}`;
          if (x===player.x && y===player.y) {
            cls.push('giocatore'); content = 'G';
          } else if (c===`${startC.x}-${startC.y}`) {
            cls.push('partenza'); content = 'S';
          } else if (c===`${goalC.x}-${goalC.y}`) {
            cls.push(percorsoDisabilitato ? 'porta-chiusa' : 'porta'); content = 'P';
          } else {
            cls.push('cespuglio');
            if (Math.abs(x-player.x) <= 1 && Math.abs(y-player.y) <= 1) {
              cls.push('visibile');
              if (trappole.has(c))       { cls.push('trappola'); content='X'; }
              else if (percorsoC.includes(c) && !percorsoDisabilitato) content='*';
              else if (indizi[c]) content='i';
            }
          }
        }
        else if (livello === 1) {
          // draw livello 2
          const cell = layoutIce[y][x], coord = `${x}-${y}`;
          if (x===player.x && y===player.y) {
            cls.push('player');
          } else if (coord===`${startG.x}-${startG.y}`) {
            cls.push('start');
          } else if (coord===`${goalG.x}-${goalG.y}`) {
            cls.push(currentStep===plateOrder.length ? 'porta' : 'porta-chiusa'); content='P';
          } else if (cell.startsWith('T')) {
            const i = plateOrder.indexOf(coord);
            cls.push(`plate${i+1}`);
            content = currentStep>i ? '✔' : 'O';
            if (currentStep>i) cls.push('plate-pressed');
          } else if (cell==='I') cls.push('ice');
          else cls.push('snow');
        }
        else {
          // draw livello 3
          if (x===player.x && y===player.y) {
            cls.push('giocatore'); content = 'G';
          } else if (x===0 && y===0) {
            cls.push('porta'); content = 'P';
          } else {
            const a = mapA[y][x]==='L', b = mapB[y][x]==='L';
            if (!inTrans) {
              if (a) cls.push('lava');
              else cls.push('vuota');
            } else {
              if (a) cls.push('lava');
              else if (b) cls.push('piattaforma','visibile');
              else cls.push('vuota');
            }
          }
        }

        html += `<div class="${cls.join(' ')}">${content}</div>`;
      }
    }

    mappa.innerHTML = html;
    if (livello===2 && Date.now() > nextToggle) {
      mapA = mapB;
      mapB = genMap();
      nextToggle = Date.now() + 3000;  // rifissa per i prossimi 3s
    }
  }

  function move(dx, dy) {
    if (!gameActive) return;
    const nx = player.x + dx, ny = player.y + dy;
    if (nx<0||nx>=DIM||ny<0||ny>=DIM) return;

    if (livello===0) {
      // move livello 1
      const c = `${nx}-${ny}`;
      player = { x:nx, y:ny };
      puntiEl.textContent = ++punti;
      if (trappole.has(c)) {
        vite = Math.max(vite-1,0);
        viteEl.textContent = vite;
        msgEl.textContent = 'TRAPPOLA! -1 vita';
        if (vite===0) {
          gameActive=false;
          msgEl.textContent=`GAME OVER! Punti:${punti}`;
          reset.classList.remove('hidden');
        }
        draw(); return;
      }
      if (!percorsoDisabilitato && !percorsoC.includes(c)) {
        percorsoDisabilitato = true;
        msgEl.textContent = 'Percorso disattivato! Torna a S';
      }
      if (percorsoDisabilitato && c===`${startC.x}-${startC.y}`) {
        percorsoDisabilitato = false;
        msgEl.textContent = 'Percorso riattivato!';
      }
      if (!percorsoDisabilitato && c===`${goalC.x}-${goalC.y}`) {
        livello=1; initLivello(); return;
      }
    }
    else if (livello===1) {
      // move livello 2
      let nx2=nx, ny2=ny;
      if (layoutIce[ny2][nx2]==='I') {
        while (layoutIce[ny2]?.[nx2]==='I') {
          player = { x:nx2, y:ny2 };
          nx2 += dx; ny2 += dy;
        }
        if (layoutIce[ny2]?.[nx2]) player = { x:nx2, y:ny2 };
      } else {
        player = { x:nx2, y:ny2 };
      }
      mosseEl.textContent = ++mosse;
      const coord = `${player.x}-${player.y}`;
      if (layoutIce[player.y][player.x].startsWith('T')) {
        if (coord===plateOrder[currentStep]) {
          currentStep++;
          msgEl.textContent = `Interruttore ${currentStep} attivato!`;
        } else {
          currentStep=0;
          msgEl.textContent = 'Ordine sbagliato! Riprova.';
        }
      }
      if (coord===`${goalG.x}-${goalG.y}`) {
        if (currentStep===plateOrder.length) {
          clearInterval(timerId);
          gameActive=false;
          msgEl.textContent=`Hai completato in ${mosse} mosse!`;
          setTimeout(()=>{ livello=2; initLivello(); },1000);
        } else {
          msgEl.textContent='Porta bloccata! Completa la sequenza.';
        }
      }
    }
    else {
      // move livello 3
      const a = mapA[ny][nx]==='L';
      if (a) {
        vite = Math.max(vite-1,0);
        viteEl.textContent = vite;
        msgEl.textContent = 'Hai toccato lava! -1 vita';
        if (vite===0) {
          gameActive=false;
          clearInterval(timerId);
          msgEl.textContent='GAME OVER!';
          reset.classList.remove('hidden');
        }
        draw(); return;
      }
      player = { x:nx, y:ny };
      if (nx===0 && ny===0) {
        gameActive=false;
        clearInterval(timerId);
        msgEl.textContent='Hai vinto! 🎉';
        reset.classList.remove('hidden');
      }
    }

    draw();
  }

  document.addEventListener('keydown', e => {
    const map = {
      ArrowUp:    [1,0],
      ArrowDown:  [-1,0],
      ArrowLeft:  [0,-1],
      ArrowRight: [0,1]
    };
    if (map[e.key]) move(...map[e.key]);
  });

  initLivello();
});
