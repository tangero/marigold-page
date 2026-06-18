---
slug: "ugc"
url: "/mobilnisite/slovnik/ugc/"
type: "slovnik"
title: "UGC – User Generated Contents"
date: 2025-01-01
abbr: "UGC"
fullName: "User Generated Contents"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/ugc/"
summary: "User Generated Contents (UGC, obsah vytvářený uživateli) označuje multimediální obsah vytvářený a sdílený koncovými uživateli přes mobilní sítě. Jde o klíkovou kategorii služeb v 3GPP, která pohání po"
---

UGC je multimediální obsah vytvářený a sdílený koncovými uživateli přes mobilní sítě, což je klíková kategorie služeb v 3GPP, která pohání požadavky na uplinkovou kapacitu a kvalitu služeb (QoS).

## Popis

User Generated Contents (UGC, obsah vytvářený uživateli) je koncept služby v rámci architektury 3GPP, který zahrnuje vytváření, nahrávání, sdílení a spotřebu multimediálního obsahu (jako je video, audio, obrázky a text) generovaného koncovými uživateli mobilní sítě, nikoli profesionálními poskytovateli obsahu. Z pohledu síťové architektury kladou služby UGC specifické nároky na uplinkovou cestu v rádiové přístupové síti (RAN) a v core síti, protože uživatelé generují a přenášejí obsah ze svého User Equipment (UE) na aplikační servery, často umístěné na internetu nebo v sítích operátorů. To je v kontrastu s tradičními broadcastovými nebo službami na vyžádání, které jsou převážně downlinkově orientované. Síť musí zvládat potenciálně sporadické, vysokorychlostní uplinkové přenosy, spravovat související toky kvality služeb (QoS) pro živé streamování a zajistit efektivní doručování obsahu ostatním uživatelům, kteří jej mohou požadovat, často s využitím cacheování a sítí pro distribuci obsahu ([CDN](/mobilnisite/slovnik/cdn/)).

Technicky UGC ovlivňuje několik aspektů systému 3GPP. V RAN ovlivňuje algoritmy pro plánování, uplinkovou agregaci nosných a uplinkové [MIMO](/mobilnisite/slovnik/mimo/) konfigurace za účelem zvýšení přenosových rychlostí a spolehlivosti. V core síti, zejména v 5G Core (5GC), jsou toky UGC provozu řízeny prostřednictvím [PDU](/mobilnisite/slovnik/pdu/) Sessions s konkrétními charakteristikami QoS, jako je garantovaná přenosová rychlost pro uplinkové toky. Session Management Function ([SMF](/mobilnisite/slovnik/smf/)) a Policy Control Function ([PCF](/mobilnisite/slovnik/pcf/)) spolupracují na zřizování a řízení těchto toků na základě zásad předplatitele a požadavků aplikace. Architektura dále může integrovat edge computing ([MEC](/mobilnisite/slovnik/mec/)) pro snížení latence při zpracování a distribuci UGC v reálném čase.

Role UGC v síťovém ekosystému je významná. Je hlavním hybatelem pro asymetrické plánování síťové kapacity, kde se uplinkové schopnosti stávají stále kritičtějšími. Standardizace ve specifikacích jako 22.947 pomáhá definovat požadavky na služby, včetně přijatelných zpoždění při nahrávání, metrik kvality videa a cílů spolehlivosti. To zajišťuje, že výrobci síťového vybavení a mobilní operátoři mohou navrhovat a nasazovat systémy, které poskytují konzistentní a kvalitní uživatelský zážitek jak pro tvůrce obsahu, tak pro jeho konzumenty, a podporují tak růst platforem závislých na účasti uživatelů.

## K čemu slouží

Koncept User Generated Contents byl formálně zaveden ve 3GPP Release 9, aby uznal a standardizoval požadavky na rychle rostoucí třídu služeb, která zásadně měnila vzorce využívání mobilních sítí. Předtím byly specifikace 3GPP silně zaměřeny na downlinkově orientované služby, jako je mobilní [TV](/mobilnisite/slovnik/tv/), video na vyžádání a prohlížení webu, kde byla primární rolí sítě efektivní doručování obsahu uživateli. Explozivní růst platforem sociálních médií, stránek pro sdílení videa a později aplikací pro živé streamování ukázal na významnou mezeru: sítě nebyly optimálně navrženy pro vysokorychlostní, nízkolatenční uplinkový přenos z milionů jednotlivých zařízení.

Vytvoření UGC jako definované kategorie služby mělo tento problém řešit tím, že poskytlo standardizovanou sadu požadavků a architektonických hledisek. Motivovalo to vylepšení v uplinkové rádiové technologii, rámců QoS pro provoz od uživatele do sítě a síťových politik, které mohly upřednostňovat nahrávání v reálném čase. Definováním UGC umožnilo 3GPP koordinovaný vývoj napříč RAN, core sítí a služební vrstvou pro efektivní podporu těchto aplikací, a zajistilo tak, že mobilní sítě mohou zůstat primární platformou pro participativní média a sociální interakci v reálném čase.

## Klíčové vlastnosti

- Zaměření na uplinkově orientované vzorce provozu a požadavky na kapacitu
- Definice požadavků QoS na nahrávání obsahu v reálném čase (např. živé video)
- Zohlednění kontinuity služby a spolehlivosti při mobilitě
- Integrace s mechanismy pro doručování a cacheování obsahu za účelem efektivní distribuce
- Podpora různých typů médií včetně videa, audia a obrázků
- Soulad s řízením politik (policy control) pro správu síťových zdrojů podle aplikace

## Související pojmy

- [QoS – Quality of Service](/mobilnisite/slovnik/qos/)
- [MEC – Multi-Access Edge Computing](/mobilnisite/slovnik/mec/)
- [PCF – Positioning Calculation Function](/mobilnisite/slovnik/pcf/)

## Definující specifikace

- **TR 22.947** (Rel-19) — Personal Broadcast Service (PBS) Use Cases

---

📖 **Anglický originál a plná specifikace:** [UGC na 3GPP Explorer](https://3gpp-explorer.com/glossary/ugc/)
