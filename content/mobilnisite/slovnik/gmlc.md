---
slug: "gmlc"
url: "/mobilnisite/slovnik/gmlc/"
type: "slovnik"
title: "GMLC – Gateway Mobile Location Center"
date: 2026-01-01
abbr: "GMLC"
fullName: "Gateway Mobile Location Center"
category: "Core Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/gmlc/"
summary: "Uzel jádra sítě v systémech 3GPP, který poskytuje služby založené na poloze správou žádostí o určení polohy. Funguje jako rozhraní mezi externími klienty lokálních služeb (LCS klienty) a mobilní sítí,"
---

GMLC je uzel jádra sítě, který poskytuje služby založené na poloze tím, že spravuje žádosti o určení polohy a funguje jako rozhraní mezi externími klienty lokálních služeb a mobilní sítí pro získání polohy uživatelského zařízení (UE).

## Popis

Gateway Mobile Location Center (GMLC) je základní součástí architektury služeb určování polohy ([LCS](/mobilnisite/slovnik/lcs/)) dle 3GPP a slouží jako brána mezi externími aplikacemi a mobilní sítí pro získání polohy uživatelského zařízení (UE). Funguje jako první kontaktní bod pro externí klienty služeb určování polohy (LCS klienty), což jsou subjekty žádající data o poloze UE pro účely jako jsou nouzové služby (např. E911), komerční aplikace nebo zákonné odposlechy. GMLC zajišťuje autentizaci, autorizaci a směrování žádostí o polohu, přičemž dbá na to, aby k polohovým informacím měli přístup pouze oprávnění klienti a aby byly dodrženy předpisy na ochranu soukromí. Po přijetí žádosti GMLC komunikuje s prvky jádra sítě, jako je Home Subscriber Server ([HSS](/mobilnisite/slovnik/hss/)) nebo Unified Data Management ([UDM](/mobilnisite/slovnik/udm/)), aby zjistil obslužný uzel UE (např. [MME](/mobilnisite/slovnik/mme/), [AMF](/mobilnisite/slovnik/amf/), SGSN), a poté žádost přepošle příslušnému Mobile Switching Center ([MSC](/mobilnisite/slovnik/msc/)), Serving [GPRS](/mobilnisite/slovnik/gprs/) Support Node (SGSN) nebo Access and Mobility Management Function (AMF) k provedení určení polohy.

Z architektonického hlediska se GMLC skládá z několika logických funkcí, včetně Requesting GMLC (R-GMLC) a Home GMLC ([H-GMLC](/mobilnisite/slovnik/h-gmlc/)), a to v závislosti na stavu roamingu UE. V případě domácí sítě sídlí H-GMLC v domácí síti UE a spravuje kontrolu předplatného a soukromí. Při roamingu UE může R-GMLC ve navštívené síti komunikovat s H-GMLC, aby koordinoval získání polohy. GMLC komunikuje přes standardizovaná rozhraní: rozhraní Le se připojuje k externím LCS klientům, rozhraní Lh je propojeno s HSS/UDM pro data o účastnících a rozhraní Lg/Lg+ se připojuje k MSC, SGSN nebo AMF pro žádosti o určení polohy. Samotné určení polohy provádí rádiová přístupová síť (RAN) pomocí metod jako je Observed Time Difference of Arrival (OTDOA) v LTE/NR nebo Assisted GPS (A-GPS) a výsledky jsou předány GMLC k doručení klientovi.

Fungování zahrnuje vícekrokový postup: nejprve LCS klient pošle přes rozhraní Le žádost o polohu na GMLC s uvedením cílového UE (např. pomocí MSISDN nebo IMSI) a požadované kvality služby (např. přesnosti). GMLC klienta ověří a zkontroluje nastavení soukromí na základě profilu účastníka UE. Poté se dotazuje na HSS/UDM, aby určil aktuální obslužný uzel a síťovou lokalitu UE. Následně GMLC žádost přepošle tomuto obslužnému uzlu (např. AMF v 5G), který spustí měření polohy v RAN. Jakmile je poloha vypočtena, je přenesena zpět přes obslužný uzel na GMLC, který výsledek naformátuje a pošle LCS klientovi. Tento proces podporuje jak určování polohy v reálném čase, tak i odložené (historické) získávání polohy, přičemž GMLC spravuje stav relace a ošetřování chyb. Specifikace jako 3GPP TS 23.271 a TS 29.172 podrobně popisují protokoly a postupy, což zajišťuje interoperabilitu od 3G až po 5G.

