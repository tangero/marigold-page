---
slug: "uto-uci"
url: "/mobilnisite/slovnik/uto-uci/"
type: "slovnik"
title: "UTO-UCI – Unused Transmission Occasion - Uplink Control Information"
date: 2025-01-01
abbr: "UTO-UCI"
fullName: "Unused Transmission Occasion - Uplink Control Information"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/uto-uci/"
summary: "Mechanismus v NR, který umožňuje UE přenášet řídicí informaci v uplinku (UCI) v předem přiděleném prostředku fyzického sdíleného kanálu v uplinku (PUSCH), který by jinak zůstal nevyužitý. Zlepšuje vyu"
---

UTO-UCI je mechanismus, při kterém UE přenáší řídicí informaci v uplinku v předem přiděleném prostředku PUSCH, který by jinak zůstal nevyužitý, čímž zlepšuje využití prostředků a snižuje latenci řídicí signalizace.

## Popis

Unused Transmission Occasion for Uplink Control Information (UTO-UCI) je funkce zavedená ve specifikaci 3GPP Release 18 pro 5G New Radio (NR). Řeší scénáře, kdy je UE naplánována pro přenos na fyzickém sdíleném kanálu v uplinku ([PUSCH](/mobilnisite/slovnik/pusch/)), ale z různých důvodů (např. nedostatek dat pro uplink) by přidělený prostředek zůstal nevyužit. Místo plýtvání tímto prostředkem mechanismus UTO-UCI umožňuje UE využít tuto 'nevyužitou přenosovou příležitost' k odeslání řídicí informace v uplinku ([UCI](/mobilnisite/slovnik/uci/)). UCI typicky zahrnuje kritickou zpětnou vazbu, jako jsou potvrzení Hybrid Automatic Repeat Request ([HARQ](/mobilnisite/slovnik/harq/) [ACK](/mobilnisite/slovnik/ack/)/[NACK](/mobilnisite/slovnik/nack/)), zprávy o stavu kanálu ([CSI](/mobilnisite/slovnik/csi/)) a žádosti o naplánování ([SR](/mobilnisite/slovnik/sr/)).

Provoz je řízen specifickými pravidly a konfiguracemi definovanými ve specifikacích fyzické vrstvy (38.212, 38.213) a specifikaci vrstvy [MAC](/mobilnisite/slovnik/mac/) (38.321). Síť může konfigurovat parametry UTO-UCI u UE, případně s uvedením, které typy UCI je povoleno přenášet v nevyužité příležitosti PUSCH. Když UE zjistí, že naplánovaná příležitost PUSCH nebude použita pro svůj primární účel přenosu dat, může v souladu s pravidly časování a multiplexování zakódovat a namapovat čekající UCI na fyzické prostředky tohoto PUSCH. To zahrnuje standardní řetězec zpracování UCI – včetně kanálového kódování, skramblování a modulace – ale namapovaný na rastr prostředků PUSCH místo na fyzický řídicí kanál v uplinku (PUCCH).

Z architektonického hlediska je UTO-UCI optimalizací napříč vrstvami zahrnující vrstvu MAC i fyzickou vrstvu. Vrstva MAC (specifikovaná v 38.321) zajišťuje logické rozhodování týkající se dostupnosti prostředků a prioritizace UCI, zatímco fyzická vrstva (specifikovaná v 38.212 a 38.213) spravuje přesné postupy kódování, multiplexování a přenosu. Tato funkce zvyšuje flexibilitu struktury rámce v uplinku. Jejím úkolem je zlepšit spektrální účinnost a snížit latenci řídicí signalizace, což je klíčové pro pokročilé případy užití NR vyžadující vysokou spolehlivost a nízkou latenci, jako je ultra-spolehlivá komunikace s nízkou latencí (URLLC). Díky příležitostnému využití již přidělených prostředků minimalizuje potřebu samostatných vyhrazených prostředků PUCCH pro řídicí signalizaci, což vede k efektivnějšímu celkovému řízení uplinkových prostředků.

## K čemu slouží

Hlavním účelem UTO-UCI je zlepšit využití uplinkových prostředků a snížit latenci řídicí signalizace v sítích 5G NR. Před jeho zavedením, pokud UE neměla žádná uplinková data k odeslání v naplánovaném prostředku PUSCH, tento prostředek zůstal prázdný, což představovalo plýtvání spektrální účinností. Zároveň, pokud měla UE čekající UCI k nahlášení (např. HARQ-ACK pro downlinkový přenos), obvykle musela čekat na další naplánovaný prostředek PUCCH nebo žádat o naplánování nového PUSCH, což zavedlo zpoždění.

UTO-UCI tuto neefektivitu řeší tím, že umožňuje UE 'přibalit' své UCI na jinak nevyužitý prostředek PUSCH. To je motivováno rostoucí poptávkou po komunikaci s nízkou latencí a vysokou účinností v 5G-Advanced (Release 18 a novější). Funkce jako rozšířené mobilní širokopásmové připojení (eMBB) s velmi dynamickým provozem a URLLC s přísnými požadavky na zpoždění těží z minimalizace času mezi událostí (např. přijetí downlinkového paketu) a odpovídající zpětnou vazbou (např. odeslání ACK). Využitím předem přidělených prostředků, které jsou již v přenosovém časovém plánu UE, poskytuje UTO-UCI mechanismus pro rychlejší řídicí zpětnou vazbu bez dodatečné režie plánování nebo soutěžení o prostředky.

Historicky existovaly podobné koncepty, jako je přibalování řídicí informace na datové kanály, ale UTO-UCI to formalizuje a optimalizuje speciálně pro dynamické plánování a flexibilní numerologii NR. Řeší omezení rigidního oddělení mezi datovými a řídicími kanály a umožňuje plynulejší a efektivnější využití rozhraní rádiového přístupu. To je součástí širšího úsilí 3GPP zavádět 'příležitostné' přenosy a zlepšovat účinnost uplinku pro pokročilá nasazení sítí.

## Klíčové vlastnosti

- Příležitostný přenos UCI na předem naplánovaných, ale nevyužitých prostředcích PUSCH
- Konfigurovatelné sítí prostřednictvím signalizace RRC pro povolené typy UCI
- Zahrnuje postupy napříč vrstvami mezi vrstvou MAC a fyzickou vrstvou
- Snižuje latenci pro hlášení HARQ-ACK, CSI a SR
- Zlepšuje spektrální účinnost uplinku minimalizací plýtvání prostředky
- Podléhá specifickým pravidlům multiplexování a časování definovaným ve specifikacích fyzické vrstvy

## Související pojmy

- [PUSCH – Physical Uplink Shared Channel](/mobilnisite/slovnik/pusch/)
- [PUCCH – Physical Uplink Control Channel](/mobilnisite/slovnik/pucch/)
- [UCI – Uplink Control Information](/mobilnisite/slovnik/uci/)
- [HARQ – Hybrid Automatic Repeat Request](/mobilnisite/slovnik/harq/)

## Definující specifikace

- **TS 38.212** (Rel-19) — NR Multiplexing and Channel Coding
- **TS 38.213** (Rel-19) — NR Physical Layer Control Procedures
- **TS 38.321** (Rel-19) — NR MAC Protocol Specification

---

📖 **Anglický originál a plná specifikace:** [UTO-UCI na 3GPP Explorer](https://3gpp-explorer.com/glossary/uto-uci/)
