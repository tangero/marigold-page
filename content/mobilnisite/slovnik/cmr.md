---
slug: "cmr"
url: "/mobilnisite/slovnik/cmr/"
type: "slovnik"
title: "CMR – Codec Mode Request"
date: 2025-01-01
abbr: "CMR"
fullName: "Codec Mode Request"
category: "Services"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/cmr/"
summary: "Codec Mode Request (CMR) je signalizační mechanismus používaný v hlasových službách přes sítě 3GPP pro dynamické vyžádání změny režimu řečového kodeku. Je zásadní pro kodeky Adaptive Multi-Rate (AMR),"
---

CMR je signalizační mechanismus používaný v hlasových službách 3GPP pro dynamické vyžádání změny režimu řečového kodeku, což umožňuje optimální adaptaci hlasové kvality na měnící se rádiové podmínky.

## Popis

Codec Mode Request (CMR) je klíčový řídicí parametr zabudovaný do řečových rámců kodeků Adaptive Multi-Rate ([AMR](/mobilnisite/slovnik/amr/)), AMR-Wideband ([AMR-WB](/mobilnisite/slovnik/amr-wb/)) a Enhanced Voice Services ([EVS](/mobilnisite/slovnik/evs/)) v systémech 3GPP. Funguje v rámci přenosové cesty hlasového kanálu, typicky mezi uživatelským zařízením (UE) a mediální bránou ([MGW](/mobilnisite/slovnik/mgw/)) nebo funkcí mediálních zdrojů ([MRF](/mobilnisite/slovnik/mrf/)) v jádru sítě. Pole CMR je součástí struktury datové části kodeku, specifikované ve formátech rámců AMR a EVS, a je přenášeno v pásmu společně s komprimovanými řečovými daty. Jeho primární funkcí je signalizovat požadovanou změnu aktivního režimu kodeku – v podstatě přenosové rychlosti a kódovacího schématu – pro následující řečové rámce od přijímající strany ke straně vysílající.

Z architektonického hlediska CMR umožňuje systém uzavřené smyčky adaptace. Během hlasového hovoru přijímač (např. vzdálené UE nebo síťový uzel) průběžně vyhodnocuje podmínky kanálu, jako je bloková chybovost ([BLER](/mobilnisite/slovnik/bler/)) nebo kvalita signálu. Na základě tohoto vyhodnocení určí nejvhodnější režim kodeku, který vyvažuje kvalitu řeči a robustnost. Například při špatných rádiových podmínkách může být upřednostněn režim s nižší přenosovou rychlostí a vyšší odolností vůči chybám (jako AMR 4,75 kbps). Přijímač pak vloží tento požadovaný režim do pole CMR dalšího odchozího řečového rámce, který vysílá zpět původnímu odesílateli. Po přijetí rámce obsahujícího CMR by měl vysílač přizpůsobit své kódování řeči na požadovaný režim pro budoucí rámce, čímž sladí přenos s vnímanými síťovými podmínkami na straně přijímače.

Klíčové komponenty zapojené do činnosti CMR zahrnují samotný řečový kodek (s jeho definovanými režimy), signalizační kanál v pásmu v rámci RTP datové části (podle [IETF](/mobilnisite/slovnik/ietf/) RFC 4867, 3267 a 3551 přijatých 3GPP) a algoritmy adaptace rychlosti v UE a síťových prvcích. Proces je řízen specifikacemi 3GPP, které detailně popisují činnost kodeku (řada TS 26.) a správu kanálů (řada TS 29.). CMR nefunguje izolovaně; spolupracuje s procedurami rekonfigurace rádiového přístupového kanálu (RAB) řízenými vrstvou řízení rádiových zdrojů ([RRC](/mobilnisite/slovnik/rrc/)) pro výraznější změny. CMR však poskytuje rychlejší metodu jemně odstupňované adaptace během relace.

Jeho role v síti je klíčová pro udržení konzistentní hlasové kvality a spolehlivosti služby. Umožněním dynamického přepínání přenosové rychlosti pomáhá CMR šetřit rádiové zdroře za dobrých podmínek (používáním režimů vyšší kvality) a zajišťuje pokračování hovoru při zhoršení (přepnutím na robustnější režimy). To přímo ovlivňuje metriky jako střední známka kvality (MOS) a míru přerušení hovorů. V nasazeních VoLTE a VoNR je CMR základní součástí zprostředkovatele hlasové služby, který zajišťuje, aby se kvalita hlasu založená na IP efektivně přizpůsobovala podkladovému rádiovému spoji LTE nebo NR.

