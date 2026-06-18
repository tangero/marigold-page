---
slug: "rohc"
url: "/mobilnisite/slovnik/rohc/"
type: "slovnik"
title: "ROHC – Robust Header Compression"
date: 2026-01-01
abbr: "ROHC"
fullName: "Robust Header Compression"
category: "Protocol"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/rohc/"
summary: "Protokol, který výrazně snižuje režii záhlaví IP paketů (např. IPv4, IPv6, UDP, RTP, TCP) přenášených přes bezdrátové spoje s omezenou šířkou pásma. Funguje tak, že mezi kompresorem a dekompresorem vy"
---

ROHC je protokol, který snižuje režii záhlaví IP paketů bezdrátovými spoji vytvořením kompresního kontextu, kdy se zpočátku posílají plná záhlaví a následně pouze malé identifikátory, čímž se zlepšuje spektrální účinnost a snižuje latence.

## Popis

Robust Header Compression (ROHC) je standardizovaný rámec původně definovaný v [IETF](/mobilnisite/slovnik/ietf/) [RFC](/mobilnisite/slovnik/rfc/) 3095 a podrobně profilovaný a přijatý organizací 3GPP pro mobilní sítě počínaje Release 5. Jde o bezeztrátový kompresní protokol určený ke kompresi záhlaví toků IP provozu před přenosem přes rozhraní rádiového rozhraní. Protokol je implementován ve vrstvě Packet Data Convergence Protocol ([PDCP](/mobilnisite/slovnik/pdcp/)) v zásobnících 3GPP ([UTRAN](/mobilnisite/slovnik/utran/), [E-UTRAN](/mobilnisite/slovnik/e-utran/), NG-RAN). ROHC identifikuje pole v záhlavích protokolů, která jsou konstantní, předvídatelná (např. sekvenčně se zvyšující čísla sekvencí), nebo odvoditelná z jiných vrstev, a potlačuje jejich přenos po počáteční synchronizaci.

Architektura zahrnuje kompresor (v uzlu vysílajícím, např. UE nebo gNB) a dekompresor (v uzlu přijímajícím). Tyto jednotky udržují synchronizované kompresní kontexty, což jsou sady informací o polích záhlaví toku paketů. ROHC pracuje v několika stavech (režimech), které umožňují kompromis mezi účinností a robustností: stav inicializace a obnovy ([IR](/mobilnisite/slovnik/ir/)), kdy se posílají plná záhlaví pro vytvoření kontextu; stav první úrovně (FO), kde se dynamická pole komprimují pomocí vzorců; a stav druhé úrovně ([SO](/mobilnisite/slovnik/so/)), kdy se pro maximální kompresi posílá pouze malý kontextový identifikátor ([CID](/mobilnisite/slovnik/cid/)) a kontrolní součet (CRC). Protokol využívá více zpětnovazebních kanálů (režimy s potvrzením, bez potvrzení a obousměrný optimistický režim) pro zvládání chyb a zajištění synchronizace kontextu i přes ztrátové rádiové spoje.

Příklad fungování pro typický VoIP (RTP/UDP/IP) paket: První paket je odeslán s plným záhlavím (IR paket). Dekompresor se naučí statická pole (IP adresy, porty) a měnící se vzorek dynamických polí (RTP číslo sekvence, časové razítko). Pro další paket kompresor odešle komprimované záhlaví obsahující malý CID a zakódované rozdíly (deltas) pro dynamická pole. V nejúčinnějším stavu může poslat pouze 1bajtové záhlaví s CRC. Pokud dekompresor detekuje chybu pomocí CRC nebo mezery v číslování sekvencí, může prostřednictvím zpětné vazby vyžádat aktualizaci kontextu nebo počkat na periodické obnovení. ROHC definuje specifické profily pro různé zásobníky protokolů (např. profil 0x0001 pro RTP/UDP/IP, profil 0x0002 pro UDP/IP, profil 0x0006 pro TCP/IP). Specifikace 3GPP podrobně popisují, jak je ROHC integrováno do vrstvy PDCP, včetně správy kontextu během předávání spojení a nastavování přenosového kanálu.

## K čemu slouží

