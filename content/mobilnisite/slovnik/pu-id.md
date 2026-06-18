---
slug: "pu-id"
url: "/mobilnisite/slovnik/pu-id/"
type: "slovnik"
title: "PU-ID – PUnctuator ID"
date: 2025-01-01
abbr: "PU-ID"
fullName: "PUnctuator ID"
category: "Identifier"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/pu-id/"
summary: "PU-ID je identifikátor pro PUnctuator (interpunkční prvek), což je síťový prvek používaný v raných specifikacích 3GPP pro textové služby jako SMS. Jednoznačně identifikuje tento prvek v rámci sítě pro"
---

PU-ID je identifikátor, který jednoznačně identifikuje PUnctuator (interpunkční prvek), což je síťový prvek používaný v raných specifikacích 3GPP pro zpracování a směrování textových zpráv, jako je SMS.

## Popis

PUnctuator ID (PU-ID) je síťový identifikátor definovaný v 3GPP TS 23.042. Slouží k jednoznačné identifikaci konkrétního prvku PUnctuator v rámci síťové architektury. PUnctuator byla funkční entita v raných vydáních 3GPP, primárně spojovaná se zpracováním textových služeb, jako je služba krátkých textových zpráv ([SMS](/mobilnisite/slovnik/sms/)). Její role zahrnovala zpracování a potenciální úpravu obsahu zpráv, včetně úloh jako převod znakových sad nebo formátování zpráv pro zajištění kompatibility mezi různými typy terminálů a síťovými schopnostmi.

Architektonicky byl PUnctuator součástí vrstvy služeb zasílání zprav. PU-ID byl používán v rámci síťových signalizačních a směrovacích protokolů k nasměrování zpráv na správnou instanci PUnctuator pro zpracování. To bylo klíčové ve scénářích, kdy zpráva vyžadovala specifickou adaptaci před doručením k mobilní stanici ([MS](/mobilnisite/slovnik/ms/)) příjemce. Tento identifikátor umožňoval síti udržovat mapování mezi požadavkem na službu a příslušným prostředkem PUnctuator schopným zpracovat specifické požadavky daného požadavku, jako je převod jazyka nebo abecedy.

Ačkoli koncept PUnctuator a jeho PU-ID byly definovány od vydání Release 99, jejich praktická implementace a rozšířené použití byly omezené. Funkcionalita byla z velké části nahrazena pokročilejšími a integrovanějšími schopnostmi služeb v pozdějších architekturách 3GPP, jako je IP Multimedia Subsystem (IMS) a vylepšené služby zasílání zpráv. V důsledku toho zůstává PU-ID historickým identifikátorem v rámci specifikačního rámce 3GPP, který je dokumentován, ale není aktivní součástí moderních nasazení sítí LTE nebo 5G pro spotřebitelské služby.

## K čemu slouží

PU-ID byl vytvořen, aby řešil potřebu inteligentní adaptace zpráv v raných sítích mobilních sítí 3G. Během přechodu ze 2G na 3G koexistovala široká škála mobilních telefonů s různými schopnostmi (velikost displeje, podporované znakové sady). PUnctuator, identifikovaný svým PU-ID, byl koncipován jako síťové řešení pro zprostředkování mezi těmito odlišnými koncovými body. Jeho účelem bylo řešit problémy interoperability v zasílání zpráv a zajistit, aby zpráva odeslaná z jednoho typu zařízení mohla být správně zobrazena na jiném, potenciálně velmi odlišném, přijímacím zařízení.

Tento přístup řešil problém na síťové úrovni namísto spoléhání se na to, že každý telefon bude podporovat všechny možné formáty. Umožňoval centralizovanou správu logiky převodu kódů a formátování zpráv. PU-ID poskytoval potřebný adresovací mechanismus pro směrování zpráv ke konkrétnímu síťovému uzlu (PUnctuator), který obsahoval příslušnou logiku adaptace pro daný tok zpráv, na základě schopností odesílatele a příjemce vyjednaných během nastavení služby.

## Klíčové vlastnosti

- Jednoznačný identifikátor pro síťový prvek PUnctuator
- Používá se pro směrování zpráv ve vrstvě služeb za účelem adaptace
- Podporuje interoperabilitu mezi různými typy terminálů
- Umožňuje síťový převod znakových sad a formátů
- Definován v kontextu služeb SMS a dalších služeb zasílání zpráv
- Součást specifikací architektury služeb raných verzí 3GPP

## Související pojmy

- [SMS – Short Message Service](/mobilnisite/slovnik/sms/)
- [MS – Mobile Station](/mobilnisite/slovnik/ms/)
- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)

## Definující specifikace

- **TS 23.042** (Rel-19) — Data Compression and Decompression for 3GPP

---

📖 **Anglický originál a plná specifikace:** [PU-ID na 3GPP Explorer](https://3gpp-explorer.com/glossary/pu-id/)
