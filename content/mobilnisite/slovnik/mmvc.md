---
slug: "mmvc"
url: "/mobilnisite/slovnik/mmvc/"
type: "slovnik"
title: "MMVC – Multi-stream Multiparty Video Conferencing"
date: 2025-01-01
abbr: "MMVC"
fullName: "Multi-stream Multiparty Video Conferencing"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/mmvc/"
summary: "Služba 3GPP umožňující kvalitní videokonference více účastníků, kde každý účastník může přijímat více nezávislých video streamů. Umožňuje dynamické řízení rozložení a selektivní sledování, což zlepšuj"
---

MMVC je služba 3GPP umožňující videokonference více účastníků, kde každý účastník může přijímat více nezávislých video streamů pro dynamické řízení rozložení a selektivní sledování přes mobilní sítě.

## Popis

Multi-stream Multiparty Video Conferencing (MMVC) je standardizovaná služba definovaná 3GPP, která výrazně vylepšuje tradiční videokonference. Funguje tak, že zřizuje centralizovanou funkci zpracování médií, často uvnitř aplikačního serveru nebo specializované Multimedia Resource Function ([MRF](/mobilnisite/slovnik/mrf/)) v jádru IP Multimedia Subsystem (IMS). Na rozdíl od starších konferenčních systémů, kde se všem účastníkům posílá jediný složený video mix, MMVC umožňuje konferenčnímu serveru generovat a spravovat více nezávislých mediálních streamů pro každého účastníka. To zahrnuje samostatné streamy pro každého aktivního mluvčího, stream s prezentací a potenciálně streamy pro různé úhly kamery nebo rozložení. Klíčovou architektonickou komponentou je Media Control Function, která vyjednává schopnosti s uživatelským zařízením (UE), spravuje mixování a směrování těchto více streamů a zajišťuje řízení práva promluvy.

Služba funguje využitím Session Initiation Protocol (SIP) a Session Description Protocol (SDP) pro zřizování relace a vyjednávání médií. Při nastavování relace uživatelské zařízení (UE) indikuje svou podporu MMVC a svou schopnost dekódovat více simultánních Real-time Transport Protocol (RTP) streamů. Konferenční fokus sítě, typicky IMS Application Server ([AS](/mobilnisite/slovnik/as/)), koordinuje relaci. Dává pokyny zdroji pro zpracování médií, které streamy vytvořit, zakódovat a přeposlat každému účastníkovi na základě jeho požadavků a síťových podmínek. To umožňuje účastníkovi například zvolit hlavní pohled na aktuálního mluvčího a zároveň mít sekundární pohled picture-in-picture na sdílenou prezentaci, přičemž vše je doručováno jako samostatné RTP streamy.

Úloha MMVC v síti spočívá v poskytování bohatého, flexibilního a personalizovaného konferenčního zážitku, který využívá rostoucí přenosovou kapacitu a výpočetní výkon mobilních zařízení. Přesouvá složitost z koncového bodu do sítě, což umožňuje pokročilé funkce na jednodušších zařízeních. Služba se integruje se základními funkcemi IMS, jako je Call Session Control Function ([CSCF](/mobilnisite/slovnik/cscf/)) pro směrování a Home Subscriber Server ([HSS](/mobilnisite/slovnik/hss/)) pro data servisního profilu. Také spolupracuje s řízením politik (PCRF/[PCF](/mobilnisite/slovnik/pcf/)), aby zajistila odpovídající Quality of Service (QoS) pro více vysokokapacitních streamů, což z ní činí klíčový prvek pro profesionální mobilní spolupráci.

## K čemu slouží

MMVC byla vytvořena, aby řešila omezení tradičních videotelefonních konferencí založených na 3G-324M nebo raných IMS, které typicky poskytovaly všem účastníkům jedinou, pevnou video kompozici („video mix“). Tento starý model neposkytoval žádnou personalizaci, plýtval přenosovou kapacitou posíláním nežádaného video obsahu a poskytoval špatný uživatelský zážitek, zejména na schůzkách s mnoha účastníky nebo více zdroji obsahu. Vzestup vysokorychlostních LTE sítí a výkonných chytrých telefonů vytvořil poptávku po obchodních a spotřebitelských videokonferenčních službách, které by mohly konkurovat nebo se integrovat s populárními over-the-top ([OTT](/mobilnisite/slovnik/ott/)) aplikacemi.

Primární problém, který MMVC řeší, je nedostatek uživatelské kontroly a flexibility rozložení v konferencích poskytovaných mobilní sítí. Standardizací více-streamového přístupu umožnilo 3GPP síťovým operátorům nabízet konkurenceschopnou službu na úrovni operátora. To umožňuje účastníkům zvolit si vlastní pohled (např. na aktivního mluvčího, galerii nebo prezentaci), což je klíčové pro efektivní vzdálenou spolupráci. Dále optimalizuje využití síťových zdrojů tím, že síti umožňuje posílat pouze streamy, které si uživatel vybral, namísto jediného složeného toku vysokého datového toku ze všech video zdrojů. Její vytvoření bylo motivováno potřebou operátorů přesáhnout základní hlasové služby a SMS, využít své investice do IMS k nabízení pokročilých, přidaných multimediálních služeb, které generují nové zdroje příjmů a snižují odchod zákazníků.

## Klíčové vlastnosti

- Simultánní přenos více nezávislých RTP video streamů do jediného koncového bodu
- Dynamické rozložení a výběr streamů řízený účastníkem (např. aktivní mluvčí, pohled na prezentaci)
- Síťové zpracování a mixování médií, které snižuje složitost koncového bodu
- Integrace s jádrem IMS pro řízení relace, autentizaci a účtování
- Podpora mechanismů řízení práva promluvy pro správu mluvících práv
- Vyjednávání Quality of Service (QoS) a vynucování politik pro více mediálních toků

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [MRF – Multimedia Resource Function](/mobilnisite/slovnik/mrf/)

## Definující specifikace

- **TR 26.948** (Rel-19) — Video enhancements for 3GPP Multimedia Services

---

📖 **Anglický originál a plná specifikace:** [MMVC na 3GPP Explorer](https://3gpp-explorer.com/glossary/mmvc/)
