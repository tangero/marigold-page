---
slug: "uli"
url: "/mobilnisite/slovnik/uli/"
type: "slovnik"
title: "ULI – User Location Information"
date: 2026-01-01
abbr: "ULI"
fullName: "User Location Information"
category: "Services"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/uli/"
summary: "Soubor datových parametrů, které identifikují geografickou nebo síťovou polohu uživatelského zařízení (UE). Je klíčový pro služby založené na poloze, tísňová volání (např. E911), zákonný odposlech, de"
---

ULI je soubor datových parametrů, které identifikují geografickou nebo síťovou polohu uživatelského zařízení pro služby jako tísňová volání, zákonný odposlech a optimalizace sítě.

## Popis

User Location Information (ULI) je v rámci standardů 3GPP komplexní pojem zahrnující různé datové prvky, které určují polohu mobilního zařízení (User Equipment neboli UE) v rámci buněčné sítě. Nejde o jedinou souřadnici, ale o soubor parametrů, které mohou popsat polohu na různých úrovních přesnosti – od velké geografické oblasti, jako je země, až po přesnou sadu [GPS](/mobilnisite/slovnik/gps/) souřadnic. ULI generují, ukládají a zpracovávají četné síťové funkce napříč jak jádrem sítě (Core Network – CN), tak přístupovou rádiovou sítí (Radio Access Network – RAN). Mezi klíčové zdroje patří Mobility Management Entity ([MME](/mobilnisite/slovnik/mme/)) v 4G, Access and Mobility Management Function ([AMF](/mobilnisite/slovnik/amf/)) v 5G, obsluhující základnová stanice ([eNB](/mobilnisite/slovnik/enb/)/gNB) a samotné UE, pokud má schopnosti [GNSS](/mobilnisite/slovnik/gnss/). Konkrétní parametry ULI jsou definovány v kontextech, jako je Evolved Packet System (EPS) Location Information (ELI) v 4G nebo 5G Location Information v 5GC.

Složení ULI může zahrnovat několik odlišných prvků. Na síťové úrovni typicky obsahuje Cell Global Identity ([CGI](/mobilnisite/slovnik/cgi/)), která jednoznačně identifikuje obsluhující buňku, a Tracking Area Identity ([TAI](/mobilnisite/slovnik/tai/)) nebo Routing Area Identity ([RAI](/mobilnisite/slovnik/rai/)), které označují větší skupinu buněk pro účely pagingu. Pro podrobnější geometrickou polohu může ULI zahrnovat parametry Geographic Location (GeoLoc), jako je zeměpisná šířka, délka, nadmořská výška a odhady nejistoty. Tato geometrická data mohou být odvozena ze síťových metod, jako je Observed Time Difference of Arrival (OTDOA) v LTE nebo Downlink Time Difference of Arrival (DL-TDOA) v 5G NR, nebo z metod založených na UE, jako je Assisted-GNSS (A-GNSS). ULI je přenášeno v rámci protokolových zpráv na různých rozhraních, jako jsou S1-MME, N2 a N4, a je klíčovým informačním prvkem v kontextu Packet Data Unit (PDU) session a signalizaci mobility managementu.

ULI hraje klíčovou provozní roli v celé síti. Pro tísňové služby je síť ze zákona povinna poskytnout přesné ULI do centra tísňového volání (Public Safety Answering Point – PSAP) při zahájení tísňového hovoru. Tento proces zahrnuje dotazování sítě na polohu UE prostřednictvím Gateway Mobile Location Centre (GMLC). Pro zákonný odposlech je ULI klíčovou součástí Intercept Related Information (IRI) poskytované orgánům činným v trestním řízení. Z pohledu správy sítě ULI umožňuje řízení politik a účtování na základě polohy (např. diferencované tarify pro domácí a roamovací zóny), detekci podvodů identifikací nepravděpodobných změn polohy a analytiku pro plánování a optimalizaci sítě. Vývoj od 4G k 5G přinesl vyšší přesnost a dostupnost ULI, přičemž služby 5G jádra sítě, jako je Location Management Function (LMF) a Network Exposure Function (NEF), poskytují standardizovaná API pro autorizované aplikace třetích stran, aby mohly žádat o informace o poloze, a to s ohledem na souhlas uživatele a předpisy o ochraně soukromí.

