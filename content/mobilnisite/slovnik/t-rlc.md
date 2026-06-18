---
slug: "t-rlc"
url: "/mobilnisite/slovnik/t-rlc/"
type: "slovnik"
title: "T-RLC – RLC Transparent Mode"
date: 2020-01-01
abbr: "T-RLC"
fullName: "RLC Transparent Mode"
category: "Protocol"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/t-rlc/"
summary: "Provozní režim řízení rádiového spoje (RLC) v 3GPP UMTS a LTE, ve kterém podsložka RLC neprovádí segmentaci, konkatenaci ani opravu chyb. Data jednoduše transparentně propouští. Používá se pro služby"
---

T-RLC je transparentní režim řízení rádiového spoje (Radio Link Control Transparent Mode) v 3GPP UMTS a LTE, ve kterém podsložka předává data dále bez segmentace nebo opravy chyb. Používá se pro služby citlivé na zpoždění, jako je hlas.

## Popis

T-RLC neboli transparentní režim [RLC](/mobilnisite/slovnik/rlc/) je jeden ze tří provozních režimů podsložky řízení rádiového spoje (RLC) v rámci protokolového zásobníku 3GPP, vedle potvrzovaného režimu ([AM](/mobilnisite/slovnik/am/)) a nepotvrzovaného režimu ([UM](/mobilnisite/slovnik/um/)). Je definován primárně pro okruhově přepínané ([CS](/mobilnisite/slovnik/cs/)) hlasové služby v UMTS a později pro určité přenosy (bearery) v LTE. V tomto režimu je podsložka RLC v podstatě obcházena při zpracování dat; nepřidává žádné hlavičky protokolu RLC a neprovádí segmentaci, zpětné sestavování, konkatenaci ani opravu chyb prostřednictvím automatického opakovaného dotazu ([ARQ](/mobilnisite/slovnik/arq/)). Entita RLC v transparentním režimu funguje jako průchozí kanál, který přeposílá jednotky dat služby ([SDU](/mobilnisite/slovnik/sdu/)) přijaté z vyšší vrstvy (např. z vrstvy [PDCP](/mobilnisite/slovnik/pdcp/) nebo přímo z hlasových kodeků CS) přímo do nižší vrstvy [MAC](/mobilnisite/slovnik/mac/) jako jednotky protokolových dat (PDU) stejné velikosti. Hlavní architektonickou rolí T-RLC je minimalizace zpracovatelského zpoždění a režijních nákladů protokolu pro provoz v reálném čase, kde je včasnost důležitější než absolutní integrita dat, a spoléhá se na kódování fyzické vrstvy a případný HARQ na vrstvě MAC pro odolnost proti chybám.

Fungování T-RLC je úzce spojeno s konkrétní konfigurací přenosu. V UMTS byl standardním režimem pro signalizační rádiový přenos (SRB) pro určité řídicí zprávy a pro konverzační CS hlasový přenos. Entita RLC je konfigurována během nastavení rádiového přenosu prostřednictvím signalizace RRC. Když data dorazí z vyšší vrstvy, entita T-RLC je neukládá do vyrovnávací paměti ani nemodifikuje. Může se však podílet na primitivních interakcích pro řízení toku, ale nejsou generována žádná specifická pořadová čísla nebo stavové zprávy RLC. Tato jednoduchost znamená, že neexistuje žádný mechanizmu opakování na úrovni RLC; jakékoli potřebné zotavení z chyb musí být řešeno jinými vrstvami nebo je považováno za přijatelné pro danou službu.

V širší síťové architektuře představuje T-RLC designovou volbu optimalizovanou pro minimální latenci. Pro služby jako Voice over LTE (VoLTE), zatímco uživatelská rovina pro hlasový přenos typicky používá nepotvrzovaný režim RLC (UM), může řídicí rovina využívat T-RLC pro specifické SRB. Jeho existence zdůrazňuje vrstvený přístup v 3GPP, kde různé požadavky služeb diktují různé konfigurace protokolů. Absence režijních nákladů hlavičky RLC (typicky 1–2 bajty) také přispívá k spektrální účinnosti pro malé, často se opakující pakety typické pro hlas. Pochopení T-RLC je zásadní pro inženýry navrhující služby s nízkou latencí a analyzující protokolové záznamy, protože jeho přítomnost indikuje přenos optimalizovaný spíše pro zpoždění než pro spolehlivost.

## K čemu slouží

T-RLC byl vytvořen pro podporu služeb v reálném čase citlivých na zpoždění, primárně okruhově přepínaného hlasu, v sítích 2G/3G UMTS a pro určité signalizační přenosy. Jádrem problému, který řeší, je nadměrná latence a režijní náklady protokolu, které zavádí plnohodnotný potvrzovaný režim RLC (AM). Ten sice poskytuje spolehlivý přenos dat prostřednictvím segmentace a opakování ARQ, ale za cenu proměnlivého a potenciálně vysokého zpoždění. Pro lidskou řeč jsou taková zpoždění a kolísání (jitter) vnímány negativně, což činí nezbytným jednodušší mechanismus téměř okamžitého předávání.

Historicky byl v GSM hlasový provoz zpracováván specifickým kanálovým kódováním bez složitého protokolu spojové vrstvy, jako je RLC. Se zavedením UMTS a jeho jednotné architektury protokolů s přepínáním paketů byl potřebný způsob, jak integrovat hlas do tohoto rámce bez obětování jeho charakteristik v reálném čase. T-RLC to poskytl tím, že v podstatě deaktivoval zpracování vrstvy RLC pro specifické přenosy, využívaje přirozenou odolnost proti chybám vyhrazeného fyzického kanálu a toleranci hlasového kodeku k občasné ztrátě rámce. Tento přístup vyvážil potřebu společného protokolového zásobníku s přísnými požadavky na kvalitu služby (QoS) konverzačních služeb.

V pozdějších verzích, jako je LTE, zatímco paketově přepínaný VoLTE převážně používá nepotvrzovaný režim RLC (UM, který přidává malou hlavičku pro číslování sekvencí, ale ne ARQ), princip T-RLC přetrvává pro specifické aplikace, kde musí být zabráněno i této režii hlavičky a zpracovatelskému zpoždění. Představuje klíčový příklad konfigurace protokolu v 3GPP s ohledem na službu, kde síť přizpůsobuje chování spojové vrstvy dat základním požadavkům provozu.

## Klíčové vlastnosti

- Žádné režijní náklady hlavičky protokolu RLC
- Žádná segmentace nebo konkatenace SDU
- Žádná oprava chyb automatickým opakovaným dotazem (ARQ)
- Minimální zpracovatelská latence
- Používá se pro přenosy s okruhovým přepojováním citlivé na zpoždění
- Konfigurováno prostřednictvím RRC během zřizování rádiového přenosu

## Související pojmy

- [RLC – Radio Link Control](/mobilnisite/slovnik/rlc/)
- [QoS – Quality of Service](/mobilnisite/slovnik/qos/)

## Definující specifikace

- **TS 44.160** (Rel-16) — GERAN Iu Mode RLC/MAC Protocol Specification

---

📖 **Anglický originál a plná specifikace:** [T-RLC na 3GPP Explorer](https://3gpp-explorer.com/glossary/t-rlc/)
