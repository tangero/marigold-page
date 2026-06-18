---
slug: "sfi"
url: "/mobilnisite/slovnik/sfi/"
type: "slovnik"
title: "SFI – Short File Identifier"
date: 2025-01-01
abbr: "SFI"
fullName: "Short File Identifier"
category: "Identifier"
segment: "User Equipment"
canonical: "https://3gpp-explorer.com/glossary/sfi/"
summary: "Dvoubajtový identifikátor používaný v rámci karty UICC nebo čipové karty pro jednoznačnou identifikaci elementárního souboru (EF). Poskytuje efektivní a kompaktní adresovací mechanismus pro aplikace,"
---

SFI je dvoubajtový identifikátor používaný v rámci karty UICC pro jednoznačnou identifikaci elementárního souboru (EF), který poskytuje efektivní adresovací mechanismus pro aplikace, jako je USIM, pro přístup k uloženým datům.

## Popis

Short File Identifier (SFI) je klíčový adresovací mechanismus v architektuře souborového systému čipové karty definované standardy 3GPP, primárně pro univerzální integrovaný obvodovou kartu (UICC), která hostuje aplikaci [USIM](/mobilnisite/slovnik/usim/). Jedná se o kompaktní dvoubajtovou (16bitovou) hodnotu, která jednoznačně identifikuje elementární soubor ([EF](/mobilnisite/slovnik/ef/)) v kontextu jeho nadřazeného vyhrazeného souboru ([DF](/mobilnisite/slovnik/df/)), typicky DF pro konkrétní aplikaci, jako je USIM (DF_GSM nebo DF_Telecom). Souborový systém na kartě UICC je hierarchický, podobný stromové struktuře s hlavním souborem ([MF](/mobilnisite/slovnik/mf/)) v kořeni, vyhrazenými soubory (DF) jako adresáři a elementárními soubory (EF) jako listy obsahujícími skutečná data. Zatímco soubory lze také vybírat pomocí delších absolutních identifikátorů souborů ([FID](/mobilnisite/slovnik/fid/)), SFI poskytuje kratší a efektivnější alternativu pro častý přístup.

Architektonicky je SFI přiřazen během fáze personalizace nebo vytváření aplikace na kartě UICC. Každému EF, k němuž se předpokládá častý přístup ze strany mobilního zařízení ([ME](/mobilnisite/slovnik/me/)), je přiřazen SFI. ME (např. mobilní telefon) používá SFI v konkrétních příkazech, jako jsou READ BINARY nebo UPDATE BINARY, aby rychle odkazovalo na požadovaný EF bez nutnosti procházet celou cestu od hlavního souboru (MF). Toto je řízeno prostřednictvím rozhraní příkazů Application Protocol Data Unit ([APDU](/mobilnisite/slovnik/apdu/)) mezi ME a kartou UICC. Když chce ME například přečíst EF obsahující mezinárodní identifikaci mobilního účastníka ([IMSI](/mobilnisite/slovnik/imsi/)), může vydat příkaz specifikující hodnotu SFI asociovanou s tímto EF, což vede k rychlejšímu a energeticky efektivnějšímu načítání dat.

Jak to funguje, zahrnuje mapovací tabulku, často definovanou ve specifikaci USIM, která koreluje hodnoty SFI s konkrétními EF a jejich účelem. Například SFI '6F07' je standardizováno pro EF obsahující IMSI. Klíčovou výhodou je efektivita z hlediska režie příkazů a doby zpracování na omezeném mikrokontroléru karty UICC. Použití plného FID může vyžadovat více příkazů SELECT k procházení stromové struktury adresářů před přístupem k EF, zatímco SFI umožňuje přímý přístup, pokud je již vybrán správný DF (aplikace). To je zvláště důležité během kritických procedur, jako je registrace v síti, kde jsou rychlost a spolehlivost prvořadé. Systém SFI zajišťuje, že k nezbytným telekomunikačním datům lze přistupovat rychle a předvídatelně, čímž tvoří nízkou, ale zásadní část infrastruktury správy identit účastníků a služeb.

## K čemu slouží

SFI bylo vytvořeno za účelem optimalizace interakce mezi mobilním zařízením (ME) a čipovou kartou (UICC/USIM) v systémech 2G/3G a novějších. Rané systémy čipových karet používaly pro přístup úplné cesty k souborům, což vyžadovalo více výměn příkazů. Vzhledem k omezenému výpočetnímu výkonu raných čipových karet a potřebě rychlých síťových přístupových procedur (jako je registrace po zapnutí) byla tato režie problematická. Hlavním problémem, který SFI řeší, je snížení komunikační latence a složitosti příkazů pro přístup k často používaným datovým souborům.

Jeho vytvoření bylo motivováno potřebou rychlého standardizovaného adresovacího schématu pro základní data účastníka a sítě. Přiřazením známých krátkých identifikátorů kritickým souborům (např. IMSI, šifrovací klíče, položky telefonního seznamu) mohlo mobilní zařízení k těmto datům přistupovat s minimem APDU příkazů. To přímo zlepšilo uživatelský zážitek snížením času potřebného k registraci v síti po zapnutí. Také šetřilo životnost baterie minimalizací aktivní doby komunikace mezi základnovým procesorem telefonu a kartou UICC. Dále poskytlo čistší abstrakci pro výrobce mobilních zařízení; mohli psát software odkazující na 'SFI pro IMSI' namísto správy složité logiky výběru souborů. SFI řešilo omezení obecnějšího, ale pomalejšího mechanismu výběru souborů používajícího plné identifikátory souborů (FID), a vytvořilo tak optimalizovanou cestu pro přístup k datům kritickým z hlediska výkonu v rámci standardizovaného ekosystému čipových karet.

## Klíčové vlastnosti

- Kompaktní dvoubajtový (16bitový) identifikátor pro efektivní adresování
- Jednoznačně identifikuje elementární soubor (EF) v rámci nadřazeného vyhrazeného souboru (DF)
- Umožňuje přímý přístup k souboru bez procházení celé cesty, čímž snižuje režii příkazů
- Standardizované hodnoty pro běžné soubory USIM (např. IMSI, úložiště SMS)
- Používá se v APDU příkazech, jako je READ BINARY, pro rychlé načítání dat
- Integrální součást architektury souborového systému čipové karty UICC/USIM

## Související pojmy

- [USIM – Universal Subscriber Identity Module](/mobilnisite/slovnik/usim/)
- [APDU – Application Protocol Data Unit](/mobilnisite/slovnik/apdu/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 31.102** (Rel-19) — USIM Application Specification
- **TS 31.103** (Rel-19) — ISIM Application Specification
- **TS 31.121** (Rel-18) — UICC-terminal interface test specification

---

📖 **Anglický originál a plná specifikace:** [SFI na 3GPP Explorer](https://3gpp-explorer.com/glossary/sfi/)
