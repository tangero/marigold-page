---
slug: "abc"
url: "/mobilnisite/slovnik/abc/"
type: "slovnik"
title: "ABC – Application Based Charging"
date: 2025-01-01
abbr: "ABC"
fullName: "Application Based Charging"
category: "Services"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/abc/"
summary: "Application Based Charging (ABC) je účtovací mechanismus 3GPP, který operátorům umožňuje uplatňovat specifické účtovací politiky na základě používané aplikace, nikoli pouze na základě spotřeby síťovýc"
---

ABC je účtovací mechanismus 3GPP, který operátorům umožňuje uplatňovat specifické účtovací politiky na základě používané aplikace, což umožňuje diferencované účtování služeb, jako je streamování nebo hraní her.

## Popis

Application Based Charging (ABC) je sofistikovaný účtovací rámec definovaný ve specifikacích 3GPP, který mobilním síťovým operátorům umožňuje implementovat podrobné, na aplikaci zaměřené účtovací politiky. Na rozdíl od tradičních objemových nebo časových účtovacích modelů umožňuje ABC operátorům identifikovat konkrétní aplikace nebo kategorie aplikací (jako je streamování videa, sociální média, hry nebo podnikové aplikace) a pro každou z nich uplatnit odlišná účtovací pravidla. Tato schopnost je implementována v rámci architektury Policy and Charging Control (PCC), kde Policy and Charging Rules Function (PCRF) nebo Policy Control Function (PCF) hraje ústřední roli při určování a vynucování účtovacích politik specifických pro aplikaci na základě reálných síťových podmínek a profilů účastníků.

Technická implementace ABC spoléhá na schopnosti hluboké kontroly paketů (DPI), typicky nasazené v Traffic Detection Function (TDF) nebo jako integrovaná funkce v Packet Gateway (PGW) či User Plane Function (UPF). Tyto komponenty analyzují hlavičky a obsah paketů, aby identifikovaly aplikace pomocí různých technik včetně detekce na základě portů, porovnávání signatur, behaviorální analýzy a algoritmů strojového učení. Jakmile je aplikace identifikována, systém ji namapuje na konkrétní účtovací pravidla definovaná v operátorově databázi politik. Účtovací pravidla mohou specifikovat různé tarifní sazby, přidělení kvót nebo limity utrácení na základě typu aplikace, denní doby, úrovně vytížení sítě nebo úrovně předplatného.

V rámci účtovací architektury ABC komunikuje s Online Charging System (OCS) pro reálné řízení kreditu a s Offline Charging System (OFCS) pro následné zpracování záznamů o účtování dat (CDR). Když účastník zahájí datovou relaci, PCRF/PCF načte jeho profil z Subscription Profile Repository (SPR) nebo Unified Data Repository (UDR), který obsahuje politiky specifické pro ABC. Když uživatel přistupuje k různým aplikacím, TDF nebo ekvivalentní detekční funkce aplikace identifikuje a nahlásí PCRF/PCF, který následně instruuje účtovací systémy, aby uplatnily příslušná účtovací pravidla. Toto dynamické, na aplikaci zaměřené účtování umožňuje operátorům nabízet inovativní služební tarify, jako jsou 'balíčky pro sociální média', 'pasy pro streamování videa' nebo 'herní balíčky', kde specifické aplikace dostávají preferenční účtovací zacházení.

Implementace ABC vyžaduje pečlivé zvážení regulačních předpisů o ochraně soukromí a výkonnosti sítě. Protože DPI zahrnuje kontrolu obsahu paketů, musí operátorů implementovat odpovídající ochranná opatření pro soukromí a získat potřebný souhlas uživatelů tam, kde to vyžadují místní předpisy. Dále musí být režie zpracování spojená s detekcí aplikací vyvážena s požadavky na výkon sítě, pomocí optimalizací jako jsou výsledky detekce ukládané do mezipaměti a analýza na úrovni toků spíše než jednotlivých paketů. ABC představuje významný vývoj od jednoduchého objemového účtování dat k inteligentní, na služby zaměřené monetizaci, která odpovídá tomu, jak účastníci skutečně používají mobilní datové služby v moderním ekosystému internetu orientovaném na aplikace.

## K čemu slouží

Application Based Charging byl vyvinut, aby řešil omezení tradičních účtovacích modelů v kontextu rychle se vyvíjejících vzorců využívání mobilních dat. Před ABC většina operátorů spoléhala primárně na objemové nebo časové účtování, které zacházelo se vším datovým provozem stejně bez ohledu na aplikaci, která jej generovala. Tento přístup nezachycoval různou hodnotu, kterou různé aplikace poskytují účastníkům, a různé požadavky různých služeb na síťové prostředky. Například streamování videa spotřebuje výrazně větší šířku pásma než aplikace pro zasílání zpráv, ale při objemovém účtování by obě byly účtovány stejně za megabajt. ABC umožňuje operátorům implementovat jemnější účtování, které odráží jak náklady na poskytnutí různých služeb, tak vnímanou hodnotu pro účastníky.

Vznik ABC byl motivován několika obchodními a technickými faktory. Z obchodního hlediska potřebovali operátorů sofistikovanější nástroje pro monetizaci, aby mohli konkurovat poskytovatelům OTT služeb a vytvářet diferencované nabídky služeb. Díky možnosti účtování specifického pro aplikaci mohli operátorů spolupracovat s poskytovateli obsahu na 'sponzorovaných datech', vytvářet cílené služební balíčky a implementovat 'zero-rating' pro konkrétní aplikace. Technicky, rozmach chytrých telefonů a mobilních aplikací vytvořil potřebu účtovacích systémů, které by dokázaly v reálném čase rozpoznat a kategorizovat tisíce různých aplikací. To vyžadovalo pokroky v technologii hluboké kontroly paketů a integraci s vyvíjející se architekturou Policy and Charging Control v sítích 3GPP.

ABC také řeší problém řízení zahlcení sítě tím, že umožňuje politiky zaměřené na aplikace, které mohou upřednostnit nebo snížit prioritu určitých typů provozu na základě technických požadavků i komerčních úvah. Operátor může například zvolit příznivější účtování pro aplikace tolerantní k zpoždění během špičkových období zahlcení, zatímco pro služby v reálném čase zachová standardní sazby. Tato flexibilita umožňuje operátorům lépe spravovat síťové prostředky a zároveň nabízet účastníkům větší volbu a transparentnost v tom, jak jsou účtováni za různé typy využití dat. Zavedení ABC ve verzi 12 představovalo významný krok k inteligentnější, na služby zaměřené monetizaci sítě v éře 4G/LTE, s pokračujícím vývojem v následujících verzích pro podporu případů užití a síťových architektur 5G.

## Klíčové vlastnosti

- Identifikace aplikací pomocí technik hluboké kontroly paketů (DPI)
- Integrace s architekturou Policy and Charging Control (PCC) pro dynamické vynucování politik
- Podpora scénářů online i offline účtování
- Podrobná účtovací pravidla založená na typu aplikace, kategorii nebo konkrétní službě
- Schopnost účtování v reálném čase s rozhraním k Online Charging System (OCS)
- Flexibilní definice politik podporující časové, objemové a událostmi spouštěné účtovací triggery

## Definující specifikace

- **TS 32.251** (Rel-19) — PS Domain Charging Management

---

📖 **Anglický originál a plná specifikace:** [ABC na 3GPP Explorer](https://3gpp-explorer.com/glossary/abc/)
