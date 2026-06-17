---
slug: "8pam"
url: "/mobilnisite/slovnik/8pam/"
type: "slovnik"
title: "8PAM – 8 Pulse-Amplitude Modulation"
date: 2025-01-01
abbr: "8PAM"
fullName: "8 Pulse-Amplitude Modulation"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/8pam/"
summary: "8PAM je digitální modulační schéma, které kóduje tři bity na symbol pomocí osmi různých úrovní amplitudy. Bylo zavedeno ve specifikaci 3GPP Release 11 pro funkci High Speed Downlink Packet Access (HSD"
---

8PAM je digitální modulační schéma zavedené ve specifikaci 3GPP Release 11 pro HSDPA, které kóduje tři bity na symbol pomocí osmi různých úrovní amplitudy za účelem zvýšení špičkové přenosové rychlosti a spektrální účinnosti v downlinku.

## Popis

8 Pulse-Amplitude Modulation (8PAM) je lineární digitální modulační technika používaná v rámci fyzické vrstvy 3GPP UMTS/HSDPA. Funguje tak, že mapuje skupiny tří binárních bitů (tribit) na jednu z osmi diskrétních, rovnoměrně rozmístěných úrovní amplitudy nosné vlny. Toto mapování je typicky reprezentováno symboly jako ±1, ±3, ±5, ±7 při normalizaci. Primární aplikace 8PAM ve standardech 3GPP není jako samostatná modulace pro rádiovou nosnou, ale jako základní komponenta pro generování modulací vyššího řádu s kvadraturní amplitudovou modulací (QAM). Konkrétně v kontextu 3GPP TS 25.213 se 8PAM používá k vytvoření fázové (I) a kvadraturní (Q) složky pro 64QAM modulaci. Pro 64QAM, která přenáší šest bitů na symbol, je modulace dosažena nezávislou aplikací 8PAM na obou kanálech I a Q. Každý kanál nese tři bity (pomocí 8 úrovní amplitudy) a jejich ortogonální kombinace vede k 64 (8x8) možným stavům symbolu v komplexní rovině.

Technická implementace, jak je podrobně popsána ve specifikacích 3GPP 25.211 (fyzické kanály) a 25.213 (rozprostření a modulace), zahrnuje přesné mapování symbolů a tvarování pulsů. Binární datový tok je nejprve převeden na symboly. Pro režim 64QAM v HSDPA jsou datové bity pro High-Speed Physical Downlink Shared Channel (HS-PDSCH) namapovány na 8PAM konstelace pro větve I a Q. Tyto PAM signály jsou poté použity k modulaci kvadraturních nosných. Kritickým aspektem je použití kořenového kosinusového filtru (RRC) pro tvarování pulsů za účelem omezení šířky pásma vysílaného signálu a minimalizace mezisymbolového rušení (ISI) v kanálu.

V rámci síťové architektury je role 8PAM omezena na vysílač Node B (základnové stanice) a přijímač uživatelského zařízení (UE) pro specifické vysokorychlostní downlinkové kanály. Její činnost je klíčovým krokem zpracování na fyzické vrstvě, který probíhá po kanálovém kódování a prokládání, ale před rozprostřením pomocí ortogonálních kódů s proměnným rozprostřovacím faktorem (OVSF) a promícháním. Přijímač musí provést přesnou synchronizaci, odhad kanálu a ekvalizaci, aby správně rozlišil osm úrovní amplitudy v přítomnosti šumu a útlumu, což činí proces demodulace citlivějším ve srovnání s modulacemi nižšího řádu, jako je QPSK nebo 16QAM.

Výkon 8PAM, a následně 64QAM, je vysoce závislý na podmínkách kanálu. Nabízí 50% nárůst spektrální účinnosti oproti 16QAM (4 bity/symbol) a 200% nárůst oproti QPSK (2 bity/symbol). To však probíhá na úkor snížené odolnosti vůči šumu. Osm úrovní amplitudy je blíže u sebe, což činí konstelaci náchylnější k bitovým chybám způsobeným šumem a zkreslením. Její použití je proto typicky omezeno na scénáře s vysokým poměrem signálu k šumu (SNR), například když je UE blízko Node B. Pro úspěšné nasazení jsou nezbytné pokročilé přijímací techniky, jako jsou ekvalizéry s podporou modulací vyššího řádu a vylepšená zpětná vazba o kvalitě kanálu (Channel Quality Indicator - CQI).

## K čemu slouží

8PAM bylo zavedeno jako odpověď na rostoucí poptávku po vyšších špičkových přenosových rychlostech a lepší spektrální účinnosti v sítích 3G UMTS, zejména pro downlinkové datové služby. Před jeho zavedením v Release 11 podporovalo HSDPA modulační schémata až do 16QAM, která nabízela teoretickou špičkovou rychlost přibližně 14 Mbps (s konkrétním kódováním). Snaha průmyslu o mobilní broadbandové zážitky srovnatelné s pevnými linkami vytvořila potřebu efektivnějšího využití přiděleného rádiového spektra. 8PAM, jako stavební kámen pro 64QAM, byla technologickou odpovědí na tuto poptávku v rámci stávajícího rámečku nosné WCDMA.

Historický kontext představuje vývoj HSDPA prostřednictvím více releasů. Release 5 a 6 zavedly HSDPA s QPSK a 16QAM. Omezení 16QAM spočívalo v jeho stropu spektrální účinnosti. Pro dosažení vyšších přenosových rychlostí bez přidělení dalšího spektra (které je vzácné a drahé) byl nezbytný přechod k modulaci vyššího řádu. 64QAM, umožněná 8PAM na větvích I a Q, zvýšila počet bitů přenesených na symbol, čímž zvýšila špičkovou přenosovou rychlost na přibližně 21 Mbps za ideálních podmínek. Tato evoluce byla součástí strategie 3GPP prodloužit konkurenceschopnost technologie 3G vůči vznikajícím sítím 4G LTE.

Dále zavedení 8PAM/64QAM vyřešilo problém neefektivního využití spektra pro uživatele v excelentních rádiových podmínkách. Bez něj by byl uživatel blízko buňky s vysokým SNR stále omezen na 16QAM, což by plýtvalo potenciální kapacitou spoje. Implementací jemnější sady modulačních a kódovacích schémat (MCS) mohla síť lépe přizpůsobit kvalitě kanálu, používat robustní QPSK pro uživatele na okraji buňky a vysoce účinné 64QAM pro uživatele ve středu buňky, čímž optimalizovala celkovou propustnost buňky a uživatelský zážitek.

## Klíčové vlastnosti

- Kóduje tři bity na symbol pomocí osmi diskrétních úrovní amplitudy
- Základní komponenta pro generování 64QAM modulace na kanálech I a Q
- Zvyšuje špičkovou přenosovou rychlost v downlinku HSDPA na přibližně 21 Mbps
- Zlepšuje spektrální účinnost o 50 % oproti 16QAM
- Vyžaduje vysoký poměr signálu k šumu (SNR) pro spolehlivý provoz
- Specifikováno pro použití na kanálu HS-PDSCH v 3GPP UMTS

## Definující specifikace

- **TS 25.211** (Rel-19) — UTRA FDD Layer 1: Transport & Physical Channels
- **TS 25.213** (Rel-19) — UTRA FDD Spreading and Modulation

---

📖 **Anglický originál a plná specifikace:** [8PAM na 3GPP Explorer](https://3gpp-explorer.com/glossary/8pam/)
