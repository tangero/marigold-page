---
slug: "vpc"
url: "/mobilnisite/slovnik/vpc/"
type: "slovnik"
title: "VPC – VoIP Positioning Centre"
date: 2025-01-01
abbr: "VPC"
fullName: "VoIP Positioning Centre"
category: "Core Network"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/vpc/"
summary: "VoIP Positioning Centre (VPC) je síťová funkce definovaná pro služby tísňového volání v sítích založených na IMS. Je zodpovědná za získání, ověření a poskytnutí polohy volajícího přes VoIP příslušné s"
---

VPC je síťová funkce v sítích založených na IMS, která je zodpovědná za získání, ověření a poskytnutí polohy volajícího přes VoIP službám tísňového volání pro přesné směrování a vyslání pomoci.

## Popis

VoIP Positioning Centre (VPC) je klíčová funkční entita v architektuře 3GPP pro podporu služeb založených na poloze, konkrétně tísňových hovorů (např. E911, eCall), pocházejících z IP hlasových služeb jako VoLTE, VoWiFi a VoNR. Definována v TS 23.167 funguje jako specializovaný Location Server ([LS](/mobilnisite/slovnik/ls/)) přizpůsobený prostředí IP Multimedia Subsystem (IMS). Jejím hlavním úkolem je zprostředkovat komunikaci mezi jádrem IMS, které zpracovává signalizaci hovoru, a různými systémy pro určení polohy za účelem získání zeměpisné polohy volajícího.

Architektonicky se VPC nachází v domácí síti nebo v síti důvěryhodné třetí strany. Komunikuje s několika klíčovými uzly. Přijímá žádosti o polohu prostřednictvím [MLP](/mobilnisite/slovnik/mlp/) (Mobile Location Protocol) přes rozhraní Le, typicky od Gateway Mobile Location Centre ([GMLC](/mobilnisite/slovnik/gmlc/)) nebo přímo od Emergency Call Session Control Function ([E-CSCF](/mobilnisite/slovnik/e-cscf/)). VPC následně řídí proces získání informace o poloze. Může dotazovat Home Subscriber Server ([HSS](/mobilnisite/slovnik/hss/)) účastníka, aby zjistila obsluhující síť a dostupné možnosti určení polohy. Pro určení polohy založené na síti může komunikovat s location servery ve navštívené přístupové síti (např. [E-SMLC](/mobilnisite/slovnik/e-smlc/) v LTE pro UE) přes standardizovaná rozhraní (např. SLg, SLs v 4G/5G). Může také zpracovávat polohu založenou na zařízení, pokud ji UE poskytne v [SIP](/mobilnisite/slovnik/sip/) signalizaci (např. v hlavičce Geolocation).

Fungování VPC zahrnuje několik kroků. Při sestavování tísňového hovoru E-CSCF identifikuje potřebu polohy a odešle žádost VPC. VPC zahájí procedury získání polohy. Ověří žádost a určí nejlepší metodu pro získání údaje – to může zahrnovat využití metod určování polohy podkladové 3GPP přístupové sítě (např. [OTDOA](/mobilnisite/slovnik/otdoa/), ECID v LTE; NR positioning v 5G), použití asistovaných GNSS dat nebo přijetí odhadu polohy poskytnutého UE. VPC následně naformátuje informaci o poloze (např. do podoby občanské adresy nebo geodetických souřadnic) a vrátí ji žádající entitě. Tato poloha se používá pro dva klíčové účely: směrování tísňového hovoru ke správnému Public Safety Answering Point (PSAP) na základě polohy volajícího (směrování založené na poloze) a poskytnutí polohy volajícího dispečerovi pro vyslání záchranných složek.

