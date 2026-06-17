---
slug: "nea"
url: "/mobilnisite/slovnik/nea/"
type: "slovnik"
title: "NEA – NR Encryption Algorithm"
date: 2026-01-01
abbr: "NEA"
fullName: "NR Encryption Algorithm"
category: "Security"
segment: "Security"
canonical: "https://3gpp-explorer.com/glossary/nea/"
summary: "Standardizovaný šifrovací algoritmus používaný k ochraně důvěrnosti dat uživatelské roviny a řídicí roviny v sítích 5G. Je základní součástí bezpečnostního rámce 5G a zajišťuje, že uživatelská data a"
---

NEA je standardizovaný šifrovací algoritmus používaný k ochraně důvěrnosti dat uživatelské roviny a řídicí roviny v sítích 5G, který zabraňuje odposlechu.

## Popis

NR Encryption Algorithm (NEA) je soubor kryptografických algoritmů specifikovaných 3GPP pro zajištění ochrany důvěrnosti v systémech 5G. Aplikuje se ve vrstvě Packet Data Convergence Protocol (PDCP) pro uživatelskou rovinu a ve vrstvě Radio Resource Control ([RRC](/mobilnisite/slovnik/rrc/)) pro řídicí rovinu přes rozhraní NR vzduch–rádio (Uu). Algoritmy NEA šifrují datové a signalizační přenášené jednotky před jejich přenosem, čímž je činí nesrozumitelnými pro neoprávněné strany. Konkrétní použitý algoritmus je vyjednán během počátečního nastavení zabezpečení mezi uživatelským zařízením (UE) a sítí (konkrétně gNB a funkcí Authentication Server Function – [AUSF](/mobilnisite/slovnik/ausf/)). Specifikace 3GPP 33.501 definuje bezpečnostní architekturu a vyžaduje podporu specifických sad algoritmů. Primárním algoritmem pro 5G je 128bitový NEA0, což je v podstatě nulový šifrovací algoritmus (používaný pro testování nebo když není šifrování vyžadováno), a 128bitové a 256bitové varianty algoritmu založeného na [AES](/mobilnisite/slovnik/aes/) v režimu [CTR](/mobilnisite/slovnik/ctr/), známé jako NEA1 a NEA2. NEA1 odpovídá SNOW 3G a NEA2 odpovídá AES-CTR. Je také specifikován nový algoritmus NEA3 (založený na ZUC). gNB a UE odvozují stejný šifrovací klíč (K_{RRCenc} pro řídicí rovinu, K_{UPenc} pro uživatelskou rovinu) z kotvícího klíče K_{gNB}. Tento klíč spolu s dalšími vstupy, jako je identita přenosového kanálu, směr a hodnota čítače, je použit vybraným algoritmem NEA k vygenerování klíčového proudu pro šifrování/dešifrování. Integrita dat je chráněna samostatně algoritmem NR Integrity Algorithm ([NIA](/mobilnisite/slovnik/nia/)). Použití silných, standardizovaných šifrovacích algoritmů je zásadní pro zachování soukromí uživatelů a bezpečnosti sítě v éře 5G.

## K čemu slouží

Sada algoritmů NEA existuje za účelem poskytnutí robustní, standardizované ochrany důvěrnosti pro komunikaci 5G, čímž řeší kritickou potřebu soukromí ve stále více propojeném světě. Řeší problém zabezpečení obrovského objemu citlivých uživatelských dat a síťové signalizace přenášených přes bezdrátové spoje, které jsou ze své podstaty náchylné k zachycení. Vytvoření vyhrazené sady algoritmů pro 5G bylo motivováno potřebou zvýšené kryptografické síly ve srovnání s předchozími generacemi (jako byly [EEA](/mobilnisite/slovnik/eea/) v LTE), což odpovídá vývoji bezpečnostních hrozeb a regulatorním požadavkům. Zajišťuje také globální interoperabilitu definováním společné sady algoritmů, které musí podporovat všechna kompatibilní UE a sítě. Historicky se šifrování v systémech 3GPP vyvíjelo od algoritmů A5 v GSM (které byly slabé) k silnějším algoritmům SNOW 3G a algoritmům založeným na [AES](/mobilnisite/slovnik/aes/) ve 3G a 4G. Sada 5G NEA na to navazuje, zavádí podporu 256bitových klíčů (pro NEA2) a šifru ZUC (NEA3) a nabízí portfolio algoritmů pro různé regulatorní prostředí a úrovně bezpečnostní jistoty, čímž zajišťuje budoucí odolnost sítě vůči pokrokům v kryptoanalýze.

## Klíčové vlastnosti

- Zajišťuje důvěrnost dat uživatelské roviny (UP) a signalizace řídicí roviny (RRC)
- Definován jako sada algoritmů zahrnující NEA0 (nulový), NEA1 (SNOW 3G), NEA2 (AES-CTR) a NEA3 (ZUC)
- Funguje ve vrstvě PDCP v rádiovém protokolovém zásobníku
- Používá klíče odvozené z procedur 5G Authentication and Key Agreement (5G-AKA) nebo EAP-AKA'
- Podporuje 128bitové a 256bitové délky klíčů pro zvýšenou bezpečnost
- Výběr algoritmu je vyjednán mezi UE a sítí během příkazu bezpečnostního režimu

## Související pojmy

- [NIA – New radio Integrity Algorithm](/mobilnisite/slovnik/nia/)

## Definující specifikace

- **TS 33.501** (Rel-20) — 5G Security Architecture and Procedures

---

📖 **Anglický originál a plná specifikace:** [NEA na 3GPP Explorer](https://3gpp-explorer.com/glossary/nea/)
