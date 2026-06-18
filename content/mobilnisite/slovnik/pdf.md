---
slug: "pdf"
url: "/mobilnisite/slovnik/pdf/"
type: "slovnik"
title: "PDF – Probability Distribution Function"
date: 2025-01-01
abbr: "PDF"
fullName: "Probability Distribution Function"
category: "Other"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/pdf/"
summary: "Matematická funkce používaná v analýze a modelování výkonnosti systémů 3GPP, která popisuje pravděpodobnost, že náhodná veličina nabude dané hodnoty nebo se bude nacházet v určitém rozsahu. Je základn"
---

PDF je matematická funkce používaná v analýze výkonnosti 3GPP k popisu pravděpodobnosti, že náhodná veličina nabude konkrétní hodnoty nebo se bude nacházet v určitém rozsahu; charakterizuje provoz, podmínky rádiového kanálu, interferenci a chování front.

## Popis

V kontextu norem 3GPP není Funkce hustoty pravděpodobnosti (PDF) síťovou entitou ani protokolem, ale základním statistickým nástrojem hojně používaným v technických specifikacích, požadavcích na výkon a hodnotících metodikách. Poskytuje úplný popis pravděpodobnostní struktury náhodné veličiny. Pro spojitou náhodnou veličinu X (např. propustnost uživatele, zpoždění paketu, poměr signálu k interferenci) PDF, označovaná jako f_X(x), definuje pravděpodobnost, že X se nachází v nekonečně malém intervalu kolem hodnoty x. Pravděpodobnost, že X leží mezi dvěma hodnotami a a b, se zjistí integrací PDF přes tento interval.

Specifikace 3GPP používají PDF (a jejich kumulativní protějšek, Kumulativní distribuční funkci - [CDF](/mobilnisite/slovnik/cdf/)) k definici systémových modelů a metrik výkonnosti. Například provozní modely pro prohlížení webu, streamování videa nebo aplikace IoT jsou definovány pomocí PDF k popisu intervalů příchodů paketů (např. exponenciální rozdělení) a velikostí paketů (např. zkrácené Paretovo rozdělení). Modely rádiového kanálu pro vyhodnocování [MIMO](/mobilnisite/slovnik/mimo/) používají PDF ke charakterizaci útlumu v důsledku vícecestného šíření (např. Rayleighovo, Ricovo rozdělení). Požadavky na výkonnost jsou často uváděny ve formě CDF/PDF; například požadavek může stanovit, že „latence uživatelské roviny musí být menší než 4 ms pro 95 % paketů“, což je odvozeno z PDF latence.

Její role je zásadní v inženýrském procesu. Při návrhu algoritmů řízení rádiových zdrojů, politik řízení přístupu nebo mechanismů síťového řezání používají inženýři stochastické modely založené na PDF k simulaci chování sítě za realistických, proměnných podmínek. Klíčové parametry jako střední hodnota, rozptyl a momenty vyšších řádů odvozené z PDF slouží ke kvantifikaci výkonnosti, porovnání systémových návrhů a zajištění, že standardizované technologie splňují cíle kvality služeb v reálném světě. Volba vhodného PDF (např. Poissonovo pro příchody hovorů, Gaussovo pro agregovanou interferenci, Beta pro soběpodobný provoz) je klíčová pro přesnou a smysluplnou analýzu systému.

## K čemu slouží

Použití Funkcí hustoty pravděpodobnosti v normách 3GPP je motivováno inherentní náhodností a stochastickou povahou systémů mobilní komunikace. Na rozdíl od deterministických modelů zažívají reálné sítě nepředvídatelné chování uživatelů, časově proměnné rádiové kanály a přerušovaný datový provoz. Pro návrh robustních systémů, které si za těchto náhodných podmínek vedou dobře, jsou kvantitativní statistické modely nezbytné.

PDF řeší problém abstrakce a formální specifikace této náhodnosti standardizovaným, matematicky rigorózním způsobem. Umožňují různým výrobcům zařízení, síťovým operátorům a výzkumníkům používat společnou sadu statistických předpokladů při simulaci, testování a dimenzování síťových komponent. To zajišťuje férové porovnávání výkonnosti a interoperabilitu. Před rozšířeným používáním takových stochastických modelů ve standardech byl výkon systému často popisován příliš zjednodušeně nebo v pojmech nejhoršího případu, což mohlo vést k neefektivnímu předimenzování nebo naopak systémům, které selhávaly při realistickém zatížení. Přijetí provozních a kanálových modelů založených na PDF, zejména od 3G generace, umožnilo návrh sítí optimalizovaných pro statistické záruky výkonnosti (např. „pokrytí na 95 %“), což je nákladově efektivní a v souladu se skutečnou uživatelskou zkušeností.

## Klíčové vlastnosti

- Popisuje relativní pravděpodobnost výsledků spojité náhodné veličiny
- Základní pro definici standardizovaných provozních modelů (např. FTP, HTTP, VoIP)
- Používá se ke charakterizaci statistik útlumu rádiového kanálu (např. Rayleighovo, Nakagamiho rozdělení)
- Základ pro výpočet metrik výkonnosti jako pravděpodobnost výpadku nebo percentilní hodnoty
- Nedílná součást metodik simulace a vyhodnocování systémů v 3GPP
- Propojena s Kumulativní distribuční funkcí (CDF) pro specifikaci požadavků

## Související pojmy

- [CDF – Cumulative Distribution Function](/mobilnisite/slovnik/cdf/)

## Definující specifikace

- **TR 21.801** (Rel-19) — 3GPP Specification Drafting Rules
- **TR 22.945** (Rel-4) — Fax Services Guidance for GSM/UMTS
- **TS 23.203** (Rel-19) — Policy and charging control architecture
- **TS 23.207** (Rel-19) — End-to-End QoS Framework for GPRS
- **TS 23.228** (Rel-19) — IMS Stage-2 Service Description
- **TS 23.417** (Rel-7) — IMS Core Component for NGN Architecture
- **TS 23.517** (Rel-8) — IMS Core Component for NGN Architecture
- **TS 23.802** (Rel-7) — Enhanced End-to-End QoS Architecture
- **TS 23.803** (Rel-7) — PCC Architecture Harmonization Study
- **TR 23.976** (Rel-19) — Push Service Requirements Analysis
- **TS 24.228** (Rel-5) — IP Multimedia Call Control Signaling Flows
- **TS 24.229** (Rel-19) — IMS call control protocol based on SIP and SDP
- **TS 26.804** (Rel-19) — 5G Media Streaming Extensions Study
- **TS 29.214** (Rel-19) — Policy and Charging Control over Rx
- **TS 32.101** (Rel-19) — Management principles and high-level requirements
- … a dalších 1 specifikací

---

📖 **Anglický originál a plná specifikace:** [PDF na 3GPP Explorer](https://3gpp-explorer.com/glossary/pdf/)
