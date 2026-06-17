---
slug: "bss-b"
url: "/mobilnisite/slovnik/bss-b/"
type: "slovnik"
title: "BSS-B – Base Station Subsystem - B"
date: 2025-01-01
abbr: "BSS-B"
fullName: "Base Station Subsystem - B"
category: "Mobility"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/bss-b/"
summary: "Cílový podsystém základnové stanice (BSS), ke kterému je mobilní stanice (MS) předávána během procedury předání služby v sítích GSM/UMTS. Představuje cílový síťový prvek, který převezme rádiovou komun"
---

BSS-B je cílový podsystém základnové stanice (Base Station Subsystem), který převezme rádiovou komunikaci s mobilním zařízením po úspěšném předání služby v sítích GSM nebo UMTS.

## Popis

BSS-B je klíčový koncept v procedurách předání služby v sítích GSM a UMTS definovaných ve specifikacích 3GPP, konkrétně představuje cílový podsystém základnové stanice (Base Station Subsystem), který bude obsluhovat mobilní stanici po úspěšném předání služby. V kontextu signalizace předání služby je BSS-B cílový [BSS](/mobilnisite/slovnik/bss/), který přijímá zprávy pro přípravu předání služby od zdrojového BSS ([BSS-A](/mobilnisite/slovnik/bss-a/)) přes jádro sítě a připravuje zdroje pro přijetí příchozího mobilního zařízení. BSS-B zahrnuje řadič základnových stanic ([BSC](/mobilnisite/slovnik/bsc/)) a základnové přenosové stanice ([BTS](/mobilnisite/slovnik/bts/)) v sítích GSM, nebo řadič rádiové sítě (RNC) a Node B v sítích UMTS, které se stanou novou obsluhující rádiovou přístupovou sítí pro mobilní zařízení.

Během přípravy předání služby zdrojový BSS (BSS-A) identifikuje potenciální cílové BSS na základě měřicích hlášení od mobilní stanice. Když je rozhodnuto o předání služby ke konkrétnímu cíli, síť zahájí přípravu předání služby směrem ke zvolenému BSS-B. Jádro sítě ([MSC](/mobilnisite/slovnik/msc/)/VLR) směruje žádost o předání služby ke správnému BSS-B, který následně alokuje potřebné rádiové zdroje (frekvenci, časový slot nebo kód) a připraví své vnitřní přepojení pro přijetí příchozího spojení. BSS-B vygeneruje zprávu Příkaz k předání služby (Handover Command) obsahující nové rádiové parametry, která bude předána k [MS](/mobilnisite/slovnik/ms/) přes zdrojový BSS.

Jakmile MS úspěšně přistoupí k novým rádiovým zdrojům v BSS-B, odešle BSS-B zprávu Dokončení předání služby (Handover Complete) do jádra sítě, čímž potvrdí úspěšné předání služby. V tomto okamžiku se BSS-B stává obsluhujícím BSS pro danou MS a spravuje veškeré řízení rádiových zdrojů, šifrování a dohled nad rádiovým spojením. Předchozí BSS (BSS-A) uvolní své zdroje pro MS po obdržení potvrzení od jádra sítě. Tento mechanismus předání služby mezi BSS-A a BSS-B umožňuje plynulou mobilitu při pohybu uživatelů mezi různými pokrytými oblastmi při zachování aktivních hovorů nebo datových relací.

## K čemu slouží

BSS-B byl definován za účelem standardizace procesu identifikace cíle a přípravy předání služby v sítích GSM, což bylo zásadní pro umožnění spolehlivé mobility mezi různými podsystémy základnových stanic. Před standardizovanými procedurami předání služby měly buněčné systémy potíže s udržením nepřetržitého provozu při pohybu uživatelů mezi pokrytými oblastmi, což vedlo k přerušeným hovorům a špatné uživatelské zkušenosti. Koncept BSS-B poskytl jasný architektonický referenční bod pro přípravu cíle předání služby, což zajistilo konzistentní implementaci napříč různými dodavateli síťových zařízení.

Zavedení BSS-B řešilo základní potřebu předání služby mezi [BSS](/mobilnisite/slovnik/bss/) v rozsáhlých buněčných sítích, kde jediný BSS nemůže zajistit souvislé pokrytí napříč širokými geografickými oblastmi. Jasným rozlišením mezi zdrojovým ([BSS-A](/mobilnisite/slovnik/bss-a/)) a cílovým (BSS-B) podsystémem specifikace 3GPP umožnily předvídatelné chování při předání služby a zjednodušily plánování sítě. Toto rozlišení se stalo obzvláště důležitým, jak sítě narůstaly na složitosti s více BSS od různých dodavatelů, které potřebovaly bezproblémově spolupracovat.

BSS-B také usnadnil vývoj pokročilých typů předání služby přesahujících základní předání služby uvnitř BSS, včetně předání služby mezi MSC a později předání služby mezi různými rádiovými přístupovými technologiemi (inter-RAT) mezi GSM a UMTS. Jasná identifikace BSS-B jako cíle předání služby umožnila standardizované procedury rezervace zdrojů, mechanismy obnovy při selhání předání služby a optimalizované směrování uživatelských dat během přechodného období předání služby. Tato architektonická přehlednost byla zachována během evoluce na UMTS, kde ekvivalentní koncept platil pro předání služby mezi RNC v rámci architektury UTRAN.

## Klíčové vlastnosti

- Identifikace cíle v signalizaci předání služby
- Příprava a alokace zdrojů v cílovém BSS
- Generování příkazu k předání služby s novými rádiovými parametry
- Koordinace s jádrem sítě pro provedení předání služby
- Přechod z role cílového na obsluhující BSS po dokončení předání služby
- Podpora scénářů předání služby uvnitř MSC i mezi MSC

## Související pojmy

- [BSS-A – Base Station System - Anchor](/mobilnisite/slovnik/bss-a/)

## Definující specifikace

- **TS 23.009** (Rel-19) — Handover Procedures in PLMNs

---

📖 **Anglický originál a plná specifikace:** [BSS-B na 3GPP Explorer](https://3gpp-explorer.com/glossary/bss-b/)
