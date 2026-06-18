---
slug: "rra"
url: "/mobilnisite/slovnik/rra/"
type: "slovnik"
title: "RRA – RAN Registration Area"
date: 2025-01-01
abbr: "RRA"
fullName: "RAN Registration Area"
category: "Mobility"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/rra/"
summary: "RAN Registration Area (RRA) je logická oblast v rádiové přístupové síti používaná pro sledování a paging uživatelského zařízení (UE) v připojeném nebo neaktivním stavu. Umožňuje efektivní správu mobil"
---

RRA je logická oblast v rádiové přístupové síti (RAN) používaná pro sledování a paging uživatelského zařízení (UE) v připojeném nebo neaktivním stavu, aby bylo možné efektivně spravovat mobilitu.

## Popis

RAN Registration Area (RRA) je koncept správy mobility definovaný v rámci specifikací 3GPP pro LTE a 5G New Radio (NR). Představuje skupinu buněk, řízenou jednou nebo více základnovými stanicemi ([eNB](/mobilnisite/slovnik/enb/) v LTE, gNB v NR), v rámci které se může uživatelské zařízení (UE) pohybovat bez provedení plné aktualizace oblasti sledování (Tracking Area Update - [TAU](/mobilnisite/slovnik/tau/)) s jádrem sítě. Když je UE ve stavu [RRC](/mobilnisite/slovnik/rrc/)_CONNECTED nebo RRC_INACTIVE, může mu RAN (konkrétně obsluhující základnová stanice) přiřadit RRA. UE je pak povinno upozornit RAN (prostřednictvím aktualizace oblasti oznámení založené na RAN) pouze tehdy, když se pohybuje mimo hranice této RRA, namísto hlášení každé změny buňky.

Architektonicky je RRA spravována uzlem RAN. Definice a konfigurace RRA jsou implementačně specifické, ale obvykle jsou přizpůsobeny základní topologii sítě pro optimalizaci signalizace. Základnová stanice nakonfiguruje sadu RRA a když UE přejde do připojeného nebo neaktivního stavu, může mu být poskytnut identifikátor RRA a seznam buněk patřících do této oblasti. Tyto informace jsou uloženy v kontextu UE v RAN. Mechanismus RRA funguje ve spojení s konceptem oblasti sledování (Tracking Area - [TA](/mobilnisite/slovnik/ta/)) jádra sítě. Zatímco TA je spravována funkcí pro správu přístupu a mobility ([AMF](/mobilnisite/slovnik/amf/)) pro paging na úrovni jádra, RRA poskytuje jemněji granulovanou oblast řízenou RAN pro častější aktualizace polohy bez zapojení jádra sítě.

Jeho role je klíčová pro snížení signalizace a úsporu energie, zejména pro hromadnou komunikaci typu stroj-stroj (mMTC) a občasné přenosy malých objemů dat. Pro UE ve stavu RRC_INACTIVE – stavu zavedeném ke snížení latence a signalizace – umožňuje RRA uchovat si kontext UE a rychle jej vyvolat (paging) ve známé oblasti bez zapojení jádra sítě pro každou událost mobility. Tím se snižuje signalizační zatížení jak na rozhraní [N2](/mobilnisite/slovnik/n2/) (mezi RAN a jádrem), tak baterie UE, protože UE provádí méně úplných registračních procedur. Uzel RAN odpovědný za RRA může provést paging UE napříč všemi buňkami v rámci RRA, když dorazí downlink data.

## K čemu slouží

RAN Registration Area byla vytvořena, aby řešila zahlcení signalizací a neefektivitu spojenou s častými aktualizacemi jádra sítě pro vysoce mobilní nebo přerušovaně aktivní zařízení. V tradiční správě mobility by UE v připojeném režimu spouštělo předání spojení (handover) s každou změnou buňky a UE v režimu nečinnosti (idle) by provádělo aktualizaci oblasti sledování ([TAU](/mobilnisite/slovnik/tau/)) při opuštění registrované [TA](/mobilnisite/slovnik/ta/). Pro zařízení internetu věcí (IoT) nebo smartphony s neustále aktivními aplikacemi to generuje značný signalizační provoz, který spotřebovává síťové zdroje a životnost baterie zařízení.

RRA to řeší decentralizací části funkce správy mobility do RAN. Zavádí hierarchické schéma správy polohy: jádro sítě sleduje UE na úrovni granularity seznamu oblastí sledování (který může být velký), zatímco RAN sleduje UE na jemnější úrovni granularity RRA. Toto oddělení odpovědností umožňuje optimalizovat signalizaci na základě stavu a vzoru aktivity UE. Primární motivací byla podpora stavu RRC_INACTIVE v LTE a NR, který je navržen jako střední stav mezi CONNECTED a IDLE, aby umožnil rychlou reaktivaci pro sporadické přenosy dat bez plné režie nastavení spojení.

Historicky se tento koncept vyvinul z dřívějších konceptů oblastí založených na RAN a byl formálně standardizován, aby umožnil efektivnější podporu hromadného IoT a služeb s nízkou latencí. Řeší omezení přístupu centrického na jádro, kde každá událost mobility vyžadovala signalizaci jádra sítě, což se dobře neškáluje pro obrovský počet zařízení předpokládaných pro 5G. Tím, že udržuje správu mobility, kde je to možné, lokální v RAN, RRA snižuje latenci pro přechody mezi stavy a minimalizuje zatížení řídicí roviny jádra sítě.

## Klíčové vlastnosti

- Logická oblast řízená RAN, zahrnující sadu buněk
- Používá se pro sledování polohy UE ve stavech RRC_CONNECTED a RRC_INACTIVE
- Snižuje signalizaci ve srovnání se sledováním na úrovni buňky nebo aktualizacemi oblasti sledování (TAU) jádra sítě
- Umožňuje efektivní paging založený na RAN pro UE ve stavu RRC_INACTIVE
- Konfigurace je implementačně specifická a spravovaná uzlem RAN
- Funguje ve spojení s oblastmi sledování (Tracking Areas) jádra sítě pro hierarchickou správu mobility

## Definující specifikace

- **TS 43.130** (Rel-19) — Iur-g Interface Overview

---

📖 **Anglický originál a plná specifikace:** [RRA na 3GPP Explorer](https://3gpp-explorer.com/glossary/rra/)
