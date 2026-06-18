---
slug: "pua"
url: "/mobilnisite/slovnik/pua/"
type: "slovnik"
title: "PUA – Presence User Agent"
date: 2025-01-01
abbr: "PUA"
fullName: "Presence User Agent"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/pua/"
summary: "PUA je klientská funkční entita v architektuře služby Presence. Sídlí v zařízení uživatele nebo síťovém uzlu, sbírá informace o přítomnosti (jako dostupnost a stav) a publikuje je agentovi přítomnosti"
---

PUA je klientská funkční entita služby Presence, která sídlí v zařízení uživatele nebo síťovém uzlu, sbírá informace o přítomnosti a publikuje je agentovi přítomnosti v síti (Presence Network Agent).

## Popis

Presence User Agent (PUA) je základní komponenta v rámci frameworku služby Presence podle 3GPP, standardizovaná v několika technických specifikacích včetně TS 23.141, 24.141, 24.841 a 25.470. Funguje jako zdroj informací o přítomnosti pro prezentitu (entitu, jejíž přítomnost je hlášena). PUA je zodpovědná za sběr, generování a konečné publikování stavu přítomnosti uživatele nebo služby do sítě. Tento stav může zahrnovat širokou škálu dynamických informací, jako je registrační stav (např. online/offline), ochota ke komunikaci (např. dostupný pro hovor, zaneprázdněn), aktuální aktivita, poloha (je-li povolena) a možnosti terminálu.

Architektonicky je PUA logická funkce, která může být implementována na různých fyzických místech. Nejčastěji sídlí v uživatelském zařízení (UE), například v klientské aplikaci v chytrém telefonu. Může však být umístěna i v síťové entitě, jako je aplikační server, která jedná jménem uživatele nebo služby. PUA nekomunikuje přímo s pozorovateli (entitami žádajícími o informace o přítomnosti). Místo toho komunikuje s agentem přítomnosti v síti (Presence Network Agent, [PNA](/mobilnisite/slovnik/pna/)) nebo, v pokročilejších architekturách založených na IMS, se serverem přítomnosti (Presence Server, [PS](/mobilnisite/slovnik/ps/)) přes referenční bod Ut pomocí protokolů jako [SIP](/mobilnisite/slovnik/sip/) PUBLISH.

Činnost PUA zahrnuje kontinuální cyklus sběru, zpracování a publikace informací. Monitoruje relevantní zdroje dat (např. stav napájení zařízení, integraci s kalendářem, ruční vstup uživatele), uplatňuje lokální politiky a pravidla ochrany soukromí, formátuje data do dokumentu přítomnosti (často za použití formátů [PIDF](/mobilnisite/slovnik/pidf/)/[RPID](/mobilnisite/slovnik/rpid/)) a zasílá aktualizace do sítě kdykoli dojde k významné změně stavu. To umožňuje bohaté služby komunikace v reálném čase tím, že ostatním uživatelům a službám poskytuje možnost činit informovaná rozhodnutí o zahájení kontaktu na základě aktuálního kontextu prezentity.

## K čemu slouží

PUA byla vytvořena za účelem umožnění bohatých služeb přítomnosti v mobilních sítích, což znamená posun za jednoduché binární indikátory stavu online/offline. Její vývoj byl motivován konvergencí celulárních sítí s komunikací založenou na internetu a vzestupem instant messagingu. PUA řeší problém, jak dynamicky zachytit a standardizovaným způsobem šířit komplexní, mnohostranný kontext uživatele (dostupnost, nálada, poloha, stav zařízení) k oprávněným stranám.

Před takovými standardizovanými architekturami přítomnosti služby spoléhaly na proprietární, izolované mechanismy přítomnosti nebo neměly žádné dynamické informace o dostupnosti. PUA jako součást služby Presence podle 3GPP poskytla jednotný model pro sběr těchto dat z různých zdrojů v zařízení nebo v síti. Odstranila omezení dřívějších statických metod tím, že umožnila automatizované, politikami řízené publikování kontextu v reálném čase, což je nezbytné pro zlepšení uživatelského zážitku ve službách jako obohacené adresáře, inteligentní směrování hovorů a kontextově povědomé zasílání zpráv.

## Klíčové vlastnosti

- Je zdrojem a generátorem informací o přítomnosti pro prezentitu
- Může sídlit v uživatelském zařízení (UE) nebo v síťovém aplikačním serveru
- Publikuje data o přítomnosti do sítě pomocí SIP PUBLISH nebo jiných definovaných metod
- Před publikací uplatňuje lokální pravidla ochrany soukromí a politiky
- Podporuje bohatou sadu atributů přítomnosti (aktivita, nálada, dostupnost služby, poloha)
- Integruje se se senzory zařízení a aplikacemi pro automatizaci aktualizací stavu

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [SIP – Session Initiation Protocol](/mobilnisite/slovnik/sip/)

## Definující specifikace

- **TS 23.141** (Rel-19) — Presence Service Stage 2 Architecture
- **TS 24.141** (Rel-19) — Presence Service Protocol Details
- **TS 24.841** (Rel-6) — Presence Service IP Multimedia Subsystem
- **TS 25.470** (Rel-19) — PCAP User Adaption (PUA) protocol specification

---

📖 **Anglický originál a plná specifikace:** [PUA na 3GPP Explorer](https://3gpp-explorer.com/glossary/pua/)
