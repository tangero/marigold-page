---
slug: "gpa"
url: "/mobilnisite/slovnik/gpa/"
type: "slovnik"
title: "GPA – GSM PLMN Area"
date: 2025-01-01
abbr: "GPA"
fullName: "GSM PLMN Area"
category: "Identifier"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/gpa/"
summary: "GSM PLMN Area (GPA) je identifikátor geografické oblasti používaný v sítích GSM k definování konkrétního regionu pokrytého veřejnou pozemní mobilní sítí (PLMN). Jde o koncept pro plánování sítě a prov"
---

GPA je identifikátor geografické oblasti používaný v sítích GSM k definování konkrétního regionu pokrytého veřejnou pozemní mobilní sítí (PLMN) pro účely plánování, provozu a správy účastníků.

## Popis

GSM [PLMN](/mobilnisite/slovnik/plmn/) Area (GPA) je logický a geografický koncept oblasti definovaný v architektuře systému GSM. PLMN (Public Land Mobile Network) je síť provozovaná jedinou administrativní entitou, identifikovaná pomocí Mobile Country Code ([MCC](/mobilnisite/slovnik/mcc/)) a Mobile Network Code ([MNC](/mobilnisite/slovnik/mnc/)). GPA tento koncept upřesňuje tím, že rozděluje celkovou pokrytou oblast PLMN na menší, spravovatelné geografické zóny. Tyto oblasti používá jádro sítě, zejména Home Location Register ([HLR](/mobilnisite/slovnik/hlr/)) a Visitor Location Register ([VLR](/mobilnisite/slovnik/vlr/)), pro správu účastníků, poskytování služeb a správu mobility. Definice a hranice GPA jsou konfigurovány operátorem sítě na základě faktorů, jako je plánování rádiové sítě, hustota účastníků a administrativní regiony.

Z architektonického hlediska je GPA identifikátor na straně sítě, který se typicky nevysílá přes rozhraní. Používá se v databázích jádra sítě a signalizačních protokolech. Například profil služeb účastníka v HLR může obsahovat pole 'GPA', které udává geografickou oblast, na kterou je účastník předplacen nebo v níž má služby povoleny. Když mobilní stanice ([MS](/mobilnisite/slovnik/ms/)) provádí aktualizaci polohy nebo se připojuje k síti, [MSC](/mobilnisite/slovnik/msc/)/VLR obsluhující dané místo může určit aktuální GPA na základě Cell Global Identity ([CGI](/mobilnisite/slovnik/cgi/)) nebo Location Area Identity (LAI) obsluhující buňky. Tyto informace o GPA pak mohou být použity k uplatnění oblastně specifických politik, například k povolení nebo omezení určitých služeb, nebo pro účely účtování (např. tarify domácí zóny).

Provozně GPA funguje jako klíč v databázových dotazech a logických kontrolách. Pokud se účastník pokusí aktivovat službu, která je platná pouze v jeho 'domácí GPA', MSC nebo servisní logika porovná aktuální obsluhující GPA (odvozenou z ID buňky) s registrovanou GPA účastníka. Neshoda může vést k zamítnutí služby nebo vyvolání procedur roamingu. Tento koncept je klíčový pro implementaci zonálních služeb, lokalizovaných oblastí přenositelnosti čísel v raných implementacích a pro úlohy správy sítě, jako je analýza provozu a monitorování výkonu na bázi jednotlivých oblastí. Jeho definice je čistě administrativní a přímo neodpovídá jedinému rádiovému parametru, ale mapuje se na skupinu buněk, lokalizačních oblastí nebo směrovacích oblastí.

## K čemu slouží

Koncept GPA byl vytvořen, aby umožnil geografickou diferenciaci služeb a politik v rámci jediné GSM sítě operátora. Rané mobilní sítě poskytovaly jednotné služby v celostátním měřítku, ale tržní požadavky si brzy vyžádaly lokalizované nabídky, jako je účtování domácí zóny, regionální omezení služeb nebo lokalizačně závislé přidané služby. GPA poskytla standardizovaný rámec pro definování těchto zón v rámci provozních podpůrných systémů PLMN.

Řešila problém příliš hrubé granularity při použití pouze ID PLMN (MCC+MNC). PLMN mohla pokrývat celou zemi, ale operátoři potřebovali spravovat účastníky a služby na úrovni města nebo okresu. Před standardizovanými koncepty oblastí používali operátoři proprietární metody, což vedlo k problémům s interoperabilitou. GPA, zavedená ve 3GPP Release 5 jako součást širších vylepšení GSM, nabídla konzistentní identifikátor, na který bylo možné odkazovat napříč systémy HLR, VLR a účtování, což usnadnilo složitou servisní logiku a efektivní správu sítě založenou na poloze účastníka.

## Klíčové vlastnosti

- Logické geografické rozdělení pokryté oblasti GSM PLMN
- Používá se pro správu účastníků a poskytování služeb v databázích jádra sítě (HLR/VLR)
- Umožňuje implementaci lokalizačních služeb a zonálních účtovacích schémat
- Mapováno z fyzických síťových prvků, jako je Cell Global Identity (CGI) nebo Location Area (LA)
- Administrativně konfigurováno operátorem sítě
- Odkazováno na v síťové signalizaci pro správu mobility a řízení služeb

## Související pojmy

- [PLMN – Public Land Mobile Network](/mobilnisite/slovnik/plmn/)
- [HLR – Home Location Register](/mobilnisite/slovnik/hlr/)
- [VLR – Visitor Location Register](/mobilnisite/slovnik/vlr/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions

---

📖 **Anglický originál a plná specifikace:** [GPA na 3GPP Explorer](https://3gpp-explorer.com/glossary/gpa/)
