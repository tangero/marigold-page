---
slug: "cs"
url: "/mobilnisite/slovnik/cs/"
type: "slovnik"
title: "CS – Circuit Switched"
date: 2026-01-01
abbr: "CS"
fullName: "Circuit Switched"
category: "Core Network"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/cs/"
summary: "Circuit Switched (CS) je tradiční telekomunikační metoda, která na celou dobu hovoru vytváří vyhrazený fyzický okruh. Tvoří základ pro zastaralé hlasové a datové služby v sítích 2G a 3G a poskytuje ga"
---

CS je tradiční telekomunikační metoda, která na celou dobu hovoru vytváří vyhrazený fyzický okruh, tvořící základ pro zastaralé hlasové a datové služby v sítích 2G a 3G.

## Popis

Technologie Circuit Switched (CS) funguje tak, že na celou dobu komunikační relace vytvoří vyhrazené, koncové fyzické nebo logické spojení mezi dvěma stranami. Toto spojení rezervuje pevné množství síťových prostředků, jako je časový úsek v rámci [TDM](/mobilnisite/slovnik/tdm/) (Time Division [Multiplexing](/mobilnisite/slovnik/multiplexing/)) nebo konkrétní frekvenční kanál, a zajišťuje jejich výhradní využití až do ukončení hovoru. V architektuře 3GPP je doména CS podsystémem jádra sítě zodpovědným za zpracování těchto tradičních telefonních služeb. Skládá se z klíčových síťových prvků, jako je Mobile Switching Center ([MSC](/mobilnisite/slovnik/msc/)), které provádí přepojování hovorů a správu mobility, a Visitor Location Register ([VLR](/mobilnisite/slovnik/vlr/)), který ukládá data účastníků nacházejících se v jeho servisní oblasti. Doména CS komunikuje s rádiovou přístupovou sítí (RAN) prostřednictvím rozhraní A v GSM nebo rozhraní Iu-CS v UMTS za účelem správy rádiových prostředků pro přenos okruhově přepínaného přenosu.

Při zahájení CS hovoru, například hlasového, síť provede proceduru sestavení, která zahrnuje autentizaci, alokaci prostředků a směrování. Je přidělen a nepřetržitě udržován vyhrazený přenos, často 64 kbps kanál pro řeč (založený na [PCM](/mobilnisite/slovnik/pcm/) kódování). Tento přenos poskytuje konstantní přenosovou rychlost, což je klíčové pro služby v reálném čase, protože minimalizuje chvění a zpoždění a zajišťuje předvídatelný výkon. Signalizace řízení hovoru, která spravuje jeho sestavení, udržování a uvolnění, je typicky řešena protokoly jako [ISDN](/mobilnisite/slovnik/isdn/) User Part ([ISUP](/mobilnisite/slovnik/isup/)) v jádru sítě a [DTAP](/mobilnisite/slovnik/dtap/) (Direct Transfer Application Part) přes rádiové rozhraní. Architektura domény CS je ze své podstaty spojově orientovaná, což znamená, že stav hovoru a jeho vyhrazená cesta jsou po celou dobu relace udržovány síťovými uzly.

Role domény CS přesahuje prostý hlas a zahrnuje okruhově přepínané datové služby, jako je fax a zastaralé datové hovory (např. přes modem). Tyto služby využívají stejný princip vyhrazeného kanálu, což zajišťuje integritu dat a časovou synchronizaci. Tento přístup je však náročný na prostředky, protože vyhrazený kanál zůstává obsazen i během tichých období konverzace, což vede k neefektivnímu využití šířky pásma ve srovnání s paketově přepínanými metodami. V sítích 3GPP doména CS koexistovala s doménou Packet Switched (PS), přičemž ta druhá zpracovávala IP datové služby. Zavedení IP Multimedia Subsystem (IMS) a Voice over LTE (VoLTE) znamenalo poskytování hlasu jako paketově přepínané služby přes IP, což nakonec vedlo k postupnému vyřazování domény CS v sítích 4G a 5G, přestože zůstává kritická pro podporu zastaralých služeb a scénáře navrácení.

## K čemu slouží

