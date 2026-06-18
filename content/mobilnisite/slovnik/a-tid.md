---
slug: "a-tid"
url: "/mobilnisite/slovnik/a-tid/"
type: "slovnik"
title: "A-TID – AKMA Temporary UE IDentifier"
date: 2025-01-01
abbr: "A-TID"
fullName: "AKMA Temporary UE IDentifier"
category: "Identifier"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/a-tid/"
summary: "A-TID je dočasný identifikátor přidělený UE pro služby AKMA (Authentication and Key Management for Applications). Umožňuje aplikačním funkcím bezpečně žádat o autentizaci a klíčový materiál ze sítě be"
---

A-TID je dočasný identifikátor přidělený UE pro služby AKMA, který umožňuje aplikačním funkcím bezpečně žádat o autentizaci a klíčový materiál bez prozrazení trvalé identity UE.

## Popis

[AKMA](/mobilnisite/slovnik/akma/) Temporary UE IDentifier (A-TID) je klíčovou součástí architektury 5G Authentication and Key Management for Applications (AKMA), standardizované ve specifikacích 3GPP Release 16 a novějších. Slouží jako dočasný pseudonym přidělený sítí, který jednoznačně identifikuje uživatelské zařízení (UE) v kontextu služeb AKMA. A-TID je generován funkcí AKMA Anchor Function (AAnF) v domovské síti po úspěšném provedení primární autentizace mezi UE a 5G Core Network (5GC). K tomuto generování obvykle dochází během počáteční fáze registrace AKMA, kdy UE a AAnF navážou sdílený AKMA kontext zahrnující A-TID a přidružený klíčový materiál odvozený z klíčů primární autentizace.

Z architektonického hlediska funguje A-TID jako referenční klíč v ekosystému AKMA. Je poskytován UE aplikační funkci ([AF](/mobilnisite/slovnik/af/)), když si UE přeje přistoupit k aplikační službě zabezpečené pomocí AKMA. AF, která se nachází mimo doménu důvěry 3GPP (např. v síti poskytovatele služeb třetí strany), použije tento A-TID k dotazování na příslušnou AAnF přes Network Exposure Function ([NEF](/mobilnisite/slovnik/nef/)) pomocí referenčního bodu N33. A-TID neobsahuje trvalý identifikátor účastnického předplatného ([SUPI](/mobilnisite/slovnik/supi/)) UE, čímž chrání soukromí uživatele. Jedná se o kryptograficky generovaný nebo přidělený řetězec, který si AAnF dokáže namapovat zpět na konkrétní AKMA kontext a klíčový materiál, který sdílí s daným UE.

Technický postup zahrnuje několik klíčových kroků. Nejprve po primární autentizaci UE a AAnF odvodí AKMA Anchor Key (K_AKMA). AAnF následně vygeneruje nebo přidělí A-TID pro dané UE a uloží vazbu mezi A-TID, identifikátorem předplatného UE (interní mapování) a K_AKMA. Když UE kontaktuje AF, zahrne do své žádosti o službu A-TID. AF, která potřebuje autentizovat UE a navázat zabezpečené klíče pro aplikační relaci, odešle pomocí NEF žádost o AKMA aplikační klíč, která obsahuje přijatý A-TID. NEF tuto žádost přepošle správné AAnF. AAnF ověří platnost A-TID, načte odpovídající K_AKMA a kontext UE a vygeneruje klíče specifické pro aplikaci (K_AF), které jsou bezpečně doručeny zpět k AF. Celý tento proces umožňuje AF a UE navázat zabezpečený kanál, aniž by AF kdy poznala trvalou identitu UE.

Role A-TID v síti je mnohostranná. Primárně funguje jako ochrana soukromí, která umožňuje zavádění zabezpečení na aplikační vrstvě na základě přihlašovacích údajů sítě 3GPP. Odděluje potřebu autentizace pro aplikační funkci od detailní databáze účastníků v jádrové síti. Dále tím, že je dočasný a specifický pro službu AKMA, omezuje sledovatelnost a korelaci uživatelských aktivit napříč různými aplikačními službami. Formát a struktura A-TID jsou definovány v příslušných specifikacích 3GPP, aby byla zajištěna interoperabilita mezi UE, AAnF a AF napříč různými implementacemi dodavatelů a nasazeními sítí.

