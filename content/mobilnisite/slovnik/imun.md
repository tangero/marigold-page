---
slug: "imun"
url: "/mobilnisite/slovnik/imun/"
type: "slovnik"
title: "IMUN – International Mobile User Number"
date: 2026-01-01
abbr: "IMUN"
fullName: "International Mobile User Number"
category: "Identifier"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/imun/"
summary: "International Mobile User Number (IMUN) je volatelný číselný formát definovaný 3GPP, založený na mezinárodním číslovacím plánu E.164. Používá se k jednoznačné identifikaci mobilního uživatele za účele"
---

IMUN je volatelné číslo založené na standardu E.164, které definuje 3GPP pro jednoznačnou identifikaci mobilního uživatele při navazování multimediálních komunikačních relací, například videohovorů, v sítích IMS.

## Popis

International Mobile User Number (IMUN) je telekomunikační identifikátor definovaný v rámci standardů 3GPP, konkrétně pro použití v sítích IP Multimedia Subsystem (IMS). Jak je uvedeno ve specifikacích jako TS 22.101 (Service Aspects) a TS 23.003 (Numbering, Addressing, and Identification), je IMUN veřejnou uživatelskou identitou, která odpovídá mezinárodnímu číslovacímu plánu [ITU-T](/mobilnisite/slovnik/itu-t/) E.164. To znamená, že se jeví jako standardní, globálně směrovatelné telefonní číslo (např. +441234567890). Jeho primárním účelem je adresování uživatele pro navazování multimediálních relací, jako jsou hovory Voice over IP (VoIP), videohovory a další služby založené na IMS.

V architektuře IMS může mít uživatel více veřejných uživatelských identit. IMUN je jedním z typů, vedle [SIP](/mobilnisite/slovnik/sip/) [URI](/mobilnisite/slovnik/uri/) (např. user@domain.com). IMUN je uloženo v uživatelském profilu předplatitele na serveru Home Subscriber Server ([HSS](/mobilnisite/slovnik/hss/)). Když se uživatel registruje v síti IMS, jeho přiřazené veřejné uživatelské identity (včetně případných IMUN) jsou zaregistrovány a stanou se dosažitelnými. IMUN se používá v signalizační cestě, zejména v protokolech jako je SIP (Session Initiation Protocol). Například při zahájení videohovoru by volající použil IMUN volaného jako Request-URI v SIP INVITE zprávě. Jádro IMS, včetně Serving-Call Session Control Function ([S-CSCF](/mobilnisite/slovnik/s-cscf/)), používá toto číslo E.164 k provedení analýzy čísla, směrování a spouštění služeb na základě uživatelského profilu.

IMUN hraje klíčovou roli ve vzájemném propojení a interoperabilitě. Protože se řídí globálně srozumitelným formátem E.164, umožňuje uživatelům IMS přijímat hovory z tradičních telefonních sítí s komutací okruhů ([PSTN](/mobilnisite/slovnik/pstn/), [PLMN](/mobilnisite/slovnik/plmn/)) a také do nich volat prostřednictvím příslušných breakoutových bran (např. [MGCF](/mobilnisite/slovnik/mgcf/)). To překlenuje propast mezi plně IP sítěmi IMS a starší telekomunikační infrastrukturou. Dále pro služby jako je videotelefonie poskytuje IMUN uživatelům zvyklým na zadávání telefonních čísel známý způsob volání.

Životní cyklus a správa IMUN jsou spojeny s IMS předplatným účastníka. Může být zřízeno operátorem a jeden uživatel může mít jak IMUN, tak SIP URI, což umožňuje flexibilitu v tom, jak je kontaktován. Formát Tel URI (který také kóduje číslo E.164) se často používá v SIP signalizaci pro přenos IMUN. Pokračující význam IMUN spočívá v trvalé potřebě adresování založeného na E.164 ve světě, kde mnoho komunikačních služeb stále spoléhá na telefonní čísla, i když migrují na paketově přepínané služby založené na IMS.

## K čemu slouží

IMUN bylo vytvořeno, aby poskytlo standardizované schéma adresování uživatelů v rámci IP Multimedia Subsystem (IMS), což je základní síťová architektura pro poskytování multimediálních služeb v sítích 3GPP, které je v souladu s E.164. Jak 3GPP vyvíjelo hlasové služby z komutace okruhů na paketově přepínaný Voice over IP (VoIP) a multimédia, klíčovou výzvou bylo zachování interoperability se stávající globální telefonní sítí (PSTN/PLMN) a poskytnutí uživatelsky přívětivého identifikátoru.

Problém, který řešilo, byl dvojí. Za prvé, uživatelé a stávající obchodní procesy byli (a stále jsou) hluboce zvyklí na telefonní čísla. Zavedení zcela odlišného schématu adresování (pouze SIP URI) pro nové multimediální služby by vytvořilo bariéru pro jejich přijetí. IMUN umožnilo, aby k novým službám založeným na IMS, jako je videotelefonie, bylo možné přistupovat pomocí známého telefonního čísla. Za druhé, pro síťové operátory bylo bezproblémové vzájemné propojení mezi IMS a staršími sítěmi klíčové pro kontinuitu služeb. Identita založená na E.164, jako je IMUN, umožňuje směrovací logice a bránovým funkcím (jako je MGCF) překládat mezi signalizací IMS založenou na SIP a signalizací s komutací okruhů založenou na ISUP/BICC pomocí společného číselného formátu.

Historicky, jak se IMS vyvíjelo od Release 5 dále, bylo IMUN definováno spolu se SIP URI, aby nabídlo možnost duálního adresování. Řešilo omezení spočívající pouze v identifikátorech zaměřených na zařízení (jako IMSI) nebo nevolatelných identifikátorech, a zajišťovalo, že uživatelé IMS mohou být integrováni do globálního číslovacího plánu. To byl klíčový faktor pro komerční úspěch služeb založených na IMS, protože jim umožnil nahradit a vylepšit tradiční telefonii, místo aby existovaly jako oddělený, nekompatibilní systém.

## Klíčové vlastnosti

- Globální telefonní číslo ve formátu E.164 používané v IMS
- Slouží jako veřejná uživatelská identita (Public User Identity) pro navazování relací
- Uloženo v uživatelském profilu na serveru Home Subscriber Server (HSS)
- Používáno v SIP signalizaci (často jako Tel URI) pro směrování hovorů
- Umožňuje vzájemné propojení mezi sítěmi IMS a tradičními sítěmi s komutací okruhů
- Poskytuje známý způsob volání pro multimediální služby, jako jsou videohovory

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [MSISDN – Mobile Station International Subscriber Directory Number](/mobilnisite/slovnik/msisdn/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 22.101** (Rel-20) — Service Principles for PLMNs
- **TS 22.105** (Rel-19) — Telecommunication Services Framework
- **TR 22.975** (Rel-4) — UMTS Numbering and Addressing Requirements

---

📖 **Anglický originál a plná specifikace:** [IMUN na 3GPP Explorer](https://3gpp-explorer.com/glossary/imun/)
