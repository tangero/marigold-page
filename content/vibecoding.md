---

title: Vibe Coding
url: /vibecoding/
---

# Vibe Coding - AI nástroje pro programování

<a href="/vibecoding-feed.xml" class="rss-link">📰 RSS Feed</a>

Přehled nejmodernějších AI nástrojů a služeb pro vibe coding a programování s pomocí umělé inteligence.

## 🛠️ Služby a nástroje

<div class="tools-categories-row">
  
  <!-- Desktop IDE -->
  <div class="category-box">
    <button class="category-toggle collapsed" onclick="toggleCategory(this)">
      💻 Desktop IDE <span class="toggle-icon">▼</span>
    </button>
    <div class="category-content">
      <div class="service-card">
        <h4><a href="/vibecoding/cursor/">🖱️ Cursor</a></h4>
        <p>Kompletní IDE založené na VS CODE s AI funkcemi pro rychlý vývoj a refactoring kódu</p>
      </div>
      <div class="service-card">
        <h4><a href="/vibecoding/windsurf/">🌊 Windsurf</a></h4>
        <p>Inteligentní IDE s pokročilými AI funkcemi pro vývoj</p>
      </div>
      <div class="service-card">
        <h4><a href="/vibecoding/memex/">🧠 Memex</a></h4>
        <p>Desktop aplikace pro vývoj software, velmi autonomní a za dobré peníze</p>
      </div>
    </div>
  </div>

  <!-- Cloudové nástroje -->
  <div class="category-box">
    <button class="category-toggle collapsed" onclick="toggleCategory(this)">
      ☁️ Cloudové nástroje <span class="toggle-icon">▼</span>
    </button>
    <div class="category-content">
      <div class="service-card">
        <h4><a href="/vibecoding/databutton/">🔴 Databutton</a></h4>
        <p>Evropská AI-powered web platforma pro vytváření aplikací bez kódování</p>
      </div>
      <div class="service-card">
        <h4><a href="/vibecoding/lovable-dev/">💖 Lovable.dev</a></h4>
        <p>AI nástroj pro rychlý vývoj moderních webových aplikací</p>
      </div>
      <div class="service-card">
        <h4><a href="/vibecoding/tempolabs/">⚡ Tempolabs</a></h4>
        <p>Rychlý webový AI nástroj pro prototypování a vývoj aplikací</p>
      </div>
      <div class="service-card">
        <h4><a href="/vibecoding/replit/">🟠 Replit</a></h4>
        <p>AI-powered cloudová platforma pro vývoj a nasazení aplikací s Replit Agent</p>
      </div>
    </div>
  </div>

  <!-- Terminálové a chat nástroje -->
  <div class="category-box">
    <button class="category-toggle collapsed" onclick="toggleCategory(this)">
      🤖 Terminálové a chat nástroje <span class="toggle-icon">▼</span>
    </button>
    <div class="category-content">
      <div class="service-card">
        <h4><a href="/vibecoding/claude-code/">🟣 Claude Code</a></h4>
        <p>Pokročilý terminálový asistent pro programování a analýzu kódu od Anthropicu</p>
      </div>
      <div class="service-card">
        <h4><a href="/vibecoding/openai-codex/">🟢 OpenAI Codex</a></h4>
        <p>AI model pro generování a porozumění kódu od OpenAI</p>
      </div>
      <div class="service-card">
        <h4><a href="/vibecoding/gemini-cli/">🔵 Gemini CLI</a></h4>
        <p>Terminálový nástroj pro práci s Google Gemini modely přímo z příkazové řádky</p>
      </div>
    </div>
  </div>

</div>

<style>
.tools-categories-row {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 20px;
  margin: 30px 0;
}

.category-box {
  border: 1px solid #ddd;
  border-radius: 8px;
  overflow: hidden;
  background: #f8f9fa;
}

.category-toggle {
  width: 100%;
  padding: 15px 20px;
  background: #f8f9fa;
  border: none;
  text-align: left;
  font-size: 16px;
  font-weight: 600;
  color: #333;
  cursor: pointer;
  display: flex;
  justify-content: space-between;
  align-items: center;
  transition: background 0.2s ease;
}

.category-toggle:hover {
  background: #e9ecef;
}

.category-toggle.collapsed .toggle-icon {
  transform: rotate(-90deg);
}

.toggle-icon {
  transition: transform 0.3s ease;
}

.category-content {
  max-height: 0;
  overflow: hidden;
  transition: max-height 0.3s ease;
  background: white;
}

.category-toggle:not(.collapsed) + .category-content {
  max-height: none;
  height: auto;
  padding: 20px;
}

.service-card {
  margin-bottom: 15px;
  padding: 15px;
  background: #fafafa;
  border-radius: 6px;
  border: 1px solid #eee;
}

.service-card:last-child {
  margin-bottom: 0;
}

.service-card h4 {
  margin: 0 0 8px 0;
  font-size: 16px;
}

.service-card h4 a {
  text-decoration: none;
  color: #333;
}

.service-card h4 a:hover {
  color: #007acc;
}

.service-card p {
  margin: 0;
  font-size: 14px;
  color: #666;
  line-height: 1.4;
}

@media (max-width: 768px) {
  .tools-categories-row {
    grid-template-columns: 1fr;
  }
}

.rss-link {
  display: inline-block;
  margin-bottom: 20px;
  padding: 5px 10px;
  background-color: #f8f8f8;
  border-radius: 4px;
  text-decoration: none;
  color: #666;
  font-size: 14px;
  transition: all 0.2s ease;
}

.rss-link:hover {
  background-color: #fff3cd;
  color: #333;
  text-decoration: none;
}
</style>

<script>
function toggleCategory(button) {
  button.classList.toggle('collapsed');
}
</script>

<!-- Note: Article listing from vibecoding collection is handled by the vibecoding.cz separate site -->