Dále je VPC zodpovědná za validaci polohy a nakládání s ochranou soukromí. Musí zajistit, aby údaje o poloze splňovaly požadavky na přesnost stanovené regulačními orgány. Také vynucuje pravidla ochrany soukromí, zajišťující, že poloha je zveřejněna pouze pro autorizované účely tísňového volání. Ve scénářích, kdy volající roamuje nebo používá nepřístup 3GPP (jako Wi-Fi), se role VPC stává ještě složitější a vyžaduje koordinaci s navštívenými síťovými prvky nebo alternativními zdroji polohy (jako Wi-Fi positioning systémy), aby mohla svou funkci splnit.

## K čemu slouží

VPC byla vytvořena, aby vyřešila zásadní problém spojený s přechodem na VoIP a telefonii založenou na IMS: jak spolehlivě a přesně určit polohu volajícího pro služby tísňového volání, když neexistuje pevná adresa spojená s linkou jako u tradiční pevné linky a když volající může být mobilní nebo používat IP přístup odkudkoli. Starší okruhově přepínané mobilní sítě měly dobře zavedenou architekturu pro služby polohy (LCS) soustředěnou kolem GMLC. IMS však odděluje servisní vrstvu od přístupové sítě, což komplikuje získání polohy pro tísňové hovory pocházející přes IP.

Primárním motivem byla regulatorní shoda a veřejná bezpečnost. Vlády po celém světě nařizují, že tísňové hovory musí poskytnout polohu volajícího, aby umožnily rychlý zásah. Stávající architektura mobilních LCS byla navržena pro netísňové služby a nebyla plně integrována s procedurami řízení hovorů IMS. VPC byla standardizována, aby tuto mezeru zaplnila, a poskytla tak vyhrazenou, na přístupu nezávislou funkci, která může propojit rámec tísňového volání IMS s různými technologiemi určování polohy dostupnými v různých typech přístupu (LTE, 5G, WLAN).

Odstranila omezení předchozích ad-hoc nebo nestandardizovaných přístupů. Před standardizací VPC se rané implementace VoIP potýkaly s tísňovým voláním, často neposkytovaly žádnou polohu nebo jen hrubou polohu odvozenou ze sítě. VPC poskytla standardizovanou, škálovatelnou a bezpečnou metodu pro získání ověřené polohy. Také zajistila architekturu připravenou na budoucnost pro nové přístupové technologie a hybridní scénáře (např. VoWiFi hovor ze zařízení, které má také mobilní rádiový modul). Centralizací logiky koordinace polohy pro tísňové hovory IMS VPC zjednodušuje návrh sítě, zajišťuje konzistentní chování mezi operátory a je klíčová pro splnění přísných požadavků služeb tísňového volání, jako jsou ty definované standardy NENA i3 a ETSI EMTEL v IP éře.

## Klíčové vlastnosti

- Specializovaný Location Server pro služby tísňového volání a služby založené na poloze v IMS
- Řídí získání polohy volajícího ze síťových metod (např. od E-SMLC), metod založených na zařízení nebo hybridních metod
- Komunikuje s jádrem IMS (E-CSCF) přes MLP na rozhraní Le a s location servery přístupové sítě
- Poskytuje validaci polohy, formátování (občanské/geodetické) a zajištění splnění regulatorních požadavků na přesnost
- Podporuje směrování tísňových hovorů založené na poloze ke správnému PSAP
- Vynucuje politiky ochrany soukromí pro zveřejnění polohy a řeší scénáře roamingu a nepřístupu 3GPP

## Související pojmy

- [E-CSCF – Emergency – Call Session Control Function](/mobilnisite/slovnik/e-cscf/)
- [GMLC – Gateway Mobile Location Center](/mobilnisite/slovnik/gmlc/)
- [LCS – Location Services](/mobilnisite/slovnik/lcs/)
- [PSAP – Public Safety Answering Point](/mobilnisite/slovnik/psap/)

## Definující specifikace

- **TS 23.167** (Rel-19) — IMS Emergency Sessions

---

📖 **Anglický originál a plná specifikace:** [VPC na 3GPP Explorer](https://3gpp-explorer.com/glossary/vpc/)
