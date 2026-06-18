---
slug: "fsa"
url: "/mobilnisite/slovnik/fsa/"
type: "slovnik"
title: "FSA – Frequency Selection Area"
date: 2025-01-01
abbr: "FSA"
fullName: "Frequency Selection Area"
category: "Radio Access Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/fsa/"
summary: "FSA je identifikátor oblasti pro výběr kmitočtu, zavedený v 3GPP Release 17 pro službu Multimedia Broadcast Multicast Service (MBS). Definuje logickou oblast, ve které pro doručování MBS platí specifi"
---

FSA je identifikátor oblasti pro výběr kmitočtu, který definuje logickou oblast, ve které pro doručování služby Multimedia Broadcast Multicast Service v sítích 5G platí specifické zásady pro výběr kmitočtu.

## Popis

Oblast pro výběr kmitočtu (Frequency Selection Area, FSA) je logický koncept a identifikátor zavedený v 3GPP Release 17 jako součást rozšířeného rámce služby Multimedia Broadcast Multicast Service ([MBS](/mobilnisite/slovnik/mbs/)) pro sítě 5G. FSA definuje geografickou nebo logickou oblast, ve které jsou pro doručování vysílacích a vícesměrových služeb uplatňovány specifické zásady a konfigurace pro výběr kmitočtu. Je klíčovou součástí pro efektivní správu rádiových zdrojů pro MBS, neboť umožňuje síti nasměrovat uživatelské zařízení (UE) na optimální kmitočty pro příjem vícesměrového/vysílacího obsahu na základě jeho polohy a stavu sítě.

Z architektonického hlediska je FSA konfigurována a spravována sítí, typicky 5G jádrem (5GC) a NG-RAN. Identifikátor FSA ID je jedinečný identifikátor, který je vysílán v systémových informacích nebo poskytován prostřednictvím dedikované signalizace UE, které mají zájem o MBS. Síť mapuje FSA na konkrétní kmitočtové vrstvy, seznamy buněk nebo oblasti MBS relací. Když UE vstoupí do FSA, použije přidružené FSA ID k určení, který kmitočet má sledovat nebo se na něj naladit pro příjem MBS, což může zahrnovat procedury převýběru nebo předávání optimalizované pro vícesměrové toky.

Fungování FSA zahrnuje několik kroků. Nejprve síť naplánuje a nakonfiguruje FSA, přiřadí identifikátory FSA ID a asociuje je se službami MBS a kmitočtovými zdroji. Tyto informace jsou předány RAN uzlům (gNB). Pro UE je identifikátor FSA ID získán buď z vysílaných bloků systémových informací ([SIB](/mobilnisite/slovnik/sib/)), nebo prostřednictvím dedikované [RRC](/mobilnisite/slovnik/rrc/) signalizace při připojování k MBS relaci. UE pak tento identifikátor použije, případně v kombinaci s předkonfigurovaným nebo sítí poskytnutým mapováním, k výběru vhodného kmitočtu nosné pro příjem MBS. Tento mechanismus umožňuje vyrovnávání zátěže, zmírnění interferencí a efektivní využití spektra vyčleněného pro vysílání/vícesměrový přenos. Klíčové specifikace jako TS 23.247 (architektura MBS) a TS 38.300 (celkový popis NR) detailně popisují jeho integraci do servisních a RAN procedur.

Role FSA v síti je klíčová pro škálovatelné a efektivní doručování MBS v 5G. Umožňuje správu zdrojů v kmitočtové oblasti pro vysílací služby a oddělení provozu MBS od jednostěnového provozu tam, kde je to výhodné. To podporuje případy užití jako komunikace pro veřejnou bezpečnost, streamování živých událostí nebo aktualizace software přes vzdušné rozhraní. Definováním FSA může síť optimalizovat pokrytí, kapacitu a životnost baterie UE pro příjem vícesměrového přenosu, což činí 5G MBS životaschopnou a efektivní technologií pro skupinovou komunikaci.

## K čemu slouží

FSA bylo vytvořeno v Release 17, aby řešilo konkrétní výzvy při nasazování efektivní služby Multimedia Broadcast Multicast Service ([MBS](/mobilnisite/slovnik/mbs/)) v sítích 5G NR. Před Rel-17 mělo MBS v LTE (eMBMS) mechanismy jako oblasti [MBSFN](/mobilnisite/slovnik/mbsfn/), ale 5G přineslo flexibilnější architekturu. Motivací pro zavedení FSA byla potřeba dynamické a efektivní správy kmitočtových zdrojů pro vysílací/vícesměrový provoz, který může mít ve srovnání s jednostěnovým provozem odlišné požadavky na pokrytí a kapacitu.

Historický kontext spočívá v práci 3GPP na vylepšení MBS pro 5G, aby podpořila nové případy užití, jako je skupinová komunikace [V2X](/mobilnisite/slovnik/v2x/), aktualizace software pro IoT nebo televizní vysílání. Klíčovým problémem bylo, jak efektivně nasměrovat UE na správný kmitočet pro MBS bez nadměrné signalizační režie nebo suboptimálního využití zdrojů. FSA to řeší tím, že poskytuje logický identifikátor, který zapouzdřuje zásady pro výběr kmitočtu pro danou oblast, zjednodušuje procedury na straně UE a umožňuje optimalizaci řízenou sítí. Odstraňuje omezení statických konfigurací tím, že umožňuje síťovému plánování přizpůsobit využití kmitočtů pro MBS v závislosti na oblasti, čímž zlepšuje efektivitu využití spektra a spolehlivost služby pro vícesměrové aplikace v různých scénářích nasazení.

## Klíčové vlastnosti

- Definuje logickou oblast pro výběr kmitočtu (Frequency Selection Area) identifikovanou jedinečným FSA ID
- Umožňuje síťově řízený výběr kmitočtu pro příjem MBS
- Podporuje dynamické mapování služeb MBS na kmitočtové vrstvy v závislosti na oblasti
- Snižuje spotřebu energie UE naváděním k efektivnímu naladění na kmitočet
- Napomáhá optimalizaci zdrojů pro MBS a správě interferencí
- Je integrováno s architekturou 5G MBS pro doručování vysílacích a vícesměrových služeb

## Související pojmy

- [MBS – Frequency Selection Area Identity](/mobilnisite/slovnik/mbs/)
- [MBSFN – Multimedia Broadcast multicast service Single Frequency Network](/mobilnisite/slovnik/mbsfn/)

## Definující specifikace

- **TS 23.247** (Rel-19) — 5G Multicast/Broadcast Service Architecture
- **TS 24.578** (Rel-19) — UE policies for A2X services in 5GS
- **TS 24.587** (Rel-19) — V2X Services Protocols for 5G System
- **TS 24.588** (Rel-19) — UE Policies for V2X Services in 5GS
- **TS 26.517** (Rel-19) — 5G MBS User Service Protocols and Formats
- **TS 29.532** (Rel-19) — MB-SMF Service Based Interface Protocol
- **TS 38.300** (Rel-19) — NG-RAN Overall Description
- **TS 38.473** (Rel-19) — 5G F1 Application Protocol (F1AP)

---

📖 **Anglický originál a plná specifikace:** [FSA na 3GPP Explorer](https://3gpp-explorer.com/glossary/fsa/)
