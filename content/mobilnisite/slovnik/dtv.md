---
slug: "dtv"
url: "/mobilnisite/slovnik/dtv/"
type: "slovnik"
title: "DTV – Digital TeleVision"
date: 2025-01-01
abbr: "DTV"
fullName: "Digital TeleVision"
category: "Services"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/dtv/"
summary: "DTV označuje poskytování služeb digitální televize přes sítě 3GPP, primárně prostřednictvím služby Multimedia Broadcast Multicast Service (MBMS) a její evolvované verze (eMBMS). Umožňuje efektivní vys"
---

DTV je poskytování služeb digitální televize přes sítě 3GPP, které primárně využívá službu Multimedia Broadcast Multicast Service (MBMS) k efektivnímu vysílání videoobsahu do mobilních zařízení.

## Popis

Digital TeleVision (DTV) v rámci standardů 3GPP definuje rámec pro vysílání digitálního televizního obsahu přes mobilní sítě za použití vysílacích/multicastových technologií. Hlavním nástrojem je služba Multimedia Broadcast Multicast Service ([MBMS](/mobilnisite/slovnik/mbms/)), zavedená ve verzi 3GPP Release 6 a dále vyvinutá do podoby evolved MBMS (eMBMS) v LTE a 5G NR. DTV využívá tyto schémata přenosu typu point-to-multipoint k efektivní distribuci lineárních [TV](/mobilnisite/slovnik/tv/) proudů, videa na vyžádání a souvisejících metadat k velkému počtu účastníků současně, čímž optimalizuje síťové zdroje ve srovnání s přenosem unicast.

Architektura zahrnuje několik klíčových síťových funkcí. Broadcast Multicast Service Center ([BM-SC](/mobilnisite/slovnik/bm-sc/)) slouží jako vstupní bod pro poskytovatele obsahu a zajišťuje oznamování služeb, zabezpečení a plánování. V páteřní síti MBMS Gateway ([MBMS-GW](/mobilnisite/slovnik/mbms-gw/)) spravuje IP multicast distribuci a řízení relací. V rádiové přístupové síti (RAN) eNodeB (pro LTE) nebo gNB (pro 5G NR) vysílá vysílací data přes vyhrazený multicastový přenosový kanál ([MTCH](/mobilnisite/slovnik/mtch/)) v rámci oblasti Multicast-Broadcast Single Frequency Network ([MBSFN](/mobilnisite/slovnik/mbsfn/)), kde více buněk synchronně vysílá stejný signál za účelem zlepšení pokrytí a spektrální účinnosti.

Služby DTV jsou specifikovány v řadě technických specifikací (TS), pokrývajících aspekty od požadavků na službu (TS 26.953) po detaily rádiového přenosu (TS 36.755 pro LTE, TS 38.860/38.892 pro NR). Tyto specifikace definují kodeky (jako [HEVC](/mobilnisite/slovnik/hevc/)), transportní protokoly (např. [RTP](/mobilnisite/slovnik/rtp/)/FLUTE) a formáty elektronického průvodce službami (ESG). Integrace s procedurami páteřní sítě zajišťuje, že účastníci mohou bezproblémově objevovat, připojovat se k vysílacím relacím a přijímat je, s podporou kvality služby (QoS) a kontinuity služby. DTV tedy představuje kompletní, standardizovaný ekosystém pro mobilní vysílací televizi, který je nedílnou součástí služeb jako LTE-based Broadcast (LTE-B) a 5G Multicast-Broadcast Services.

## K čemu slouží

DTV bylo vytvořeno za účelem umožnění efektivního a kvalitního poskytování televizních služeb do mobilních zařízení přes mobilní sítě, čímž řeší neefektivitu používání unicastových spojení pro populární živý obsah. Před zavedením MBMS by vysílání oblíbených událostí mnoha uživatelům zatěžovalo kapacitu sítě duplicitními datovými toky. DTV tento problém řeší zavedením nativních vysílacích/multicastových schopností do systémů 3GPP.

Historicky se služby mobilní televize spoléhaly na samostatné vysílací sítě (jako DVB-H) nebo neefektivní unicast, což vedlo k roztříštěným uživatelským zkušenostem a vysokým nákladům na infrastrukturu. 3GPP standardizovalo DTV, aby využilo stávající mobilní infrastruktury pro vysílání, což umožnilo operátorům nabízet konkurenceschopné mobilní televizní a video služby. Služba také podporuje varování obyvatelstva a komunikace pro zásadní služby, kde je životně důležité současné šíření informací. Vývoj napříč jednotlivými verzemi se zaměřoval na zlepšování kvality videa, spektrální účinnosti a integrace s IP médii, aby byla uspokojena rostoucí spotřebitelská poptávka po mobilním videu.

## Klíčové vlastnosti

- Využívá MBMS/eMBMS pro efektivní přenos typu point-to-multipoint
- Podporuje video kodeky pro vysoké a ultra-vysoké rozlišení, jako je HEVC
- Umožňuje využití Multicast-Broadcast Single Frequency Network (MBSFN) pro lepší pokrytí a spektrální účinnost
- Obsahuje Electronic Service Guide (ESG) pro objevování služeb a metadata
- Poskytuje integraci s IP Multimedia Subsystem (IMS) pro řízení služeb
- Podporuje kontinuitu služby a mobilitu pro pohybující se přijímače

## Související pojmy

- [MBMS – Multimedia Broadcast Multicast Service](/mobilnisite/slovnik/mbms/)
- [MBSFN – Multimedia Broadcast multicast service Single Frequency Network](/mobilnisite/slovnik/mbsfn/)

## Definující specifikace

- **TR 26.953** (Rel-19) — Study on Service Interactivity for Streaming & Download
- **TS 36.755** (Rel-15) — US 600 MHz LTE Band 71 Technical Report
- **TR 38.860** (Rel-17) — NR; Study on Extended 600 MHz NR band
- **TR 38.892** (Rel-18) — Technical Report

---

📖 **Anglický originál a plná specifikace:** [DTV na 3GPP Explorer](https://3gpp-explorer.com/glossary/dtv/)
