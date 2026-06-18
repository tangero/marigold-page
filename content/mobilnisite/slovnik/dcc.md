---
slug: "dcc"
url: "/mobilnisite/slovnik/dcc/"
type: "slovnik"
title: "DCC – Diameter Credit Control"
date: 2025-01-01
abbr: "DCC"
fullName: "Diameter Credit Control"
category: "Protocol"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/dcc/"
summary: "DCC je protokol založený na Diameteru, definovaný v 3GPP pro řízení kreditu v reálném čase a online účtování v paketových sítích. Umožňuje síťovým operátorům spravovat útratu účastníka, vynucovat kvót"
---

DCC je protokol založený na Diameteru, definovaný v rámci 3GPP, pro řízení kreditu v reálném čase a online účtování. Umožňuje operátorům spravovat útratu účastníka, vynucovat kvóty a podporovat předplacené účtování během relací služeb.

## Popis

Diameter Credit Control (DCC) je protokol specifikovaný v 3GPP TS 29.212, který definuje aplikační zprávy a procedury Diameter pro online řízení kreditu. Funguje v rámci architektury Online Charging System ([OCS](/mobilnisite/slovnik/ocs/)), kde zprostředkovává interakci v reálném čase mezi síťovými funkcemi (jako je [P-GW](/mobilnisite/slovnik/p-gw/) nebo [SMF](/mobilnisite/slovnik/smf/)) a OCS za účelem autorizace využití služby na základě dostupného kreditu. Protokol je relací orientovaný, což znamená, že pro konkrétní datový tok služby nebo relaci účastníka vytváří relaci řízení kreditu. Podporuje více servisních kontextů, což umožňuje detailní účtování na úrovni služby (např. hlas, data, zprávy) nebo agregované účtování napříč službami.

V jádru DCC funguje prostřednictvím mechanismu žádost-odpověď využívajícího příkazy Diameter. Klíčovým příkazem je Credit-Control-Request ([CCR](/mobilnisite/slovnik/ccr/)), který odesílá síťová funkce (vystupující jako klient Diameter, např. Charging Trigger Function) směrem k OCS (vystupující jako server Diameter). CCR hlásí spotřebu (např. objem, dobu trvání, události) a žádá o autorizaci pro další spotřebu služby. OCS tento požadavek zpracuje vůči zůstatku na účtu účastníka a příslušným politikám a následně odpoví pomocí Credit-Control-Answer ([CCA](/mobilnisite/slovnik/cca/)). CCA obsahuje instrukce, jako je přidělení kvóty (např. 10 MB dat), zamítnutí služby z důvodu nedostatku financí nebo ukončení probíhající relace. Síťová funkce tyto kvóty vynucuje, monitoruje spotřebu a odesílá průběžné aktualizace prostřednictvím CCR, dokud relace neskončí nebo se nevyčerpá kredit.

Mezi klíčové komponenty v DCC patří Credit-Control-Client (např. P-GW, SMF), který spouští účtovací události, a Credit-Control-Server (součást OCS), který rozhoduje o kreditu. Protokol definuje několik stavů relace: INITIAL, UPDATE a TERMINATION, odpovídající začátku, průběhu a konci relace řízení kreditu. Podporuje také funkce jako správa kvót, kdy OCS může přidělovat kvóty s konkrétní dobou platnosti nebo prahovými hodnotami, a spouštěče přeautorizace, kdy klient musí požádat o novou kvótu před vypršením platnosti stávající. DCC navíc elegantně zvládá selhání, s definovanými záložními mechanismy (jako pokračování služby nebo její ukončení) pro scénáře, kdy je komunikace s OCS ztracena.

