---
slug: "s1-u"
url: "/mobilnisite/slovnik/s1-u/"
type: "slovnik"
title: "S1-U – S1 User Plane Interface"
date: 2025-01-01
abbr: "S1-U"
fullName: "S1 User Plane Interface"
category: "Interface"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/s1-u/"
summary: "S1-U je uživatelská rovina rozhraní mezi eNodeB (základnovou stanicí) a Serving Gateway (SGW) v sítích LTE. Přenáší skutečné uživatelské datové pakety, jako je internetový provoz, za použití GTP-U tun"
---

S1-U je uživatelská rovina rozhraní mezi eNodeB a Serving Gateway v sítích LTE, která přenáší uživatelské datové pakety pomocí GTP-U tunelování.

## Popis

Rozhraní S1-U je klíčovou komponentou uživatelské roviny v rámci Evolved Packet System (EPS), definovanou 3GPP jako logické rozhraní spojující Evolved NodeB (eNodeB) v [E-UTRAN](/mobilnisite/slovnik/e-utran/) se Serving Gateway ([SGW](/mobilnisite/slovnik/sgw/)) v Evolved Packet Core (EPC). Funguje přes IP transportní síť a využívá [GPRS](/mobilnisite/slovnik/gprs/) Tunneling Protocol pro uživatelskou rovinu ([GTP-U](/mobilnisite/slovnik/gtp-u/)) k zapouzdření a tunelování uživatelských datových paketů mezi těmito uzly. GTP-U používá jako transportní protokol [UDP](/mobilnisite/slovnik/udp/), což poskytuje odlehčený a efektivní mechanismus pro přeposílání dat, který zahrnuje identifikátory koncových bodů tunelu ([TEID](/mobilnisite/slovnik/teid/)) pro rozlišení různých datových toků a UE. Rozhraní je navrženo pro přenos dat s vysokou propustností a nízkou latencí a podporuje dynamické vytváření, modifikaci a uvolňování tunelů při připojování, pohybu nebo změně přenosových kanálů (bearerů) UE.

V provozu S1-U zpracovává skutečný uživatelský datový provoz, jako je prohlížení webu, streamování videa nebo VoIP pakety, poté, co příslušná signalizace řídicí roviny (přes [S1-MME](/mobilnisite/slovnik/s1-mme/)) nastaví potřebné přenosové kanály. Když UE naváže datovou relaci, [MME](/mobilnisite/slovnik/mme/) koordinuje se SGW a eNodeB vytvoření Evolved Radio Access Bearer (E-RAB), který zahrnuje rádiový přenosový kanál přes rozhraní vzduchu a GTP-U tunel přes S1-U. Datové pakety z UE jsou eNodeB zapouzdřeny do GTP-U paketů s TEID odpovídajícím koncovému bodu tunelu SGW, a naopak pro downlinkový provoz. Rozhraní podporuje procedury správy cest, jako jsou Echo Request a Response, pro monitorování životaschopnosti tunelů, a dokáže zpracovávat indikace chyb pro řešení problémů. Při předávání spojení (handoveru) hraje S1-U klíčovou roli v přeposílání dat – například při předávání založeném na X2 může zdrojové eNodeB přeposílat právě přenášené pakety do cílového eNodeB prostřednictvím nepřímého tunelování přes SGW, aby se zabránilo ztrátě dat.

Z architektonického hlediska S1-U ztělesňuje princip oddělení řídicí a uživatelské roviny (CUPS), což umožňuje nezávislé škálování a optimalizaci funkcí přenosu dat. Na rozdíl od S1-MME v řídicí rovině, které používá spolehlivý SCTP, S1-U využívá pro rychlost a jednoduchost UDP a spoléhá se na protokoly vyšších vrstev (např. TCP v uživatelských datech) pro spolehlivost, když je to potřeba. Rozhraní je typicky point-to-point, přičemž každé eNodeB je připojeno k jednomu nebo více SGW pro vyrovnávání zátěže a redundanci, ačkoli nepodporuje sdružování (pooling) stejným způsobem jako S1-MME. Návrh S1-U klade důraz na efektivitu: GTP-U tunelování minimalizuje režii opětovným využitím IP infrastruktury, zatímco funkce jako komprese hlaviček (např. ROHC) mohou být aplikovány na eNodeB pro optimalizaci využití rádiových prostředků. Celkově je S1-U zásadní pro doručování dat v LTE, umožňuje bezproblémovou mobilitu, vynucování QoS prostřednictvím mapování přenosových kanálů a integraci s externími paketovými datovými sítěmi přes PGW.

## K čemu slouží

