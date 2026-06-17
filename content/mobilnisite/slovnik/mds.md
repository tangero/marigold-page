---
slug: "mds"
url: "/mobilnisite/slovnik/mds/"
type: "slovnik"
title: "MDS – Multimedia Distribution Service"
date: 2025-01-01
abbr: "MDS"
fullName: "Multimedia Distribution Service"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/mds/"
summary: "MDS je raný koncept služby 3GPP pro vysílání multimediálního obsahu, jako je audio a video, mobilním uživatelům. Představuje základní rámec pro mobilní televizi a distribuci obsahu, který zkoumal síťo"
---

MDS je raný koncept služby 3GPP pro vysílání multimediálního obsahu mobilním uživatelům, který poskytuje základní rámec pro mobilní televizi a efektivní doručování obsahu velkému publiku.

## Popis

Multimedia Distribution Service (MDS) je koncept služby definovaný ve velmi raných vydáních specifikací 3GPP (počínaje Release 99). Konceptualizuje systém pro efektivní doručování multimediálního obsahu – jako jsou televizní vysílání, rádiové proudy a stahování souborů – potenciálně velkému počtu mobilních uživatelských zařízení (UE) současně. MDS není jediný protokol nebo rozhraní, ale spíše rámec servisní architektury, který identifikuje potřebné síťové funkce, přenosové služby a požadavky na uživatelské služby pro distribuci obsahu typu point-to-multipoint přes mobilní sítě.

Rámec MDS, jak je nastíněn ve specifikaci 21.905 (Vocabulary for 3GPP Specifications), zvažuje dvě primární metody distribuce: streamování a stahování. Pro distribuci streamováním jsou kontinuální multimediální data (např. živý televizní kanál) doručována uživatelům v reálném čase. Pro distribuci stahováním jsou diskrétní datové soubory (např. zpravodajská vsuvka nebo softwarová aktualizace) doručeny k uložení a pozdější spotřebě. Architektura zahrnuje zdroje služeb, distribuční systém uvnitř sítě a uživatelská zařízení (UE). Zkoumá, jak je obsah vložen do sítě, jak je směrován a replikován přes core network a radio access network, a nakonec jak je přenášen přes rozhraní rádiového přístupu k účastníkům.

Klíčovým aspektem MDS je jeho zaměření na efektivitu. Na rozdíl od unicastového doručování, které vyčleňuje samostatný kanál pro každého uživatele, se služba vysílání/multicastu, jako je MDS, snaží použít jeden sdílený kanál k obsluze mnoha uživatelů v konkrétní oblasti, čímž šetří cenné zdroje rádiové a přenosové sítě. Rámec řešil výzvy jako oznámení služby (jak uživatelé objevují dostupný obsah), předplatné a správa klíčů pro placené služby a podpora mobility pro uživatele pohybující se mezi buňkami. Zatímco MDS sám o sobě byl z velké části konceptuální studií, jeho požadavky a architektonické myšlenky přímo přispěly k vývoji a standardizaci služby Multimedia Broadcast Multicast Service ([MBMS](/mobilnisite/slovnik/mbms/)), která se stala konkrétní realizací těchto konceptů v sítích 3GPP.

## K čemu slouží

MDS byl vytvořen na počátku 21. století, aby prozkoumal, jak lze vznikající 3G sítě využít pro více než jen hlasové hovory a individuální přístup k internetu. Hnacím problémem bylo neefektivní využití síťové kapacity, když mnoho uživatelů ve stejné oblasti chtělo přistupovat ke stejnému oblíbenému obsahu (např. významná sportovní událost nebo zpravodajské vysílání). Použití tradičních point-to-point (unicast) spojení pro tento účel by rychle zahltilo síť. Telekomunikační průmysl viděl příležitost nabízet služby mobilní televize a rádia, což vyžadovalo nový, efektivní mechanismus doručování typu point-to-multipoint.

Koncept MDS byl motivován omezeními stávající mobilní architektury, která byla zásadně navržena pro unicastovou komunikaci. Sloužil jako studie požadavků a proveditelnosti k definování toho, jak by měla mobilní vysílací služba vypadat. Řešil otázky týkající se poskytování služeb, účtování, zabezpečení a možností koncových zařízení. Tato základní práce byla klíčová pro sjednocení zainteresovaných stran (operátorů, dodavatelů, vysílatelů) na společné vizi. Výstupy studií MDS poskytly přímý vstup pro podrobný technický návrh [MBMS](/mobilnisite/slovnik/mbms/), který byl standardizován počínaje 3GPP Release 6. MDS tedy představuje počáteční, vysokou úroveň definice služby, která připravila cestu pro praktické implementace vysílání a multicastu v mobilních sítích.

## Klíčové vlastnosti

- Konceptuální rámec pro distribuci multimediálního obsahu typu point-to-multipoint.
- Zahrnuje metody distribuce streamováním (v reálném čase) i stahováním (na bázi souborů).
- Zaměřuje se na efektivní využití zdrojů rádiové a core sítě pro oblíbený obsah.
- Definuje architektonické požadavky na oznámení a objevování služeb.
- Zvažuje modely předplatného, zabezpečení a účtování pro vysílací služby.
- Poskytuje základní definici služby, která vedla ke standardu MBMS.

## Související pojmy

- [MBMS – Multimedia Broadcast Multicast Service](/mobilnisite/slovnik/mbms/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions

---

📖 **Anglický originál a plná specifikace:** [MDS na 3GPP Explorer](https://3gpp-explorer.com/glossary/mds/)
