---
slug: "xudt"
url: "/mobilnisite/slovnik/xudt/"
type: "slovnik"
title: "XUDT – SCCP Extended Unitdata"
date: 2025-01-01
abbr: "XUDT"
fullName: "SCCP Extended Unitdata"
category: "Protocol"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/xudt/"
summary: "XUDT je typ zprávy Signalizačního spojovacího řídicího subsystému (SCCP) používaný v jádrových sítích založených na SS7 pro přenos dat bez spojení s rozšířenými schopnostmi. Rozšiřuje základní zprávu"
---

XUDT je typ zprávy SCCP pro přenos signalizačních dat bez spojení, který rozšiřuje základní UDT o volitelné parametry pro segmentaci, zpětné sestavení a řízení čítače přeskoků, což umožňuje spolehlivý přenos větších datových jednotek.

## Popis

Zpráva [SCCP](/mobilnisite/slovnik/sccp/) Extended Unitdata (XUDT) je protokolová datová jednotka v rámci zásobníku signalizačního systému č. 7 ([SS7](/mobilnisite/slovnik/ss7/)), konkrétně pro Signalizační spojovací řídicí subsystém (SCCP) v bezspojové služební třídě 0 nebo 1. SCCP samotný leží nad Částí pro přenos zpráv ([MTP](/mobilnisite/slovnik/mtp/)) a poskytuje rozšířené adresování (překlad globálního titulu) a služby přenosu zpráv. Zpráva XUDT je navržena pro přenos uživatelských dat (uživatelské zprávy SCCP) bezspojovým způsobem, což znamená, že se předem nezakládá vyhrazené signalizační spojení. Jejím klíčovým architektonickým účelem je překonání omezení základní zprávy Unitdata ([UDT](/mobilnisite/slovnik/udt/)): UDT může přenášet pouze omezené množství uživatelských dat definované limity podkladového MTP. Zpráva XUDT zavádí dva klíčové volitelné parametry: Segmentaci a Zpětné sestavení. Když je uživatelská zpráva SCCP příliš velká pro jeden XUDT, zdrojový uzel SCCP ji může segmentovat do více XUDT zpráv, z nichž každá obsahuje segment původních dat a parametr segmentace udávající její pozici. Příjemní uzel SCCP tento parametr použije k opětovnému sestavení původní zprávy před jejím doručením vyšší vrstvě. Dalším důležitým parametrem je Čítač přeskoků, který se snižuje v každém mezilehlém uzlu SCCP fungujícím jako přenosový bod (např. při směrování pomocí Globálního titulu). Pokud čítač dosáhne nuly, je zpráva zahozena, čímž se zabrání nekonečnému smyčkování v síti. Struktura zprávy zahrnuje povinné parametry jako Třída protokolu, Zdrojový a Cílový lokální odkaz (pro bezspojovou službu nastaveny na nulu) a Adresa volané a volající strany spolu s parametrem Data obsahujícím vlastní uživatelskou náplň. XUDT je potvrzen na úrovni MTP, ale ne na úrovni SCCP pro bezspojovou službu, což z něj činí datagram typu 'odešli a zapomeň' s podporou segmentace.

## K čemu slouží

Zpráva XUDT byla vytvořena k řešení potřeby přenosu větších bloků signalizačních dat v bezspojové síti [SS7](/mobilnisite/slovnik/ss7/) bez nutnosti navazovat nákladné a stavové [SCCP](/mobilnisite/slovnik/sccp/) spojení. Základní zpráva [UDT](/mobilnisite/slovnik/udt/) byla dostačující pro krátké dotazy a odpovědi, ale stala se úzkým hrdlem pro aplikace vyžadující přenos větších objemů dat, jako jsou některé operace [MAP](/mobilnisite/slovnik/map/) (Mobile Application Part) nebo hromadné výměny dat. Primární problém, který XUDT řeší, je omezení velikosti. Díky umožnění segmentace a zpětného sestavení umožňuje SCCP transparentně zpracovávat uživatelské zprávy překračující maximální přenosovou jednotku podkladového MTP, aniž by to vyžadovalo správu fragmentace na aplikační vrstvě. Tím se zvyšuje flexibilita a účinnost signalizační sítě. Mechanismus čítače přeskoků řeší spolehlivost sítě tím, že poskytuje jednoduchý mechanismus prevence smyček pro zprávy směrované přes více uzlů SCCP pomocí Překladu globálního titulu, což je běžný scénář u mezinárodního roamingu nebo distribuovaných síťových architektur. Její zavedení podpořilo vývoj složitějších telekomunikačních služeb v jádrových sítích 2G (GSM) a 3G (UMTS), které spoléhaly na signalizaci SS7, a poskytlo robustní bezspojový přenosový mechanismus pro kritickou signalizaci nesouvisející s okruhy.

## Klíčové vlastnosti

- Podporuje bezspojový přenos uživatelských zpráv SCCP s možností segmentace.
- Obsahuje volitelný parametr Segmentace umožňující rozdělení velké zprávy do více paketů XUDT.
- Obsahuje volitelný parametr Čítač přeskoků pro prevenci smyček při směrování pomocí Globálního titulu.
- Nese povinné parametry Adresa volané a volající strany pro směrování SCCP.
- Používá Třídu protokolu k definování charakteristik zpracování (např. s řízením pořadí zpráv nebo bez něj).
- Umožňuje přenos uživatelských dat větších, než je maximální velikost podporovaná základní zprávou UDT.

## Související pojmy

- [SCCP – Signalling Connection Control Part](/mobilnisite/slovnik/sccp/)
- [UDT – SCCP Unitdata Message](/mobilnisite/slovnik/udt/)
- [SS7 – Signalling System Number 7](/mobilnisite/slovnik/ss7/)
- [MTP – Message Transfer Part](/mobilnisite/slovnik/mtp/)
- [MAP – Mobile Application Protocol](/mobilnisite/slovnik/map/)

## Definující specifikace

- **TS 29.204** (Rel-19) — SS7 Security Gateway Functional Description

---

📖 **Anglický originál a plná specifikace:** [XUDT na 3GPP Explorer](https://3gpp-explorer.com/glossary/xudt/)
