---
slug: "phr"
url: "/mobilnisite/slovnik/phr/"
type: "slovnik"
title: "PHR – Power Headroom Reporting"
date: 2025-01-01
abbr: "PHR"
fullName: "Power Headroom Reporting"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/phr/"
summary: "Mechanismus měření a hlášení ze strany UE v LTE a NR, který informuje základnovou stanici (eNodeB/gNB) o rozdílu mezi maximálním vysílacím výkonem UE a jejím aktuálně využívaným výkonem. Tyto informac"
---

PHR (Power Headroom Reporting) je mechanismus hlášení ze strany UE, který informuje základnovou stanici o rozdílu mezi jejím maximálním a aktuálně využívaným výkonem pro vysílání, což umožňuje efektivní řízení výkonu a plánování v uplinku.

## Popis

Power Headroom Reporting (PHR) je základní procedura hlášení a schopnost UE definovaná ve specifikacích 3GPP pro LTE (od Release 8) a NR (od Release 15). Jedná se o řídicí prvek vrstvy [MAC](/mobilnisite/slovnik/mac/) (Medium Access Control), kde uživatelské zařízení (UE) periodicky nebo na základě události informuje obsluhující základnovou stanici (eNodeB v LTE, gNB v NR) o své dostupné rezervě vysílacího výkonu, známé jako power headroom. Tato rezerva se vypočítá jako rozdíl mezi maximálním nakonfigurovaným nebo jmenovitým vysílacím výkonem UE (P_CMAX) a odhadovaným výkonem potřebným pro její aktuální uplinkový přenos na konkrétní komponentní nosné nebo skupině buněk. Tato zpráva poskytuje síti zásadní přehled o tom, zda je UE limitována výkonem.

Z architektonického hlediska je PHR generováno vrstvou MAC UE na základě měření a konfigurací fyzické vrstvy. Zpráva je přenášena jako MAC Control Element (MAC [CE](/mobilnisite/slovnik/ce/)) na sdíleném kanálu v uplinku ([PUSCH](/mobilnisite/slovnik/pusch/) v LTE, PUSCH nebo [PUCCH](/mobilnisite/slovnik/pucch/) v NR). Existují různé typy PHR hlášení. V LTE se Type 1 PHR počítá pro přenosy PUSCH, zatímco Type 2 zahrnuje jak PUSCH, tak PUCCH (pokud je nakonfigurován). V NR jsou hlášení kategorizována pro konkrétní skupiny buněk (např. Primary Cell Group, Secondary Cell Group) a mohou zahrnovat rezervu výkonu pro PUSCH i PUCCH, stejně jako informace o potřebném maximálním snížení výkonu ([MPR](/mobilnisite/slovnik/mpr/)) z důvodu modulace vyššího řádu nebo místních předpisů [SAR](/mobilnisite/slovnik/sar/).

Princip fungování: UE průběžně odhaduje svůj potřebný vysílací výkon pro přidělené zdroje na základě příkazů pro řízení výkonu s otevřenou a uzavřenou smyčkou od sítě. Když je splněna podmínka pro spuštění PHR – například výrazná změna útlumu na trase, vypršení periodického časovače nebo změna konfigurace parametrů řízení výkonu – UE sestaví PHR MAC CE. Tento CE obsahuje jedno nebo více polí pro rezervu výkonu (typicky v dB) pro každou aktivní obsluhovanou buňku. Plánovač sítě tyto informace využívá k určení, zda je UE limitována výkonem. Pokud je hlášená rezerva nízká nebo záporná (což znamená, že UE již pracuje na nebo nad svým maximálním výkonem), může plánovač přidělit méně bloků zdrojů ([RB](/mobilnisite/slovnik/rb/)) nebo použít robustnější schéma modulace a kódování ([MCS](/mobilnisite/slovnik/mcs/)), aby zajistil spolehlivý přenos. Naopak velká kladná rezerva naznačuje, že UE by mohla podporovat více RB nebo MCS vyššího řádu, což plánovači umožňuje zvýšit propustnost v uplinku.

