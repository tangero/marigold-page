---
author: Patrick Zandl
categories:
- AI
- Claude Code
- Claude
- Anthropic
- vibecoding
layout: post
post_excerpt: Láká vás tvorba webových aplikací pomocí AI, ale nevíte, jak začít? Tohle je video pro naprosté začátečníky. Ukážeme si, jak si instalujete Claude Code a jak si vytvoříte svou první webovou aplikaci - krok za krokem. 
title: "🎥 Video: Začínáme s Claude Code"
thumbnail: https://www.marigold.cz/assets/claude-code-zaciname.jpeg
---

Láká vás tvorba webových aplikací pomocí AI, ale nevíte, jak začít? Tohle je video pro naprosté začátečníky. Ukážeme si, jak si instalujete Claude Code a jak si vytvoříte svou první webovou aplikaci - krok za krokem. 

<iframe width="700" height="394" src="https://www.youtube.com/embed/WcatDGbqomg?si=55gOCJ9VLrAJp4UK" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

### Souhrn a Popis Videa: Claude Code pro začátečníky

-   **Úvod a Představení Claude Code**
    
    -   **[[00:00](http://www.youtube.com/watch?v=WcatDGbqomg&t=0)]**  Představení přednášejícího (Patrik Zandl) a cíle: nadchnout pro programování webových aplikací pomocí nástrojů AI.
        
    -   **[[00:19](http://www.youtube.com/watch?v=WcatDGbqomg&t=19)]**  Zaměření na  **Claude Code**  jako primárně terminálové rozhraní, které je výkonnější než jeho webová verze.
        
-   **Příprava Terminálu**
    
    -   **[[00:36](http://www.youtube.com/watch?v=WcatDGbqomg&t=36)]**  Vysvětlení, jak funguje terminál (na příkladu Macu) a upozornění, že pro neprogramátory to může být nezvyklé.
        
    -   **[[01:27](http://www.youtube.com/watch?v=WcatDGbqomg&t=87)]**  Doporučení a instalace speciálního terminálu  **Warp**(`warp.dev`) s podporou AI, který je zdarma a multiplatformní.
        
-   **Instalace a Spuštění Claude Code**
    
    -   **[[02:02](http://www.youtube.com/watch?v=WcatDGbqomg&t=122)]**  Instalace Claude Code se provádí pomocí příkazu zkopírovaného z webu Anthropic, zadáním do terminálu.
        
    -   **[[03:23](http://www.youtube.com/watch?v=WcatDGbqomg&t=203)]**  Spuštění Claude Code příkazem  `claude`  z pracovního adresáře, který je určen pro vývoj projektu.
        
    -   **[[04:15](http://www.youtube.com/watch?v=WcatDGbqomg&t=255)]**  Vysvětlení a zapnutí režimu  **Sandbox**  (přidáním parametru k příkazu  `claude`) – tento režim zvyšuje bezpečnost tím, že omezuje operace AI mimo pracovní adresář a komunikaci s internetem.
        
-   **Prostředí a Financování**
    
    -   **[[06:03](http://www.youtube.com/watch?v=WcatDGbqomg&t=363)]**  Popis spartánského prostředí, které zobrazuje kontextové informace a používaný model (Sonet 4.5).
        
    -   **[[06:32](http://www.youtube.com/watch?v=WcatDGbqomg&t=392)]**  Důležité: Vysvětlení cenových režimů – doporučení registrace a použití režimu  **Pro za 17 USD**  měsíčně namísto staršího, dražšího režimu platby za tokeny přes API.
        
    -   **[[08:26](http://www.youtube.com/watch?v=WcatDGbqomg&t=506)]**  Popis příkazového řádku (prompt) pro komunikaci s AI a statusového řádku (Context, připojení k GitHubu).
        
-   **Návrh a Zadání Projektu (PRD)**
    
    -   **[[10:27](http://www.youtube.com/watch?v=WcatDGbqomg&t=627)]**  Doporučený postup: Namísto primitivního zadání vytvořit  **Product Requirement Document (PRD)**.
        
    -   **[[10:56](http://www.youtube.com/watch?v=WcatDGbqomg&t=656)]**  Definování ukázkové aplikace  **"Hot or Not"**  pro výběr ze dvou obrazů, s cílem hostovat ji na platformě  **Cloudflare Free tier**(zdarma), aby AI zvolila vhodnou technologii.
        
    -   **[[12:31](http://www.youtube.com/watch?v=WcatDGbqomg&t=751)]**  Upřesnění požadavků s Claude (použít top 100 obrazů po roce 1850, data z WikiArt, metadata zobrazit až po volbě, duplicitní hlasování řešit přes  `localStorage`).
        
    -   **[[17:49](http://www.youtube.com/watch?v=WcatDGbqomg&t=1069)]**  Claude generuje PRD, navrhuje technologie vhodné pro Cloudflare (Frontend:  **React/Vite**, Backend:  **Cloudflare Workers**, Databáze:  **D1 - SQLite**, Styling:  **Tailwind CSS**).
        
-   **Implementace a Nasazení**
    
    -   **[[19:45](http://www.youtube.com/watch?v=WcatDGbqomg&t=1185)]**  Vytvoření plánu implementace pomocí příkazu  `vytvořme plán implementace...`  a odvolání se na PRD soubor (`@Art_Battle_PRD.md`).
        
    -   **[[23:11](http://www.youtube.com/watch?v=WcatDGbqomg&t=1391)]**  Spuštění kompletní implementace, která trvá přibližně 10 minut a vytvoří 36 souborů.
        
    -   **[[24:23](http://www.youtube.com/watch?v=WcatDGbqomg&t=1463)]**  Vytvoření souhrnné dokumentace projektu do souboru  `cloud.md`  pomocí příkazu  `init`, pro budoucí použití AI.
        
    -   **[[26:48](http://www.youtube.com/watch?v=WcatDGbqomg&t=1608)]**  Nasazení (deployment) aplikace na Cloudflare pomocí příkazu  `proveď deployment na cloudflare`.
        
-   **Testování a Závěr**
    
    -   **[[27:40](http://www.youtube.com/watch?v=WcatDGbqomg&t=1660)]**  Testování živé aplikace na frontendové URL a zjištění prvního nedostatku (stránka se neobnoví po hlasování).
        
    -   **[[28:45](http://www.youtube.com/watch?v=WcatDGbqomg&t=1725)]**  Následuje fáze ladění (dopilovávání) projektu, která je přenechána uživatelům pro další experimenty.
        
    -   **[[29:44](http://www.youtube.com/watch?v=WcatDGbqomg&t=1784)]**  Závěrečné doporučení k experimentování a odkaz na web  **[vibecoding.cz](http://www.vibecoding.cz/)**  pro více informací o programování s AI.
        

Video si můžete spustit také přímo na Youtube:  [Začínáme vibecoding s Claude Code](http://www.youtube.com/watch?v=WcatDGbqomg)