---
slug: "dpc"
url: "/mobilnisite/slovnik/dpc/"
type: "slovnik"
title: "DPC – Device Playback Capabilities"
date: 2025-01-01
abbr: "DPC"
fullName: "Device Playback Capabilities"
category: "Services"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/dpc/"
summary: "Soubor parametrů popisujících audio a video přehrávací charakteristiky uživatelského zařízení, jako jsou podporované kodeky, rozlišení a datové toky. Používá se při adaptaci médií a vyjednávání služeb"
---

DPC je soubor parametrů popisujících audio a video přehrávací charakteristiky zařízení, jako jsou podporované kodeky a rozlišení, používaný pro adaptaci médií a vyjednávání služeb.

## Popis

Device Playback Capabilities (DPC) označují technické specifikace a limity subsystému pro vykreslování multimédií v uživatelském zařízení (UE). V architektuře 3GPP nejde o samostatný protokol, ale o konceptuální soubor atributů používaných v protokolech a procedurách aplikační vrstvy. Tyto schopnosti jsou typicky sdělovány UE síťovým prvkům, jako je aplikační server ([AS](/mobilnisite/slovnik/as/)) nebo funkce mediálních prostředků ([MRF](/mobilnisite/slovnik/mrf/)), během zahájení služby nebo vyjednávání relace. DPC zahrnuje podrobné informace o podporovaných audio a video kodecích (např. [AMR-WB](/mobilnisite/slovnik/amr-wb/), [EVS](/mobilnisite/slovnik/evs/), H.264, [HEVC](/mobilnisite/slovnik/hevc/)) včetně jejich profilů, úrovní a konfiguračních parametrů. Zahrnuje také charakteristiky displeje, jako je maximální podporované rozlišení, snímková frekvence, barevná hloubka a velikost obrazovky, stejně jako audio schopnosti, například počet kanálů a podporované vzorkovací frekvence.

Mechanismus pro sdělení DPC často využívá stávající protokoly. Například v IP Multimedia Subsystem (IMS) se pro výměnu mediálních schopností během navazování relace používá Session Description Protocol (SDP) uvnitř zpráv SIP. UE ve své SDP nabídce uvádí své preference a omezení týkající se kodeků. Síťová strana (např. server služby multimediální telefonie) tyto informace využívá, případně v kombinaci se síťovými politikami a dostupnou šířkou pásma, k provedení adaptace médií nebo překódování datového toku. Tím je zajištěno, že mediální stream zaslaný UE je v rámci jeho možností dekódování a vykreslování. Proces zahrnuje porovnání DPC s charakteristikami obsahu a stavem sítě za účelem výběru optimálního mediálního formátu, čímž se předejde chybám při přehrávání, nadměrné spotřebě baterie v důsledku dekódování nepodporovaných formátů nebo plýtvání přenosovou kapacitou zasíláním zbytečně vysoce kvalitních streamů.

Ve specifikacích 3GPP, jako je TS 26.265 (kodek pro vylepšené hlasové služby) a TS 25.423 (rozhraní Iur), se informace související s DPC používají k zajištění kontinuity a kvality služeb. Například při předávání spojení nebo ve scénářích multimediálního vysílání pomáhá znalost DPC sítě rozhodnout o nejvhodnější konfiguraci přenosového kanálu nebo vysílacího profilu. Role DPC je klíčová pro zajištění konzistentního uživatelského zážitku (QoE) napříč heterogenním ekosystémem zařízení, kde telefony, tablety a zařízení IoT mají velmi rozdílný výpočetní výkon a možnosti zobrazení. Umožňuje efektivní využití rádiových prostředků tím, že se zabrání přenosu médií, která zařízení nedokáže zpracovat, což je klíčový aspekt pro plánování a optimalizaci kapacity sítě.

## K čemu slouží

Device Playback Capabilities existují proto, aby řešily problém heterogenity zařízení v masově rozšířených mobilních službách. Jak se mobilní sítě vyvíjely od primárně hlasových služeb k bohatým multimédiím, rozmanitost uživatelských zařízení explodovala, přičemž každé mělo jiné hardwarové možnosti. Bez možnosti tyto schopnosti sdělovat by sítě musely buď předpokládat nejnižšího společného jmenovatele (což by vedlo ke špatné kvalitě pro schopná zařízení), nebo vysílat vysoce kvalitní streamy, které některá zařízení nedokázala dekódovat (což by způsobilo selhání služby nebo plýtvání prostředky). DPC poskytuje potřebné informace pro inteligentní adaptaci médií.

Vznik tohoto konceptu byl motivován potřebou efektivního poskytování služeb a lepšího uživatelského zážitku. Rané mobilní video služby často používaly pevné formáty, což vedlo k problémům s kompatibilitou. Integrace DPC do protokolů pro vyjednávání relací, jako je SDP, umožnila dynamický a optimální výběr formátu. Tím se odstranila omezení statického poskytování a univerzálních řešení. V kontextu 3GPP specifikace odkazující na DPC (např. pro služby založené na IMS nebo [MBMS](/mobilnisite/slovnik/mbms/)) zajišťují, že multimediální služby jsou dostupné a dobře fungují na jakémkoli kompatibilním zařízení, což je zásadní pro komerční úspěch služeb jako videohovory, mobilní TV a streamování. Umožňuje také síťovým operátorům efektivněji spravovat síťovou zátěž přizpůsobením mediálních streamů možnostem zařízení.

## Klíčové vlastnosti

- Popisuje podporované audio/video kodeky, profily a úrovně
- Zahrnuje parametry zobrazení zařízení, jako je rozlišení a snímková frekvence
- Sděleno prostřednictvím SDP v IMS/SIP nebo jiných protokolech aplikační vrstvy
- Umožňuje síťovou adaptaci médií a překódování datového toku
- Používá se pro optimální výběr přenosového kanálu a správu kontinuity služeb
- Základní pro zajištění kvality uživatelského zážitku na různorodých zařízeních

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [CODEC – Coder/Decoder](/mobilnisite/slovnik/codec/)

## Definující specifikace

- **TS 25.423** (Rel-19) — UTRAN RNSAP Specification
- **TS 25.427** (Rel-19) — UTRAN Iub/Iur User Plane Protocols
- **TS 26.265** (Rel-19) — Video Operation Points & Capabilities
- **TR 45.903** (Rel-19) — SAIC Feasibility Study for GSM Networks

---

📖 **Anglický originál a plná specifikace:** [DPC na 3GPP Explorer](https://3gpp-explorer.com/glossary/dpc/)
