---
slug: "lcctf"
url: "/mobilnisite/slovnik/lcctf/"
type: "slovnik"
title: "LCCTF – Location Client Co-ordinate Transformation Function"
date: 2025-01-01
abbr: "LCCTF"
fullName: "Location Client Co-ordinate Transformation Function"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/lcctf/"
summary: "LCCTF je síťová funkce v architektuře služeb určení polohy (LCS) 3GPP, která převádí geografické souřadnice mezi různými referenčními systémy. Zajišťuje, že polohová data hlášená externím klientům jso"
---

LCCTF je funkce služeb určení polohy (LCS) podle 3GPP, která převádí geografické souřadnice mezi různými referenčními systémy, například z místního elipsoidu na WGS-84, aby zajistila, že data pro externí klienty jsou v použitelném formátu.

## Popis

Location Client Co-ordinate Transformation Function (LCCTF) je specializovaná logická funkce v architektuře služeb určení polohy ([LCS](/mobilnisite/slovnik/lcs/)) 3GPP. Jejím jediným účelem je provádět matematické transformace sad geografických souřadnic. Když síť určí polohu UE, nezpracovaná polohová data mohou být vypočtena a reprezentována v konkrétním geodetickém datu nebo souřadnicovém systému (např. v místní národní síti nebo konkrétním elipsoidu používaném pro plánování rádiové sítě). LCCTF převádí tyto souřadnice do formátu explicitně požadovaného externím LCS klientem prostřednictvím [LCCF](/mobilnisite/slovnik/lccf/).

Funkce pracuje na základě jasně definovaných transformačních algoritmů a parametrů. Běžnou transformací je převod souřadnic z místního terestrického referenčního systému na Světový geodetický systém 1984 ([WGS-84](/mobilnisite/slovnik/wgs-84/)), což je globální standard používaný [GPS](/mobilnisite/slovnik/gps/) a povinný pro hlášení polohy v 3GPP. LCCTF aplikuje příslušný posun datumu, který může zahrnovat parametry translace, rotace a změny měřítka, aby dosáhla přesné konverze. Je vyvolána LCCF nebo [GMLC](/mobilnisite/slovnik/gmlc/) poté, co je získána základní poloha, ale předtím, než je výsledek doručen externímu klientovi.

Architektonicky může být LCCTF implementována jako samostatná služba nebo integrována v jiných uzlech LCS, jako je Gateway Mobile Location Centre (GMLC). Je klíčovým prvkem pro interoperabilitu, zejména pro služby založené na poloze, které fungují napříč různými zeměmi nebo regiony, jež mohou používat zastaralé národní souřadnicové systémy. Poskytnutím této transformační služby uvnitř sítě odlehčuje externího LCS klienta od nutnosti porozumět nebo implementovat složité geodetické transformace a zajišťuje, že klient přijímá polohová data v konzistentním, očekávaném formátu bez ohledu na nativní referenční rámec používaný pro určování polohy v podkladové síti.

## K čemu slouží

LCCTF byla vytvořena k řešení základního problému globální interoperability služeb určení polohy: nesouladu mezi souřadnicovými systémy. Mobilní sítě v různých zemích byly často plánovány a optimalizovány pomocí místních geodetických dat (jako ED50 v Evropě nebo Tokyo Datum v Japonsku). Externí aplikace, zejména globální, jako jsou mapové služby nebo směrování nouzových volání, však pro správnou funkci vyžadují jediný univerzální souřadnicový systém ([WGS-84](/mobilnisite/slovnik/wgs-84/)).

Bez LCCTF by polohová data poskytnutá aplikaci mohla být posunuta o stovky metrů, pokud by souřadnicový systém nebyl správně interpretován, což by činilo službu nepoužitelnou nebo dokonce nebezpečnou v případě zásahu při mimořádných událostech. LCCTF standardizuje tuto transformaci uvnitř sítě a zajišťuje, že složité geodetické výpočty jsou správně a transparentně zpracovány operátorem sítě, který má přístup ke správným transformačním parametrům pro svůj region.

Zavedena spolu s širší architekturou [LCS](/mobilnisite/slovnik/lcs/) ve verzi [R99](/mobilnisite/slovnik/r99/) byla LCCTF motivována potřebou spolehlivých komerčních a nouzových služeb (E-112). Abstrahovala geografické složitosti a umožnila vývojářům aplikací pracovat s jediným, dobře známým souřadnicovým systémem (WGS-84). To dramaticky zjednodušilo vývoj aplikací založených na poloze a zajistilo, že poloha uživatele hlášená sítí v Německu může být přesně zakreslena do mapové aplikace vyvinuté ve Spojených státech, což podpořilo globální růst služeb LBS.

## Klíčové vlastnosti

- Provádí převod mezi různými geodetickými souřadnicovými systémy
- Běžně transformuje místní síťové souřadnice na standardní WGS-84
- Aplikuje algoritmy pro posun datumu (např. Helmertovu transformaci)
- Zajišťuje interoperabilitu polohových dat pro globální služby
- Je integrována do toku odpovědi LCS před doručením klientovi
- Používá standardizované nebo nakonfigurované transformační parametry

## Související pojmy

- [LCS – Location Services](/mobilnisite/slovnik/lcs/)
- [WGS-84 – World Geodetic System 1984](/mobilnisite/slovnik/wgs-84/)
- [GMLC – Gateway Mobile Location Center](/mobilnisite/slovnik/gmlc/)

## Definující specifikace

- **TS 03.071** (Rel-7) — Location Services (LCS) Stage 2 Description
- **TS 23.171** (Rel-4) — LCS Stage 2 Specification for UMTS
- **TS 23.271** (Rel-19) — LCS Stage 2 Specification

---

📖 **Anglický originál a plná specifikace:** [LCCTF na 3GPP Explorer](https://3gpp-explorer.com/glossary/lcctf/)
