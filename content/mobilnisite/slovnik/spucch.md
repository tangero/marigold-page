---
slug: "spucch"
url: "/mobilnisite/slovnik/spucch/"
type: "slovnik"
title: "SPUCCH – Short Physical Uplink Control Channel"
date: 2025-01-01
abbr: "SPUCCH"
fullName: "Short Physical Uplink Control Channel"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/spucch/"
summary: "SPUCCH je fyzický řídicí kanál v uplinku v LTE a NR navržený pro přenos řídicích informací v uplinku (UCI), jako je HARQ ACK/NACK a žádosti o plánování, s nízkou latencí. Používá krátkodobý formát, kt"
---

SPUCCH (zkrácený fyzický řídicí kanál v uplinku) je krátkodobý fyzický řídicí kanál v uplinku v LTE a NR určený pro přenos řídicích informací v uplinku (jako HARQ zpětná vazba a žádosti o plánování) s nízkou latencí.

## Popis

Short Physical Uplink Control Channel (SPUCCH) je kanál fyzické vrstvy standardizovaný v 3GPP, primárně pro systémy LTE a NR, který přenáší řídicí informace v uplinku ([UCI](/mobilnisite/slovnik/uci/)) se zkrácenou dobou přenosu. Na rozdíl od staršího [PUCCH](/mobilnisite/slovnik/pucch/), který zabírá celý subrámec nebo slot, je SPUCCH navržen s krátkou dobou trvání, často pouze několik symbolů v rámci subrámce nebo slotu. Tento návrh minimalizuje latenci pro řídicí signalizaci, což je zásadní pro aplikace vyžadující ultra-spolehlivou komunikaci s nízkou latencí ([URLLC](/mobilnisite/slovnik/urllc/)), jako je průmyslová automatizace a autonomní vozidla. SPUCCH přenáší kritickou zpětnou vazbu, jako jsou potvrzení Hybrid Automatic Repeat Request ([HARQ](/mobilnisite/slovnik/harq/)) ([ACK](/mobilnisite/slovnik/ack/)/[NACK](/mobilnisite/slovnik/nack/)), informace o stavu kanálu ([CSI](/mobilnisite/slovnik/csi/)) a žádosti o plánování ([SR](/mobilnisite/slovnik/sr/)), čímž zajišťuje efektivní využití zdrojů a spolehlivý přenos dat.

Architektonicky je SPUCCH integrován do rámcové struktury uplinku a zabírá specifické prvky zdrojů (RE) v časově-frekvenční mřížce. Funguje v rámci fyzické vrstvy (vrstva 1) protokolového zásobníku, jak je definováno ve specifikacích jako 36.201 a 36.212 pro LTE a 38.889 pro NR. Kanál používá modulační schémata jako Binary Phase Shift Keying (BPSK) nebo Quadrature Phase Shift Keying (QPSK) pro kódování řídicích bitů a může využívat sekvenčně nebo blokově založené rozprostírací techniky pro zvýšení odolnosti proti rušení. Mezi klíčové komponenty patří mechanismus přidělování zdrojů, který dynamicky nebo semi-staticky přiřazuje zdroje SPUCCH prostřednictvím signalizace Radio Resource Control (RRC), a schéma multiplexování, které umožňuje více uživatelům sdílet zdroje SPUCCH pomocí ortogonálních sekvencí nebo frekvenčního dělení.

Při provozu SPUCCH funguje tak, že mapuje zakódované bity UCI na fyzické zdroje na základě konfigurací od základnové stanice (např. eNB v LTE nebo gNB v NR). Proces přenosu zahrnuje kódování kanálu, modulaci a mapování na RE, následované inverzní rychlou Fourierovou transformací (IFFT) pro generování OFDM vlnového tvaru. SPUCCH podporuje více formátů přizpůsobených různým velikostem užitečného zatížení a požadavkům na latenci, jako jsou krátkodobé formáty pro ACK/NACK a delší formáty pro hlášení CSI. Jeho role v síti je klíčová pro udržování adaptace spoje, umožnění rychlých retransmisí a podporu dynamického plánování, čímž zlepšuje celkový výkon systému, spektrální účinnost a uživatelský komfort v nasazeních LTE i 5G NR.

## K čemu slouží

SPUCCH byl vytvořen, aby řešil rostoucí poptávku po řídicí signalizaci s nízkou latencí v moderních mobilních sítích, zejména s nástupem 5G a jeho důrazem na URLLC. Před SPUCCH používal starší PUCCH v LTE delší doby přenosu (např. celé subrámy), což zavádělo zpoždění ve zpětnovazebních smyčkách pro HARQ a plánování. Toto omezení bránilo aplikacím vyžadujícím latenci na úrovni milisekund, jako je řízení v reálném čase v průmyslovém IoT a komunikace vozidlo-se-vším (V2X). SPUCCH to řeší zkrácením doby trvání řídicího kanálu, což umožňuje rychlejší potvrzení a žádosti o zdroje, a tím zlepšuje odezvu a spolehlivost sítě.

Historicky, jak se 3GPP vyvíjelo od Rel-14 k Rel-15, potřeba efektivnějších řídicích kanálů v uplinku se stala zřejmou se zavedením NR a vylepšených funkcí LTE. SPUCCH byl motivován požadavkem na podporu různých případů užití v 5G, včetně komunikace s masivním počtem strojů (mMTC) a vylepšeného mobilního širokopásmového přístupu (eMBB), kde je efektivní řídicí signalizace klíčová pro škálovatelnost a výkon. Minimalizací režie a latence řídicí signalizace SPUCCH usnadňuje pokročilé techniky, jako je uplinkový přenos bez udělení grantu a dynamický TDD, čímž řeší omezení předchozích přístupů, které byly optimalizovány pro méně přísné cíle latence.

## Klíčové vlastnosti

- Krátkodobý formát pro přenos UCI s nízkou latencí
- Podporuje HARQ ACK/NACK, CSI a žádosti o plánování
- Používá modulaci BPSK/QPSK a sekvenčně založené rozprostírání
- Dynamické nebo semi-statické přidělování zdrojů prostřednictvím signalizace RRC
- Více formátů pro různé velikosti užitečného zatížení a případy užití
- Zvýšená odolnost proti rušení prostřednictvím ortogonálního multiplexování

## Související pojmy

- [PUCCH – Physical Uplink Control Channel](/mobilnisite/slovnik/pucch/)
- [UCI – Uplink Control Information](/mobilnisite/slovnik/uci/)
- [HARQ – Hybrid Automatic Repeat Request](/mobilnisite/slovnik/harq/)
- [URLLC – Ultra Reliable Low Latency Communication](/mobilnisite/slovnik/urllc/)

## Definující specifikace

- **TS 36.201** (Rel-19) — LTE Physical Layer General Description
- **TS 36.212** (Rel-19) — LTE Multiplexing and Channel Coding
- **TS 36.300** (Rel-19) — E-UTRAN Radio Interface Protocol Architecture Overview
- **TS 36.302** (Rel-19) — E-UTRA Physical Layer Services
- **TS 36.331** (Rel-19) — LTE RRC Protocol Specification
- **TR 38.889** (Rel-16) — NR-based access to unlicensed spectrum study

---

📖 **Anglický originál a plná specifikace:** [SPUCCH na 3GPP Explorer](https://3gpp-explorer.com/glossary/spucch/)
