---
slug: "nsdu"
url: "/mobilnisite/slovnik/nsdu/"
type: "slovnik"
title: "NSDU – Network Service Data Unit"
date: 2025-01-01
abbr: "NSDU"
fullName: "Network Service Data Unit"
category: "Protocol"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/nsdu/"
summary: "Protokolová datová jednotka (PDU) používaná v kontextu síťových služebních protokolů, jako je například Base Station System Application Part (BSSAP). Představuje jednotku dat vyměňovanou mezi síťovými"
---

NSDU je protokolová datová jednotka používaná síťovými služebními protokoly k přenosu služebních informací mezi síťovými entitami, což umožňuje strukturovanou komunikaci přes síťová rozhraní.

## Popis

Network Service Data Unit (NSDU) je základní konstrukcí v telekomunikačních protokolových zásobnících, zejména v kontextu síťových služeb definovaných 3GPP. Představuje samostatný blok dat přenášený mezi partnerskými síťovými služebními entitami. NSDU obsahuje řídicí informace protokolu a volitelně i uživatelská data, které společně tvoří užitečné zatížení pro primitivu síťové služby. Struktura a obsah NSDU jsou definovány konkrétním služebním protokolem, který jej používá, jako jsou například ty podrobně popsané v specifikacích TS 21.905 (Vocabulary for 3GPP Specifications) a TS 22.060 (General Packet Radio Service ([GPRS](/mobilnisite/slovnik/gprs/)); Service description).

Během provozu je NSDU generováno protokolem vyšší vrstvy nebo aplikací, když požaduje službu od podkladové vrstvy síťové služby. Tato vrstva, často součást řídicí roviny, je zodpovědná za spolehlivý přenos dat a správu spojení mezi síťovými uzly. Servisní vrstva obalí NSDU vlastní hlavičkou, která obsahuje adresování a řídicí informace, a vytvoří tak protokolovou datovou jednotku ([PDU](/mobilnisite/slovnik/pdu/)) vhodnou pro přenos přes fyzický spoj. Po přijetí servisní vrstva partnerské entity zpracuje hlavičku, extrahuje NSDU a doručí jej odpovídající entitě protokolu vyšší vrstvy.

Role NSDU je vrstvených síťových architekturách klíčová. Slouží jako standardizovaný prostředek pro výměnu informací přes definované služební přístupové body (SAPs). Například v kontextu signalizace sítí GPRS nebo raných sítí GSM se NSDU používají k přenosu zpráv pro správu mobility, správu relací nebo službu krátkých zpráv. Přesná definice toho, co tvoří NSDU – její velikostní omezení, struktura a přidružená primitiva (např. N-UNITDATA request/indication) – zajišťuje, že různé implementace síťových entit mohou správně spolupracovat a rozumět tomu, jak tyto základní datové jednotky zabalit, přenést a interpretovat.

## K čemu slouží

Koncept NSDU byl vytvořen, aby poskytl jasný, standardizovaný model pro výměnu dat v rámci vrstvené protokolové architektury telekomunikačních sítí. Před takovou formalizací mohly ad-hoc metody pro balení a přenos řídicích a uživatelských dat mezi síťovými uzly vést k problémům s interoperabilitou a ke složitému, nemodulárnímu návrhu softwaru. Model NSDU zavádí abstrakci a oddělení zájmů, což umožňuje aplikacím vyšších vrstev být nezávislé na podkladových transportních mechanismech.

Jeho primárním účelem je definovat kvantum informací, které se síťová služební vrstva zavazuje transparentně přenést z jedné entity na druhou. Tím řeší problém, jak mohou různé síťové funkce – umístěné na různých fyzických uzlech, jako je Mobile Switching Center ([MSC](/mobilnisite/slovnik/msc/)) a Base Station Controller ([BSC](/mobilnisite/slovnik/bsc/)) – komunikovat komplexní služební požadavky a odpovědi spolehlivým a uspořádaným způsobem. NSDU je objekt, který je předáván přes služební hranici a umožňuje služby jako spojovaný nebo nespojovaný přenos dat.

Historicky jeho zavedení v dřívějších vydáních, jako je Rel-4, formalizovalo výměnu dat pro služby GSM a vyvíjejících se služeb [GPRS](/mobilnisite/slovnik/gprs/). Poskytlo základní stavební kámen, na kterém mohly být v pozdějších vydáních 3GPP vybudovány pokročilejší služby a protokoly. Díky konzistentní definici datové jednotky standardy zajišťují, že rozhraní síťových služeb jsou dobře definována, což je nezbytné pro více-dodavatelská nasazení sítí a pro stabilní vývoj síťových schopností v čase.

## Klíčové vlastnosti

- Představuje standardizovanou jednotku dat pro výměnu síťových služeb
- Obsahuje řídicí informace protokolu a/nebo uživatelská data
- Přenášeno pomocí definovaných služebních primitiv (např. request, indication)
- Základní pro spojované i nespojované síťové služby
- Zajišťuje interoperabilitu mezi implementacemi síťových entit
- Definováno v kontextu konkrétních služebních protokolů, jako je BSSAP

## Související pojmy

- [PDU – Protocol Data Unit](/mobilnisite/slovnik/pdu/)
- [BSSAP – Base Station Subsystem Application Part](/mobilnisite/slovnik/bssap/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 22.060** (Rel-19) — GPRS Stage 1 Service Description

---

📖 **Anglický originál a plná specifikace:** [NSDU na 3GPP Explorer](https://3gpp-explorer.com/glossary/nsdu/)
