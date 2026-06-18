---
slug: "v-pcf"
url: "/mobilnisite/slovnik/v-pcf/"
type: "slovnik"
title: "V-PCF – Visited Policy Control Function"
date: 2026-01-01
abbr: "V-PCF"
fullName: "Visited Policy Control Function"
category: "Core Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/v-pcf/"
summary: "Funkce řízení politik (Policy Control Function) umístěná v navštívené veřejné pozemní mobilní síti (VPLMN) pro roamující koncové zařízení (UE) v systému 5G. Působí jako primární bod pro rozhodování o"
---

V-PCF je funkce řízení politik (Policy Control Function) v navštívené síti pro roamujícího uživatele 5G, která zde působí jako primární bod pro rozhodování o politikách za účelem prosazování politik domácího operátora.

## Popis

Funkce řízení politik v navštívené síti (V-PCF) je základní součástí architektury 5G jádra (5GC), konkrétně navržená pro zvládání řízení politik v roamujících scénářích. Když se koncové zařízení (UE) připojí k 5G síti mimo pokrytí svého domácího operátora (navštívená [PLMN](/mobilnisite/slovnik/plmn/)), V-PCF v této navštívené síti přebírá zodpovědnost za rozhodování o politikách souvisejících s touto roamující relací. Je součástí sady řídicích funkcí (CPF) navštívené sítě. V-PCF komunikuje s několika klíčovými síťovými funkcemi. Zásadně komunikuje s domácím [PCF](/mobilnisite/slovnik/pcf/) ([H-PCF](/mobilnisite/slovnik/h-pcf/)) v domácí síti účastníka přes referenční bod N24, což je rozhraní založené na službách. Prostřednictvím tohoto rozhraní může V-PCF získávat informace o politikách specifických pro účastníka, jako je povolený výběr síťových řezů, profil kvality služeb (QoS) podle předplatného a výdajové limity. V-PCF také komunikuje s dalšími funkcemi navštívené sítě, jako je funkce správy přístupu a mobility (V-AMF) přes rozhraní N15 pro politiky týkající se přístupu a mobility, a s funkcí správy relací ([V-SMF](/mobilnisite/slovnik/v-smf/)) přes rozhraní N7 pro politiky správy relací ([PCC](/mobilnisite/slovnik/pcc/) pravidla). V-PCF působí jako bod pro rozhodování o politikách ([PDP](/mobilnisite/slovnik/pdp/)), který převádí obecné požadavky na služby od H-PCF a síťové podněty na konkrétní pravidla politik. Tato pravidla řídí aspekty, jako je to, ke které instanci síťového řezu může UE přistupovat, parametry QoS pro jeho relace protokolových datových jednotek ([PDU](/mobilnisite/slovnik/pdu/)) a politiky související s účtováním a směrováním provozu. V-PCF pak tato rozhodnutí předává příslušným vynucovacím funkcím (jako je V-SMF) v rámci navštívené sítě. Tato architektura zajišťuje, že rámec politik domácího operátora je konzistentně uplatňován i v případě, že provoz účastníka je směrován přes funkce uživatelské roviny cizí sítě.

## K čemu slouží

V-PCF byla zavedena se systémem 5G (5GS) ve specifikaci 3GPP Release 15, aby poskytla moderní, na službách založený a flexibilní rámec pro řízení politik při roamování, který nahradil dřívější architekturu založenou na [PCRF](/mobilnisite/slovnik/pcrf/) používanou v 4G. Systém 5G přinesl nové složitosti, jako jsou síťové řezy, různé požadavky na služby (eMBB, URLLC, mMTC) a architektura založená na službách (SBA). Jednoduché rozšíření staršího konceptu V-PCRF bylo nedostatečné. V-PCF byla navržena jako centrální rozhodčí orgán pro politiky v navštívené síti, schopná zvládat rozhodování o politikách pro tyto nové 5G paradigmaty. Řeší problém uplatňování podrobných, na řezy citlivých a služebně specifických politik z domácí sítě v rámci infrastruktury jiného operátora. Tím, že existuje vyhrazená funkce pro politiky v navštívené doméně, která bezproblémově komunikuje s domácí doménou, umožňuje pokročilé roamovací funkce, jako je plynulý přístup ke konkrétním síťovým řezům, konzistentní uplatňování QoS politik pro služby kritické z hlediska spolehlivosti a podpora scénářů edge computingu na navštívených místech. Poskytuje potřebné oddělení řídicí roviny a flexibilitu vyžadovanou pro různorodé případy užití v 5G, při zachování autonomie operátorů a obchodních dohod mezi domácí a navštívenou sítí.

## Klíčové vlastnosti

- Primární bod pro rozhodování o politikách pro roamující UE v navštívené 5G PLMN
- Komunikuje s domácím PCF (H-PCF) přes rozhraní založené na službách N24
- Poskytuje řízení politik pro přístup/mobilitu (přes AMF), správu relací (přes SMF) a výběr síťových řezů
- Podporuje politiky specifické pro 5G včetně síťových řezů, QoS a účtování
- Součást architektury 5G založené na službách (SBA) s rozhraními založenými na HTTP/2
- Umožňuje uplatňování politik předplatného domácí sítě v navštívené síti

## Související pojmy

- [PCF – Positioning Calculation Function](/mobilnisite/slovnik/pcf/)
- [H-PCF – Home Policy Control Function](/mobilnisite/slovnik/h-pcf/)
- [AMF – Access and Mobility Management Function](/mobilnisite/slovnik/amf/)
- [SMF – Service Management Function](/mobilnisite/slovnik/smf/)

## Definující specifikace

- **TS 23.503** (Rel-20) — 5G Policy and Charging Control Framework
- **TS 24.502** (Rel-19) — 5G Core Access via Non-3GPP Networks; Stage 3
- **TS 24.526** (Rel-19) — UE Policies for 5GS; Stage 3
- **TS 29.507** (Rel-19) — 5G Access & Mobility Policy Control Service
- **TS 29.514** (Rel-19) — 5G System; Policy Authorization Service; Stage 3
- **TS 29.525** (Rel-19) — 5G UE Policy Control Service Stage 3

---

📖 **Anglický originál a plná specifikace:** [V-PCF na 3GPP Explorer](https://3gpp-explorer.com/glossary/v-pcf/)
