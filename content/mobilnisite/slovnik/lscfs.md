---
slug: "lscfs"
url: "/mobilnisite/slovnik/lscfs/"
type: "slovnik"
title: "LSCFS – Location System Control Function in SAS"
date: 2025-01-01
abbr: "LSCFS"
fullName: "Location System Control Function in SAS"
category: "Other"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/lscfs/"
summary: "Řídicí funkce v rámci samostatného centra polohových služeb (SAS), která spravuje požadavky na polohové služby a koordinuje polohovací procedury. Je klíčová pro zajištění síťových polohových služeb, j"
---

LSCFS je řídicí funkce v rámci samostatného centra polohových služeb (SAS), která spravuje požadavky na polohové služby a koordinuje polohovací procedury pro síťové polohové služby.

## Popis

Location System Control Function in [SAS](/mobilnisite/slovnik/sas/) (LSCFS) je kritická logická komponenta v architektuře samostatného centra polohových služeb (SAS) definovaná pro [UTRAN](/mobilnisite/slovnik/utran/). SAS je síťový prvek odpovědný za poskytování polohových služeb ([LCS](/mobilnisite/slovnik/lcs/)) pro uživatelské zařízení (UE). LSCFS funguje jako centrální řídicí a koordinační entita v rámci SAS. Jejím hlavním úkolem je spravovat celou polohovou relaci, interpretovat požadavky na polohové služby od externích LCS klientů nebo od jádra sítě a řídit nezbytné kroky pro určení geografické polohy UE.

Po přijetí polohového požadavku je LSCFS zodpovědná za autentizaci, autorizaci a kontrolu soukromí cílového UE. Následně vybere vhodnou polohovací metodu (např. Cell-ID, [OTDOA](/mobilnisite/slovnik/otdoa/), [U-TDOA](/mobilnisite/slovnik/u-tdoa/), Assisted-GNSS) na základě požadované kvality služby, možností UE a stavu sítě. LSCFS komunikuje s dalšími síťovými prvky, především s přístupovou rádiovou sítí (RAN), aby zahájila a řídila polohovací proceduru. Odesílá polohovací požadavky k [RNC](/mobilnisite/slovnik/rnc/) (Radio Network Controller) a přijímá jako odpověď měřicí data nebo odhady polohy.

Funkce také komunikuje s Location System Coordinate Transformation Function ([LSCTF](/mobilnisite/slovnik/lsctf/)) pro převod surových polohovacích dat (jako jsou časová měření nebo satelitní data) do standardizovaného geografického formátu (např. zeměpisná šířka a délka). Spravuje celý životní cyklus polohové transakce, včetně zpracování chyb a konečného hlášení odhadu polohy žádajícímu klientovi. Díky centralizovanému řízení LSCFS zajišťuje efektivní využití zdrojů, podporuje více souběžných polohových požadavků a udržuje integritu a bezpečnost polohové služby.

## K čemu slouží

LSCFS byla zavedena, aby poskytla standardizovaný síťový řídicí mechanismus pro polohové služby v architektuře 3GPP. Před její specifikací byly polohové služby často proprietární nebo postrádaly jednotnou řídicí rovinu, což vedlo k problémům s interoperabilitou a neefektivnímu využití síťových zdrojů. Vytvoření LSCFS reagovalo na rostoucí regulatorní a komerční poptávku po spolehlivém a přesném určování polohy mobilních zařízení.

Mezi klíčové problémy, které řeší, patří potřeba centralizované entity pro autorizaci polohových požadavků (zásadní pro soukromí), koordinace složitých polohovacích sekvencí zahrnujících více síťových uzlů ([RNC](/mobilnisite/slovnik/rnc/), Node B, UE) a abstrakce různých polohovacích technologií od servisní vrstvy. Umožňuje entitám jádra sítě a externím aplikacím žádat o polohové informace prostřednictvím jediného, dobře definovaného rozhraní bez nutnosti porozumět specifikům podkladové rádiové přístupové technologie. Toto oddělení řízení od provádění polohovacích měření bylo zásadním architektonickým rozhodnutím pro zajištění škálovatelnosti a připravenosti na budoucí vývoj nových polohovacích metod.

## Klíčové vlastnosti

- Centralizované řízení a správa relací pro síťově iniciované i mobilním zařízením ukončené polohové požadavky
- Zpracování autentizace, autorizace a ochrany soukromí (AAP) pro přístup k polohovým službám
- Dynamický výběr polohovací metody (např. Cell-ID, OTDOA, A-GNSS) na základě možností a QoS
- Řízení signalizace mezi SAS, RNC a dalšími prvky jádra sítě
- Rozhraní s LSCTF pro výpočet a transformaci souřadnic
- Zpracování chyb a hlášení pro celou proceduru určování polohy

## Související pojmy

- [SAS – Security Attributes Service](/mobilnisite/slovnik/sas/)
- [LSCTF – Location System Coordinate Transformation Function](/mobilnisite/slovnik/lsctf/)
- [MLC – Mobile Location Center](/mobilnisite/slovnik/mlc/)

## Definující specifikace

- **TS 25.305** (Rel-19) — UTRAN UE Positioning Stage 2

---

📖 **Anglický originál a plná specifikace:** [LSCFS na 3GPP Explorer](https://3gpp-explorer.com/glossary/lscfs/)
