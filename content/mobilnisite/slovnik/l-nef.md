---
slug: "l-nef"
url: "/mobilnisite/slovnik/l-nef/"
type: "slovnik"
title: "L-NEF – Local Network Exposure Function"
date: 2025-01-01
abbr: "L-NEF"
fullName: "Local Network Exposure Function"
category: "Core Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/l-nef/"
summary: "Lokalizovaná instance funkce pro zpřístupnění sítě (NEF) nasazená na okraji sítě. Poskytuje zabezpečené rozhraní založené na API, přes které mohou autorizované aplikace třetích stran s nízkou latencí"
---

L-NEF je lokalizovaná instance funkce pro zpřístupnění sítě (Network Exposure Function) nasazená na okraji sítě, která poskytuje aplikacím třetích stran nízkolatenční a zabezpečený přístup k síťovým schopnostem a informacím prostřednictvím API.

## Popis

Lokální funkce pro zpřístupnění sítě (L-NEF) je funkční prvek v architektuře založené na službách ([SBA](/mobilnisite/slovnik/sba/)) 5G jádra sítě, speciálně navržený pro nasazení na okraji sítě, blízko rádiové přístupové sítě a uživatelských rovinových funkcí ([UPF](/mobilnisite/slovnik/upf/)). Jedná se o lokalizovanou variantu centralizované funkce pro zpřístupnění sítě ([NEF](/mobilnisite/slovnik/nef/)). Z architektonického hlediska L-NEF implementuje podmnožinu schopností NEF, ale je optimalizována pro nízkolatenční interakce s aplikacemi na okraji sítě a místními síťovými funkcemi. Typicky komunikuje s lokálními instancemi dalších funkcí jádra sítě, jako je lokální funkce řízení politik (L-PCF) a lokální funkce správy relací (L-SMF), stejně jako s místní UPF.

Jak funguje: Poskytuje rozhraní [API](/mobilnisite/slovnik/api/) (Application Programming Interface) směrem k aplikacím na okraji sítě. Aplikace běžící na platformě edge computingu může volat API L-NEF a žádat o síťové služby, například aktivovat zvýšení QoS pro konkrétní datový tok, získat nízkolatenční informace o poloze UE nebo se přihlásit k odběru notifikací o síťových událostech (např. změně stavu připojení UE). L-NEF tyto požadavky na API autentizuje a autorizuje, převádí je na interní rozhraní založená na službách dle 3GPP (např. Npcf, Nudm, Nsmf) a komunikuje s příslušnými lokálními nebo centrálními síťovými funkcemi, aby požadavek vyřídila. Klíčovým aspektem je její schopnost zpracovávat požadavky lokálně, bez nutnosti vždy komunikovat s centrální NEF, čímž se snižuje latence – což je kritický požadavek pro aplikace na okraji sítě pracující v reálném čase, jako jsou autonomní vozidla nebo průmyslová automatizace.

Mezi klíčové komponenty patří vrstva pro zpřístupnění API (podporující RESTful API dle specifikací 3GPP), engine pro zabezpečení a vynucování politik, který aplikuje řízení přístupu, omezení rychlosti a ochranu soukromí (např. anonymizaci dat účastníka), a mediační funkce, která mapuje parametry externího API na interní operace síťových služeb. Jejím úkolem je bezpečně „zpřístupnit“ schopnosti lokalizovaného síťového řezu nebo edge nasazení autorizovaným aplikacím, což jim umožní dynamicky ovlivňovat chování sítě pro optimalizaci výkonu aplikace. Tím překlenuje propast mezi [IT](/mobilnisite/slovnik/it/) aplikacemi a [CT](/mobilnisite/slovnik/ct/) síťovými schopnostmi v kontextu edge computingu.

## K čemu slouží

L-NEF existuje proto, aby rozšířila paradigma zpřístupnění sítě na její okraj a řešila tak požadavky nových vertikálních aplikací na nízkou latenci a lokalitu. Centralizovaná [NEF](/mobilnisite/slovnik/nef/), zavedená v 5G, poskytuje výkonný mechanismus pro interakci třetích stran se sítí, ale pro aplikace na okraji sítě vyžadující odezvu na úrovni milisekund může být zpoždění způsobené cestou do centralizované NEF v cloudu nepřijatelné. L-NEF tento problém řeší tím, že přináší funkci zpřístupnění blíže k místu, kde se nachází aplikace a uživatelský provoz.

Motivace vychází z vize 5G podporovat ultra-spolehlivou nízkolatenční komunikaci ([URLLC](/mobilnisite/slovnik/urllc/)) a komunikaci mezi masou strojů (mMTC) pro vertikální odvětví, jako je výroba, zdravotnictví a doprava. Tato odvětví potřebují provozovat aplikace citlivé na latenci na okraji sítě a vyžadují programové, reálné řízení místních síťových zdrojů (např. zaručení šířky pásma pro robotickou paži, získání přesné polohy zařízení). Centralizovaný bod zpřístupnění nemohl splnit tyto přísné požadavky na latenci a spolehlivost. L-NEF jako součást podpůrných prvků edge computingu definovaných od Release 17 tuto mezeru přímo zaplňuje.

Historicky předchozí přístupy postrádaly standardizovaný a bezpečný způsob, jak mohou aplikace na okraji sítě interagovat s lokalizovaným síťovým řezem. Vyžadovaly proprietární rozhraní nebo hlubokou integraci. L-NEF navazuje na úspěšné koncepty SBA a NEF v 5G, ale přizpůsobuje je pro distribuované nasazení. Řeší problém poskytování zabezpečeného, standardizovaného a nízkolatenčního zpřístupnění síťových schopností na okraji sítě, což je zásadní pro monetizaci 5G sítí prostřednictvím nabídek síť-jako-sluzba pro podnikové a vertikální zákazníky.

## Klíčové vlastnosti

- Nízkolatenční zpřístupnění API pro aplikace na okraji sítě
- Lokální zpracování požadavků na zpřístupnění, aby se zabránilo cestě do centrálního cloudu
- Zabezpečená autentizace, autorizace a řízení provozu pro spotřebitele API
- Zpřístupnění lokalizovaných síťových schopností (např. stav edge UPF, místní správa QoS)
- Integrace s lokálními funkcemi 5G jádra sítě (L-PCF, L-SMF) na okraji sítě
- Podpora ochrany soukromí účastníků a anonymizace dat v lokálním kontextu

## Související pojmy

- [NEF – Network Exposure Function](/mobilnisite/slovnik/nef/)
- [UPF – User Plane Function](/mobilnisite/slovnik/upf/)

## Definující specifikace

- **TS 23.548** (Rel-19) — 5G System Edge Computing Enhancements
- **TS 29.564** (Rel-19) — Nupf Service Based Interface Protocol

---

📖 **Anglický originál a plná specifikace:** [L-NEF na 3GPP Explorer](https://3gpp-explorer.com/glossary/l-nef/)
