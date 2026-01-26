---
author: Patrick Zandl
categories:
- AI
- Google
- Antigravity
- IDE
- bezpečnost
- sandboxing
layout: post
post_excerpt: Google Antigravity přináší sandboxing terminálových příkazů na úrovni jádra systému. Zatím funguje pouze na macOS přes Seatbelt, podpora Linuxu se chystá.
summary_points:
- Google Antigravity zavádí sandboxing terminálových příkazů s izolací na úrovni jádra
- Funkce je dostupná pouze na macOS, využívá mechanismus Seatbelt (sandbox-exec)
- Agent může zapisovat pouze do pracovního adresáře, síťový přístup lze řídit nezávisle
- V režimu Request Review lze sandbox obejít pro jednotlivé příkazy
- Secure Mode automaticky aktivuje sandboxing s odepřeným síťovým přístupem
title: Google Antigravity zavádí sandboxing agentů
---

Google rozšířil své vývojové prostředí [Antigravity](https://antigravity.google/) o sandboxing terminálových příkazů. Nová funkce poskytuje izolaci na úrovni jádra operačního systému pro veškeré příkazy, které AI agent v terminálu spouští. Cílem je ochrana systému před nechtěnými modifikacemi souborů nebo neoprávněným síťovým přístupem ze strany autonomně pracujícího agenta.

Jen malá rekapitulace na začátek. Antigravity je agentní vývojové prostředí od Google představené v listopadu 2025 společně s modely Gemini 3. Na rozdíl od klasických pomocníků pro psaní kódu umožňuje delegovat celé vývojové úlohy na autonomní agenty, kteří mohou plánovat, psát kód, spouštět terminálové příkazy a testovat aplikace v prohlížeči. Právě tato autonomie vytváří bezpečnostní rizika, která sandboxing řeší.

**Aktuální stav a dostupnost**

Sandboxing je v současné verzi ve výchozím nastavení vypnutý, ale podle dokumentace se to může v budoucích verzích změnit. Funkce je zatím dostupná výhradně na macOS, kde využívá mechanismus [Seatbelt](https://developer.apple.com/documentation/security/app_sandbox) (sandbox-exec), tedy nativní sandboxovací vrstvu na úrovni jádra od Apple. Podpora pro Linux je podle Google v přípravě, konkrétní termín však stanoven nebyl.

**Nastavení a konfigurace**

Sandboxing lze zapnout v uživatelských nastaveních Antigravity přepínačem „Enable Terminal Sandboxing”. Síťový přístup se řídí nezávisle prostřednictvím přepínače „Sandbox Allow Network”, což umožňuje kombinovat omezení souborového systému s povoleným nebo zakázaným síťovým přístupem podle potřeb konkrétního projektu.

**Omezení souborového systému**

Při aktivním sandboxingu mohou terminálové příkazy agenta zapisovat pouze do určeného pracovního adresáře (workspace) a nezbytných systémových lokací. Agent tak nemůže omylem smazat nebo modifikovat soubory mimo aktuální projekt. Pokud se příkaz pokusí o zápis mimo povolené umístění, operace selže a uživatel obdrží oznámení o blokaci.

**Řízení síťového přístupu**

Síťová konektivita funguje jako nezávislá vrstva omezení. Lze ji zakázat i při povolených operacích se souborovým systémem, což je užitečné v situacích, kdy agent potřebuje pracovat s lokálními soubory, ale nemá důvod komunikovat s externími servery. Typickým příkladem blokace je pokus o stažení balíčků nebo volání externích rozhraní API.

**Řešení konfliktů a obcházení sandboxu**

Pokud příkaz selže kvůli omezením sandboxu, má uživatel dvě možnosti. První je trvalé vypnutí sandboxingu v nastavení. Druhou představuje jednorázové obejití při použití režimu „Request Review”, kdy se u každého příkazu zobrazí možnost „Bypass Sandbox” pro spuštění bez omezení.

Režim Request Review odpovídá tomu, co Google označuje jako „Review-driven development”, tedy doporučený způsob práce, kdy agent navrhuje akce a uživatel je schvaluje. V tomto režimu má vývojář kontrolu nad každým krokem včetně rozhodnutí o úrovni izolace.

**Integrace se Secure Mode**

Antigravity nabízí také Secure Mode, který poskytuje zvýšené bezpečnostní kontroly pro celého agenta. Při jeho aktivaci se sandboxing automaticky zapne a síťový přístup je odepřen. Tato kombinace zajišťuje maximální ochranu pro situace, kdy je bezpečnost prioritou, například při práci s citlivým kódem nebo v produkčním prostředí.

**Kontext bezpečnostních opatření v Antigravity**

Sandboxing doplňuje další bezpečnostní mechanismy, které Antigravity obsahuje. Patří mezi ně systém oprávnění pro automatické spouštění terminálových příkazů (Terminal Command Auto Execution), seznamy povolených a zakázaných příkazů (Allow Lists, Deny Lists) a již zmíněné vývojové režimy s různou mírou autonomie agenta. Agent-driven development poskytuje agentovi plnou autonomii, Review-driven development vyžaduje schvalování kroků a Agent-assisted development ponechává kontrolu na vývojáři s asistencí agenta.

Rozšíření pro ovládání prohlížeče v Antigravity rovněž používá izolované prostředí, aby agent nemohl přistupovat k uživatelským datům jako uložená hesla nebo přihlášení na sociálních sítích. Právě tato izolace prohlížečového profilu způsobila po vydání Antigravity zmatek mezi uživateli, kteří si mysleli, že přišli o svá data.

**Praktické dopady**

Pro vývojáře pracující na macOS představuje sandboxing vítanou vrstvu ochrany při experimentování s autonomními agenty. Omezení na pracovní adresář zabraňuje situacím, kdy by chybný příkaz mohl poškodit systémové soubory nebo jiné projekty. Nezávislé řízení síťového přístupu umožňuje testovat kód v offline režimu bez rizika úniku dat. Antigravity se tak inspiruje úspěchem sandboxingu z Claude Code, které představilo tuto funkci vloni na podzim.

Absence podpory Linuxu je v současnosti limitující, protože významná část profesionálních vývojářů a serverových prostředí běží právě na Linuxu. Google nespecifikoval, zda linuxová verze využije podobný mechanismus jako seccomp-bpf nebo jiné řešení. Pro Windows není sandbox v této úrovni vůbec možný, protoze mu chybí podpora na úrovni systému.

|Vlastnost               |Stav                               |
|------------------------|-----------------------------------|
|Dostupnost              |macOS (Seatbelt)                   |
|Linux podpora           |plánována                          |
|Windows podpora         |neuvedeno                          |
|Výchozí stav            |vypnuto                            |
|Omezení zápisu          |pracovní adresář + systémové lokace|
|Síťový přístup          |nezávisle konfigurovatelný         |
|Integrace se Secure Mode|automatická aktivace               |

Sandboxing v Google Antigravity představuje pragmatický krok směrem k bezpečnějšímu využívání autonomních agentů. Míra ochrany závisí na tom, nakolik uživatelé funkci skutečně aktivují a nakolik se naučí pracovat s režimem Request Review namísto trvalého vypnutí omezení kvůli pohodlí.​​​​​​​​​​​​​​​​