## K čemu slouží

PHR bylo zavedeno, aby vyřešilo kritický problém efektivního plánování zdrojů v uplinku v přítomnosti proměnných výkonových omezení UE. V LTE a NR má řízení výkonu v uplinku za cíl zajistit, aby signály byly přijímány s dostatečnou kvalitou, a zároveň minimalizovat interference. Každé UE má však konečný maximální vysílací výkon. Bez znalosti rezervy výkonu UE by základnová stanice mohla naplánovat příliš mnoho bloků zdrojů nebo příliš vysoké MCS, což by způsobilo, že UE dosáhne svého výkonového stropu (saturace výkonu). To vede ke zhoršené kvalitě signálu, neúspěšným přenosům a plýtvání rádiovými zdroji. PHR poskytuje síti potřebný přehled, aby mohla činit inteligentní rozhodnutí o plánování, která se této situaci vyhnou.

Historicky měly dřívější buněčné systémy méně sofistikované plánování v uplinku a často pracovaly s kontinuálním přenosem nebo jednoduššími smyčkami řízení výkonu. Nástup uplinku SC-FDMA (Single-Carrier FDMA) v LTE, který vyžaduje souvislou alokaci bloků zdrojů, učinil vztah mezi přidělenou šířkou pásma a potřebným vysílacím výkonem přímějším a kritičtějším. Vytvoření PHR v Release 8 bylo motivováno potřebou efektivně podporovat adaptivní alokaci šířky pásma a adaptaci spojení, zejména pro UE na okraji buňky, u kterých je nejpravděpodobnější, že budou limitována výkonem. Řešilo to omezení sítě, která měla pouze odhad útlumu na trase UE, aniž by znala skutečnou rezervu výkonového zesilovače UE nebo jakákoli interní snížení výkonu.

Tento mechanismus je zásadní pro optimalizaci systémové kapacity, spravedlnosti mezi uživateli a životnosti baterie. Tím, že PHR předchází saturaci výkonu, pomáhá udržovat spolehlivost řídicího kanálu v uplinku (PUCCH) a výkon datového kanálu (PUSCH). Umožňuje síti vyvážit alokaci zdrojů mezi uživatele v centru buňky a na jejím okraji, čímž zlepšuje celkové pokrytí. V NR, s širšími šířkami pásma, agregací nosných a složitějšími scénáři sdílení výkonu (např. mezi více panely nebo simultánními přenosy PUSCH/PUCCH), se PHR vyvinulo tak, aby poskytovalo ještě podrobnější informace, což gNB umožňuje spravovat uplinkové přenosy v komplexnějším prostředí rádiových zdrojů.

## Klíčové vlastnosti

- Hlásí rozdíl mezi maximálním a aktuálně využívaným vysílacím výkonem UE
- Spouští se událostmi, jako je změna útlumu na trase, vypršení časovače nebo změna konfigurace
- Přenáší se jako MAC Control Element (MAC CE) v uplinku
- Podporuje více typů (např. Type 1/2 v LTE) pro PUSCH a PUCCH
- Poskytuje informace o rezervě výkonu na jednotlivé nosné nebo skupiny buněk při CA
- Zahrnuje virtuální PHR, když nedochází k žádnému skutečnému přenosu

## Související pojmy

- [PUSCH – Physical Uplink Shared Channel](/mobilnisite/slovnik/pusch/)
- [PUCCH – Physical Uplink Control Channel](/mobilnisite/slovnik/pucch/)

## Definující specifikace

- **TS 36.306** (Rel-19) — E-UTRA UE Radio Access Capability Parameters
- **TS 36.321** (Rel-19) — E-UTRA MAC Protocol Specification
- **TS 38.321** (Rel-19) — NR MAC Protocol Specification

---

📖 **Anglický originál a plná specifikace:** [PHR na 3GPP Explorer](https://3gpp-explorer.com/glossary/phr/)