Role DCC je nedílnou součástí účtovací architektury 3GPP, zejména pro online účtování (OCS). Umožňuje účtování v reálném čase na základě událostí pro služby jako prohlížení dat, IMS relace nebo [SMS](/mobilnisite/slovnik/sms/), což zajišťuje těsné propojení účtování s poskytováním služby. Protokol je rozšiřitelný, podporuje vendor-specific AVPs (Attribute-Value Pairs) pro vlastní účtovací scénáře. Jeho použití Diameteru zajišťuje spolehlivý a bezpečný transport přes TCP nebo [SCTP](/mobilnisite/slovnik/sctp/) s vestavěnou podporou pro převzetí služeb při selhání a vyvažování zátěže. V moderních sítích se DCC vyvinulo tak, aby podporovalo konvergované účtování v 5G, kde komunikuje s [CHF](/mobilnisite/slovnik/chf/) (Charging Function), a zachovává přitom své základní principy a zároveň se přizpůsobuje novým servisním modelům, jako je síťové dělení (network slicing) a edge computing.

## K čemu slouží

DCC bylo vytvořeno, aby uspokojilo potřebu řízení kreditu v reálném čase v paketových mobilních sítích, zejména když operátoři přecházeli od tradičních okruhově přepínaných hlasových služeb k datově orientovaným službám. Před jeho zavedením se účtování často opíralo o offline mechanismy (jako CDR) nebo jednoduché předplacené systémy, kterým chyběla podrobnost a interakce v reálném čase. To vedlo k problémům, jako je únik výnosů, kdy účastníci mohli nadměrně využívat služby bez okamžité kontroly platby, a omezená podpora komplexních fakturačních modelů, jako je účtování na základě relace nebo události. DCC tyto problémy vyřešilo poskytnutím standardizovaného rozhraní na bázi protokolu pro dynamickou autorizaci kreditu během aktivních relací.

Motivace pramenila z růstu služeb GPRS a později datových služeb 3G/4G, které vyžadovaly flexibilnější účtování než modely s paušálem. Operátoři potřebovali implementovat předplacené datové tarify, účtování podle úrovně QoS a limity útraty, aniž by narušili uživatelský zážitek. DCC to umožnilo tím, že síťové prvky mohly v reálném čase dotazovat centrální účtovací systém a přidělovat kvóty šité na míru typu služby, úrovni účastníka nebo síťovým podmínkám. To podpořilo nové obchodní modely, jako jsou tlačítka pro turbo rychlost nebo časové datové pasy, a zároveň předcházelo nečekaně vysokým účtům a podvodům.

Historicky DCC navázalo na základní protokol Diameter (RFC 6733), který se sám vyvinul z RADIUS a nabízí lepší škálovatelnost, zabezpečení a spolehlivost. Standardizací DCC v 3GPP Release 11 byla zajištěna interoperabilita napříč zařízeními různých dodavatelů a soulad se širšími účtovacími architekturami, jako je 3GPP Charging Architecture (TS 32.240). Odstranilo omezení dřívějších přístupů tím, že poskytlo stavový, na relaci citlivý protokol, který dokáže obsluhovat více souběžných služeb a integrovat se s řízením politik (prostřednictvím PCRF/PCF), což umožňuje jednotné vynucování účtování a politik. Tento základ umožnil DCC zůstat relevantní i v éře 5G, kde podporuje pokročilé účtování pro síťové řezy (network slices) a edge služby.

## Klíčové vlastnosti

- Autorizace kreditu v reálném čase prostřednictvím zpráv Diameter CCR/CCA
- Podpora více servisních kontextů a detailního účtování na úrovni datového toku
- Správa kvót s časovači platnosti a spouštěči přeautorizace
- Zpracování stavů relace (INITIAL, UPDATE, TERMINATION) pro správu životního cyklu
- Mechanismy pro zálohování a zvládání selhání při ztrátě komunikace s OCS
- Integrace s Online Charging System (OCS) pro předplacené a hybridní účtování

## Definující specifikace

- **TS 29.212** (Rel-19) — Gx/Gxx/Sd/St Diameter Protocol

---

📖 **Anglický originál a plná specifikace:** [DCC na 3GPP Explorer](https://3gpp-explorer.com/glossary/dcc/)
