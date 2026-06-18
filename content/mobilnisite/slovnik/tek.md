---
slug: "tek"
url: "/mobilnisite/slovnik/tek/"
type: "slovnik"
title: "TEK – Traffic Encryption Key"
date: 2025-01-01
abbr: "TEK"
fullName: "Traffic Encryption Key"
category: "Security"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/tek/"
summary: "Kryptografický klíč používaný k šifrování a dešifrování uživatelských dat (uživatelská rovina) nebo signalizace (řídicí rovina) mezi UE a sítí. Je základním prvkem zabezpečení komunikace přes rozhraní"
---

TEK je kryptografický klíč používaný k šifrování a dešifrování uživatelských dat nebo signalizačního provozu mezi uživatelským zařízením a sítí v mobilních systémech 3GPP.

## Popis

Klíč pro šifrování provozu (Traffic Encryption Key, TEK) je symetrický šifrovací klíč odvozený během procedury autentizace a dohody klíčů ([AKA](/mobilnisite/slovnik/aka/)) mezi uživatelským zařízením (UE) a sítí. Používá se šifrovacím algoritmem (např. [AES](/mobilnisite/slovnik/aes/), SNOW 3G, ZUC) k zajištění ochrany důvěrnosti dat přenášených přes rozhraní vzduchu. TEK se nepoužívá přímo, ale slouží jako základ, ze kterého jsou generovány skutečné šifrovací proudy klíčů. V systémech 3GPP je TEK součástí hierarchie klíčů. Pro EPS (LTE) je klíčem nejvyšší úrovně K_[ASME](/mobilnisite/slovnik/asme/) odvozený z [CK](/mobilnisite/slovnik/ck/) a [IK](/mobilnisite/slovnik/ik/) během AKA. Z K_ASME odvozuje [MME](/mobilnisite/slovnik/mme/) klíč KeNB. Z KeNB odvozuje eNodeB klíč K_UPenc, což je TEK pro uživatelskou rovinu, a klíč K_RRCenc pro šifrování [RRC](/mobilnisite/slovnik/rrc/) signalizace. Odvození používá specifické vstupy identifikátorů algoritmů, aby zajistilo oddělení klíčů.

Pro řídicí rovinu je šifrovací klíč pro [NAS](/mobilnisite/slovnik/nas/) signalizaci (K_NASenc) odvozen z K_ASME MME a UE. Tento proces zajišťuje, že pro různé oblasti ochrany (uživatelská rovina vs. řídicí rovina, přístupová vrstva vs. nepřístupová vrstva) a různé kryptografické algoritmy se používají různé klíče, čímž se zabrání tomu, aby kompromitace v jedné oblasti ovlivnila ostatní. TEK je dynamicky generován pro každou relaci a může být aktualizován během předávání mezi buňkami nebo prostřednictvím procedur příkazu režimu zabezpečení bez nutnosti úplné přeautentizace, což je vlastnost známá jako dopředná bezpečnost klíčů.

V systémech 5G (založených na 5G AKA nebo EAP-AKA') je hierarchie klíčů vylepšena, ale řídí se podobným principem. Kotvovým klíčem je K_AMF. Z něj odvozuje SEAF klíč K_gNB. gNB následně odvozuje šifrovací klíč uživatelské roviny (K_UPenc) a šifrovací klíč RRC (K_RRCenc). Architektura zabezpečení 5G také zavádí koncept kryptografického oddělení sítě, kde lze K_AMF dále odvozovat na klíče specifické pro síťový řez, což zajišťuje izolaci řezů. TEK (K_UPenc) se používá ve vrstvě PDCP v LTE i NR k provádění šifrování dat uživatelské roviny před jejich přenosem vzduchem, což zajišťuje, že uživatelská data nelze odposlouchávat.

## K čemu slouží

TEK existuje za účelem poskytnutí důvěrnosti, základní bezpečnostní služby, která zabraňuje neoprávněnému prozrazení informací. V mobilních sítích je rozhraní vzduchu obzvláště zranitelné vůči odposlechu. Bez šifrování by všechna uživatelská data (prohlížení webu, zprávy, hlasové pakety) a citlivé signalizační zprávy byly přenášeny v otevřené podobě, což by vystavovalo uživatele narušení soukromí a síť různým útokům. Motivace pro vyhrazený TEK, oddělený od klíčů integrity, vychází z kryptografických osvědčených postupů známých jako oddělení klíčů. Používání různých klíčů pro různé funkce (důvěrnost vs. integrita) omezuje dopad potenciální kompromitace klíče.

Historicky měly dřívější buněčné systémy slabší nebo volitelné šifrování. Vytvoření robustní, povinné hierarchie klíčů s TEK v 3GPP UMTS a jeho vývoj v EPS a 5G NR bylo hnací silou rostoucích požadavků na soukromí uživatelů, nástupu datových služeb přenášejících citlivé informace (např. bankovnictví, e-mail) a regulačních požadavků. Šifrování založené na TEK řeší omezení statických nebo špatně odvozených klíčů tím, že zajišťuje, že klíče jsou specifické pro relaci, odvozené z čerstvých autentizačních vektorů a mohou být během relace změněny, aby byla zachována dopředná bezpečnost, což znamená, že minulá komunikace zůstane zabezpečená, i když je aktuální klíč kompromitován.

## Klíčové vlastnosti

- Symetrický klíč odvozený z procesu autentizace a dohody klíčů (AKA)
- Používán specificky pro ochranu důvěrnosti (šifrování) provozu uživatelské nebo řídicí roviny
- Součást hierarchie klíčů zajišťující oddělení mezi klíči integrity a šifrování
- Dynamicky generován pro každou relaci a může být aktualizován během událostí mobility
- Odvození závislé na algoritmu podporuje více šifrovacích algoritmů (např. 128-EEA1, 128-EEA2, 128-EEA3)
- Aplikován ve vrstvě PDCP pro ochranu přes rozhraní vzduchu v LTE a NR

## Související pojmy

- [AKA – Authentication and Key Agreement](/mobilnisite/slovnik/aka/)
- [PDCP – Packet Data Convergence Protocol](/mobilnisite/slovnik/pdcp/)

## Definující specifikace

- **TS 23.333** (Rel-19) — MRFC-MRFP Mp Interface Requirements
- **TS 24.380** (Rel-19) — MCPTT Media Plane Control Protocol
- **TS 24.581** (Rel-19) — MCVideo Media Plane Control Protocol Specification
- **TS 29.333** (Rel-19) — MRFC-MRFP Mp Interface Protocol
- **TS 29.828** (Rel-12) — IMS Media Plane Security H.248 Profiles Study
- **TS 33.328** (Rel-19) — IMS Media Plane Security Specification

---

📖 **Anglický originál a plná specifikace:** [TEK na 3GPP Explorer](https://3gpp-explorer.com/glossary/tek/)
