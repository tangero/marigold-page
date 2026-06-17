---
slug: "mvno"
url: "/mobilnisite/slovnik/mvno/"
type: "slovnik"
title: "MVNO – Mobile Virtual Network Operator"
date: 2026-01-01
abbr: "MVNO"
fullName: "Mobile Virtual Network Operator"
category: "Management"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/mvno/"
summary: "Poskytovatel mobilních služeb, který nevlastní vlastní rádiové spektrum ani síťovou infrastrukturu. Místo toho nakupuje síťovou kapacitu velkoobchodně od mobilního síťového operátora (MNO) a pod vlast"
---

MVNO (mobilní virtuální operátor) je poskytovatel mobilních služeb, který nevlastní rádiové spektrum ani infrastrukturu, ale nakupuje velkoobchodní síťovou kapacitu od MNO, aby pod vlastní značkou prodával maloobchodní služby koncovým uživatelům.

## Popis

Mobile Virtual Network Operator (MVNO, mobilní virtuální operátor) je obchodní subjekt, který poskytuje zákazníkům služby mobilní komunikace bez vlastnictví podkladové sítě rádiového přístupu (RAN) nebo licencovaného spektra. Technicky je MVNO závislé na obchodní dohodě s jedním nebo více hostitelskými mobilními síťovými operátory ([MNO](/mobilnisite/slovnik/mno/)) pro získání přístupu k síťovým zdrojům. Stupeň technické nezávislosti se výrazně liší v závislosti na modelu MVNO. Plnohodnotné MVNO (full MVNO) provozuje vlastní prvky jádra sítě, jako je Home Subscriber Server ([HSS](/mobilnisite/slovnik/hss/)), Mobile Switching Center ([MSC](/mobilnisite/slovnik/msc/)) nebo v 5G Unified Data Management ([UDM](/mobilnisite/slovnik/udm/)) a Session Management Function ([SMF](/mobilnisite/slovnik/smf/)). Tyto prvky připojuje k RAN operátora MNO prostřednictvím standardizovaných rozhraní. Tento model poskytuje MVNO větší kontrolu nad službami, provizionováním a zákaznickými daty.

Na druhé straně lehké MVNO (light MVNO) nebo MVNO jako pouhý prodejce služeb může provozovat pouze fakturační systém, zákaznickou podporu a marketing, přičemž se plně spoléhá na jádrovou síť MNO a jednoduše přeprodává jeho služby. Klíčovým technickým rozhraním mezi MVNO a MNO je často síť [GRX](/mobilnisite/slovnik/grx/)/[IPX](/mobilnisite/slovnik/ipx/) ([GPRS](/mobilnisite/slovnik/gprs/) Roaming eXchange/IP eXchange) pro konektivitu a specifické referenční body, jako je rozhraní S8 v 4G (mezi PGW MVNO a SGW MNO) nebo rozhraní N9 v 5G. Abonenti MVNO jsou identifikováni vlastním Mobile Network Code (MNC), který je součástí jejich IMSI, což umožňuje síti MNO směrovat signalizaci a provoz k síťovým prvkům MVNO pro autentizaci a obsluhu služeb.

Z architektonického hlediska model MVNO zavádí logické oddělení mezi vrstvou infrastruktury (vlastněnou MNO) a vrstvou služeb (provozovanou MVNO). To vyžaduje robustní rozhraní systémů pro podporu obchodu (BSS) a systémů pro provozní podporu (OSS) pro provizionování, fakturaci a správu poruch. Role MVNO spočívá v inovacích na úrovni služeb a marketingu, přičemž cílí na niky trhu (např. nízkonákladové služby, specifické etnické skupiny, IoT vertikály) bez masivních kapitálových výdajů na vybudování fyzické sítě. Síť provoz MVNO vidí jako velkoobchodní roamingový provoz, na který uplatňuje dohodnuté QoS a politiky řízení na základě smlouvy o úrovni služeb (SLA).

## K čemu slouží

Koncept MVNO vznikl za účelem zvýšení konkurence a inovací na trhu mobilních telekomunikací, aniž by bylo nutné, aby noví účastníci získávali vzácné a drahé spektrální licence a budovali duplicitní celonárodní infrastrukturu. Před příchodem MVNO byly bariéry vstupu na trh nepřekonatelně vysoké, což omezovalo výběr pro spotřebitele. MVNO tento problém řeší využitím nadbytečné kapacity zavedených MNO, což umožňuje MNO dále monetizovat jejich síťové investice a zároveň umožňuje novým hráčům nabízet služby na míru.

MVNO se zaměřují na specifické tržní segmenty, které velcí MNO mohou zanedbávat. Mohou například nabízet nízkonákladové předplacené tarify, balíčky pro mezinárodní volání nebo specializované plány konektivity pro IoT. Jejich vznik byl motivován jednak regulatorními snahami v některých regionech podpořit konkurenci, jednak čistě obchodními příležitostmi. Z technického hlediska byla pro tento model klíčová standardizace architektur MVNO v rámci 3GPP (počínaje Release 99), která zajišťuje interoperabilitu mezi různými zařízeními MNO a MVNO a umožňuje škálovatelné a bezpečné velkoobchodní přístupové modely. To umožnilo vznik živého ekosystému poskytovatelů služeb, který snižuje ceny a zvyšuje rozmanitost služeb pro koncové uživatele.

## Klíčové vlastnosti

- Provozuje mobilní služby bez vlastnictví licencovaného spektra nebo RAN infrastruktury
- Využívá velkoobchodní dohody o síťovém přístupu s jedním nebo více hostitelskými MNO
- Může se pohybovat od lehkého modelu (pouhý prodejce) až po plnohodnotný model (vlastní jádro sítě)
- Spravuje vlastní zákaznické vztahy, značku, fakturaci a tarify
- Je identifikován vlastním jedinečným Mobile Network Code (MNC) v rámci IMSI svých účastníků
- Propojuje se se sítí MNO prostřednictvím standardizovaných rozhraní 3GPP (např. S8, N9) a sítě GRX/IPX

## Související pojmy

- [MNO – Mobile Network Operator](/mobilnisite/slovnik/mno/)
- [IMSI – International Mobile Subscriber Identity](/mobilnisite/slovnik/imsi/)
- [HPLMN – Home Public Land Mobile Network](/mobilnisite/slovnik/hplmn/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 22.240** (Rel-19) — 3GPP Generic User Profile Requirements
- **TS 22.261** (Rel-20) — 5G System Service Requirements
- **TR 26.941** (Rel-19) — 5G Media Slicing Extensions
- **TR 28.843** (Rel-18) — Technical Report on Charging Aspects for Vertical Scenarios
- **TS 32.240** (Rel-19) — Charging Management Architecture & Principles
- **TS 32.296** (Rel-19) — Online Charging System (OCS) Architecture
- **TR 43.901** (Rel-19) — Generic Access to A/Gb Interface Feasibility Study

---

📖 **Anglický originál a plná specifikace:** [MVNO na 3GPP Explorer](https://3gpp-explorer.com/glossary/mvno/)
