---
slug: "psdb"
url: "/mobilnisite/slovnik/psdb/"
type: "slovnik"
title: "PSDB – Packet Set Delay Budget"
date: 2026-01-01
abbr: "PSDB"
fullName: "Packet Set Delay Budget"
category: "QoS"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/psdb/"
summary: "Packet Set Delay Budget (PSDB) je parametr kvality služby (QoS) zavedený v 5G pro deterministické komunikační služby. Definuje maximální povolené koncové zpoždění pro sadu (nebo skupinu) paketů, které"
---

PSDB (rozpočet zpoždění sady paketů) je parametr kvality služby (QoS) v 5G, který definuje maximální povolené koncové zpoždění pro časově závislou sadu paketů, čímž zajišťuje jejich synchronizované doručení pro deterministické služby.

## Popis

Packet Set Delay Budget (PSDB) je charakteristika kvality služby (QoS) zavedená v 5G systému (5GS) pro podporu deterministické komunikace, zejména pro průmyslový internet věcí (IIoT) a časově citlivé sítě. Na rozdíl od tradičního rozpočtu zpoždění paketu ([PDB](/mobilnisite/slovnik/pdb/)), který stanovuje mez zpoždění pro jednotlivé pakety, se PSDB vztahuje na 'sadu paketů'. Sada paketů je definována jako jeden nebo více paketů, které jsou časově související, například pakety vygenerované z jediného snímacího cyklu senzoru nebo z koordinovaného příkazu pro více aktuátorů. PSDB definuje maximální povolený čas od vygenerování prvního paketu v sadě ve zdrojové aplikaci až do úspěšného doručení posledního paketu v sadě do cílové aplikace, při průchodu 5G systémem. Toto koncové zpoždění zahrnuje veškerá zpracování, fronty a přenosová zpoždění napříč koncovým zařízením (UE), rádiovou přístupovou sítí (RAN), funkcemi uživatelské roviny ([UPF](/mobilnisite/slovnik/upf/)) a jakýmikoli přidruženými překladači pro časově citlivé sítě ([TSN](/mobilnisite/slovnik/tsn/)). Jádrová síť 5G používá PSDB spolu s dalšími parametry QoS, jako je identifikátor QoS 5G ([5QI](/mobilnisite/slovnik/5qi/)), k vytvoření odpovídajících toků QoS s potřebnou alokací prostředků a zásadami plánování v RAN a jádru. Pro RAN může podpora PSDB vyžadovat vylepšené plánovací algoritmy, které berou v úvahu časový vztah v rámci sady paketů, a potenciálně upřednostňují doručení zbývajících paketů v sadě, jak se blíží termín rozpočtu zpoždění PSDB. PSDB je klíčovým prvkem umožňujícím, aby se 5GS choval jako most TSN, a bezproblémově se integroval s kabelovými TSN sítěmi, které používají podobné koncepty skupinového načasování. Jeho specifikace zahrnuje složitou interakci mezi rozhraním založeným na službách ([SBI](/mobilnisite/slovnik/sbi/)) pro řízení zásad QoS (prostřednictvím [PCF](/mobilnisite/slovnik/pcf/)) a rozhraními [N2](/mobilnisite/slovnik/n2/)/N4 pro správu relací a vynucování přepravních pravidel.

## K čemu slouží

Vznik parametru Packet Set Delay Budget (PSDB) byl motivován přísnými požadavky nově se objevujících aplikací průmyslové automatizace a řízení v rámci architektury 5G. Tradiční mechanismy QoS, navržené pro služby orientované na člověka, jako je hlas nebo streamování videa, se zaměřují na výkon jednotlivých paketů (např. průměrné zpoždění, chvění). V koordinovaném kyberneticko-fyzickém systému, jako je robotický montážní pás nebo řízení pohybu, však správná funkce závisí na synchronizovaném příjmu související sady datových paketů na více koncových bodech. Selhání nebo nadměrné zpoždění i jediného paketu v sadě může učinit celou sadu nepoužitelnou a narušit řídicí smyčku. Individuální rozpočet zpoždění paketu ([PDB](/mobilnisite/slovnik/pdb/)) byl nedostatečný pro zaručení této kolektivní včasnosti. PSDB byl zaveden, aby tuto mezeru zaplnil, a poskytuje tak metrický parametr QoS, který odpovídá sémantickým požadavkům deterministických aplikací. Umožňuje síti pochopit a vynucovat časové záruky pro logicky seskupená data, což 5G poprvé umožňuje podporovat skutečné deterministické zpoždění. Tento vývoj byl poháněn prací 3GPP na integraci s IEEE Time-Sensitive Networking (TSN) a potřebami vertikálních odvětví v rámci vylepšení komunikace s ultra-spolehlivým nízkým zpožděním (URLLC). PSDB řeší problém poskytování časové koordinace přes bezdrátové médium, což je kritický krok pro adopci 5G v prostředích průmyslových misí s kritickým významem, kde jsou rozšířené kabelové TSN sítě.

## Klíčové vlastnosti

- Definuje maximální mez zpoždění pro doručení kompletní sady časově souvisejících paketů.
- Platí koncově napříč 5G systémem, od zdrojové aplikace k cílové aplikaci.
- Zásadní pro podporu deterministické komunikace a funkce 5G-jako-most-TSN.
- Používá se jádrem 5G (PCF, SMF) k odvození parametrů toku QoS a požadavků na prostředky.
- Může ovlivnit plánovací algoritmy RAN tak, aby upřednostňovaly sady paketů blížící se termínu svého rozpočtu zpoždění.
- Klíčový parametr QoS pro pokročilé případy užití URLLC a průmyslového internetu věcí (IIoT).

## Související pojmy

- [5QI – 5G QoS Identifier](/mobilnisite/slovnik/5qi/)
- [URLLC – Ultra Reliable Low Latency Communication](/mobilnisite/slovnik/urllc/)

## Definující specifikace

- **TS 23.501** (Rel-20) — 5G System Architecture Stage 2
- **TS 23.700** (Rel-20) — XR Services Application Enablement Layer
- **TS 26.804** (Rel-19) — 5G Media Streaming Extensions Study
- **TS 29.514** (Rel-19) — 5G System; Policy Authorization Service; Stage 3
- **TS 38.300** (Rel-19) — NG-RAN Overall Description
- **TR 38.835** (Rel-18) — Technical Report on XR Enhancements for NR

---

📖 **Anglický originál a plná specifikace:** [PSDB na 3GPP Explorer](https://3gpp-explorer.com/glossary/psdb/)
