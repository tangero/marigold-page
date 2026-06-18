---
slug: "sema"
url: "/mobilnisite/slovnik/sema/"
type: "slovnik"
title: "SEMA – Simple Electromagnetic Analysis"
date: 2025-01-01
abbr: "SEMA"
fullName: "Simple Electromagnetic Analysis"
category: "Security"
segment: "Security"
canonical: "https://3gpp-explorer.com/glossary/sema/"
summary: "Simple Electromagnetic Analysis (SEMA) je typ útoku postranním kanálem, který extrahuje tajné informace, jako jsou kryptografické klíče, ze zařízení analýzou jeho nezáměrného elektromagnetického (EM)"
---

SEMA je pasivní útok postranním kanálem, který extrahuje tajné informace z zařízení analýzou korelací mezi jeho zpracováním dat a nezáměrným elektromagnetickým zářením.

## Popis

Simple Electromagnetic Analysis (SEMA) je kryptografická technika útoku postranním kanálem, studovaná v pracovní skupině pro bezpečnost 3GPP (SA3). Na rozdíl od útoků založených na chybách nebo invazivního sondování je SEMA pasivní útok, při kterém protivník monitoruje elektromagnetické emise unikající z čipu (např. z univerzální integrovaného obvodu karty (UICC) hostujícího [USIM](/mobilnisite/slovnik/usim/)) během provádění kryptografických operací, jako je autentizace (pomocí algoritmu Milenage) nebo generování klíčů. Tyto emise jsou způsobeny variacemi v průtoku proudu a spínací aktivitě uvnitř polovodiče při zpracování dat. Klíčové je, že spotřeba energie a [EM](/mobilnisite/slovnik/em/) signatura tranzistorového hradla závisí na zpracovávaném datovém bitu (0 nebo 1). Umístěním citlivé EM sondy v blízkosti cílového zařízení (např. mobilního telefonu nebo čtečky čipových karet) může útočník zachytit stopu EM pole v čase.

Útok probíhá tak, že se získá mnoho EM stop, zatímco zařízení zpracovává známé nebo zvolené vstupy. Útočník následně provede statistickou analýzu, jako je diferenciální elektromagnetická analýza ([DEMA](/mobilnisite/slovnik/dema/)), aby koreloval specifické rysy v EM stopě (např. špičky, vzory) s mezilehlými hodnotami vypočítanými během kryptografického algoritmu. Například útočník může hypotetizovat část tajného klíče, vypočítat očekávaný výstup operace substitučního boxu (S-box) v [AES](/mobilnisite/slovnik/aes/) a ověřit korelaci mezi touto hypotetickou hodnotou a skutečně naměřenou EM amplitudou v přesném časovém vzorku. Silná korelace odhalí správnost odhadu klíče. Iterativní analýzou různých částí algoritmu lze extrahovat celý tajný klíč.

Zapojení 3GPP, dokumentované ve specifikacích jako TS 35.934, se zaměřuje na vyhodnocení náchylnosti platforem USIM/UICC k takovým útokům a na standardizaci testovacích metodik a protiopatření. Analýza zohledňuje celý signální řetězec: charakteristiky EM sondy, zesílení a digitalizaci signálu a techniky digitálního zpracování signálu používané k extrakci klíče. Protiopatření vyvinutá v reakci na hrozby SEMA zahrnují techniky na hardwarové úrovni, jako je přidání interních generátorů šumu, implementace algoritmů s konstantní vykonávací cestou, použití stínění proti úniku energie a EM záření a zahrnutí náhodných zpoždění do zpracování. Softwarová protiopatření zahrnují maskování citlivých dat náhodnými hodnotami během výpočtů, aby se přerušila korelace mezi emisemi a tajným klíčem.

## K čemu slouží

SEMA a související útoky postranním kanálem se objevily jako významná hrozba s rozšířením vestavěných kryptografických zařízení, jako jsou čipové karty a [USIM](/mobilnisite/slovnik/usim/), které jsou fyzicky přístupné útočníkovi (např. v ukradeném telefonu). Tradiční modely kryptografické bezpečnosti předpokládaly 'černou skříňku', kde útočník viděl pouze vstupy a výstupy, ale útoky postranním kanálem využívají úniků z fyzické implementace. Účelem studia SEMA v rámci 3GPP je proaktivně řešit tyto zranitelnosti v mobilním ekosystému dříve, než mohou být zneužity.

Vytvoření tohoto souboru prací bylo motivováno potřebou chránit dlouhodobá tajemství uložená na USIM, zejména klíč pro autentizaci účastníka (K), který je základem bezpečnosti pro přístup k mobilní síti. Pokud je K extrahován pomocí SEMA, mohl by útočník naklonovat identitu účastníka nebo vydávat se za síť. Předchozí bezpečnostní hodnocení často tyto fyzické útočné vektory přehlížela. Standardizací požadavků na analýzu a odolnost si 3GPP klade za cíl zvýšit laťku hardwarové bezpečnosti a zajistit, aby USIM a další bezpečnostní prvky nasazené v sítích 3G, 4G a 5G byly odolné nejen proti logickým útokům, ale také proti fyzickým útokům postranním kanálem. Tím se chrání jak soukromí účastníků, tak integrita sítě proti sofistikovaným protivníkům.

## Klíčové vlastnosti

- Pasivní, neinvazivní útok založený na měření elektromagnetických emisí
- Využívá datově závislé variace v odběru proudu a EM emisích čipu
- Používá statistickou analýzu (např. techniky diferenciální analýzy spotřeby/DPA) ke korelaci emisí s bity tajného klíče
- Cílí na kryptografické operace prováděné USIM/UICC a dalšími bezpečnostními prvky
- Řídí standardizaci testovacích metodik pro odolnost vůči útokům postranním kanálem
- Motivuje implementaci hardwarových a softwarových protiopatření v návrhu zabezpečených integrovaných obvodů

## Související pojmy

- [USIM – Universal Subscriber Identity Module](/mobilnisite/slovnik/usim/)
- [DPA – Differential Power Analysis](/mobilnisite/slovnik/dpa/)

## Definující specifikace

- **TR 35.934** (Rel-19) — Tuak algorithm set for 3GPP auth & key gen

---

📖 **Anglický originál a plná specifikace:** [SEMA na 3GPP Explorer](https://3gpp-explorer.com/glossary/sema/)
