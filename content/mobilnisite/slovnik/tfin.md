---
slug: "tfin"
url: "/mobilnisite/slovnik/tfin/"
type: "slovnik"
title: "TFIN – Transport Format INdicator"
date: 2025-01-01
abbr: "TFIN"
fullName: "Transport Format INdicator"
category: "Radio Access Network"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/tfin/"
summary: "Parametr používaný v GSM/EDGE Radio Access Network (GERAN) k označení transportního formátu pro datové bloky přenášené přes rozhraní vzduchu. Informuje přijímač o použité kódovací a modulační schéma,"
---

TFIN je parametr v GERAN, který indikuje transportní formát pro datové bloky a informuje přijímač o použité kódovací a modulační schéma, aby umožnil správné dekódování.

## Popis

Transport Format INdicator (TFIN) je koncept specifický pro GSM/[EDGE](/mobilnisite/slovnik/edge/) Radio Access Network ([GERAN](/mobilnisite/slovnik/geran/)), zavedený jako součást pokračující evoluce platformy GSM směrem k vyšším datovým rychlostem a efektivnějšímu provozu paketových dat. Funguje koncepčně podobně jako [TFI](/mobilnisite/slovnik/tfi/) v UMTS, ale je přizpůsoben časově dělené struktuře GERAN. TFIN je spojen s přenosem rádiových bloků na kanálech pro paketová data (jako je [PDTCH](/mobilnisite/slovnik/pdtch/)). Rádiový blok je přenášen přes čtyři po sobě jdoucí [TDMA](/mobilnisite/slovnik/tdma/) rámce a nese datovou část, jejíž velikost a úroveň ochrany se může lišit v závislosti na zvoleném modulačním a kódovacím schématu ([MCS](/mobilnisite/slovnik/mcs/)).

TFIN je pole v hlavičce rádiového bloku, které signalizuje přijímací entitě ([MS](/mobilnisite/slovnik/ms/) nebo [BSS](/mobilnisite/slovnik/bss/)), který transportní formát byl pro daný blok použit. Transportní formát definuje parametry jako úroveň MCS, počet bitů datové části, kódovací poměr a schéma punkturace. Po přijetí bloku přijímač nejprve dekóduje hlavičku, aby získal TFIN. Tento indikátor pak použije k vyhledání odpovídající definice transportního formátu z předem nakonfigurované sady. Tato znalost je nezbytná pro následné kroky depunkturace, demodulace a kanálového dekódování datové části rádiového bloku.

V architektuře GERAN je TFIN spravován vrstvami Radio Link Control (RLC) a Medium Access Control (MAC). Síť (BSS) vybírá vhodné MCS, a tedy i transportní formát, na základě hlášení o kvalitě kanálu od mobilní stanice. Zvolený TFIN je pak zahrnut do hlavičky bloku pro přenos. Tento mechanismus umožňuje dynamickou adaptaci spoje, kdy síť může přepínat mezi robustním kódováním s nízkou rychlostí (např. MCS-1) pro špatné signálové podmínky a vysoce účinným kódováním s vysokou rychlostí (např. MCS-9) pro výborné podmínky, a to vše v rámci stejné struktury logického kanálu. TFIN je klíčovým prvkem pro dosažení špičkových datových rychlostí a zlepšení spektrální účinnosti, které přinesly EDGE a pozdější vylepšení GERAN.

## K čemu slouží

TFIN byl zaveden za účelem vylepšení datových schopností zralého systému GSM, konkrétně pro EDGE (Enhanced Data rates for GSM Evolution) a jeho následná vylepšení. Původní systém GPRS používal omezenější sadu kódovacích schémat (CS-1 až CS-4) s pevnými přiřazeními. Účelem TFIN je poskytnout flexibilní a rozšiřitelný signalizační mechanismus pro širší a jemněji odstupňovanou sadu modulačních a kódovacích schémat vyžadovaných pro vyšší modulace, jako je 8-PSK, a později 16-QAM a 32-QAM zavedené v EDGE Evolution.

Řeší problém efektivního signalizování přesného přenosového formátu bez nutnosti samostatného řídicího kanálu nebo složité signalizace mimo pásmo pro každý rádiový blok. Vložením TFIN do hlavičky bloku zajišťuje, že přijímač má okamžitý přístup k informacím potřebným pro správné dekódování. Toto byla nutná evoluce od jednodušší identifikace kódovacího schématu GPRS k podpoře pokročilých technik adaptace spoje a přírůstkové redundance (IR), které jsou charakteristické pro EDGE. Mechanismus TFIN umožnil GERAN zůstat konkurenceschopným díky výraznému zvýšení propustnosti paketových dat v rámci stávající šířky pásma nosné 200 kHz, čímž reagoval na rostoucí poptávku po mobilních internetových službách před všeobecným pokrytím sítěmi 3G/4G.

## Klíčové vlastnosti

- Signalizuje transportní formát pro rádiový blok GERAN na kanálech pro paketová data
- Vložen do hlavičky rádiového bloku pro okamžitý přístup přijímače
- Indikuje použitou úroveň modulačního a kódovacího schématu (MCS)
- Umožňuje dynamickou adaptaci spoje na základě rádiových podmínek
- Podporuje pokročilé funkce jako přírůstková redundance (IR)
- Rozšiřitelný pro podporu nových modulačních schémat (např. 16-QAM, 32-QAM)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TR 45.902** (Rel-19) — Flexible Layer One (FLO) for GERAN

---

📖 **Anglický originál a plná specifikace:** [TFIN na 3GPP Explorer](https://3gpp-explorer.com/glossary/tfin/)
