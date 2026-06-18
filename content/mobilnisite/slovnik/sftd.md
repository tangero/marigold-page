---
slug: "sftd"
url: "/mobilnisite/slovnik/sftd/"
type: "slovnik"
title: "SFTD – SFN and Frame Timing Difference"
date: 2025-01-01
abbr: "SFTD"
fullName: "SFN and Frame Timing Difference"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/sftd/"
summary: "SFTD je měření hlášené uživatelským zařízením 5G NR, které udává časový rozdíl mezi dvěma buňkami. Je klíčové pro podporu více-RAT Dual Connectivity (EN-DC, NR-DC) a procedur mobility, což síti umožňu"
---

SFTD je naměřený časový rozdíl mezi číslem systémového rámce (SFN) a časováním rámců dvou buněk, který hlásí uživatelské zařízení 5G NR pro podporu více-RAT Dual Connectivity a procedur mobility.

## Popis

Rozdíl čísla systémového rámce a časování rámců (SFTD) je specifické měření definované v 5G New Radio (NR) pro použití ve scénářích s více připojeními a mobilitou. Kvantifikuje relativní časový rozdíl mezi dvěma buňkami, což mohou být dvě NR buňky nebo LTE buňka a NR buňka. Měření hlásí uživatelské zařízení (UE) síti, typicky obsluhujícímu gNB nebo [eNB](/mobilnisite/slovnik/enb/). Měření SFTD se skládá ze dvou složek: rozdílu v čísle systémového rámce ([SFN](/mobilnisite/slovnik/sfn/)) a rozdílu v čase začátku rámce mezi dvěma měřenými buňkami. Tato měření jsou hlášena se specifickou granularitou a rozsahem definovaným v technických specifikacích (např. TS 38.133).

Princip funkce SFTD spočívá v tom, že UE průběžně monitoruje referenční signály (např. SSB – blok synchronizačního signálu) jak od své obsluhující buňky, tak od sousední cílové buňky. UE vypočítá časový rozdíl mezi příjmem hranic rámců od těchto dvou buněk. Rozdíl SFN je rozdíl v absolutních číslech rámců, zatímco rozdíl v časování rámců je submikrosekundový posun. UE toto měření hlásí síti prostřednictvím signalizace [RRC](/mobilnisite/slovnik/rrc/) (Radio Resource Control), jak je specifikováno v TS 38.331. Síť tyto informace využívá k pochopení synchronizačního vztahu mezi buňkami, který není v nasazeních 5G zaručen, zejména v scénářích Dual Connectivity s neideální přenosovou sítí.

Klíčová role SFTD spočívá v konfiguraci a udržování více-RAT Dual Connectivity, jako je [EN-DC](/mobilnisite/slovnik/en-dc/) (E-UTRA-NR Dual Connectivity) a [NR-DC](/mobilnisite/slovnik/nr-dc/). Aby síť mohla správně plánovat přenosy přes hlavní uzel ([MN](/mobilnisite/slovnik/mn/)) a sekundární uzel ([SN](/mobilnisite/slovnik/sn/)) bez škodlivého rušení, potřebuje přesně znát časové zarovnání mezi zúčastněnými buňkami. Měření SFTD umožňuje síti vypočítat a aplikovat potřebné časové posuny nebo procedury zarovnání. Dále se SFTD používá při událostech mobility, jako je příprava přechodu spojení, což umožňuje předkonfigurovat cílovou buňku s přesnými časovými informacemi vzhledem ke zdrojové buňce, což vede k plynulejším a rychlejším přechodům spojení se sníženou dobou přerušení.

## K čemu slouží

SFTD existuje, aby řešil kritický problém správy časové synchronizace v heterogenních a více-připojených 5G sítích. V dřívějších generacích mobilních sítí přechody spojení a operace s jedním připojením často předpokládaly síťově synchronizované buňky. Avšak se zavedením Dual Connectivity v LTE a jeho rozšířením v 5G NR často nejsou buňky od různých základnových stanic (nebo dokonce různých [RAT](/mobilnisite/slovnik/rat/)) dokonale časově synchronizovány, zejména když jsou propojeny přes neideální přenosovou síť (např. rozhraní X2/Xn s proměnnou latencí). Tento nedostatek synchronizace může vést ke konfliktům v plánování, zvýšenému rušení a neúspěšným procedurám spojení, pokud není správně řízen.

Motivace pro vytvoření SFTD ve verzi 15 byla přímo spojena se zavedením 5G NR a silnou závislostí na EN-DC pro raná nasazení 5G (s využitím LTE kotvy). Předchozí mechanismy byly nedostatečné pro poskytování přesných měření časového rozdílu s asistencí UE potřebných pro robustní provoz DC. SFTD poskytuje standardizovaný způsob, jakým UE může měřit a hlásit tento rozdíl, čímž síti poskytuje potřebná data pro koordinaci vysílání a příjmu přes více přenosových bodů. Tím se řeší omezení odhadu synchronizace pouze na straně sítě, který může být přes neideální přenosovou síť nepřesný.

Tím, že SFTD umožňuje efektivní více-připojenost, přímo podporuje služby rozšířeného mobilního širokopásmového připojení (eMBB) tím, že umožňuje agregaci rádiových zdrojů z více buněk, čímž zvyšuje propustnost a spolehlivost pro uživatele. Je základním prvkem pro funkce jako podmíněný přechod spojení a přechod spojení typu make-before-break, které vyžadují přesnou znalost časování mezi kandidátními buňkami k provedení plynulé mobility pro uživatele, zejména při vysokých rychlostech nebo v hustých městských prostředích.

## Klíčové vlastnosti

- Měří a hlásí rozdíl v čísle systémového rámce (SFN) mezi dvěma buňkami
- Měří a hlásí rozdíl v čase začátku rámce s jemnou granularitou
- Podporuje měření mezi dvojicemi buněk NR-NR a LTE-NR
- Používá se pro konfiguraci a údržbu více-RAT Dual Connectivity (MR-DC)
- Zlepšuje přípravu a provedení přechodu spojení poskytnutím časových informací o cílové buňce
- Definované formáty hlášení a požadavky na přesnost v RRC a výkonnostních specifikacích

## Související pojmy

- [EN-DC – E-UTRA NR Dual Connectivity with MCG using E-UTRA and SCG using NR](/mobilnisite/slovnik/en-dc/)

## Definující specifikace

- **TS 38.133** (Rel-19) — 5G UE Radio Requirements for RRC_IDLE Mobility
- **TS 38.331** (Rel-19) — NR Radio Resource Control (RRC) Protocol Specification
- **TS 38.522** (Rel-19) — UE Conformance Test Applicability Statement

---

📖 **Anglický originál a plná specifikace:** [SFTD na 3GPP Explorer](https://3gpp-explorer.com/glossary/sftd/)
