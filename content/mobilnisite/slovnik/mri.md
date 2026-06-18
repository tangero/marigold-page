---
slug: "mri"
url: "/mobilnisite/slovnik/mri/"
type: "slovnik"
title: "MRI – Magnetic Resonance Imaging"
date: 2025-01-01
abbr: "MRI"
fullName: "Magnetic Resonance Imaging"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/mri/"
summary: "V rámci 3GPP se termín MRI (Magnetic Resonance Imaging) týká využití sítí 5G pro podporu vzdálených a mobilních systémů magnetické rezonance. Umožňuje vysokokapacitní, nízkolatenční a spolehlivý přeno"
---

MRI je využití sítí 5G pro podporu vzdálených a mobilních systémů magnetické rezonance (Magnetic Resonance Imaging) tím, že umožňuje vysokokapacitní přenos rozsáhlých dat lékařských zobrazovacích vyšetření s nízkou latencí.

## Popis

V rámci standardizačního rámce 3GPP je magnetická rezonance (MRI) studována a standardizována jako klíčová vertikální aplikace pro sítě 5G a novější, zejména v oblasti zdravotnictví a lékařských služeb. Zahrnuje využití vylepšených schopností systémů 5G – jako je rozšířené mobilní širokopásmové připojení (eMBB), ultra-spolehlivá komunikace s nízkou latencí ([URLLC](/mobilnisite/slovnik/urllc/)) a síťové segmenty (network slicing) – pro podporu provozu, řízení a správy dat přístrojů MRI. Systém MRI generuje extrémně rozsáhlé datové sady z 3D skenů, často v rozsahu od stovek megabajtů po několik gigabajtů na vyšetření. Přenos těchto dat téměř v reálném čase pro vzdálenou diagnózu, druhé stanovisko nebo centralizovanou analýzu vyžaduje síť s velmi vysokou propustností, konzistentní spolehlivostí a specifickými zárukami kvality služeb (QoS).

Z architektonického hlediska podpora MRI přes 5G zahrnuje integraci zařízení MRI jako specializovaného uživatelského zařízení (UE) nebo jako součásti nastavení pevného bezdrátového přístupu připojeného k síti 5G. Mezi klíčové síťové funkce patří User Plane Function ([UPF](/mobilnisite/slovnik/upf/)) pro vysokokapacitní přenos dat, Session Management Function ([SMF](/mobilnisite/slovnik/smf/)) pro vytváření vyhrazených [PDU](/mobilnisite/slovnik/pdu/) relací s příslušnými QoS toky a Policy Control Function ([PCF](/mobilnisite/slovnik/pcf/)) pro vynucování služebních politik lékařské třídy. Kritickým aspektem je využití síťových segmentů (network slicing) k vytvoření izolované, virtualizované instance sítě vyhrazené pro zdravotnické služby. Tento segment pro MRI by měl vyhrazené prostředky, přísné bezpečnostní politiky (v souladu s předpisy jako HIPAA nebo GDPR) a garantované výkonnostní parametry, jako je šířka pásma, latence a míra ztrátovosti paketů.

Při provozu, když je proveden sken MRI, jsou nezpracovaná nebo zpracovaná obrazová data paketizována a přenášena přes síť 5G. Pro interaktivní relace v reálném čase, například když vzdálený expert řídí průběh vyšetření, schopnosti URLLC v 5G zajišťují minimální latenci mezi pohybem a zobrazením, což umožňuje přesné dálkové ovládání. Schopnosti eMBB zvládají hromadný přenos dat dokončených snímků do nemocničního systému pro archivaci a komunikaci obrazových dat (PACS) nebo do cloudové analytické platformy. Systém 5G monitoruje metriky QoS relace v reálném čase a síťový segment může dynamicky upravovat prostředky nebo spouštět redundantní mechanismy, aby byla zachována požadovaná úroveň služeb, což je zásadní pro časově citlivou diagnostiku.

## K čemu slouží

Standardizace podpory MRI v 3GPP, zejména od Release 17, reaguje na rostoucí potřebu digitální transformace ve zdravotnictví a na omezení předchozích komunikačních technologií pro lékařské zobrazování. Tradiční metody sdílení dat MRI, jako fyzická média ([DVD](/mobilnisite/slovnik/dvd/)) nebo kabelové nemocniční sítě, jsou pomalé, nepohodlné a omezují potenciál telemedicíny, zejména v odlehlých nebo nedostatečně obsluhovaných oblastech nebo v nouzových situacích, jako jsou mobilní jednotky MRI při reakci na katastrofy. Sítě 4G/LTE často postrádají konzistentní vysokou kapacitu a ultra-spolehlivou nízkou latenci potřebnou pro přenos lékařských snímků vysoké věrnosti a dálkové ovládání zařízení v reálném čase.

Motivací pro její zařazení do standardů 3GPP je odemknout nové paradigmaty ve zdravotnictví: teleradiologii, kde specialisté mohou diagnostikovat pacienty odkudkoli; vzdálené chirurgické vedení pomocí MRI; a nasazování mobilních skenerů MRI v sanitkách nebo venkovských klinikách připojených přes 5G. Definováním požadavků a síťových architektur pro podporu MRI jako služby umožňuje 3GPP vývoj ekosystému – zajišťuje, že síťové vybavení 5G, modemy zařízení a zdravotnické [IT](/mobilnisite/slovnik/it/) systémy mohou spolupracovat a poskytovat bezproblémovou, bezpečnou a předpisům vyhovující službu. To transformuje MRI z izolovaného nástroje vázaného na konkrétní místo na připojenou komponentu distribuovaného zdravotnického systému, což zlepšuje dostupnost, rychlost diagnózy a umožňuje pokročilé aplikace, jako je analýza snímků v reálném čase založená na [AI](/mobilnisite/slovnik/ai/) v cloudu.

## Klíčové vlastnosti

- Podpora vysokokapacitního přenosu dat rozsáhlých datových sad MRI (eMBB)
- Ultra-spolehlivé nízkolatenční připojení pro dálkové ovládání a vedení v reálném čase (URLLC)
- Vyhrazené síťové segmenty (network slicing) pro poskytnutí izolovaných, garantovaných prostředků pro lékařský provoz
- Vylepšené mechanismy zabezpečení a ochrany soukromí pro soulad s předpisy ve zdravotnictví
- Integrace s lékařskými systémy, jako jsou PACS a nemocniční informační systémy
- Podpora mobilních a přenosných jednotek MRI prostřednictvím bezdrátového připojení 5G

## Související pojmy

- [URLLC – Ultra Reliable Low Latency Communication](/mobilnisite/slovnik/urllc/)
- [QoS – Quality of Service](/mobilnisite/slovnik/qos/)

## Definující specifikace

- **TR 22.826** (Rel-17) — Study on 5G for Critical Medical Applications
- **TS 29.561** (Rel-19) — 5G Interworking with External Data Networks
- **TS 38.212** (Rel-19) — NR Multiplexing and Channel Coding

---

📖 **Anglický originál a plná specifikace:** [MRI na 3GPP Explorer](https://3gpp-explorer.com/glossary/mri/)