## K čemu slouží

GMLC byl představen ve vydání 3GPP Release 99 za účelem standardizace služeb založených na poloze napříč mobilními sítěmi, čímž reagoval na rostoucí poptávku po možnostech určování polohy hnánou regulatorními požadavky (např. určení polohy pro nouzová volání) a komerčními aplikacemi. Před touto standardizací existovala proprietární řešení, ta však postrádala interoperabilitu a škálovatelnost, což ztěžovalo externím aplikacím konzistentní přístup k poloze UE u různých operátorů a v různých regionech. GMLC poskytl jednotnou bránu, která abstrahovala síťovou komplexitu a umožnila bezproblémovou integraci lokalizačních služeb.

Historicky byla klíčovým motivátorem pro vývoj GMLC snaha o vylepšené nouzové služby, jako je například mandát E911 v USA. Vyřešil problém rychlého a přesného určení polohy volajícího v nouzi bez ohledu na jeho připojení k síti. Centralizací zpracování žádostí a správy soukromí GMLC zajistil, že k polohovým datům mají přístup pouze oprávněné subjekty (např. přijímací místa tísňového volání), čímž vyvážil užitečnost a soukromí uživatele. V průběhu jednotlivých vydání jeho role expandovala, aby podporovala komerční případy užití jako navigace, sledování vozového parku nebo reklamy založené na poloze, a to v důsledku rozšíření chytrých telefonů a zařízení IoT.

GMLC navíc překonal omezení dřívějších systémů určování polohy tím, že poskytl flexibilní architekturu vyvíjející se spolu se síťovými technologiemi. Od sítí s přepojováním okruhů ve 2G/3G k přepojování paketů ve 4G/5G se GMLC přizpůsobil prostřednictvím rozhraní jako Lg pro MSC a Lg+ pro AMF, čímž zajistil zpětnou i dopřednou kompatibilitu. Jeho vznik umožnil operátorům monetizovat polohová data a zároveň plnit regulatorní požadavky, čímž podpořil ekosystém aplikací LCS. V 5G se GMLC integruje s Network Exposure Function (NEF) pro vystavení lokalizačních schopností aplikacím třetích stran, což zdůrazňuje jeho pokračující relevanci v servisně orientované architektuře.

## Klíčové vlastnosti

- Brána pro externí klienty služeb určování polohy pro zasílání žádostí o určení polohy UE
- Spravuje autentizaci, autorizaci a kontrolu soukromí pro žádosti o polohu
- Komunikuje s HSS/UDM pro zjištění obslužného uzlu UE a směrovacích informací
- Podporuje získávání polohy v reálném čase i odložené napříč generacemi 3GPP
- Zvládá scénáře roamingu prostřednictvím funkcí Requesting GMLC a Home GMLC
- Integruje se s 5G servisně orientovanou architekturou prostřednictvím vystavení přes NEF

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TR 22.935** (Rel-13) — LCS Feasibility Study for 3GPP-WLAN Interworking
- **TS 23.078** (Rel-19) — CAMEL Phase 4 Stage 2 Specification
- **TS 23.127** (Rel-6) — Virtual Home Environment Stage 2 Specification
- **TS 23.141** (Rel-19) — Presence Service Stage 2 Architecture
- **TS 23.171** (Rel-4) — LCS Stage 2 Specification for UMTS
- **TS 23.228** (Rel-19) — IMS Stage-2 Service Description
- **TS 23.271** (Rel-19) — LCS Stage 2 Specification
- **TS 23.273** (Rel-19) — 5G Location Services Stage 2 Architecture
- **TS 23.501** (Rel-20) — 5G System Architecture Stage 2
- **TS 23.700** (Rel-20) — XR Services Application Enablement Layer
- **TR 23.730** (Rel-14) — Study on extended CIoT architecture
- **TS 24.571** (Rel-19) — Control Plane LCS Procedures
- **TS 25.305** (Rel-19) — UTRAN UE Positioning Stage 2
- **TS 28.702** (Rel-19) — Core Network NRM IRP Information Service
- … a dalších 24 specifikací

---

📖 **Anglický originál a plná specifikace:** [GMLC na 3GPP Explorer](https://3gpp-explorer.com/glossary/gmlc/)
