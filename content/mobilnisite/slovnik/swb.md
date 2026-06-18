---
slug: "swb"
url: "/mobilnisite/slovnik/swb/"
type: "slovnik"
title: "SWB – Super Wideband"
date: 2025-01-01
abbr: "SWB"
fullName: "Super Wideband"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/swb/"
summary: "Zvukové pásmo 50–14000 Hz, známé také jako HD Voice nebo Wideband+, používané v hlasových službách k poskytnutí výrazně vyšší kvality zvuku a přirozenosti ve srovnání s tradiční úzkopásmovou telefonii"
---

SWB je zvukové pásmo 50–14000 Hz používané v mobilních hlasových službách k zajištění vyšší kvality zvuku zachycením větší části spektra lidského hlasu.

## Popis

Super Wideband (SWB) označuje rozsah audiofrekvencí od 50 Hz do 14 000 Hz (14 kHz) používaný pro kódování a přenos hlasových signálů v telekomunikacích. Jedná se o podstatné rozšíření oproti tradičnímu úzkopásmovému ([NB](/mobilnisite/slovnik/nb/)) hlasu (300–3400 Hz) i standardnímu širokopásmovému ([WB](/mobilnisite/slovnik/wb/)) hlasu (50–7000 Hz). Zvýšená šířka pásma umožňuje audiokodekům zachytit a reprodukovat mnohem bohatší část akustického spektra, včetně vyšších frekvencí souhlásek (jako 's' a 'f'), jemných harmonických složek a přirozenějšího zabarvení, což vede ke kvalitě hlasu často popisované jako 'živá' nebo 'tváří v tvář'.

Technicky je SWB umožněno pokročilými audiokodeky standardizovanými 3GPP a [ITU-T](/mobilnisite/slovnik/itu-t/), jako je kodek Enhanced Voice Services ([EVS](/mobilnisite/slovnik/evs/)). Kodek EVS je hlavním prvkem umožňujícím SWB v sítích 3GPP. Pracuje s více režimy šířky pásma, včetně SWB. Proces zahrnuje zachycení audia až do 14 kHz mikrofonem a audiofront-endem v zařízení. Kódovník EVS poté tento signál efektivně komprimuje. Zakódovaný bitový proud je paketizován a přenášen přes hlasový bearer sítě (např. prostřednictvím VoLTE nebo VoNR). Na přijímací straně dekodér EVS rekonstruuje SWB audio signál, který je následně přehrán reproduktorem. End-to-end.

Její role v síti je jako klíčová kvalitativní funkce pro služby Voice over LTE (VoLTE) a Voice over NR (VoNR). Operátoři nasazují a konfigurují kodek EVS s podporou SWB ve svém IMS (IP Multimedia Subsystem) jádru. Během sestavování hovoru si koncová zařízení a síť vyjednávají nejvyšší vzájemně podporovaný režim kodeku pomocí signalizace [SIP](/mobilnisite/slovnik/sip/)/[SDP](/mobilnisite/slovnik/sdp/). Pokud ji podporují oba konce i síťová cesta, je navázán SWB hovor. Síť musí zajistit dostatečnou kvalitu služeb (např. nízkou ztrátu paketů, chvění a latenci), aby udržela výhody vyššího datového toku SWB kódování. SWB je významným krokem k imerzním komunikačním zážitkům a základní schopností pro budoucí služby, jako jsou komunikace v rozšířené realitě ([XR](/mobilnisite/slovnik/xr/)).

## K čemu slouží

Super Wideband audio bylo vytvořeno za účelem posunutí hranic vnímané kvality hlasu v mobilních sítích za možnosti širokopásmového přenosu ([HD](/mobilnisite/slovnik/hd/) Voice). Zatímco širokopásmový přenos (50–7000 Hz) poskytl významné zlepšení oproti úzkopásmovému, stále mu chyběly nejvyšší frekvence, které přispívají k pocitu přítomnosti, srozumitelnosti a přirozenosti, zejména v hlučném prostředí. SWB to řeší rozšířením zachytávaného pásma na 14 kHz, což pokrývá téměř celý rozsah základních frekvencí a důležitých harmonických složek lidského hlasu.

Motivace byla hnána konkurenčním tlakem nabízet prémiové hlasové služby a zlepšit uživatelský zážitek jako diferenciátor. Slouží také technickým cílům vývoje sítě. Jak sítě migrovaly na plně IP jádra (IMS) s VoLTE, byla odstraněna omezení starších okruhově spínaných hlasových kodeků, což vytvořilo příležitost zavést pokročilejší a efektivnější kodeky, jako je EVS. Podpora SWB v rámci EVS řeší problém doručování studiové kvality hlasu přes mobilní pakety při zachování odolnosti vůči ztrátě paketů a efektivního využití šířky pásma. Byl to přirozený vývoj v úsilí o transparentní kvalitu audia, kdy je přenášený hlas nerozlišitelný od přímého, akusticky dokonalého spojení.

## Klíčové vlastnosti

- Rozsah audiofrekvencí 50–14000 Hz (šířka pásma 14 kHz)
- Umožněno primárně kodekem 3GPP EVS (Enhanced Voice Services)
- Poskytuje 'živou' nebo 'tváří v tvář' kvalitu hlasu a srozumitelnost
- Vyžaduje podporu v hardwaru koncového zařízení (mikrofony/reproduktory), softwaru a síťovém IMS
- Vyjednáváno během sestavování IMS hovoru pomocí vyjednávání kodeků SIP/SDP
- Často operátory uváděno na trh jako 'HD Voice+' nebo 'Full HD Voice'

## Související pojmy

- [EVS – Enhanced Voice Services (specifically, the AMR-WB IO mode: AMR-WB Interoperable)](/mobilnisite/slovnik/evs/)
- [AMR-WB – Adaptive Multi-Rate Wideband Speech Codec](/mobilnisite/slovnik/amr-wb/)
- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)

## Definující specifikace

- **TR 22.813** (Rel-10) — Enhanced Voice Services for EPS Study
- **TS 23.782** (Rel-15) — Interworking between LTE MC and non-LTE MC systems
- **TS 26.103** (Rel-19) — 3GPP Codec Lists for OoBTC and TrFO
- **TS 26.179** (Rel-19) — Codecs and Media Handling for MCPTT
- **TS 26.258** (Rel-19) — IVAS Codec Floating-Point C Code Specification
- **TS 26.441** (Rel-19) — EVS Audio Processing Introduction
- **TS 26.442** (Rel-19) — EVS Codec Fixed Point ANSI-C Code
- **TS 26.443** (Rel-19) — EVS Codec Floating-Point C Code
- **TS 26.444** (Rel-19) — EVS Codec Conformance Test Sequences
- **TS 26.446** (Rel-19) — EVS Codec AMR-WB Backward Compatibility Spec
- **TS 26.447** (Rel-19) — EVS Frame Loss Concealment Procedure
- **TS 26.448** (Rel-19) — EVS Jitter Buffer Management Specification
- **TS 26.450** (Rel-19) — EVS Codec DTX System Level Aspects
- **TS 26.451** (Rel-19) — EVS Codec Voice Activity Detector (VAD) Specification
- **TS 26.452** (Rel-19) — EVS Codec Fixed-Point C Code Implementation
- … a dalších 5 specifikací

---

📖 **Anglický originál a plná specifikace:** [SWB na 3GPP Explorer](https://3gpp-explorer.com/glossary/swb/)
