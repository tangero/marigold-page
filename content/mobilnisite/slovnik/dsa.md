---
slug: "dsa"
url: "/mobilnisite/slovnik/dsa/"
type: "slovnik"
title: "DSA – Digital Signature Algorithm"
date: 2025-01-01
abbr: "DSA"
fullName: "Digital Signature Algorithm"
category: "Security"
segment: "Security"
canonical: "https://3gpp-explorer.com/glossary/dsa/"
summary: "Kryptografický algoritmus s veřejným klíčem standardizovaný organizací NIST (FIPS 186) pro generování a ověřování digitálních podpisů. V rámci 3GPP se používá v bezpečnostních specifikacích pro ochran"
---

DSA je kryptografický algoritmus s veřejným klíčem standardizovaný organizací NIST a používaný v bezpečnostních specifikacích 3GPP pro ochranu integrity, autentizaci a nepopiratelnost.

## Popis

Digital Signature Algorithm (DSA) je standardizovaný kryptografický algoritmus s veřejným klíčem pro vytváření a ověřování digitálních podpisů. Je definován ve standardu americké vlády Federal Information Processing Standard ([FIPS](/mobilnisite/slovnik/fips/)) 186. V ekosystému 3GPP je DSA odkazován a využíván v různých bezpečnostních specifikacích k zajištění služeb integrity dat, autentizace a nepopiratelnosti. Algoritmus je založen na matematických principech problému diskrétního logaritmu v podskupině prvočíselného řádu v konečném poli. Digitální podpis dokazuje, že zprávu vytvořil známý odesílatel (autentizace), že odesílatel nemůže popřít její odeslání (nepopiratelnost) a že zpráva nebyla během přenosu změněna (integrita).

Technické fungování DSA zahrnuje pár klíčů: soukromý klíč známý pouze podepisující straně a veřejný klíč, který je široce distribuován. Proces podepisování využívá soukromý klíč a hash zprávy k vytvoření dvou celých čísel, r a s, které tvoří podpis. Proces ověření využívá veřejný klíč podepisující strany, původní zprávu a přijatý podpis (r, s) k výpočtu hodnoty, která se v případě platného podpisu musí shodovat s komponentou r. Bezpečnost DSA závisí na výpočetní náročnosti řešení problému diskrétního logaritmu. Ve specifikacích 3GPP je použití DSA často specifikováno spolu s dalšími algoritmy, jako je [RSA](/mobilnisite/slovnik/rsa/) nebo [ECDSA](/mobilnisite/slovnik/ecdsa/), s konkrétními délkami klíčů a sadami parametrů (např. L=2048, N=256 podle FIPS 186-4) požadovanými pro různé úrovně zabezpečení.

V architektuře 3GPP lze DSA použít v několika kontextech. Je specifikován pro použití v architektuře Authentication and Key Management for Applications ([AKMA](/mobilnisite/slovnik/akma/)) k umožnění aplikacím využívat přihlašovací údaje 3GPP. Používá se také v bezpečnostních specifikacích pro rozhraní správy sítě (např. rozhraní Itf-N) k ochraně dat správy. Dále může být DSA nasazen v kontextu zákonného odposlechu (Lawful Interception, [LI](/mobilnisite/slovnik/li/)) a specifikace Security Assurance Specification ([SCAS](/mobilnisite/slovnik/scas/)) pro zabezpečení síťových funkcí. Jeho úlohou je poskytovat ověřitelnou a standardizovanou metodu pro zajištění důvěryhodnosti kritické signalizace, příkazů správy nebo autentizačních tokenů na úrovni aplikací v rámci 5G jádra a dalších částí sítě.

## K čemu slouží

DSA byl vyvinut a standardizován organizací [NIST](/mobilnisite/slovnik/nist/) za účelem poskytnutí bezpečného, efektivního a vládou schváleného algoritmu pro digitální podpisy, který nabízí alternativu k algoritmu [RSA](/mobilnisite/slovnik/rsa/). Jeho účelem ve specifikacích 3GPP je poskytnout kryptograficky silný, standardizovaný mechanismus pro dosažení autentizace, integrity a nepopiratelnosti v různých částech telekomunikačního systému. Tím řeší základní bezpečnostní problém ověření původu a integrity dat v potenciálně nedůvěryhodném síťovém prostředí, zejména když se služby stávají více softwarovými a vystavenými širší škále hrozeb.

Motivace pro zahrnutí DSA do standardů 3GPP vychází z potřeby agility algoritmů a souladu s různými národními a mezinárodními bezpečnostními předpisy. Zatímco systémy 3GPP historicky používaly symetrickou kryptografii (např. MILENAGE pro autentizaci) a další asymetrické algoritmy, DSA poskytuje konkrétní, důkladně prověřenou možnost pro případy užití vyžadující formální digitální podpisy. Řeší omezení čistě symetrických systémů, které nemohou poskytnout nepopiratelnost, a nabízí standardizovanou alternativu k RSA, která je založena na jiném matematickém problému (faktorizace celých čísel). Jeho zařazení, zejména od vydání Release 8, odráží rozšiřující se rozsah systémů 3GPP pro podporu obecnější bezpečnosti aplikací (jako je AKMA) a zabezpečených rovin správy, kde jsou standardizované algoritmy podpisů s veřejným klíčem nezbytností.

## Klíčové vlastnosti

- Kryptografie s veřejným klíčem založená na problému diskrétního logaritmu
- Generuje pár podpisu (r, s) z hashe zprávy a soukromého klíče
- Poskytuje služby integrity dat, autentizace a nepopiratelnosti
- Standardizován v NIST FIPS 186 s definovanými sadami parametrů (např. 2048bitové klíče)
- Používán v 3GPP pro autentizaci AKMA a zabezpečení rozhraní pro správu
- Nabízí standardizovanou alternativu podpisového algoritmu k RSA a ECDSA

## Související pojmy

- [AKMA – Authentication and Key Management for Applications](/mobilnisite/slovnik/akma/)
- [ECDSA – Elliptic Curve Digital Signature Algorithm](/mobilnisite/slovnik/ecdsa/)

## Definující specifikace

- **TS 32.808** (Rel-8) — Common User Profile Storage Framework
- **TS 33.303** (Rel-19) — ProSe Security Specification for EPS
- **TS 33.885** (Rel-14) — Security Study for V2X Services
- **TR 33.969** (Rel-19) — Security for Public Warning System (PWS)

---

📖 **Anglický originál a plná specifikace:** [DSA na 3GPP Explorer](https://3gpp-explorer.com/glossary/dsa/)