Rozhraní S1-U bylo zavedeno ve 3GPP Release 8 jako součást architektury LTE/EPC, aby řešilo omezení dřívějších systémů 3GPP, zejména UMTS, kde byla uživatelská rovina rozhraní složitější a méně efektivní. V UMTS cestovala uživatelská data přes rozhraní Iu-PS mezi RNC a SGSN, zahrnující více protokolových vrstev a RNC jako zprostředkovatele, což přidávalo latenci a snižovalo datovou propustnost. S1-U bylo vytvořeno za účelem zploštění sítě tím, že umožnilo přímé propojení uživatelské roviny mezi základnovou stanicí (eNodeB) a bránou (SGW), čímž odstranilo vrstvu RNC. Tento návrh snižuje počet skoků pro datové pakety, snižuje latenci a zvyšuje efektivitu šířky pásma, což je nezbytné pro podporu vysokorychlostních mobilních širokopásmových služeb a aplikací v reálném čase, jako jsou online hry a videokonference.

Historicky motivace pro S1-U vycházela z explozivního růstu využívání mobilního internetu a potřeby celo-IP síťové architektury, která by se mohla škálovat podle poptávky. Oddělením uživatelské roviny (S1-U) od řídicí roviny (S1-MME) umožnilo 3GPP operátorům nasazovat a škálovat funkce zpracování dat nezávisle – například geograficky distribuovat SGW pro snížení latence při centralizaci řídicích funkcí. Toto oddělení také usnadnilo přijetí GTP-U tunelování, osvědčené technologie z dřívějších sítí GPRS/UMTS, která poskytuje standardizovanou metodu pro zapouzdření uživatelských dat a podporu mobility bez nutnosti změn podkladové IP infrastruktury. Použití UDP a GTP-U v S1-U umožňuje rychlé přeposílání paketů a efektivní správu tunelů, což je klíčové pro zvládání nárazové povahy internetového provozu.

Dále S1-U řeší problémy související s bezproblémovou mobilitou a kontinuitou služeb. Prostřednictvím GTP-U tunelování umožňuje dynamické přesměrování datových paketů během předávání spojení, minimalizuje ztrátu paketů a zajišťuje plynulý uživatelský zážitek. To byl významný pokrok oproti předchozím systémům, kde události mobility mohly způsobovat znatelné přerušení. Rozhraní také podporuje diferenciaci QoS mapováním různých datových toků na specifické přenosové kanály s odpovídajícími charakteristikami tunelu, což operátorům umožňuje nabízet služby různých úrovní. Standardizací S1-U napříč releasy zajistilo 3GPP interoperabilitu se staršími systémy (např. prostřednictvím mezisystémového předávání spojení) a poskytlo základ pro budoucí vylepšení, jako jsou ta v LTE-Advanced a pro spolupráci s 5G. V konečném důsledku je účelem S1-U poskytnout vysoce výkonné, škálovatelné rozhraní uživatelské roviny, které tvoří základ datových schopností LTE, umožňuje efektivní přenos uživatelského provozu a zároveň podporuje pokročilé funkce mobility a QoS.

## Klíčové vlastnosti

- Používá GTP-U přes UDP pro efektivní tunelování uživatelských dat
- Podporuje identifikátory koncových bodů tunelu (TEID) pro diferenciaci toků
- Umožňuje dynamické vytváření, modifikaci a uvolňování tunelů
- Usnadňuje přeposílání dat během procedur předávání spojení (handoveru)
- Poskytuje správu cest prostřednictvím zpráv Echo Request/Response
- Integruje se s E-RAB pro správu přenosových kanálů (bearerů) end-to-end

## Související pojmy

- [S1-C – S1 Control Plane](/mobilnisite/slovnik/s1-c/)
- [S1-MME – S1 Control Plane Interface to the Mobility Management Entity](/mobilnisite/slovnik/s1-mme/)
- [SGW – Signalling Gateway](/mobilnisite/slovnik/sgw/)
- [GTP-U – GPRS Tunnelling Protocol for User Plane](/mobilnisite/slovnik/gtp-u/)
- [EPC – Evolved Packet Core Network](/mobilnisite/slovnik/epc/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TR 25.912** (Rel-19) — Evolved UTRA and UTRAN Technical Report
- **TS 29.274** (Rel-19) — GTPv2-C Control Plane Protocol Specification
- **TS 36.300** (Rel-19) — E-UTRAN Radio Interface Protocol Architecture Overview
- **TS 36.302** (Rel-19) — E-UTRA Physical Layer Services
- **TS 36.410** (Rel-19) — S1 Interface: General Aspects and Principles

---

📖 **Anglický originál a plná specifikace:** [S1-U na 3GPP Explorer](https://3gpp-explorer.com/glossary/s1-u/)
