---
slug: "frmcs"
url: "/mobilnisite/slovnik/frmcs/"
type: "slovnik"
title: "FRMCS – Future Railway Mobile Communication System"
date: 2026-01-01
abbr: "FRMCS"
fullName: "Future Railway Mobile Communication System"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/frmcs/"
summary: "Nástupce systému GSM-R standardizovaný organizací 3GPP, který poskytuje služby kritické z hlediska spolehlivosti (mission-critical) pro hlas a data v železničním provozu. Využívá technologie 4G/5G k u"
---

FRMCS je nástupce systému GSM-R standardizovaný organizací 3GPP, který poskytuje služby kritické z hlediska spolehlivosti (mission-critical) pro hlas a data v železničním provozu využívající technologie 4G/5G.

## Popis

Future Railway Mobile Communication System (FRMCS) je komplexní soubor specifikací 3GPP definující novou generaci komunikačního systému pro železniční operátory. Je navržen jako přímá evoluce a náhrada za zastarávající standard [GSM-R](/mobilnisite/slovnik/gsm-r/) (Global System for Mobile Communications – Railway). Z architektonického hlediska není FRMCS samostatnou sítí, ale servisním profilem a aplikačním rámcem, který jako podpůrnou přenosovou síť využívá 3GPP síť 4G LTE a především 5G System (5GS). Mezi základní systémové komponenty patří FRMCS Equipment, což je 3GPP User Equipment (UE) – například modem nebo palubní jednotka – s vyhrazeným FRMCS Application klientem, a odpovídající FRMCS Application Server v síti.

FRMCS Application poskytuje konkrétní služby pro železniční provoz, jako jsou Mission-Critical Push-To-Talk ([MCPTT](/mobilnisite/slovnik/mcptt/)), Mission-Critical Data (MCData) a Mission-Critical Video ([MCVideo](/mobilnisite/slovnik/mcvideo/)), standardizované 3GPP pro veřejnou bezpečnost a nyní přizpůsobené potřebám železničního provozu. Tyto aplikace běží nad 3GPP IP Multimedia Subsystem (IMS) pro hlasové a multimediální služby a využívají schopnosti 5G core sítě, jako je Network Slicing, Ultra-Reliable Low-Latency Communication (URLLC) a enhanced Mobile Broadband (eMBB). Klíčovým architektonickým aspektem je podpora duální konektivity nebo spolupráce se staršími sítěmi GSM-R během přechodového období, což umožňuje vlakům vybaveným kombinovanými FRMCS/GSM-R zařízeními zachovat nepřetržitý provoz.

Princip fungování spočívá v připojení FRMCS UE k 5G síti, případně s využitím vyhrazeného síťového řezu (network slice) nakonfigurovaného pro železniční provozní služby se zaručenou kvalitou služeb (Quality of Service, QoS). Pro hlasové hovory se UE registruje v IMS core. Když strojvedoucí zahájí skupinový hovor (například k dispečerovi), FRMCS Application použije protokoly MCPTT přes IMS k navázání relace s nízkou latencí a vysokou prioritou. Pro kritická data, jako je signalizace evropského vlakového zabezpečovače (European Train Control System, ETCS), síť poskytuje vyhrazený QoS tok s charakteristikami URLLC, což zajišťuje splnění cílů pro zpoždění paketů a spolehlivost i při vysokých rychlostech. Systém také definuje specifické funkce zaměřené na železnici, jako je funkční číslování, adresování závislé na poloze (hovory na konkrétní úsek trati) a provoz v posunovacím režimu.

## K čemu slouží

FRMCS byl vytvořen, aby řešil technologické zastarání a omezení systému [GSM-R](/mobilnisite/slovnik/gsm-r/), který je založen na 2G GSM technologii. GSM-R, ačkoli je vysoce spolehlivý pro hlas a základní data, postrádá potřebnou šířku pásma, výkon z hlediska latence a flexibilitu nutnou pro moderní digitální železniční aplikace. Mezi omezení GSM-R patří nedostatečná kapacita pro video dohled, neschopnost podporovat vysokorychlostní výměnu dat pro prediktivní údržbu a informační systémy pro cestující a plánované ukončení podpory jeho podkladové 2G technologie mnoha síťovými operátory a výrobci zařízení.

Hlavní motivací pro FRMCS je zajistit budoucnost železničních komunikací prostřednictvím využití globálního rozsahu, kontinuální inovace a ekonomických výhod ekosystému 3GPP, zejména 5G. 5G poskytuje potřebné technické základy: network slicing pro vytváření logicky izolovaných, vyhrazených sítí pro železniční provoz na sdílené fyzické infrastruktuře; URLLC pro bezpečnostně kritickou řídicí signalizaci; a podporu massive IoT pro rozsáhlé nasazení senzorů. Tento přechod umožňuje nové provozní modely, jako je signalizace s pohyblivým blokem (vyžadující nepřetržitou komunikaci vlak–země s vysokou integritou), automatizovaný provoz vlaku ([ATO](/mobilnisite/slovnik/ato/)) a přenosy videa v reálném čase z vlaků a podél trati pro bezpečnostní a situační povědomí.

FRMCS dále usiluje o zajištění interoperability přes národní hranice v rámci Evropy i globálně, čímž snižuje náklady a složitost pro železniční operátory a výrobce kolejových vozidel. Standardizací v rámci 3GPP se vyhýbá uzamčení u jednoho dodavatele a podporuje konkurenční trh s vybavením. Jeho vytvoření bylo řízeno Mezinárodní železniční unií (UIC) v úzké spolupráci s 3GPP, což zajišťuje, že standardy splňují specifické, přísné bezpečnostní a provozní požadavky železničního průmyslu, které jsou stejně kritické jako požadavky na sítě pro veřejnou bezpečnost.

## Klíčové vlastnosti

- Standardizovaný nástupce GSM-R založený na architektuře 3GPP 5G System
- Podporuje služby kritické z hlediska spolehlivosti (MCPTT, MCData, MCVideo) přes IMS
- Využívá 5G Network Slicing pro vyhrazenou, garantovanou izolaci železničních služeb
- Poskytuje Ultra-Reliable Low-Latency Communication (URLLC) pro bezpečnostně kritická data
- Definuje funkce specifické pro železnici, jako je funkční číslování a adresování založené na poloze
- Umožňuje spolupráci a migraci ze starších sítí GSM-R

## Související pojmy

- [GSM-R – Global System for Mobile Communications – Rail(way)](/mobilnisite/slovnik/gsm-r/)

## Definující specifikace

- **TR 22.889** (Rel-17) — FRMCS Study; Stage 1
- **TR 22.890** (Rel-19) — Study on Railway Smart Station Services
- **TR 22.989** (Rel-20) — FRMCS Analysis and Requirements
- **TS 23.790** (Rel-15) — FRMCS Gap Analysis and Architecture Enhancements
- **TR 37.829** (Rel-18) — Technical Report
- **TS 38.104** (Rel-19) — NR Base Station RF Requirements
- **TS 38.141** (Rel-19) — NR Base Station RF Conformance Testing Part 1

---

📖 **Anglický originál a plná specifikace:** [FRMCS na 3GPP Explorer](https://3gpp-explorer.com/glossary/frmcs/)
