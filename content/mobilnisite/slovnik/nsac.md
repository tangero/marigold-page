---
slug: "nsac"
url: "/mobilnisite/slovnik/nsac/"
type: "slovnik"
title: "NSAC – Network Slice Admission Control"
date: 2026-01-01
abbr: "NSAC"
fullName: "Network Slice Admission Control"
category: "Network Slicing"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/nsac/"
summary: "Řídicí mechanismus, který zajišťuje, aby počet UE registrovaných ke konkrétnímu síťovému řezu nepřekročil nastavený maximální limit. Je klíčový pro udržení výkonu řezu, prevenci zahlcení a umožňuje op"
---

NSAC je řídicí mechanismus, který zajišťuje, aby počet uživatelských zařízení registrovaných ke konkrétní síťovému řezu nepřekročil nastavený maximální limit, a tím udržoval výkon a předcházel zahlcení.

## Popis

Network Slice Admission Control (NSAC) je základní funkce řídicí roviny zavedená ve specifikaci 3GPP Release 17 pro správu rozsahu a kapacity síťových řezů. Funguje tak, že vynucuje maximální povolený počet uživatelských zařízení (UE), která mohou být současně registrovaná k dané instanci síťového řezu ([NSI](/mobilnisite/slovnik/nsi/)). Nejde o řízení přístupu ke zdrojům pro datový provoz, ale o řízení přístupu na úrovni registrace. Primárním cílem je zabránit přetížení řezu registrovanými UE, což by mohlo degradovat kvalitu služeb pro všechny uživatele tohoto řezu a potenciálně ovlivnit i další řezy sdílející stejnou podkladovou infrastrukturu. NSAC je mechanismus založený na politikách, přičemž maximální počet UE na řez je klíčovým parametrem politiky definovaným síťovým operátorem, často v souladu s komerčními nebo technickými smlouvami o úrovni služeb ([SLA](/mobilnisite/slovnik/sla/)).

Funkce NSAC je typicky implementována v rámci řídicí roviny jádra sítě a komunikuje s klíčovými síťovými funkcemi, jako je Access and Mobility Management Function ([AMF](/mobilnisite/slovnik/amf/)) a Network Slice Admission Control Function ([NSACF](/mobilnisite/slovnik/nsacf/)). Když UE zahájí registrační proceduru a požaduje síťový řez, AMF konzultuje mechanismus NSAC, aby ověřil, zda může být UE přijato k požadovanému řezu. Tato kontrola zahrnuje ověření, zda aktuální počet registrací pro daný řez je pod nastaveným maximálním limitem. Pokud limit nebyl dosažen, registrace je povolena a čítač je zvýšen. Pokud je limit dosažen, registrační požadavek pro tento konkrétní řez může být zamítnut, nebo může být UE přesměrováno na alternativní řez, v závislosti na síťových politikách a schopnostech UE.

NSAC funguje ve spolupráci s funkcí Network Slice Admission Control Function (NSACF), což je entita odpovědná za udržování počtů registrací a vynucování přístupových politik. AMF komunikuje s NSACF prostřednictvím rozhraní služebního typu (např. Namf_Communication), aby hlásil události registrace a deregistrace. NSACF udržuje čítače na řez, aktualizuje je na základě těchto událostí a poskytuje rozhodnutí o přístupu pro AMF. Tato architektura centralizuje logiku řízení přístupu, což umožňuje konzistentní vynucování politik v celé síti. NSAC také podporuje možnosti monitorování a reportingu, což operátorům umožňuje sledovat využití řezů a činit informovaná rozhodnutí o plánování kapacity a správě životního cyklu řezů.

## K čemu slouží

NSAC byl vytvořen, aby vyřešil kritickou mezeru v původní architektuře síťového řezování 3GPP definované v Release 15. Zatímco raná vydání poskytovala mechanismy pro vytváření a správu řezů, postrádala robustní řízení pro omezení rozsahu řezu z hlediska připojených uživatelů. Bez takové kontroly by oblíbený řez (např. pro službu masivního IoT nebo populární podnikovou aplikaci) mohl zažít nekontrolovaný příliv UE, což by vedlo k signalizačním bouřím, vyčerpání zdrojů a degradaci výkonu pro všechny uživatele tohoto řezu a potenciálně i pro sdílené síťové funkce. To představovalo významné riziko pro stabilitu sítě a schopnost garantovat izolovaný výkon, jak slibuje řezování.

Zavedení NSAC v Release 17 bylo motivováno potřebou operátorů nabízet spolehlivé a předvídatelné služby založené na řezech s vymahatelnými [SLA](/mobilnisite/slovnik/sla/). Umožňuje operátorům definovat 'kapacitu' řezu nejen z hlediska šířky pásma, ale i z hlediska podporovaných zařízení, což je zásadní pro komerční modely (např. prodej řezu podniku pro až 10 000 zařízení). Řeší problém přetížení řezu tím, že poskytuje pevný limit, čímž chrání řez před zahlcením. Dále umožňuje efektivnější plánování zdrojů a brání tomu, aby jeden řez monopolizoval společné zdroje řídicí roviny, čímž podporuje princip izolace zdrojů, který je základem síťového řezování.

## Klíčové vlastnosti

- Vynucuje maximální limit počtu UE současně registrovaných k instanci síťového řezu.
- Poskytuje řízení přístupu na úrovni řezu během registrace UE a procedur mobility.
- Centralizované vynucování politik prostřednictvím interakce s NSACF.
- Udržuje dynamické čítače pro registrace a deregistrace UE na řez.
- Podporuje zamítnutí registračních požadavků při dosažení kapacity řezu.
- Umožňuje síťovým operátorům implementovat komerční a technické SLA pro kapacitu řezů.

## Související pojmy

- [NSACF – Network Slice Admission Control Function](/mobilnisite/slovnik/nsacf/)
- [AMF – Access and Mobility Management Function](/mobilnisite/slovnik/amf/)
- [S-NSSAI – Single Network Slice Selection Assistance Information](/mobilnisite/slovnik/s-nssai/)

## Definující specifikace

- **TS 23.501** (Rel-20) — 5G System Architecture Stage 2
- **TS 24.501** (Rel-19) — 5G NAS Protocols Specification
- **TS 28.203** (Rel-18) — Charging management
- **TS 29.122** (Rel-19) — T8 Reference Point for Northbound APIs
- **TS 29.522** (Rel-19) — 5G NEF Northbound APIs Stage 3
- **TS 29.536** (Rel-19) — NSACF Service Based Interface Protocol

---

📖 **Anglický originál a plná specifikace:** [NSAC na 3GPP Explorer](https://3gpp-explorer.com/glossary/nsac/)