ROHC byl vytvořen k řešení značné neefektivity přenosu plných IP záhlaví přes bezdrátové spoje s nízkou šířkou pásma, vysokou latencí a náchylné k chybám. Na počátku 21. století, kdy začaly 3G sítě přenášet IP provoz, se ukázalo, že režie záhlaví IPv4 (20 bajtů) nebo IPv6 (40 bajtů) plus UDP (8 bajtů) a RTP (12 bajtů) může být větší než samotný hlasový užitečný obsah u VoIP. Tím se plýtvalo vzácným rádiovým spektrem a zvyšovalo se zpoždění paketů. Předchozí řešení před ROHC byla méně odolná vůči ztrátě paketů a měla omezenou kompresní účinnost.

Motivace pro standardizaci ROHC v rámci 3GPP spočívala v umožnění efektivní podpory služeb v reálném čase, jako je Voice over IP (VoIP) a streamování videa přes mobilní sítě. Protokol přímo řeší problém nízké spektrální účinnosti pro provoz s malými pakety a citlivý na zpoždění. Snížením velikosti záhlaví ze 40-60 bajtů na pouhé 1-4 bajty může ROHC zdvojnásobit či ztrojnásobit efektivní kapacitu pro hlasová volání. Jeho odolnost vůči ztrátě paketů — klíčový konstrukční cíl — zajišťuje spolehlivou dekompresi i při zhoršení podmínek na rádiovém spoji a zabraňuje desynchronizaci kontextu, která by vedla k fatálnímu selhání. Jeho přijetí od Release 5 (HSDPA) až po 5G NR dokazuje jeho trvalou hodnotu při šetření rádiových zdrojů a snižování latence, což je klíčové pro kapacitu sítě a uživatelský zážitek.

## Klíčové vlastnosti

- Rámec pro kompresi záhlaví IP, UDP, RTP, ESP a TCP
- Pracuje s více kompresními stavy (IR, FO, SO) pro optimalizaci kompromisu mezi účinností a robustností
- Využívá kompresní kontexty synchronizované mezi kompresorem a dekompresorem
- Podporuje více režimů robustnosti (jednosměrný, obousměrný optimistický, obousměrný spolehlivý)
- Definuje specifické profily pro různé kombinace zásobníků protokolů
- Integrován do vrstvy PDCP v 3GPP pro provoz přes rozhraní Uu a rádiová rozhraní

## Související pojmy

- [PDCP – Packet Data Convergence Protocol](/mobilnisite/slovnik/pdcp/)
- [VOIP – Voice over IP](/mobilnisite/slovnik/voip/)
- [QoS – Quality of Service](/mobilnisite/slovnik/qos/)
- [E-UTRAN – Evolved Universal Terrestrial Radio Access Network](/mobilnisite/slovnik/e-utran/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.280** (Rel-20) — Common Architecture for Mission Critical Services
- **TS 23.479** (Rel-19) — MBMS API for Mission Critical Services
- **TS 23.792** (Rel-16) — MBMS API for Mission Critical Services
- **TS 24.301** (Rel-19) — NAS protocol for Evolved Packet System
- **TS 24.379** (Rel-19) — Mission Critical Push To Talk (MCPTT) call control
- **TS 24.380** (Rel-19) — MCPTT Media Plane Control Protocol
- **TS 25.323** (Rel-19) — Packet Data Convergence Protocol (PDCP) Specification
- **TS 25.331** (Rel-19) — UTRAN RRC Protocol Specification
- **TR 25.912** (Rel-19) — Evolved UTRA and UTRAN Technical Report
- **TR 25.993** (Rel-19) — UTRA RAB Examples and Radio Interface Mapping
- **TS 26.517** (Rel-19) — 5G MBS User Service Protocols and Formats
- **TR 26.935** (Rel-19) — Speech Codec Performance for Packet Switched Multimedia
- **TR 26.936** (Rel-19) — Audio Codec Characterization Technical Report
- **TR 26.937** (Rel-19) — 3GPP PSS Characterization
- … a dalších 14 specifikací

---

📖 **Anglický originál a plná specifikace:** [ROHC na 3GPP Explorer](https://3gpp-explorer.com/glossary/rohc/)