## K čemu slouží

CMR byl vytvořen k řešení zásadní výzvy poskytování konzistentní, kvalitní hlasové služby přes bezdrátové kanály charakterizované velmi proměnlivými a nepředvídatelnými podmínkami, jako je útlum, interference a měnící se mobilita uživatele. Před adaptivními kodeky, jako je AMR, se používaly kodeky s pevnou přenosovou rychlostí (např. Full Rate nebo Enhanced Full Rate v GSM). Tyto kodeky pracovaly na jediné přenosové rychlosti, což je činilo suboptimálními: buď plýtvaly kapacitou, když byly podmínky kanálu dobré (nevyužitím dostupné šířky pásma pro vyšší kvalitu), nebo trpěly nepřijatelným zhoršením kvality, když byly podmínky špatné, protože jim chyběl mechanismus pro dynamické vyvážení přenosové rychlosti a zvýšené ochrany proti chybám.

Zavedení AMR v 3GPP Release 98 (GSM) a jeho integrace do UMTS (Release 99) představovalo změnu paradigmatu, přičemž CMR byl jeho klíčovým řídicím mechanismem. Účelem CMR je umožnit tuto adaptaci v reálném čase během aktivního hovoru. Řeší omezení statických kodeků tím, že poskytuje signalizační kanál v pásmu s nízkou latencí, aby přijímač mohl informovat vysílač o optimálním pracovním bodě. To bylo motivováno potřebou současně zlepšit efektivitu využití spektra a uživatelský zážitek. CMR umožňuje síti maximalizovat hlasovou kapacitu (zařazením více uživatelů při použití nižších rychlostí) a zároveň zajistit, aby byla kvalita jednotlivých hovorů udržována během výkyvů signálu.

Dále, jak se služby vyvíjely směrem k širokopásmovému (AMR-WB) a superširokopásmovému (EVS) hlasu, rozsah možných režimů kodeku se významně rozšířil, čímž se zvýšil potenciální přínos dynamické adaptace. CMR byl rozšířen na tyto kodeky, čímž vyřešil problém efektivního řízení mnohem větší sady přenosových rychlostí a šířek pásma přes IP přenosy, jako je VoLTE. Zajišťuje, že vylepšená hlasová kvalita EVS například nepřichází na úkor spolehlivosti; kodek může plynule přejít na užší šířku pásma nebo robustnější režim, když je to potřeba, a to vše řízeno mechanismem CMR.

## Klíčové vlastnosti

- Signalizace v pásmu uvnitř datové části řečového rámce pro minimální latenci
- Dynamické vyžádání změny režimu kodeku (přenosová rychlost/šířka pásma) od přijímače k vysílači
- Podpora více rodin kodeků: AMR, AMR-WB a EVS
- Umožňuje kompromis mezi kvalitou řeči a odolností vůči chybám na základě rádiových podmínek
- Funguje nezávisle, ale doplňuje se s rekonfigurací RAB řízenou sítí
- Standardizovaný formát rámce a umístění pole CMR v 3GPP TS 26.103 a souvisejících specifikacích

## Definující specifikace

- **TS 26.103** (Rel-19) — 3GPP Codec Lists for OoBTC and TrFO
- **TS 26.114** (Rel-19) — IMS Multimedia Telephony Media Handling
- **TS 26.253** (Rel-19) — IVAS Codec Algorithmic Description
- **TS 26.453** (Rel-19) — EVS Codec Generic Frame Format for 3G CS Networks
- **TR 26.910** (Rel-19) — MTSI enhancements for RAN delay budget reporting
- **TR 26.919** (Rel-19) — Study on 5G Conversational Media Handling
- **TR 26.935** (Rel-19) — Speech Codec Performance for Packet Switched Multimedia
- **TS 29.163** (Rel-19) — Interworking between 3GPP IM CN and CS networks
- **TS 29.414** (Rel-19) — Nb Interface Bearer Transport & Control Protocols
- **TS 29.415** (Rel-19) — Nb User Plane Protocol Specification
- **TS 36.321** (Rel-19) — E-UTRA MAC Protocol Specification
- **TS 36.750** (Rel-14) — Study on enhancement of VoLTE
- **TS 38.306** (Rel-19) — NR UE Radio Access Capability Parameters
- **TS 38.522** (Rel-19) — UE Conformance Test Applicability Statement
- **TS 45.009** (Rel-19) — GSM AMR Link Adaptation & Control

---

📖 **Anglický originál a plná specifikace:** [CMR na 3GPP Explorer](https://3gpp-explorer.com/glossary/cmr/)