## K čemu slouží

A-TID byl vytvořen, aby řešil rostoucí potřebu zabezpečené a bezproblémové autentizace pro over-the-top ([OTT](/mobilnisite/slovnik/ott/)) a aplikační služby třetích stran v sítích 5G. Před zavedením [AKMA](/mobilnisite/slovnik/akma/) musely aplikace buď implementovat své vlastní, často slabší, autentizační mechanismy (jako hesla), nebo se spoléhat na komplexní řešení brány. To vytvářelo bezpečnostní mezery, špatnou uživatelskou zkušenost s více přihlášeními a omezovalo schopnost operátorů využívat jejich robustní síťovou autentizaci jako službu. A-TID poskytuje klíčový prvek, který umožňuje aplikaci, které jádrová síť nedůvěřuje, spustit proces doručení klíče založený na silné síťové autentizaci, aniž by se kdy dozvěděla soukromou identitu uživatele.

Historicky dřívější generace mobilních sítí postrádaly standardizovaný mechanismus, který by aplikacím umožnil využívat autentizaci na síťové úrovni. Vytvoření AKMA a A-TID v Release 16 bylo motivováno vizí 5G v oblasti vystavení síťových funkcí a architektury založené na službách. Řeší problém, jak rozšířit důvěru navázanou během počátečního přístupu UE do sítě (pomocí autentizace založené na [SIM](/mobilnisite/slovnik/sim/)) na široký ekosystém externích poskytovatelů aplikací. A-TID konkrétně řeší omezení soukromí a zabezpečení, která by plynula z prostého předání trvalého identifikátoru, jako je [SUPI](/mobilnisite/slovnik/supi/), externí entitě. Funguje jako neprůhledný token platný pouze v rámci architektury AKMA, což brání sledování a profilování uživatelů poskytovateli aplikací napříč různými službami nebo relacemi.

Dále A-TID umožňuje nové obchodní modely pro mobilní operátory, kteří tak mohou nabízet autentizaci jako službu podnikovým a vertikálním partnerům. Poskytnutím standardizovaného, zabezpečeného identifikátoru, jako je A-TID, vytvořil 3GPP základní prvek, který podporuje zabezpečený přístup k IoT službám, single sign-on pro podnikové aplikace a další scénáře, kde je bezpečnost mezi zařízením a aplikací prvořadá. Účinně překlenuje propast mezi uzavřenou, důvěryhodnou doménou jádrové sítě 3GPP a otevřenou, nedůvěryhodnou doménou internetových aplikací.

## Klíčové vlastnosti

- Ochrana soukromí tím, že nedochází k prozrazení trvalého SUPI UE aplikačním funkcím
- Slouží jako jedinečný referenční klíč pro AAnF k načtení správného AKMA kontextu a klíčového materiálu
- Umožňuje aplikačním funkcím žádat o autentizaci a odvození klíčů od jádrové sítě 5G
- Dočasný a specifický pro službu AKMA, což omezuje dlouhodobou sledovatelnost uživatele
- Standardizovaný formát zajišťující interoperabilitu mezi UE, AAnF a AF v sítích více dodavatelů
- Klíčový pro zavádění zabezpečení na aplikační úrovni (klíče K_AF) z přihlašovacích údajů 3GPP

## Související pojmy

- [AKMA – Authentication and Key Management for Applications](/mobilnisite/slovnik/akma/)
- [SUPI – Subscription Permanent Identifier](/mobilnisite/slovnik/supi/)

## Definující specifikace

- **TS 24.501** (Rel-19) — 5G NAS Protocols Specification
- **TS 29.522** (Rel-19) — 5G NEF Northbound APIs Stage 3
- **TS 33.535** (Rel-19) — 5G AKMA: Authentication and Key Management for Apps

---

📖 **Anglický originál a plná specifikace:** [A-TID na 3GPP Explorer](https://3gpp-explorer.com/glossary/a-tid/)
