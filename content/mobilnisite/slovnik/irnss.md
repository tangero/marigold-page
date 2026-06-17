---
slug: "irnss"
url: "/mobilnisite/slovnik/irnss/"
type: "slovnik"
title: "IRNSS – Indian Regional Navigation Satellite System"
date: 2025-01-01
abbr: "IRNSS"
fullName: "Indian Regional Navigation Satellite System"
category: "Other"
segment: "User Equipment"
canonical: "https://3gpp-explorer.com/glossary/irnss/"
summary: "IRNSS, známý také jako NavIC, je nezávislý indický regionální satelitní navigační systém. Standardy 3GPP podporují jeho využití pro určování polohy v mobilních zařízeních, čímž poskytují alternativu k"
---

IRNSS je indický regionální navigační satelitní systém, jehož podporu pro určování polohy mobilních zařízení jakožto regionální alternativy k GPS na území Indie definují standardy 3GPP.

## Popis

Indický regionální navigační satelitní systém (IRNSS), který je provozován pod názvem NavIC (Navigation with Indian Constellation), je satelitní systém rádiové navigace vyvinutý Indickou organizací pro kosmický výzkum (ISRO). Je navržen tak, aby poskytoval službu přesné informace o poloze uživatelům v Indii a v regionu sahajícím až 1500 km od její hranice. V kontextu 3GPP je IRNSS integrován jako podporovaný globální navigační satelitní systém ([GNSS](/mobilnisite/slovnik/gnss/)) pro metody určování polohy založené na uživatelském zařízení (UE) a asistované uživatelským zařízením, vedle dalších systémů jako [GPS](/mobilnisite/slovnik/gps/), [GLONASS](/mobilnisite/slovnik/glonass/), Galileo a BeiDou.

Z pohledu architektury 3GPP je podpora IRNSS implementována v lokalizačních schopnostech UE a v mechanismech sítě pro poskytování asistenčních dat. UE musí mít kompatibilní GNSS přijímač schopný zpracovávat signály IRNSS. Síť, typicky prostřednictvím funkce správy polohy ([LMF](/mobilnisite/slovnik/lmf/)) v 5G nebo vylepšeného centra polohy mobilní stanice ([E-SMLC](/mobilnisite/slovnik/e-smlc/)) v LTE, může poskytnout UE asistenční data za účelem zlepšení času do prvního určení polohy (TTFF), přesnosti a citlivosti lokalizace založené na IRNSS. Tato asistenční data, definovaná ve specifikacích 3GPP, zahrnují parametry specifické pro IRNSS, jako jsou efemeridy, almanach, časování a ionosférické korekce.

Technické fungování spočívá v tom, že UE měří dobu příchodu signálů z více satelitů IRNSS. Pomocí známých poloh satelitů (z dekódovaných nebo asistovaných navigačních dat) a změřených dob šíření signálu vypočítá UE svou vlastní polohu pomocí trilaterace. Konstelace IRNSS se skládá ze satelitů na geostacionární dráze ([GEO](/mobilnisite/slovnik/geo/)) a geosynchronní dráze ([GSO](/mobilnisite/slovnik/gso/)), což v porovnání s konstelacemi na střední oběžné dráze Země ([MEO](/mobilnisite/slovnik/meo/)), jako je GPS, poskytuje nad indickým regionem lepší viditelnost a vyšší elevace, což může potenciálně nabídnout vyšší přesnost v městských kaňonech. Specifikace 3GPP definují charakteristiky signálu (např. pásma L5 a S) a formáty zpráv, které musí UE zvládnout.

Integrace IRNSS do standardů 3GPP umožňuje operátorům mobilních sítí v Indii a okolních regionech využívat suverénní, spolehlivý zdroj pro určování polohy. To je zvláště důležité pro služby tísňového volání (jako E911/E112), služby založené na poloze, optimalizaci sítě a různé aplikace IoT. Díky podpoře více GNSS konstelací může UE dosáhnout vyšší přesnosti a odolnosti určování polohy prostřednictvím hybridního určení, zejména v náročném prostředí, kde mohou být signály z jedné konstelace blokovány.

## K čemu slouží

Hlavním účelem IRNSS/NavIC je poskytnout Indii nezávislý regionální navigační satelitní systém a snížit tak závislost na zahraničních systémech, jako je GPS, které jsou kontrolovány jinými vládami. Tato nezávislost je klíčová ze strategických, bezpečnostních a suverénních důvodů, neboť zajišťuje přístup k přesným službám určování polohy a času za všech okolností, včetně konfliktů nebo období geopolitického napětí, kdy může být přístup k jiným GNSS omezen nebo odepřen.

Z perspektivy standardizace 3GPP byla motivací k integraci IRNSS tržní poptávka a regulatorní požadavky v Indii. S růstem penetrace chytrých telefonů vznikla potřeba, aby zařízení podporovala místní navigační systém a umožnila tak přesné lokalizační služby pro indické uživatele. Standardizace zajišťuje interoperabilitu, takže jakékoli kompatibilní UE může používat signály IRNSS, pokud je vybaveno příslušným hardwarem. Také umožňuje síťovým operátorům efektivně poskytovat asistenční data specifická pro IRNSS.

Před začleněním do specifikací 3GPP se zařízení s podporou IRNSS spoléhala na proprietární implementace, což vedlo k fragmentaci a zvýšeným nákladům. Standardizace tento problém řeší vytvořením jednotného technického rámce pro výrobce čipových sad a zařízení. Řeší problém bezproblémové integrace regionálního GNSS do globálního mobilního ekosystému, což umožňuje indickým uživatelům těžit ze zlepšené přesnosti určování polohy a dostupnosti služeb, zatímco výrobcům zařízení umožňuje mít jediný globální design, který prostřednictvím společného rozhraní definovaného 3GPP podporuje všechny hlavní GNSS konstelace.

## Klíčové vlastnosti

- Regionální pokrytí zaměřené na Indii a okolní oblasti (až 1500 km za její hranicí)
- Dvoufrekvenční provoz (pásma L5 a S) pro vyšší přesnost a ionosférické korekce
- Konstelace satelitů na GEO a GSO dráhách pro lepší viditelnost nad servisním regionem
- Podpora v 3GPP pro metody určování polohy založené na UE, asistované UE a založené na síti
- Poskytuje nezávislé služby určování polohy, navigace a časování (PNT)
- Umožňuje hybridní určování polohy s jinými GNSS konstelacemi (GPS, Galileo apod.)

## Související pojmy

- [GNSS – Global Navigation Satellite System](/mobilnisite/slovnik/gnss/)

## Definující specifikace

- **TS 36.171** (Rel-19) — A-GNSS Minimum Performance Requirements for UE
- **TS 37.355** (Rel-19) — LTE Positioning Protocol (LPP)
- **TS 38.171** (Rel-19) — 5G A-GNSS UE Positioning Requirements

---

📖 **Anglický originál a plná specifikace:** [IRNSS na 3GPP Explorer](https://3gpp-explorer.com/glossary/irnss/)
