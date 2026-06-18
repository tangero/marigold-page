---
slug: "eplmn"
url: "/mobilnisite/slovnik/eplmn/"
type: "slovnik"
title: "EPLMN – Equivalent PLMN"
date: 2025-01-01
abbr: "EPLMN"
fullName: "Equivalent PLMN"
category: "Mobility"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/eplmn/"
summary: "Seznam veřejných pozemních mobilních sítí (PLMN) považovaných za ekvivalentní registrované PLMN pro výběr a převýběr buňky. Umožňuje uživatelskému zařízení (UE) zacházet s těmito sítěmi jako s 'domovs"
---

EPLMN je seznam veřejných pozemních mobilních sítí (PLMN) považovaných za ekvivalentní registrované PLMN pro výběr a převýběr buňky, což umožňuje uživatelskému zařízení (UE) zacházet s nimi jako s 'domovskou' sítí pro plynulý přenos spojení a vyrovnávání zatížení.

## Popis

Ekvivalentní [PLMN](/mobilnisite/slovnik/plmn/) (EPLMN) je koncept identifikátoru sítě klíčový pro správu mobility v systémech 3GPP. Když se uživatelské zařízení (UE) zaregistruje v síti (své registrované PLMN neboli [RPLMN](/mobilnisite/slovnik/rplmn/)), může mu síť v rámci zprávy Attach Accept nebo Tracking Area Update Accept poskytnout seznam dalších identifikátorů PLMN (PLMN ID), které má UE považovat za ekvivalentní RPLMN pro účely výběru buňky, převýběru buňky a předání spojení. UE ukládá tento seznam EPLMN do své nevolatilní paměti spolu s RPLMN. Primární technickou funkcí je rozšířit koncept 'domovského' území UE za rámec jediného identifikátoru PLMN.

Provozně, během procedur v režimu nečinnosti, jako je výběr a převýběr buňky, UE vyhodnocuje dostupné buňky. Pokud buňka patří k PLMN, která je v seznamu EPLMN (nebo se shoduje s RPLMN), je upřednostněna jako kandidát s nejvyšší prioritou. To znamená, že se UE pokusí připojit k EPLMN a zaregistrovat se v ní stejně snadno jako ve své RPLMN, aniž by ji považovala za 'cizí' síť vyžadující manuální výběr nebo roamingové dohody pro základní přístup. Seznam EPLMN je řízen sítí a může být dynamicky aktualizován signalizací, což operátorům umožňuje spravovat partnerství a dohody o sdílení sítě v reálném čase.

Jeho role je klíčová v moderních nasazeních sítí, zejména ve scénářích sdílení sítí, jako je Multi-Operator Core Network ([MOCN](/mobilnisite/slovnik/mocn/)) nebo Gateway Core Network ([GWCN](/mobilnisite/slovnik/gwcn/)), a pro národní roamingové dohody. V nasazení MOCN vysílá jedna rádiová přístupová síť (RAN) více identifikátorů PLMN. UE registrované u jednoho operátora (PLMN-A) může obdržet seznam EPLMN obsahující PLMN-B, která sdílí stejnou RAN. To UE sděluje, že buňky vysílající PLMN-B jsou pro přístup stejně platné, což umožňuje efektivní využití sdílených rádiových zdrojů a plynulý přenos spojení mezi logickými sítěmi. Efektivně odděluje identitu bodu rádiového přístupu od identity jádra sítě z pohledu UE, a to na základě politiky operátora.

## K čemu slouží

Koncept EPLMN byl zaveden, aby řešil rostoucí složitost scénářů sdílení sítí, národního roamingu a fúzí v mobilním průmyslu. Před jeho formalizací by UE bralo v úvahu pouze svou registrovanou [HPLMN](/mobilnisite/slovnik/hplmn/) (Home [PLMN](/mobilnisite/slovnik/plmn/)) nebo, v případech roamingu, [VPLMN](/mobilnisite/slovnik/vplmn/) (Visited PLMN) z předem nakonfigurovaného seznamu. Tento rigidní model vytvářel neefektivitu a problémy s uživatelským zážitkem v prostředích se sdílenými sítěmi. Například v zemi s dohodou o sdílení sítě se mohlo UE připojit k slabému signálu z exkluzivní buňky svého vlastního operátora, zatímco mnohem silnější signál z buňky sdíleného partnera (vysílající jiný identifikátor PLMN) byl dostupný, ale považován za nižší prioritu.

Zavedení EPLMN ve verzi 11 (Release 11) poskytlo standardizovaný, dynamický mechanismus, který operátorům umožňuje deklarovat partnerské a ekvivalentní vztahy. Řeší problém statických, na [SIM](/mobilnisite/slovnik/sim/) kartě založených roamingových seznamů tím, že síti umožňuje informovat UE v reálném čase o tom, které další sítě mají být považovány za 'ekvivalentní domovské'. To umožňuje plynulé rozdělení provozu napříč sdílenou infrastrukturou RAN, zlepšuje celkovou kapacitu sítě a uživatelský zážitek tím, že umožňuje UE připojit se k nejlepšímu dostupnému signálu bez ohledu na konkrétní vysílaný identifikátor PLMN, a zjednodušuje provozní správu pro operátory zapojené do sdílení sítí nebo pro ty, kteří procházejí fúzemi, kde je třeba pro účastníky sloučit více starších identifikátorů PLMN.

## Klíčové vlastnosti

- Dynamicky poskytován sítí UE prostřednictvím NAS signalizace
- Trvale uložen v USIM/nevolatilní paměti UE
- Používán pro výběr a převýběr buňky se stejnou prioritou spolu s RPLMN
- Klíčový prvek pro sdílení typu Multi-Operator Core Network (MOCN)
- Usnadňuje vyrovnávání zatížení a plynulý přenos spojení mezi partnerskými sítěmi
- Lze aktualizovat během procedur Tracking Area Update

## Související pojmy

- [PLMN – Public Land Mobile Network](/mobilnisite/slovnik/plmn/)
- [RPLMN – Registered Public Land Mobile Network](/mobilnisite/slovnik/rplmn/)
- [HPLMN – Home Public Land Mobile Network](/mobilnisite/slovnik/hplmn/)
- [VPLMN – Visited Public Land Mobile Network](/mobilnisite/slovnik/vplmn/)
- [MOCN – Multiple Operator Core Network](/mobilnisite/slovnik/mocn/)

## Definující specifikace

- **TS 37.320** (Rel-19) — Minimization of Drive Tests (MDT) Overview

---

📖 **Anglický originál a plná specifikace:** [EPLMN na 3GPP Explorer](https://3gpp-explorer.com/glossary/eplmn/)
