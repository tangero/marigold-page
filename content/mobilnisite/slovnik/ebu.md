---
slug: "ebu"
url: "/mobilnisite/slovnik/ebu/"
type: "slovnik"
title: "EBU – European Broadcasting Union"
date: 2025-01-01
abbr: "EBU"
fullName: "European Broadcasting Union"
category: "Other"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/ebu/"
summary: "Evropská vysílací unie (EBU) je klíčové průmyslové sdružení pro média veřejné služby v Evropě. V 3GPP je na ni odkazováno jako na zainteresovanou stranu a zdroj specifikací pro služby související s vy"
---

EBU je Evropská vysílací unie (European Broadcasting Union), klíčové průmyslové sdružení, na které se 3GPP odkazuje jako na zainteresovanou stranu a zdroj specifikací pro služby související s vysíláním, aby byla zajištěna interoperabilita s mobilními sítěmi.

## Popis

Evropská vysílací unie (EBU) není technologie definovaná 3GPP, ale externí normalizační orgán, jehož specifikace jsou přijímány a na které se odkazuje v technických zprávách a specifikacích 3GPP, zejména pro doručování médií a přístupnostní služby. Systém 3GPP, především prostřednictvím služby Multimedia Broadcast Multicast Service ([MBMS](/mobilnisite/slovnik/mbms/)) a její vylepšené verze evolved Multimedia Broadcast Multicast Service (eMBMS), dokáže doručovat vysílací (broadcast) a skupinové (multicast) obsahy. Aby byly tyto služby kompatibilní s existujícími vysílacími ekosystémy, odkazuje 3GPP na specifikace EBU pro formáty médií, metadata a časovaný text (titulky). To umožňuje mobilním sítím poskytovat služby podobné televiznímu vysílání, včetně živého streamování se synchronizovanými titulky a audiopopisem, a tím splňovat regulační požadavky na přístupnost.

Integrace funguje tak, že se v rámci 3GPP (např. v TS 26.346 pro MBMS) definují přenosové formáty a protokoly, které dokážou zapouzdřit mediální komponenty definované EBU. Například vysílací proud eMBMS může nést video, audio a přidružené soubory titulků EBU-TT-D (Timed Text). Specifikace 3GPP podrobně popisují, jak jsou tyto komponenty signalizovány, synchronizovány a doručovány přes vysílací/skupinový přenosový kanál (bearer). Mediální přehrávač v UE pak musí být schopen tyto standardizované komponenty společně dekódovat a zobrazovat.

Role EBU v 3GPP je především zdrojem interoperabilních, v rámci průmyslu dohodnutých formátů pro doplňková média. Tím se předchází fragmentaci a umožňuje se výrobcům zařízení a poskytovatelům služeb implementovat jedinou, dobře otestovanou metodu pro zpracování vysílacích titulků. Odkazy se typicky nacházejí v pracovních skupinách Technické specifikační skupiny pro služby a systémové aspekty ([TSG](/mobilnisite/slovnik/tsg/) [SA](/mobilnisite/slovnik/sa/)) a Radiového přístupového sítě (TSG RAN) v 3GPP, kde se definují mediální kodeky a transport. Její zařazení zdůrazňuje závazek 3GPP vytvářet sítě, které mohou bezproblémově integrovat s jinými systémy distribuce médií.

## K čemu slouží

Účelem odkazování na EBU ve specifikacích 3GPP je využít ustavené, robustní standardy z profesionálního vysílacího průmyslu pro doručování médií přes mobilní sítě. Tím se řeší problém vytváření nových, nekompatibilních formátů pro služby, jako je živé televizní vysílání a video na požádání přes LTE a 5G. Přijetím standardů EBU zajišťuje 3GPP, že obsah připravený pro tradiční vysílání ([DVB](/mobilnisite/slovnik/dvb/) apod.) může být efektivně použit pro mobilní distribuci bez složité a ztrátové překódování (transkódování) nebo samostatných procesů tvorby.

Historicky používaly mobilní video služby proprietární nebo zjednodušené textové formáty, kterým chyběly pokročilé funkce (jako stylování, pozicování a přesné časování) vyžadované pro profesionální titulkování a přístupnost. Motivací pro integraci standardů EBU bylo vylepšení [MBMS](/mobilnisite/slovnik/mbms/) na eMBMS v LTE, což pozicionovalo buněčné sítě jako skutečné vysílací médium. Aby byly tyto mobilní vysílací služby konkurenceschopné vůči pozemní a satelitní [TV](/mobilnisite/slovnik/tv/), potřebovaly podporovat stejnou úroveň služeb, včetně přístupnostních funkcí vyžadovaných zákonem v mnoha regionech. Odkazování na specifikace EBU to vyřešilo tím, že poskytlo hotové, mezinárodně uznávané řešení.

Tento přístup řeší problém interoperability mezi vysílacím a telekomunikačním průmyslem. Umožňuje vysílatelům používat jejich stávající pracovní postupy a soubory pro přípravu obsahu i pro mobilní distribuci, čímž snižuje náklady a složitost. Pro uživatele zaručuje konzistentní, vysoce kvalitní zážitek z titulků a audiopopisu, ať už obsah sledují na TV set-top boxu nebo na mobilním zařízení přes síť 3GPP.

## Klíčové vlastnosti

- Externí standard, na který se odkazuje pro interoperabilitu vysílacích médií
- Poskytuje specifikace pro formáty časovaného textu (titulkování) a audiopopisu
- Umožňuje splnění regionálních regulačních požadavků na přístupnost video služeb
- Podporuje bezproblémové opětovné využití obsahu z vysílacích sítí do mobilních sítí
- Základ pro synchronizované doručování titulků v eMBMS/MBMS
- Zajišťuje profesionální úroveň stylování a časování textu na obrazovce

## Související pojmy

- [EBU-TT – European Broadcasting Union Timed Text](/mobilnisite/slovnik/ebu-tt/)
- [MBMS – Multimedia Broadcast Multicast Service](/mobilnisite/slovnik/mbms/)
- [DASH – Dynamic Adaptive Streaming over HTTP](/mobilnisite/slovnik/dash/)

## Definující specifikace

- **TR 26.936** (Rel-19) — Audio Codec Characterization Technical Report
- **TR 26.949** (Rel-19) — TV Service Profiles for 3GPP Networks
- **TR 26.955** (Rel-19) — Video Codec Analysis for 5G Services

---

📖 **Anglický originál a plná specifikace:** [EBU na 3GPP Explorer](https://3gpp-explorer.com/glossary/ebu/)