## K čemu slouží

ULI existuje za účelem splnění rozmanité sady regulatorních, komerčních a provozních požadavků, které jsou vlastní mobilní telekomunikaci. Nejzásadnějším důvodem je regulatorní shoda pro tísňové služby. V návaznosti na nařízení jako E911 v USA a eCall v EU musí být mobilní sítě schopny poskytnout přesnou polohu volajícího záchranným složkám za účelem záchrany životů. ULI poskytuje standardizovaný mechanismus pro splnění této zákonné povinnosti. Komerčně ULI umožňuje rozsáhlý ekosystém služeb založených na poloze (Location-Based Services – LBS), jako je navigace, místní vyhledávání, cílená reklama a sledování vozového parku, což vytváří významné zdroje příjmů pro operátory a poskytovatele aplikací.

Z pohledu provozu sítě měly sítě před zavedením sofistikovaného sledování polohy omezenou možnost vidět distribuci uživatelů nad rámec připojení na úrovni buňky. To činilo úkoly, jako je plánování kapacity, identifikace hotspotů a správa roamingu, náročnými. ULI tento problém řeší poskytováním dat pro pokročilou analytiku. Je také nezbytné pro bezpečnostní funkce; náhlé, nemožné skoky v poloze (např. z New Yorku do Londýna během minut) mohou indikovat podvody typu SIM box nebo pokusy o převzetí účtu. Vytvoření a standardizace ULI napříč releasy 3GPP bylo motivováno potřebou jednotného, interoperabilního rámce. Rané buněčné systémy měly proprietární nebo omezené možnosti určování polohy. Počínaje Release 8 s EPS systematicky definovala 3GPP architekturu (zahrnující uzly jako GMLC, MME) a protokoly pro služby určování polohy, což zajišťuje, že poloha UE může být určena a hlášena konzistentně, ať je UE stacionární nebo se pohybuje vysokou rychlostí, a napříč zařízeními různých výrobců.

Vývoj ULI také řeší omezení dřívějších, méně přesných metod. Zatímco Cell-ID poskytuje hrubou polohu, integrace A-GNSS a pokročilých síťových metod určování polohy, jako je OTDOA, do rámce ULI vyřešila problém prostředí uvnitř budov nebo městských kaňonů, kde jsou signály GPS slabé. Pokračující vylepšení v 5G s podporou pozicování s pomocí senzorů a vyššími požadavky na přesnost pro průmyslový IoT ukazují, že ULI je kontinuálně se vyvíjející schopnost, která je klíčová pro umožnění nových vertikálních aplikací a splnění stále přísnějších výkonnostních benchmarků.

## Klíčové vlastnosti

- Agreguje více parametrů polohy: Cell ID, Tracking Area, geografické souřadnice
- Podporuje různé metody určování polohy: síťové (OTDOA), založené na UE (A-GNSS), hybridní
- Nezbytné pro regulatorní poskytování polohy pro tísňové služby (např. E911, eCall)
- Umožňuje komerční služby založené na poloze (LBS) prostřednictvím vystavených síťových API
- Kritický vstup pro systémy optimalizace sítě, analytiky a správy podvodů
- Přenášeno ve standardizovaných protokolových zprávách napříč rozhraními jádra a přístupové sítě

## Související pojmy

- [GMLC – Gateway Mobile Location Center](/mobilnisite/slovnik/gmlc/)
- [LMF – Location Management Function](/mobilnisite/slovnik/lmf/)
- [NEF – Network Exposure Function](/mobilnisite/slovnik/nef/)

## Definující specifikace

- **TS 23.041** (Rel-19) — Cell Broadcast Service and Public Warning System
- **TS 23.700** (Rel-20) — XR Services Application Enablement Layer
- **TS 23.843** (Rel-12) — Signalling Overload Scenarios & Solutions
- **TS 29.274** (Rel-19) — GTPv2-C Control Plane Protocol Specification
- **TS 38.401** (Rel-19) — NG-RAN Architecture Specification
- **TS 38.413** (Rel-19) — NG Application Protocol (NGAP)

---

📖 **Anglický originál a plná specifikace:** [ULI na 3GPP Explorer](https://3gpp-explorer.com/glossary/uli/)
