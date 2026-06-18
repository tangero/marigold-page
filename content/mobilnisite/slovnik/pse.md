---
slug: "pse"
url: "/mobilnisite/slovnik/pse/"
type: "slovnik"
title: "PSE – Personal Service Environment"
date: 2025-01-01
abbr: "PSE"
fullName: "Personal Service Environment"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/pse/"
summary: "Koncept architektury služeb 3GPP představující personalizovaný soubor služeb, servisních dat a preferencí uživatele. Umožňuje přenositelnost služeb mezi zařízeními a sítěmi a tvoří základ pro personal"
---

PSE je koncept architektury služeb 3GPP představující personalizovaný soubor služeb, dat a preferencí uživatele, který umožňuje přenositelnost služeb mezi zařízeními a sítěmi.

## Popis

Personal Service Environment (PSE) je základní koncept architektury služeb v 3GPP, zavedený v raných vydáních ([R99](/mobilnisite/slovnik/r99/)) a vyvíjený v následujících generacích. Nejde o jeden síťový uzel, ale o logickou konstrukci reprezentující celkovost informací, preferencí a dat předplatného uživatele vztahujících se ke službám. PSE zahrnuje uživatelský servisní profil, který obsahuje servisní triggery, předplacené služby (jako přesměrování hovoru, zákazy, multimediální telefonie) a osobní nastavení. Toto prostředí je spravováno domovskou sítí a je přístupné obslužným sítím, aby poskytovaly konzistentní, personalizované služby bez ohledu na polohu nebo zařízení uživatele.

PSE funguje tak, že odděluje servisní logiku a uživatelská data od podkladové síťové přístupové technologie. Klíčové síťové entity pracují s daty PSE. Home Subscriber Server ([HSS](/mobilnisite/slovnik/hss/)) v jádru sítě je primárním úložištěm pro data související s PSE, ukládá uživatelské profily a autentizační vektory. Pro služby založené na IMS jsou data PSE rozšířena v rámci HSS a přístupná Serving-CSCF ([S-CSCF](/mobilnisite/slovnik/s-cscf/)) k provedení servisní logiky uživatele. Architektura umožňuje přenositelnost služeb; když uživatel roamuje, entity navštívené sítě (jako Visited-CSCF) mohou načíst relevantní části PSE z domovské sítě přes standardizovaná rozhraní (např. Cx, Sh).

Klíčové komponenty PSE zahrnují User Service Identity (která může být odlišná od identity zařízení), servisní profily, nastavení soukromí a data specifická pro služby. Jeho role je poskytovat jednotný pohled na uživatele pro servisní platformy, umožňující funkce jako jednotné přihlášení, konzistentní chování služeb napříč zařízeními a síťovou personalizaci služeb (např. stav, preference zasílání zpráv). Je to základní kámen pro dosažení vize "Virtual Home Environment" ([VHE](/mobilnisite/slovnik/vhe/)), kde uživatelé zažívají konzistentní soubor služeb personalizovaný pro ně, nezávisle na přístupové síti.

## K čemu slouží

Koncept PSE byl vytvořen, aby vyřešil problém servisních sil a nedostatku personalizace v raných mobilních sítích. Zpočátku byly služby pevně svázány se specifickými síťovými přepínači nebo platformami, což činilo uživatelská data a servisní logiku nepřenositelnými. To znamenalo, že uživatelské služby (jako hlasová schránka, přesměrování hovoru) nebyly konzistentně dostupné při roamingu nebo při použití jiného zařízení. Průmysl uznal potřebu uživatelsky orientovaného, spíše než síťově orientovaného, přístupu k poskytování služeb.

Historický kontext je přesun k all-IP sítím a vývoj IP Multimedia Subsystem (IMS). PSE byl klíčovým enablerem pro vizi 3GPP o Virtual Home Environment, kde by uživatelé mohli bezproblémově přistupovat ke svým personalizovaným službám. Řešil omezení zavedením standardizovaného, centralizovaného úložiště pro uživatelská servisní data (zpočátku v [HLR](/mobilnisite/slovnik/hlr/), později [HSS](/mobilnisite/slovnik/hss/)), což umožnilo provádět servisní logiku na základě identity a profilu uživatele, nikoli jeho fyzické polohy. Tato abstraktní vrstva motivovala vytvoření bohatých, personalizovaných multimediálních služeb a byla zásadní pro úspěch IMS, umožňující servisní inovace poskytovatelům aplikací třetích stran, kteří mohli využít standardizovaný uživatelský kontext.

## Klíčové vlastnosti

- Představuje uživatelsky orientovanou kolekci servisních profilů, dat a preferencí
- Umožňuje přenositelnost služeb a konzistentní zkušenost napříč sítěmi (roaming) a zařízeními
- Centralizované uložení v domovské síti (např. v HSS) se zabezpečeným přístupem pro obslužné sítě
- Odděluje servisní logiku od přístupové technologie, podporuje servisní inovace
- Základní pro implementaci konceptu Virtual Home Environment (VHE)
- Podporuje jak okruhově spínané, tak paketově spínané (IMS) domény služeb

## Související pojmy

- [VHE – Virtual Home Environment](/mobilnisite/slovnik/vhe/)
- [HSS – Home Subscriber Server](/mobilnisite/slovnik/hss/)
- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [CSCF – Call Session Control Function](/mobilnisite/slovnik/cscf/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 22.121** (Rel-5) — Virtual Home Environment Requirements
- **TS 22.127** (Rel-9) — Open Service Access (OSA) Requirements
- **TS 23.127** (Rel-6) — Virtual Home Environment Stage 2 Specification
- **TS 23.171** (Rel-4) — LCS Stage 2 Specification for UMTS
- **TS 23.271** (Rel-19) — LCS Stage 2 Specification
- **TS 29.198** (Rel-9) — OSA API Overview Specification

---

📖 **Anglický originál a plná specifikace:** [PSE na 3GPP Explorer](https://3gpp-explorer.com/glossary/pse/)
