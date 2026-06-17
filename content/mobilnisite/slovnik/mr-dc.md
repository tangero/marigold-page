---
slug: "mr-dc"
url: "/mobilnisite/slovnik/mr-dc/"
type: "slovnik"
title: "MR-DC – Multi-Radio Dual Connectivity"
date: 2026-01-01
abbr: "MR-DC"
fullName: "Multi-Radio Dual Connectivity"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/mr-dc/"
summary: "Multi-Radio Dual Connectivity (MR-DC) je funkce 3GPP, která umožňuje uživatelskému zařízení (UE) současné připojení ke dvěma různým základnovým stanicím využívajícím více technologií rádiového přístup"
---

MR-DC je funkce 3GPP umožňující uživatelskému zařízení (UE) současné připojení ke dvěma základnovým stanicím využívajícím různé rádiové technologie, jako LTE a 5G NR, za účelem zvýšení přenosových rychlostí a efektivity sítě.

## Popis

Multi-Radio Dual Connectivity (MR-DC) je pokročilá architektura rádiové přístupové sítě (RAN) definovaná standardem 3GPP, která umožňuje uživatelskému zařízení (UE) udržovat souběžná připojení ke dvěma různým základnovým stanicím, typicky zahrnující různé technologie rádiového přístupu (RAT), jako jsou LTE a New Radio (NR). Toho je dosaženo prostřednictvím hlavního uzlu ([MN](/mobilnisite/slovnik/mn/)) a sekundárního uzlu (SN), kde MN zajišťuje připojení řídicí roviny a SN přidává další prostředky uživatelské roviny. UE využívá více přijímačů a vysílačů pro komunikaci s oběma uzly a agreguje datové toky za účelem zvýšení propustnosti a spolehlivosti. Mezi klíčové varianty patří [EN-DC](/mobilnisite/slovnik/en-dc/) (E-UTRA-NR Dual Connectivity) s LTE jako hlavním a NR jako sekundárním, [NE-DC](/mobilnisite/slovnik/ne-dc/) (NR-E-UTRA Dual Connectivity) s NR jako hlavním a LTE jako sekundárním a [NR-DC](/mobilnisite/slovnik/nr-dc/) (NR-NR Dual Connectivity) v rámci 5G. Architektura zahrnuje možnosti rozdělených přenašečů (split bearer), kde datové rádiové přenašeče ([DRB](/mobilnisite/slovnik/drb/)) mohou být ukončeny v MN, SN nebo v obou, což umožňuje flexibilní směrování provozu a vyrovnávání zátěže.

Provozně MR-DC závisí na úzké koordinaci mezi MN a SN prostřednictvím standardizovaných rozhraní: rozhraní X2 pro uzly založené na LTE nebo rozhraní Xn pro uzly založené na NR. MN zpracovává signalizaci s jádrem sítě (např. přes rozhraní S1 nebo [NG](/mobilnisite/slovnik/ng/)) a spravuje kontext UE, zatímco SN přispívá dalšími rádiovými prostředky bez přímého připojení k jádru sítě. Postupy zahrnují přidání, modifikaci a uvolnění SN, řízené měřicími hlášeními od UE za účelem optimalizace výkonu. UE měří kvalitu signálu od obou uzlů, což umožňuje dynamické přidělování prostředků a události mobility, jako jsou předávání hovorů (handover). Toto uspořádání podporuje funkce jako agregace nosných napříč RAT, vylepšená mobilita prostřednictvím předávání hovorů typu make-before-break a zlepšené pokrytí využitím nižších kmitočtových pásem z jednoho RAT a vyšších kmitočtových pásem z druhého.

V síti hraje MR-DC klíčovou roli při usnadnění plynulých přechodů mezi 4G a 5G, což operátorům umožňuje postupně zavádět 5G při současném využití stávající infrastruktury LTE. Zlepšuje uživatelský zážitek poskytováním vyšších špičkových přenosových rychlostí, nižšího zpoždění pro rozdělené přenašeče a zvýšené spolehlivosti prostřednictvím diverzity cest. Pro síťové operátory MR-DC optimalizuje využití spektra a kapitálové výdaje tím, že umožňuje nesamostatná (NSA) nasazení 5G, kde je 5G NR ukotveno k jádru LTE. Tato technologie je zásadní pro dosažení výkonnostních cílů 5G, jako je vylepšené mobilní širokopásmové připojení (eMBB), a podporuje pokročilé případy užití, jako je ultra-spolehlivá komunikace s nízkým zpožděním (URLLC), využitím duální konektivity pro redundanci.

