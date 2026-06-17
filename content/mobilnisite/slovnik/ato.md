---
slug: "ato"
url: "/mobilnisite/slovnik/ato/"
type: "slovnik"
title: "ATO – Automatic Train Operation"
date: 2026-01-01
abbr: "ATO"
fullName: "Automatic Train Operation"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/ato/"
summary: "Automatic Train Operation (ATO) je služba 3GPP umožňující bezobslužný provoz vlaků po sítích 5G. Poskytuje přesné určování polohy vlaku, řízení v reálném čase a komunikaci kritickou z hlediska bezpečn"
---

ATO je služba 3GPP umožňující bezobslužný provoz vlaků po sítích 5G tím, že poskytuje přesné určování polohy, řízení v reálném čase a komunikaci kritickou z hlediska bezpečnosti pro autonomní železniční systémy.

## Popis

Automatic Train Operation (ATO) je komplexní specifikace služby 3GPP, která umožňuje plně automatizované řízení a provoz vlaků s využitím schopností sítí 5G. Architektura integruje železniční operační technologie s mobilními sítěmi 5G prostřednictvím standardizovaných rozhraní a služebních prvků. Mezi klíčové komponenty patří ATO server, který spravuje pohyby vlaků a jízdní řády; palubní jednotka ATO instalovaná ve vlacích; a infrastruktura sítě 5G poskytující spolehlivé spojení s nízkou latencí. Systém funguje prostřednictvím nepřetržité výměny řídicích zpráv mezi ATO serverem a vlaky, přičemž síť 5G zajišťuje deterministický komunikační výkon vyžadovaný pro operace kritické z hlediska bezpečnosti.

Technická implementace využívá schopnosti 5G pro ultra-spolehlivou komunikaci s nízkou latencí (URLLC) k dosažení koncové latence pod 10 milisekund a spolehlivosti přesahující 99,999 %. Služba ATO využívá přesné technologie určování polohy včetně augmentace [GNSS](/mobilnisite/slovnik/gnss/) a síťového určování polohy k dosažení přesnosti na úrovni centimetrů. Komunikace mezi ATO serverem a vlaky se řídí standardizovanými protokoly definovanými ve specifikacích 3GPP, což zajišťuje interoperabilitu mezi zařízeními různých výrobců. Systém zahrnuje více mechanismů redundance včetně duální konektivity, síťového řezání a záložních komunikačních cest pro udržení provozu při výpadcích sítě.

Role ATO v síti přesahuje základní konektivitu a zahrnuje orchestraci služeb, správu kvality služeb a integraci se železničními zabezpečovacími systémy. Síť 5G přiděluje pro provoz ATO vyhrazené síťové řezy se zaručenými parametry šířky pásma, latence a spolehlivosti. Tyto řezy jsou izolovány od ostatního síťového provozu, aby se zabránilo rušení operací kritických z hlediska bezpečnosti. Systém se také integruje se stávajícími železničními systémy, jako je European Train Control System (ETCS) a Communication-Based Train Control (CBTC), čímž poskytuje zpětnou kompatibilitu a zároveň umožňuje pokročilé funkce automatizace.

Mezi klíčové technické aspekty patří definice smluv o úrovni služeb (SLA) pro komunikaci ATO, správa mobility pro vysokorychlostní vlaky (až 500 km/h) a optimalizace předávání mezi buňkami 5G. Architektura podporuje jak centralizované řídicí modely, kde většina inteligence sídlí v ATO serveru, tak distribuované modely se zvýšenými schopnostmi palubního zpracování. Bezpečnostní mechanismy zahrnují vzájemnou autentizaci mezi vlaky a ATO serverem, šifrování řídicích zpráv a ochranu integrity proti neoprávněným úpravám. Systém také zahrnuje monitorovací a diagnostické schopnosti pro detekci a reakci na komunikační anomálie v reálném čase.

## K čemu slouží

ATO bylo vytvořeno, aby řešilo rostoucí potřebu automatizovaných železničních systémů, které mohou zvýšit kapacitu, zlepšit bezpečnost a snížit provozní náklady. Tradiční železniční provoz se silně spoléhá na lidské strojvedoucí a starší zabezpečovací systémy, které omezují frekvenci a efektivitu vlaků. Díky umožnění bezobslužného provozu prostřednictvím konektivity 5G umožňuje ATO přesnější řízení vlaků, zkrácení intervalů mezi vlaky a optimalizovanou spotřebu energie. Technologie řeší omezení předchozích automatizovaných vlakových systémů, které často vyžadovaly rozsáhlou vyhrazenou infrastrukturu a postrádaly flexibilitu celulárních sítí.

Historický kontext vývoje ATO zahrnuje rostoucí urbanizaci a potřebu efektivnějších systémů veřejné dopravy. Předchozí přístupy k automatizaci vlaků typicky využívaly proprietární komunikační systémy s omezenou šířkou pásma a škálovatelností. Standardizace ATO v rámci 3GPP umožňuje interoperabilitu mezi různými železničními operátory a výrobci zařízení, čímž snižuje náklady a složitost nasazení. Technologie také řeší bezpečnostní požadavky prostřednictvím standardizovaných záruk spolehlivosti a latence, které bylo obtížné dosáhnout s předchozími generacemi celulárních sítí.

Další klíčovou motivací byla konvergence operačních technologií ([OT](/mobilnisite/slovnik/ot/)) a informačních technologií ([IT](/mobilnisite/slovnik/it/)) v dopravních systémech. ATO využívá schopnost 5G řezat síť k vytvoření virtuálních vyhrazených sítí pro železniční provoz, přičemž sdílí fyzickou infrastrukturu s dalšími službami. Tento přístup snižuje kapitálové výdaje ve srovnání s výstavbou samostatných komunikačních sítí pro železnice. Technologie také umožňuje nové provozní modely, jako je virtuální spojování, kdy mohou vlaky operovat v těsně rozestavených soupravách, což významně zvyšuje kapacitu trati bez nutnosti rozšiřování fyzické infrastruktury.

## Klíčové vlastnosti

- Ultra-spolehlivá komunikace s nízkou latencí (URLLC) s koncovou latencí <10 ms
- Přesné určování polohy na úrovni centimetrů s využitím GNSS a síťových metod
- Síťové řezání pro izolovanou, zaručenou kvalitu služeb
- Podpora vysokorychlostní mobility až do 500 km/h
- Integrace se stávajícími železničními zabezpečovacími systémy (ETCS, CBTC)
- Redundantní komunikační cesty a mechanismy převzetí služeb při selhání

## Související pojmy

- [MEC – Multi-Access Edge Computing](/mobilnisite/slovnik/mec/)

## Definující specifikace

- **TR 22.889** (Rel-17) — FRMCS Study; Stage 1
- **TR 22.989** (Rel-20) — FRMCS Analysis and Requirements

---

📖 **Anglický originál a plná specifikace:** [ATO na 3GPP Explorer](https://3gpp-explorer.com/glossary/ato/)
