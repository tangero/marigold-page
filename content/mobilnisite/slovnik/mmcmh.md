---
slug: "mmcmh"
url: "/mobilnisite/slovnik/mmcmh/"
type: "slovnik"
title: "MMCMH – Multi-stream Multiparty Conferencing Media Handling"
date: 2025-01-01
abbr: "MMCMH"
fullName: "Multi-stream Multiparty Conferencing Media Handling"
category: "Services"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/mmcmh/"
summary: "Multi-stream Multiparty Conferencing Media Handling (MMCMH) je schopnost IMS Media Server definovaná pro 5G, která umožňuje pokročilé konferenční služby. Umožňuje Media Resource Function (MRF) zpracov"
---

MMCMH je schopnost IMS Media Server pro 5G, která umožňuje Media Resource Function zpracovávat více nezávislých mediálních proudů na účastníka pro rozsáhlé interaktivní konferenční hovory.

## Popis

Multi-stream Multiparty Conferencing Media Handling (MMCMH) je sofistikovaná funkce Media Resource Function ([MRF](/mobilnisite/slovnik/mrf/)) v rámci IP Multimedia Subsystem (IMS), speciálně navržená pro konferenční služby příští generace. V tradičním audio konferenčním můstku jsou všechny audio proudy účastníků smíchány do jednoho složeného proudu, který je pak odeslán zpět každému účastníkovi. MMCMH překračuje tento jednoduchý model mixování a distribuce. Místo toho umožňuje MRF přijímat, zpracovávat a přeposílat více samostatných mediálních proudů od každého konferenčního účastníka a pro něj. Toto zpracování na úrovni jednotlivých proudů je klíčové pro podporu pokročilých konferenčních funkcí, zejména těch zahrnujících video a prostorový zvuk, ve velkých skupinových hovorech.

Architektura zahrnuje Application Server ([AS](/mobilnisite/slovnik/as/)), který hostuje logiku konferenční služby a ovládá MRF pomocí protokolů pro řízení médií, jako je H.248 nebo framework Media Control [API](/mobilnisite/slovnik/api/). MRF implementující MMCMH funguje jako výkonný mediální procesor. Pro každého účastníka může udržovat samostatné příchozí a odchozí proudy pro různé typy médií. Například ve videokonferenci může přijímat jedinečný video proud od každého účastníka. MRF pak může provádět selektivní přeposílání, odesílání konkrétní sady video proudů (např. pouze aktivních mluvčích) každému účastníkovi na základě jeho obrazového rozložení nebo preferencí, namísto jediného smíchaného videa. Pro audio umožňuje vytváření scén s prostorovým zvukem, kde hlasy účastníků zdánlivě přicházejí z různých směrů ve virtuální místnosti, což výrazně zlepšuje srozumitelnost ve velkých hovorech.

Fungování MMCMH je definováno ve specifikacích 3GPP TS 23.333 (Procedury) a TS 29.333 (Media Control API). Servisní logika v AS určuje konferenční politiku (kdo může mluvit, jaké rozložení použít) a posílá pokyny MRF. MRF využívající svou schopnost MMCMH tyto pokyny provádí v mediální rovině. Může provádět transkódování mezi různými kodeky, vkládat tóny nebo oznámení, nahrávat konferenci a aplikovat analýzu médií v reálném čase. Toto oddělení servisního řízení (v AS) od komplexního zpracování médií (v MRF) umožňuje škálovatelné a flexibilní nasazení služeb. MRF může být optimalizován pro vysoce výkonnou manipulaci s médii, zatímco AS může být vyvíjeno nezávisle za účelem vytváření inovativních uživatelských zážitků.

Role MMCMH je klíčová pro umožnění konferenčních služeb éry 5G, které vyžadují vysokou kvalitu, nízkou latenci a bohatou interaktivitu. Podporuje případy užití jako masivní virtuální schůzky, interaktivní tele-vzdělávání a cloudové hraní her s živým komentářem. Díky zpracování proudů jednotlivě umožňuje síťové a klientské optimalizace; například účastník se špatným připojením může přijímat pouze audio proud a jeden video proud, zatímco jiný na připojení 5G přijímá všechny video proudy ve vysokém rozlišení. Tato detailní kontrola představuje významný vývoj oproti monolitickým konferenčním můstkům minulosti a je klíčovým prvkem pro schopnosti Media Processing ([MP](/mobilnisite/slovnik/mp/)) v rámci architektury 5G Media Streaming.