## K čemu slouží

MR-DC bylo vytvořeno, aby řešilo výzvy spojené s vývojem mobilních sítí ze 4G na 5G, a zajistilo zpětnou kompatibilitu a efektivní využití prostředků během přechodu. Před MR-DC existovala duální konektivita v rámci jedné RAT (např. LTE-LTE [DC](/mobilnisite/slovnik/dc/)), ale nemohla využít výhod kombinace různých RAT, jako jsou LTE a NR. Toto omezení bránilo schopnosti poskytovat vysoké přenosové rychlosti a nízké zpoždění slibované 5G bez plného samostatného nasazení. MR-DC to řeší tím, že umožňuje UE současně využívat LTE a NR rádiové rozhraní, maximalizuje dostupné spektrum a zlepšuje výkon sítě bez nutnosti okamžitých upgrade jádra sítě.

Historicky motivace pro MR-DC vycházela z potřeby průmyslu najít nákladově efektivní cestu k 5G, protože vybudování zcela nových 5G sítí od základů bylo příliš nákladné. Tím, že MR-DC umožňuje nesamostatné 5G architektury, dává operátorům možnost rychle zavést 5G služby využitím stávající infrastruktury LTE pro funkce řídicí roviny a NR pro zvýšenou kapacitu. Řeší problémy, jako jsou mezery v pokrytí v raných nasazeních 5G, kde vysokofrekvenční NR pásma mají omezený dosah, ukotvením připojení k rozšířenějším LTE sítím. Tento přístup také zvyšuje robustnost mobility, protože UE si může udržet připojení prostřednictvím LTE a zároveň přidat NR pro zvýšení propustnosti.

MR-DC navíc podporuje rostoucí poptávku po různorodých službách a síťovém řezání (network slicing) v 5G. Agregací prostředků napříč RAT poskytuje flexibilitu pro splnění různých požadavků na kvalitu služeb (QoS), od vysokorychlostního přenosu dat po spolehlivou komunikaci s nízkým zpožděním. Tato technologie podporuje inovace v koordinaci více RAT a připravuje cestu pro budoucí vylepšení, jako je integrovaný přístup a přenosová síť (IAB) a pokročilá agregace nosných. Její standardizace v 3GPP zajišťuje globální interoperabilitu, umožňuje bezproblémové uživatelské zážitky a usnadňuje koexistenci více generací sítí.

## Klíčové vlastnosti

- Současná konektivita ke dvěma základnovým stanicím s různými RAT (např. LTE a NR)
- Architektura s hlavním uzlem (MN) a sekundárním uzlem (SN) pro rozdělení řídicí a uživatelské roviny
- Podpora více variant: EN-DC, NE-DC, NR-DC
- Zvýšené přenosové rychlosti a spolehlivost prostřednictvím agregace prostředků
- Standardizovaná rozhraní (X2/Xn) pro koordinaci mezi uzly
- Umožňuje nesamostatná (NSA) nasazení 5G a plynulý vývoj sítě

## Související pojmy

- [EN-DC – E-UTRA NR Dual Connectivity with MCG using E-UTRA and SCG using NR](/mobilnisite/slovnik/en-dc/)

## Definující specifikace

- **TS 28.540** (Rel-20) — 5G Network Resource Model (NRM) Management
- **TS 32.425** (Rel-19) — E-UTRAN Performance Measurements
- **TS 33.501** (Rel-20) — 5G Security Architecture and Procedures
- **TS 36.331** (Rel-19) — LTE RRC Protocol Specification
- **TS 37.340** (Rel-19) — Multi-Connectivity Operation Overview
- **TS 38.133** (Rel-19) — 5G UE Radio Requirements for RRC_IDLE Mobility
- **TS 38.306** (Rel-19) — NR UE Radio Access Capability Parameters
- **TS 38.331** (Rel-19) — NR Radio Resource Control (RRC) Protocol Specification
- **TS 38.425** (Rel-19) — NR User Plane Protocol Specification
- **TS 38.508** (Rel-19) — 5G NR UE Radio Transmission & Reception
- **TS 38.521** (Rel-19) — NR Physical Layer UE Conformance Testing
- **TR 38.846** (Rel-18) — Technical Report

---

📖 **Anglický originál a plná specifikace:** [MR-DC na 3GPP Explorer](https://3gpp-explorer.com/glossary/mr-dc/)
