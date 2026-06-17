---
slug: "mvig"
url: "/mobilnisite/slovnik/mvig/"
type: "slovnik"
title: "MVIG – MCVideo Imminent peril Group"
date: 2025-01-01
abbr: "MVIG"
fullName: "MCVideo Imminent peril Group"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/mvig/"
summary: "Skupina definovaná v rámci služby MCVideo (Mission Critical Video) pro uživatele, kteří musí být varováni a koordinováni při bezprostředním ohrožení nebo nouzové situaci. Umožňuje rychlou cílenou komu"
---

MVIG je skupina v rámci služby MCVideo určená pro varování a koordinaci uživatelů při bezprostředním ohrožení, umožňující rychlou cílenou komunikaci pro veřejnou bezpečnost a záchranné složky.

## Popis

Skupina pro bezprostřední ohrožení služby [MCVideo](/mobilnisite/slovnik/mcvideo/) (MCVideo Imminent peril Group, MVIG) je specializovaná skupinová struktura v rámci standardizovaného rámce služeb kritických pro misi (Mission Critical Services, [MCS](/mobilnisite/slovnik/mcs/)) podle 3GPP, konkrétně pro službu MCVideo. Nejde o samostatný síťový prvek, ale o logické seskupení uživatelů (účastníků) a jejich přidružených komunikačních parametrů, definované v rámci systému správy skupin služby kritické pro misi. MVIG je obvykle předkonfigurována administrátorem služby kritické pro misi tak, aby zahrnovala konkrétní záchranné složky, dispečery nebo další personál, který musí být okamžitě zapojen do reakce na kritickou událost. Definice skupiny zahrnuje identity členů, jejich role a konkrétní komunikační služby MCVideo (jako skupinové hovory, sdílení videa) autorizované pro použití v kontextu bezprostředního ohrožení.

Z architektonického hlediska jsou data MVIG uložena a spravována v rámci funkčních entit služby kritické pro misi, jako je Group Management Application Server. Když je vyhlášena událost bezprostředního ohrožení, servisní logika odkazuje na konkrétní MVIG, aby určila cílové příjemce výstrah a navázala počáteční komunikační relaci. Konfigurace skupiny určuje, jak je služba MCVideo vyvolána – například může spustit automatický, přednostní skupinový hovor MVIG (MCVideo Imminent Peril Group Call, [MVIGC](/mobilnisite/slovnik/mvigc/)), který přiděluje vysoce prioritní prostředky a může potenciálně přerušit jiný síťový provoz, aby zajistil okamžitou konektivitu pro členy skupiny.

Její úlohou v síti je poskytovat deterministický a rychlý mechanismus mobilizace pro zásahové jednotky s podporou videa. Díky předdefinování těchto skupin je doba potřebná k navázání kritické komunikace drasticky snížena ve srovnání s ad-hoc vytvářením skupin během krize. Síť používá identifikátor MVIG k aplikaci specifických zásad kvality služeb (Quality of Service, QoS), prioritního zacházení a bezpečnostních kontrol definovaných pro komunikaci kritickou pro misi, čímž zajišťuje, že video přenosy pro skupinu získají potřebnou šířku pásma, nízkou latenci a vysokou spolehlivost v síti LTE nebo 5G.

## K čemu slouží

MVIG byla vytvořena, aby řešila kritickou potřebu okamžité a koordinované video komunikace během život ohrožujících mimořádných událostí pro organizace veřejné bezpečnosti. Před standardizací služeb kritických pro misi přes mobilní sítě se záchranné složky spoléhaly na starší systémy pozemní mobilní rádiové komunikace (Land Mobile Radio, [LMR](/mobilnisite/slovnik/lmr/)), kterým často chyběly integrované video schopnosti a efektivní mechanismy skupinového varování pro bezprostřední hrozby. Přechod na širokopásmové sítě založené na standardech 3GPP umožnil použití bohatých médií, jako je video, ale vyžadoval standardizované metody pro replikaci a vylepšení funkcí rychlého skupinového nasazení známých z LMR.

Zavedení MVIG ve vydání 14 jako součásti širší sady služeb [MCVideo](/mobilnisite/slovnik/mcvideo/) vyřešilo problém pomalého a manuálního vytváření skupin během mimořádných událostí. Umožňuje operačním střediskům a systémům spustit koordinovanou video odezvu jedinou akcí, cílenou na předem definovanou skupinu personálu. To je klíčové ve scénářích, jako jsou útoky aktivních střelců, rozsáhlé požáry nebo přírodní katastrofy, kde se počítají vteřiny a situační povědomí prostřednictvím videa je zásadní. MVIG poskytuje logický rámec, který síti umožňuje zacházet s komunikací skupiny s nejvyšší prioritou, a zajišťuje tak okamžité přidělení prostředků na podporu zásahu.

## Klíčové vlastnosti

- Předkonfigurovaná logická skupina uživatelů služeb kritických pro misi pro scénáře bezprostředního ohrožení
- Umožňuje rychlé spuštění vysoce prioritních skupinových komunikačních relací MCVideo
- Integruje se s architekturou služby MCVideo pro spravované skupinové hovory a datové relace
- Podporuje aplikaci zásad kvality služeb (QoS) a prioritních zásad kritických pro misi pro všechny členy skupiny
- Usnadňuje cílené varování a okamžitou mobilizaci týmů záchranných složek
- Spravována prostřednictvím rozhraní správy služeb kritických pro misi (např. MCX)

## Související pojmy

- [MCVideo – Mission Critical Video](/mobilnisite/slovnik/mcvideo/)
- [MCS – Modulation and Coding Schemes](/mobilnisite/slovnik/mcs/)

## Definující specifikace

- **TS 24.281** (Rel-19) — MCVideo Signalling Control Specification
- **TS 37.579** (Rel-18) — Mission Critical services conformance testing

---

📖 **Anglický originál a plná specifikace:** [MVIG na 3GPP Explorer](https://3gpp-explorer.com/glossary/mvig/)
