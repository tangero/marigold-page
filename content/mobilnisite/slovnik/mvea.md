---
slug: "mvea"
url: "/mobilnisite/slovnik/mvea/"
type: "slovnik"
title: "MVEA – MCVideo Emergency Alert"
date: 2025-01-01
abbr: "MVEA"
fullName: "MCVideo Emergency Alert"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/mvea/"
summary: "Služba v rámci Mission Critical Video (MCVideo), která umožňuje rychlé vysílání nouzových video upozornění cílové skupině uživatelů. Je klíčová pro veřejnou bezpečnost a zásahy v mimořádných situacích"
---

MVEA je služba Mission Critical Video (kritické video) umožňující rychlé vysílání nouzových video upozornění cílovým skupinám pro účely veřejné bezpečnosti a zásahů v mimořádných situacích.

## Popis

[MCVideo](/mobilnisite/slovnik/mcvideo/) Emergency Alert (MVEA) je standardizovaná služba definovaná 3GPP pro komunikaci v oblasti veřejné bezpečnosti, konkrétně v rámci architektury Mission Critical Services ([MCS](/mobilnisite/slovnik/mcs/)). Funguje jako součást architektury MCVideo, která je rozšířením služby Mission Critical Push-to-Talk ([MCPTT](/mobilnisite/slovnik/mcptt/)) o video schopnosti. MVEA umožňuje autorizovanému uživateli, typicky dispečerovi nebo veliteli zásahu, zahájit nouzové upozornění obsahující video. Toto upozornění je následně vysíláno předem definované nebo dynamicky vytvořené skupině uživatelů MCVideo, například záchranářům v konkrétní geografické oblasti. Služba využívá základní síťovou infrastrukturu LTE nebo 5G, přičemž pro řízení relace používá IP Multimedia Subsystem (IMS) a pro servisní logiku a správu skupin aplikační server MCVideo.

Architektura MVEA zahrnuje několik klíčových komponent. Klient MCVideo na uživatelském zařízení (UE) podporuje schopnost odesílat a přijímat nouzová upozornění. Aplikační server MCVideo, který může být součástí vyhrazené sítě pro veřejnou bezpečnost nebo komerční sítě s podporou MCS, zajišťuje autorizaci, směrování a distribuci upozornění. Rozhraní se systémem správy skupin určuje cílové příjemce, často na základě členství ve skupině (např. tým pro zásah v mimořádné situaci) nebo polohy. Zahájení upozornění typicky zahrnuje aktivaci nouzové funkce uživatelem, což spustí proceduru navázání relace přes IMS. Video obsah, který může být předem nahraný nebo živě streamovaný, je následně přenášen pomocí protokolu Real-time Transport Protocol ([RTP](/mobilnisite/slovnik/rtp/)) přes zřízený přenosový kanál, přičemž mechanismy Quality of Service (QoS) zajišťují prioritu a nízkou latenci.

MVEA funguje prostřednictvím integrace s vylepšeními pro nouzové služby v jádru sítě. Při zahájení MVEA server MCVideo ověří přihlašovací údaje iniciátora a kontext mimořádné události. Následně zřídí komunikační relaci typu jeden-vůči-mnoha. Upozornění může kromě videa obsahovat metadata, jako je stupeň naléhavosti, poloha a textový popis. Systém zajišťuje spolehlivé doručení, často za použití mechanismů jako potvrzení o přečtení. Jeho úlohou v síti je poskytnout standardizovanou, interoperabilní metodu pro nouzové video vysílání, která je nezbytná pro koordinované zásahy při katastrofách, teroristických útocích nebo rozsáhlých nehodách, kde vizuální informace mohou výrazně zlepšit povědomí o situaci a rozhodování.

## K čemu slouží

MVEA byla vytvořena pro řešení kritické potřeby rychlé, spolehlivé a multimediální nouzové komunikace ve scénářích veřejné bezpečnosti. Před její standardizací byla nouzová upozornění většinou omezena na hlas (např. sirény, rozhlasové vysílání) nebo text (např. [SMS](/mobilnisite/slovnik/sms/), Cell Broadcast), kterým chybí kontextová hloubka živého videa. Omezení těchto přístupů zahrnovala zpožděné pochopení situace, nejednoznačnost při popisu složitých scén a neschopnost poskytovat vizuální informace v reálném čase distribuovaným týmům. Motivací pro MVEA byly poznatky z velkých incidentů, kdy zasahujícím jednotkám chybělo sdílené vizuální povědomí, což vedlo k neefektivnímu nasazení zdrojů a zvýšenému riziku.

Historicky se komunikace veřejné bezpečnosti opírala o starší systémy pozemní mobilní radiokomunikace (Land Mobile Radio - [LMR](/mobilnisite/slovnik/lmr/)), které jsou zaměřené na hlas a mají omezené datové schopnosti. Přechod na širokopásmové sítě LTE a 5G v rámci konceptu Mission Critical Services od 3GPP umožnil multimediální služby. MVEA konkrétně řeší problém šíření naléhavých vizuálních informací – jako jsou živé záběry z požáru, obraz podezřelé osoby nebo únik nebezpečné látky – všem relevantním osobám současně. Zajišťuje, že velitelé mohou předávat složité situace efektivněji než pouze hlasem, což může zachraňovat životy a majetek.

Vytvoření MVEA bylo hnáno požadavky orgánů veřejné bezpečnosti z celého světa, koordinovanými prostřednictvím normalizačních orgánů jako je 3GPP. Integruje se s dalšími komponentami [MCS](/mobilnisite/slovnik/mcs/), jako jsou [MCPTT](/mobilnisite/slovnik/mcptt/) a MCData, a poskytuje tak komplexní ekosystém pro kritické mise. Standardizací MVEA zajišťuje 3GPP interoperabilitu mezi různými výrobci a sítěmi, což je klíčové pro přeshraniční mimořádné události a zásahy více složek. Představuje významný vývoj oproti tradičním systémům varování tím, že využívá moderní sítě založené na IP ke zvýšení připravenosti a schopností zásahu v mimořádných situacích.

## Klíčové vlastnosti

- Autorizované zahájení nouzových video upozornění určenými uživateli (např. dispečery)
- Vysílání typu jeden-vůči-mnoha předem definovaným nebo dynamickým skupinám MCVideo
- Podpora živého streamování nebo předem nahraného video obsahu v rámci upozornění
- Integrace s IMS pro řízení relací a přenosové kanály s podporou QoS
- Zařazení metadat (např. poloha, naléhavost, textový popis) společně s video upozorněním
- Mechanismy pro potvrzení o přijetí a zobrazení upozornění příjemci

## Související pojmy

- [MCVideo – Mission Critical Video](/mobilnisite/slovnik/mcvideo/)
- [MCPTT – Mission Critical Push to Talk Identity](/mobilnisite/slovnik/mcptt/)

## Definující specifikace

- **TS 24.281** (Rel-19) — MCVideo Signalling Control Specification
- **TS 37.579** (Rel-18) — Mission Critical services conformance testing

---

📖 **Anglický originál a plná specifikace:** [MVEA na 3GPP Explorer](https://3gpp-explorer.com/glossary/mvea/)
