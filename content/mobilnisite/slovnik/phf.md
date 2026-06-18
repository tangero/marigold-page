---
slug: "phf"
url: "/mobilnisite/slovnik/phf/"
type: "slovnik"
title: "PHF – Packet Handler Function"
date: 2025-01-01
abbr: "PHF"
fullName: "Packet Handler Function"
category: "Core Network"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/phf/"
summary: "Funkční entita v rámci architektury 3GPP Generic User Profile (GUP). Je odpovědná za zpracování a správu aspektů paketových dat v profilu uživatele a usnadňuje přístup k uživatelsky specifickým inform"
---

PHF je funkční entita v architektuře 3GPP GUP odpovědná za zpracování a správu aspektů paketových dat v profilu uživatele.

## Popis

Packet Handler Function (PHF) je specializovaná komponenta v rámci architektury 3GPP Generic User Profile ([GUP](/mobilnisite/slovnik/gup/)), definovaná na počátku 21. století. Architektura GUP byla koncipována tak, aby poskytovala standardizovanou, jednotnou metodu pro přístup a správu uživatelských dat rozptýlených napříč různými síťovými doménami a úložišti. PHF se konkrétně zaměřuje na paketovou ([PS](/mobilnisite/slovnik/ps/)) doménu uživatelského profilu. Funguje jako logický zprostředkovatel nebo přístupový bod pro další síťové funkce, které vyžadují informace o uživatelských službách paketových dat, předplatných a nastaveních.

Z architektonického hlediska se PHF nachází v domovské síti a komunikuje se serverem GUP nebo úložištěm, které ukládá skutečná uživatelská data PS domény. Implementuje rozhraní a protokoly specifické pro GUP (např. založené na Diameter nebo [SOAP](/mobilnisite/slovnik/soap/)/[XML](/mobilnisite/slovnik/xml/)) ke zpracování dotazů. Když síťová entita, jako je Gateway [GPRS](/mobilnisite/slovnik/gprs/) Support Node (GGSN) nebo Policy and Charging Rules Function ([PCRF](/mobilnisite/slovnik/pcrf/)), potřebuje uživatelsky specifické informace o paketových datech, nedotazuje se databáze přímo. Místo toho odešle požadavek na PHF. PHF následně načte relevantní fragmenty dat z podřízeného úložiště profilů, případně agreguje informace z různých zdrojů dat, a vrátí strukturovanou odpověď žádající entitě.

Role PHF spočívá v abstrakci složitosti a heterogenity podkladového úložiště dat. Poskytuje jednotný, konzistentní pohled na informace z uživatelského profilu pro paketová data, bez ohledu na to, jak jsou fyzicky uložena. To zahrnuje data jako předplacené Access Point Names ([APN](/mobilnisite/slovnik/apn/)), povolené QoS profily, charakteristiky účtování a nastavení specifická pro služby. Centralizací přístupu prostřednictvím PHF síť zajišťuje konzistenci dat, zjednodušuje interoperabilitu mezi zařízeními různých výrobců a poskytuje jasný bod pro implementaci řízení přístupu a logování dotazů na profily. Ačkoli explicitní entita PHF, jak byla definována v raných specifikacích GUP, není v pozdějších monolitických návrzích síťových prvků vždy viditelná, její konceptuální funkce – specializovaný handler pro data profilu PS domény – je integrována v moderních jednotných datových úložištích ([UDR](/mobilnisite/slovnik/udr/)) a v rozhraních PCRF nebo 5G Unified Data Management (UDM).

## K čemu slouží

PHF byla vytvořena, aby řešila rostoucí složitost správy uživatelských dat v sítích 2.5G a 3G. Jak se služby vyvíjely za hranice jednoduchého hlasu a zahrnovaly různé služby paketových dat (WAP, MMS, přístup k internetu), informace v uživatelském profilu se fragmentovaly napříč více síťovými prvky, jako jsou HLR, AAA servery a databáze specifické pro služby. To ztěžovalo poskytnutí uceleného pohledu na uživatelská předplatná a nastavení, což komplikovalo poskytování služeb, roaming a zavádění nových služeb.

Architektura GUP a v ní obsažená PHF si kladly za cíl toto řešit definicí standardizované architektury pro přístup k uživatelskému profilu, nezávislé na konkrétním úložišti. PHF konkrétně řešila problém, jak mohou síťové funkce zaměřené na paketová data spolehlivě a jednotně přistupovat k požadovaným uživatelským datům. Poskytovala jasné oddělení mezi úložištěm dat a spotřebiteli dat, což operátorům umožnilo modernizovat nebo měnit své backendové systémy bez dopadu na servisní logiku v GGSN nebo jiných uzlech.

Historicky vycházela motivace z potřeby rychlejšího nasazení služeb a lepší interoperability v sítích s více dodavateli. Před takovou standardizací mohl každý síťový prvek používat proprietární metody pro načítání uživatelských dat, což vedlo k problémům s integrací. Koncept PHF podporoval servisně orientovaný přístup k přístupu k datům, který později ovlivnil návrh modernějších architektur, jako jsou IMS a 5G Core, kde je centralizovaná správa dat (např. UDM/UDR) klíčovým principem. Řešil omezení izolované, funkčně specifické správy dat a připravil cestu pro konvergovanou správu uživatelských dat.

## Klíčové vlastnosti

- Specializovaný handler pro data paketové (PS) domény v rámci architektury GUP.
- Poskytuje standardizované rozhraní pro síťové prvky k dotazování informací z uživatelského profilu pro PS doménu.
- Abstrahuje detaily podkladového úložiště dat, čímž podporuje interoperabilitu.
- Spravuje data jako předplacené APN, QoS profily a parametry účtování.
- Usnadňuje konzistentní a řízený přístup k fragmentovaným uživatelským datům.
- Funguje jako logická komponenta v systému správy profilů domovské sítě.

## Související pojmy

- [APN – Access Point Name](/mobilnisite/slovnik/apn/)
- [UDM – Unified Data Management](/mobilnisite/slovnik/udm/)
- [UDR – Unified Data Repository](/mobilnisite/slovnik/udr/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions

---

📖 **Anglický originál a plná specifikace:** [PHF na 3GPP Explorer](https://3gpp-explorer.com/glossary/phf/)