Technologie Circuit Switched byla vytvořena za účelem poskytování spolehlivých telekomunikačních služeb v reálném čase, primárně hlasových hovorů, garantováním vyhrazených síťových prostředků na dobu trvání relace. Řešila základní problém umožnění synchronní komunikace na velké vzdálenosti se stálou kvalitou, nízkou latencí a minimální ztrátou paketů. Před nástupem digitálního paketového přepínání byl CS dominantním paradigmatem v telefonních sítích (jako PSTN) a jeho integrace do mobilních sítí (GSM, UMTS) umožnila bezproblémové mobilní hlasové služby s interoperabilitou s pevnými sítěmi. Vyhrazený okruh zajišťuje, že jakmile je hovor sestaven, je kvalita služby udržována bez konkurence ostatních uživatelů, což je zásadní pro konverzační služby.

Historický kontext CS v 3GPP začíná u GSM (2G), kde byla jedinou metodou pro poskytování hlasových a nízkorychlostních datových služeb. Řešila omezení dřívějších analogových celulárních systémů poskytováním digitální, zabezpečené a standardizované hlasové komunikace. Návrh domény CS byl motivován potřebou předvídatelného výkonu a kompatibility s existující globální telefonní infrastrukturou, což umožnilo mezinárodní roaming a vzájemné propojení. Její model rezervace prostředků však vede k neefektivitě, protože šířka pásma není sdílena statisticky a zůstává nevyužitá během tichých období. Tato neefektivita spolu s rostoucí poptávkou po datových službách poháněla vývoj paketově přepínaných alternativ.

V pozdějších vydáních 3GPP se účel CS vyvinul na podporu zastaralých služeb během přechodu na plně IP sítě. Poskytovala mechanismus navrácení pro hlasové služby v oblastech bez pokrytí paketově přepínaného hlasu (např. Circuit Switched Fallback - CSFB v LTE) a zajišťovala zpětnou kompatibilitu. Technologie řešila bezprostřední problém udržení kontinuity hlasových služeb během migrace na 4G a 5G, ale její dlouhodobá role se zmenšila, když se standardem pro poskytování hlasu staly služby založené na IMS, jako VoLTE a VoNR (Voice over New Radio), nabízející větší flexibilitu a integraci s multimediálními službami.

## Klíčové vlastnosti

- Vyhrazené koncové spojení na celou dobu trvání hovoru
- Garantovaná šířka pásma a konstantní přenosová rychlost pro služby v reálném čase
- Nízká latence a minimální chvění vhodné pro hlasové a videohovory
- Založeno na principech TDM (Time Division Multiplexing) v zastaralých implementacích
- Používá standardizované signalizační protokoly jako ISUP a DTAP pro řízení hovoru
- Poskytuje interoperabilitu se zastaralou PSTN a dalšími okruhově přepínanými sítěmi

## Definující specifikace

- **TS 21.810** (Rel-4) — Multi-mode UE Issues - Categories, principles and procedures
- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TR 21.910** (Rel-4) — Multi-mode UE Operation Principles
- **TS 22.038** (Rel-19) — USIM Application Toolkit (USAT) Stage 1
- **TS 22.057** (Rel-19) — Mobile Execution Environment (MExE) Stage 1
- **TS 22.100** (Rel-4) — UMTS Service Requirements Phase 1
- **TS 22.135** (Rel-19) — Multicall Supplementary Service Specification
- **TS 22.173** (Rel-20) — IMS Multimedia Telephony Service Definition
- **TS 22.226** (Rel-19) — Global Text Telephony (GTT) Stage 1
- **TS 22.228** (Rel-19) — IP Multimedia Service Requirements
- **TS 22.234** (Rel-13) — 3GPP-WLAN Interworking Index Specification
- **TS 22.273** (Rel-7) — IMS Multimedia Telephony with PSTN/ISDN Simulation
- **TS 22.495** (Rel-7) — NGN Requirements for IMS Services
- **TS 22.811** (Rel-7) — Network Selection Mechanisms Overview
- **TR 22.813** (Rel-10) — Enhanced Voice Services for EPS Study
- … a dalších 127 specifikací

---

📖 **Anglický originál a plná specifikace:** [CS na 3GPP Explorer](https://3gpp-explorer.com/glossary/cs/)