## K čemu slouží

MMCMH bylo vytvořeno, aby řešilo omezení tradičního konferenčního mixování, které se stává nedostatečným pro moderní, rozsáhlé a na média bohaté kolaborativní relace. Jednoduché audio mixování trpí degradací kvality, ztrátou identity mluvčího a neschopností podporovat funkce jako identifikace aktivního mluvčího nebo oddělené diskusní místnosti. Pro video je prosté skládání všech zdrojů do jedné mřížky na serveru neefektivní a nepružné, protože vnucuje stejné video rozložení všem klientům bez ohledu na možnosti jejich zařízení nebo preference uživatelů. Účelem MMCMH je poskytnout standardizovaný, výkonný framework pro zpracování médií v rámci IMS, který dokáže uspokojit požadavky pokročilých, interaktivních služeb pro více účastníků.

Historický kontext zahrnuje růst over-the-top ([OTT](/mobilnisite/slovnik/ott/)) konferenčních řešení, která nabízela kontrolu na úrovni jednotlivých proudů a inovativní funkce, čímž vytvořila uživatelská očekávání, která legacy telekomunikační konferenční služby nemohly splnit. 3GPP standardizovalo MMCMH, aby umožnilo síťovým operátorům a poskytovatelům služeb nabízet konkurenceschopné, provozně spolehlivé konference s vynikající spolehlivostí, zabezpečením a integrací s dalšími IMS službami (jako je tísňové volání). Řeší problém škálovatelnosti a kvality ve velkých konferencích tím, že umožňuje inteligentní, selektivní distribuci médií namísto hrubého mixování.

Dále MMCMH umožňuje nové obchodní modely a imerzivní zážitky. Je základní technologií pro sociální prostory rozšířené reality ([AR](/mobilnisite/slovnik/ar/))/virtuální reality ([VR](/mobilnisite/slovnik/vr/)) a aplikace metaverse, kde jsou prostorový zvuk a nezávislé video proudy nezbytné pro realističnost. Definováním těchto schopností ve standardech 5G zajišťuje 3GPP interoperabilitu mezi [MRF](/mobilnisite/slovnik/mrf/) od různých dodavatelů a poskytuje jasnou cestu vývojářům k vytváření služeb komunikace příští generace, které využívají vysokou přenosovou kapacitu a nízkou latenci sítí 5G. Jeho vytvoření bylo motivováno vizí učinit telekomunikační sítě přední platformou pro skupinovou komunikaci v reálném čase.

## Klíčové vlastnosti

- Umožňuje zpracování médií na úrovni jednotlivých proudů a účastníků v konferenci, což překračuje monolitické mixování
- Podporuje selektivní přeposílání audio a video proudů na základě aktivních mluvčích, uživatelských rolí nebo možností klienta
- Umožňuje vytváření scén s prostorovým zvukem pro imerzivní konferenční zážitky
- Umožňuje dynamické vkládání médií (tóny, nahrávky, oznámení) do individuálních proudů účastníků
- Poskytuje transkódování médií a adaptaci mezi různými kodeky a formáty pro heterogenní koncové body
- Zpřístupňuje řízení prostřednictvím standardizovaných API (např. Media Control API v TS 29.333) pro flexibilní vývoj služeb

## Související pojmy

- [MRF – Multimedia Resource Function](/mobilnisite/slovnik/mrf/)
- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)

## Definující specifikace

- **TS 23.333** (Rel-19) — MRFC-MRFP Mp Interface Requirements
- **TS 29.333** (Rel-19) — MRFC-MRFP Mp Interface Protocol

---

📖 **Anglický originál a plná specifikace:** [MMCMH na 3GPP Explorer](https://3gpp-explorer.com/glossary/mmcmh/)
