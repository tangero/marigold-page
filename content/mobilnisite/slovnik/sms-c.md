---
slug: "sms-c"
url: "/mobilnisite/slovnik/sms-c/"
type: "slovnik"
title: "SMS-C – Short Message Service - Center"
date: 2010-01-01
abbr: "SMS-C"
fullName: "Short Message Service - Center"
category: "Core Network"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/sms-c/"
summary: "Centrální síťový uzel v architektuře služby SMS, zodpovědný za ukládání, přeposílání a směrování krátkých zpráv. Zajišťuje spolehlivé doručení správou front zpráv, interakcí s HLR pro zjištění polohy"
---

SMS-C je centrální síťový uzel zodpovědný za ukládání, přeposílání a směrování krátkých zpráv, který zajišťuje spolehlivé doručení správou front a interakcí s registry polohy účastníků.

## Popis

Short Message Service - Center (SMS-C), běžněji známý jako Short Message Service Centre ([SMSC](/mobilnisite/slovnik/smsc/)), je základní síťový prvek, který funguje jako centrální uzel pro veškerý [SMS](/mobilnisite/slovnik/sms/) provoz v mobilní síti. Je zodpovědný za mechanismus ulož-a-přepošli (store-and-forward), který definuje SMS a zajišťuje spolehlivé doručení zpráv i v případě, kdy je příjemce dočasně nedostupný. SMS-C přijímá zprávy od odesílajících zařízení nebo aplikací, dočasně je ukládá a následně je přeposílá zamýšleným příjemcům na základě směrovacích informací získaných od dalších síťových entit. Rozhraní má ke klíčovým komponentám, jako je [HLR](/mobilnisite/slovnik/hlr/) (Home Location Register) pro dotazování na stav a polohu účastníka, a k [MSC](/mobilnisite/slovnik/msc/) (Mobile Switching Centre), [SGSN](/mobilnisite/slovnik/sgsn/) (Serving [GPRS](/mobilnisite/slovnik/gprs/) Support Node) nebo [MME](/mobilnisite/slovnik/mme/) (Mobility Management Entity) pro doručení zpráv do rádiové přístupové sítě.

Architektonicky se SMS-C skládá z několika funkčních modulů: úložiště zpráv pro jejich zařazování do front, směrovacího enginu pro určení dalšího směrovacího kroku a signalizačních rozhraní pro komunikaci s jádrem sítě. Používá protokoly jako [MAP](/mobilnisite/slovnik/map/) (Mobile Application Part) přes SS7 v legacy sítích, nebo Diameter a SIP (Session Initiation Protocol) v IP sítích, jako je IMS. Při odeslání SMS (mobile-originated) SMS-C ověří odesílatele a příjemce, zkontroluje pravidla pro spam nebo filtrování a následně dotazuje HLR, aby získal aktuální obsluhující uzel příjemce (např. číslo MSC). Je-li příjemce dostupný, SMS-C přepošle zprávu do tohoto uzlu; pokud ne, zprávu uloží a periodicky opakuje pokusy o doručení na základě konfigurovatelných časovačů. SMS-C také generuje doručovací zprávy (delivery reports), aby informoval odesílatele o úspěchu či neúspěchu, a podporuje funkce jako doba platnosti zprávy, úrovně priority a náhradní zprávy.

Ve svém provozu hraje SMS-C klíčovou roli pro škálovatelnost a spolehlivost služby SMS. Zvládá vysoké objemy zpráv, často s vyvažováním zátěže mezi více instancemi. Pro SMS přes IP v pozdějších releasech 3GPP se SMS-C může integrovat s IP-SM-GW (IP Short Message Gateway) pro rozhraní k IMS sítím, což umožňuje doručování SMS přes LTE a 5G. SMS-C také podporuje nadstandardní služby, jako jsou krátká čísla pro prémiové zprávy, gateway funkce pro výměnu SMS mezi operátory a API pro aplikace (A2P messaging). Jeho návrh zajišťuje nízkou latenci a vysokou dostupnost, což jej činí nepostradatelným jak pro komunikaci mezi lidmi, tak pro kritické aplikace typu stroj-stroj (M2M), jako jsou ověřovací kódy a výstražná upozornění.

## K čemu slouží

SMS-C byl vytvořen k umožnění funkce ulož-a-přepošli (store-and-forward), která činí SMS spolehlivou a všudypřítomnou. V raných mobilních sítích bylo přímé zasílání zpráv mezi zařízeními nepraktické kvůli omezením, jako je nedostupnost příjemce a mezery v síťovém pokrytí. SMS-C tento problém řeší oddělením procesu odeslání a doručení zprávy, přičemž zprávy ukládá, dokud není příjemce dosažitelný. To zajišťuje, že SMS funguje i když jsou telefony vypnuté nebo mimo dosah sítě, což je klíčová výhoda oproti metodám komunikace v reálném čase.

Historicky, jak SMS získávala na popularitě v 90. letech, se SMS-C stal nezbytným pro správu rostoucího provozu zpráv a zajištění interoperability mezi různými operátory a síťovými technologiemi. Řešil potřebu centralizovaného bodu pro zpracování směrování, účtování a servisní logiky. S vývojem směrem k 3G, 4G a 5G se SMS-C přizpůsobil, aby podporoval IP transport a integraci s IMS, a zajistil tak kontinuitu služby SMS při migraci sítí od legacy okruhově přepínaných infrastruktur. Jeho role se rozšířila o podporu pokročilých funkcí zasílání zpráv a regulatorních požadavků, jako je kontrola spamu nebo nouzová upozornění, čímž udržuje SMS jako základní službu v telekomunikačním ekosystému.

## Klíčové vlastnosti

- Mechanismus ulož-a-přepošli (store-and-forward) pro spolehlivé doručení zpráv
- Integrace s HLR pro dotazy na polohu a stav účastníka
- Podpora signalizačních protokolů MAP, Diameter a SIP
- Fronty zpráv s konfigurovatelnými časovači opakování a dobami platnosti
- Generování doručovacích zpráv (delivery reports) a sledování stavu
- Rozhraní s IP-SM-GW pro SMS přes IP v IMS sítích

## Související pojmy

- [SMS – Short Message Service](/mobilnisite/slovnik/sms/)
- [HLR – Home Location Register](/mobilnisite/slovnik/hlr/)
- [MAP – Mobile Application Protocol](/mobilnisite/slovnik/map/)
- [IP-SM-GW – IP Short Message Gateway](/mobilnisite/slovnik/ip-sm-gw/)
- [SMS-GMSC – Short Message Service Gateway MSC](/mobilnisite/slovnik/sms-gmsc/)

## Definující specifikace

- **TS 23.198** (Rel-9) — Open Service Access (OSA); Stage 2
- **TS 29.199** (Rel-9) — Multimedia Messaging Web Services

---

📖 **Anglický originál a plná specifikace:** [SMS-C na 3GPP Explorer](https://3gpp-explorer.com/glossary/sms-c/)
