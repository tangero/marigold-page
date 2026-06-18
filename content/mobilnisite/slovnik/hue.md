---
slug: "hue"
url: "/mobilnisite/slovnik/hue/"
type: "slovnik"
title: "HUE – Home NodeB User Equipment"
date: 2025-01-01
abbr: "HUE"
fullName: "Home NodeB User Equipment"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/hue/"
summary: "HUE označuje uživatelské zařízení (UE), které je přihlášeno k buňce Home NodeB (HNB), což je femtobuňka. Jde o klasifikaci používanou ve specifikacích 3GPP k identifikaci UE fungujících v rámci pokryt"
---

HUE je uživatelské zařízení (UE), které je přihlášeno k femtobuňce Home NodeB (HNB). Jde o klasifikaci používanou ve specifikacích 3GPP k identifikaci UE v rámci pokrytí pro domácnosti nebo malé kanceláře za účelem specifického řízení.

## Popis

Home NodeB User Equipment (HUE) je termín definovaný ve specifikacích 3GPP, konkrétně v TS 25.967, pro kategorizaci uživatelského zařízení (UE), které je aktuálně registrováno a přihlášeno k Home NodeB ([HNB](/mobilnisite/slovnik/hnb/)). Home NodeB, známý také jako femtobuňka, je nízkovýkonová, spotřebitelsky nasazená základnová stanice určená ke zlepšení vnitřního pokrytí a kapacity, typicky v domácím nebo malém firemním prostředí. Klasifikace HUE je pro síť klíčová, aby mohla uplatňovat specifické politiky, správu mobility a přidělování zdrojů šité na míru přístupové vrstvě femtobuňky, která funguje odlišně od makrobuněčné sítě.

Z architektonického hlediska, když se UE přihlásí k HNB, naváže spojení přes HNB do core sítě prostřednictvím vyhrazené brány Home NodeB Gateway ([HNB-GW](/mobilnisite/slovnik/hnb-gw/)) nebo, v pozdějších architekturách, integrovaných bran. Subsystém HNB, včetně HUE, tvoří uzavřenou nebo hybridní přístupovou skupinu, často spojenou s Closed Subscriber Group ([CSG](/mobilnisite/slovnik/csg/)). Síť identifikuje UE jako HUE, aby mohla vynutit řízení přístupu, zajistit legální odposlech, uplatnit specifické tarifní pravidla a spravovat předávání hovorů mezi femtobuňkou a okolní makro sítí. Tato identifikace je součástí kontextu UE, který si síť udržuje.

Z provozní perspektivy stav HUE ovlivňuje několik síťových funkcí. Ovlivňuje mobilní procedury, protože předávání hovorů z makro buňky do buňky HNB (a naopak) vyžaduje specifickou signalizaci a řízení přístupu kvůli možným omezením CSG. Má také dopad na správu rádiových zdrojů ([RRM](/mobilnisite/slovnik/rrm/)), protože řízení výkonu a koordinace rušení mohou být v hustém, neplánovaném nasazení typickém pro femtobuňky řešeny odlišně. Dále bezpečnostní procedury, včetně autentizace a odvozování klíčů, mohou zahrnovat specifický bezpečnostní kontext HNB. Koncept HUE je nedílnou součástí standardizace technologie femtobuněk v 3GPP a poskytuje jasné vymezení pro síťové entity, aby s těmito UE v rámci širšího ekosystému UMTS (a později LTE/5G) nakládaly odpovídajícím způsobem.

## K čemu slouží

Koncept HUE byl zaveden, aby formálně řešil provozní a řídicí výzvy spojené s nasazením femtobuněk (Home NodeB) v sítích 3GPP, počínaje UMTS ve Release 8. Před femtobuňkami se UE připojovala pouze k základnovým stanicím makro sítě (NodeB), které operátoři centrálně plánovali a nasazovali. Vzestup spotřebitelsky nasazených, nízkovýkonových základnových stanic pro vnitřní pokrytí vytvořil novou třídu síťového přístupu, která vyžadovala odlišné zacházení z hlediska mobility, bezpečnosti a správy zdrojů.

Hlavním problémem, který HUE řeší, je potřeba sítě rozpoznat a odlišit UE připojené přes femtobuňku od těch připojených přes tradiční makro síť. Toto rozlišení je nezbytné pro uplatnění správného řízení přístupu (např. pro [CSG](/mobilnisite/slovnik/csg/)), implementaci vhodných politik předávání hovorů a mobility mezi heterogenními vrstvami (makro a femto), umožnění přesného účtování pro služby domácí zóny a zajištění, aby bezpečnostní protokoly zohledňovaly odlišný model důvěry u spotřebitelsky nasazeného přístupového bodu. Bez klasifikace HUE by síť zacházela se všemi UE jednotně, což by při zapojení femtobuněk vedlo k možným porušením přístupu, suboptimálnímu předávání hovorů a nesprávnému účtování.

Historickým motivem byla snaha operátorů odlehčit přenosy, zlepšit vnitřní pokrytí tam, kde je makro signál slabý, a vytvořit nové služby, jako jsou 'femto zóny.' Identifikátor HUE se stal základním prvkem specifikací 3GPP pro systémy Home NodeB a později Home eNodeB, což umožnilo standardizovaný způsob správy jedinečných aspektů zařízení připojených k femtobuňkám napříč různými výrobci zařízení a síťovými nasazeními.

## Klíčové vlastnosti

- Identifikuje UE přihlášené k Home NodeB (femtobuňce) pro účely síťového řízení.
- Umožňuje uplatňování politik řízení přístupu pro Closed Subscriber Group (CSG).
- Spouští specifické procedury správy mobility pro předávání hovorů mezi femto a makro buňkami.
- Umožňuje odlišná pravidla účtování a tarifikace pro služby domácí zóny.
- Usnadňuje cílenou správu rádiových zdrojů a koordinaci rušení pro hustá nasazení femtobuněk.
- Integruje se s bezpečnostními rámci pro autentizaci ve scénářích s spotřebitelsky nasazeným přístupem.

## Související pojmy

- [HNB – Home Node B](/mobilnisite/slovnik/hnb/)
- [CSG – Closed Subscriber Group](/mobilnisite/slovnik/csg/)
- [UE – User Equipment](/mobilnisite/slovnik/ue/)
- [HNB-GW – Home Node B Gateway](/mobilnisite/slovnik/hnb-gw/)

## Definující specifikace

- **TR 25.967** (Rel-19) — Home NodeB RF Requirements Technical Report

---

📖 **Anglický originál a plná specifikace:** [HUE na 3GPP Explorer](https://3gpp-explorer.com/glossary/hue/)
