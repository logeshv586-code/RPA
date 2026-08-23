async function loadHealth() {
  const pill = document.getElementById('health-pill');
  try {
    const response = await fetch('/health');
    if (!response.ok) throw new Error('health request failed');
    const data = await response.json();
    pill.textContent = `Service online · v${data.version}`;
    pill.classList.add('ok');
  } catch (error) {
    pill.textContent = 'Service status unavailable';
  }
}

async function loadCapabilities() {
  const grid = document.getElementById('capability-grid');
  try {
    const response = await fetch('/capabilities');
    if (!response.ok) throw new Error('capability request failed');
    const data = await response.json();

    grid.innerHTML = data.capabilities.map((capability) => `
      <article class="capability">
        <div class="capability-head">
          <h3>${capability.name}</h3>
          <span class="status ${capability.status}">${capability.status}</span>
        </div>
        <p>${capability.description}</p>
      </article>
    `).join('');
  } catch (error) {
    grid.innerHTML = '<div class="loading">Capability registry is temporarily unavailable.</div>';
  }
}

loadHealth();
loadCapabilities();
