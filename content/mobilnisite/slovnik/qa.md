---
slug: "qa"
url: "/mobilnisite/slovnik/qa/"
type: "slovnik"
title: "QA – Q Interface Adapter"
date: 2025-01-01
abbr: "QA"
fullName: "Q Interface Adapter"
category: "Management"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/qa/"
summary: "Adaptér rozhraní Q (QA) je zprostředkovací funkce definovaná ve standardech 3GPP TMN (Telecommunications Management Network). Přizpůsobuje nebo konvertuje informace a protokoly mezi proprietárním rozh"
---

QA je zprostředkovací funkce, která přizpůsobuje informace a protokoly mezi proprietárním rozhraním pro správu síťového prvku a standardizovaným rozhraním Qx pro integraci do systému podpory provozu (OSS) založeného na TMN.

## Popis

Adaptér rozhraní Q (QA) je klíčová zprostředkovací komponenta v rámci architektury 3GPP Telecommunications Management Network ([TMN](/mobilnisite/slovnik/tmn/)), jak je definována ve specifikacích řady 21.905 a souvisejících dokumentech. Funguje v rámci logické vrstvené architektury TMN, konkrétně na vrstvě správy síťových prvků ([NML](/mobilnisite/slovnik/nml/)) nebo vrstvě správy elementů ([EML](/mobilnisite/slovnik/eml/)). Hlavní funkcí QA je adaptace protokolů a informačního modelu. Síťové prvky ([NE](/mobilnisite/slovnik/ne/)), jako jsou základnové stanice nebo přepínače, často mají dodavatelsky specifická nebo starší rozhraní pro správu, která nativně nevyhovují standardizovanému rozhraní Qx dle TMN. QA se nachází mezi takovým NE a správcem prvků ([EM](/mobilnisite/slovnik/em/)) nebo systémem provozu (OS) vyšší úrovně.

Technicky QA provádí obousměrnou konverzi. V severním směru (směrem k EM/OS) přijímá příkazy a dotazy pro správu od OS přes standardizované rozhraní Qx, které používá protokoly jako [CMIP](/mobilnisite/slovnik/cmip/) (Common Management Information Protocol) nebo případně pozdější adaptace. QA poté přeloží tyto standardizované příkazy do proprietárního protokolu, formátu zpráv a informačního modelu, kterému rozumí konkrétní síťový prvek. Tento překlad zahrnuje mapování standardizovaných tříd a atributů spravovaných objektů ([MO](/mobilnisite/slovnik/mo/)) na jejich dodavatelsky specifické protějšky. Opačně, v jižním směru, QA přijímá oznámení, alarmy a měření výkonu od NE v jeho nativním formátu, převádí je do standardizovaného informačního modelu TMN a předává je OS přes rozhraní Qx.

Architektura QA může být implementována jako samostatné fyzické zařízení, softwarový modul integrovaný do správce prvků, nebo dokonce jako funkce vestavěná do samotného síťového prvku (ačkoli to druhé je pro roli QA méně obvyklé). Zpracovává klíčové funkce, jako je normalizace dat, konverze protokolových zásobníků (např. ze [SNMP](/mobilnisite/slovnik/snmp/) na CMIP), a může poskytovat lokální ukládání do mezipaměti nebo vyrovnávací paměť pro data správy. Tímto přizpůsobením QA efektivně 'skryje' heterogenitu podkladového síťového vybavení před systémem správy a prezentuje jednotný, standardy založený pohled. To je zásadní pro dosažení interoperability více dodavatelů a zefektivnění síťových operací.

## K čemu slouží

Adaptér rozhraní Q (QA) byl vytvořen k řešení základního problému v raném managementu telekomunikačních sítí: závislosti na dodavateli a provozní složitosti způsobené proprietárními rozhraními pro správu. Před rozšířeným přijetím TMN poskytoval každý dodavatel zařízení vlastní systém správy s jedinečnými protokoly a datovými modely. Pro síťové operátory využívající infrastrukturu od více dodavatelů to znamenalo provoz několika nesourodých systémů správy, což vedlo k vysokým provozním nákladům, neefektivním procesům a obtížím při korelaci chyb nebo dat o výkonu v celé síti.

Architektura TMN, standardizovaná ITU-T a přijatá 3GPP, zavedla koncept standardizovaných rozhraní (Q, F, X) pro umožnění interoperability. Rozhraní Qx bylo definováno pro komunikaci mezi síťovými prvky a správci prvků. Nicméně rozsáhlá instalovaná základna zařízení a dokonce i nová zařízení nativně Qx nepodporovala. QA byla pragmatickým řešením tohoto přechodového problému. Umožnila operátorům postupně zavádět systémy podpory provozu (OSS) vyhovující TMN bez nutnosti okamžité a nákladné výměny veškerého stávajícího síťového hardwaru.

Jejím účelem je tedy zprostředkování a migrace. Chrání investice do starší infrastruktury a zároveň umožňuje výhody standardizované, integrované správy. QA řeší omezení nestandardních rozhraní tím, že funguje jako překladač, díky čemuž proprietární zařízení 'vypadá' jako standardní prvek spravovaný TMN pro systémy správy vyšší úrovně. To byl klíčový faktor pro dosažení cílů automatizace a efektivity architektury TMN.

## Klíčové vlastnosti

- Konverze protokolů mezi proprietárními jižními rozhraními a standardizovaným rozhraním TMN Qx.
- Zprostředkování informačního modelu, překlad dodavatelsky specifických datových modelů do/z standardizovaných definic spravovaných objektů (MO) TMN.
- Umožňuje integraci starších a nevyhovujících TMN síťových prvků do standardizovaného prostředí OSS.
- Podporuje obousměrný tok dat správy poruch, konfigurace, výkonu a zabezpečení (FCAPS).
- Může být implementován jako samostatné zařízení nebo softwarový modul uvnitř správce prvků.
- Usnadňuje správu sítí více dodavatelů tím, že prezentuje jednotné rozhraní pro správu v severním směru.

## Související pojmy

- [TMN – Telecommunications Management Network](/mobilnisite/slovnik/tmn/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions

---

📖 **Anglický originál a plná specifikace:** [QA na 3GPP Explorer](https://3gpp-explorer.com/glossary/qa/)
