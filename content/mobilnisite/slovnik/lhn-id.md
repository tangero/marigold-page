---
slug: "lhn-id"
url: "/mobilnisite/slovnik/lhn-id/"
type: "slovnik"
title: "LHN-ID – Local Home Network Identifier"
date: 2025-01-01
abbr: "LHN-ID"
fullName: "Local Home Network Identifier"
category: "Identifier"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/lhn-id/"
summary: "Identifikátor pro lokální domácí síť používaný ve specifikacích 3GPP k rozlišení a správě přístupu zařízení v rámci konkrétní domény lokální sítě. Je klíčový pro umožnění lokalizovaných služeb a řízen"
---

LHN-ID je identifikátor pro lokální domácí síť používaný ve specifikacích 3GPP k rozlišení a správě přístupu zařízení v rámci konkrétní domény lokální sítě.

## Popis

Local Home Network Identifier (LHN-ID) je parametr definovaný v protokolech 3GPP core sítě, konkrétně ve vrstvě Non-Access Stratum ([NAS](/mobilnisite/slovnik/nas/)). Slouží jako jedinečný štítek pro lokální domácí síť, což je typicky síť malého rozsahu, jako je rezidenční, podniková nebo kampusová síť využívající technologie jako Home NodeBs ([HNB](/mobilnisite/slovnik/hnb/)) nebo Home eNodeBs (HeNB). LHN-ID je přenášen v signalizačních zprávách NAS, například těch specifikovaných v TS 24.008 pro GSM/UMTS a TS 24.301 pro EPS, což umožňuje core síti identifikovat konkrétní lokální síť, ke které se User Equipment (UE) pokouší připojit nebo je v ní aktuálně registrováno.

Architektonicky je LHN-ID spojen s konceptem Closed Subscriber Groups ([CSG](/mobilnisite/slovnik/csg/)) a hybridních přístupových režimů. Když HeNB/HNB vysílá CSG Identity, může být také nakonfigurována s LHN-ID. Tento identifikátor je hlášen UE do Mobility Management Entity ([MME](/mobilnisite/slovnik/mme/)) v EPS nebo Serving [GPRS](/mobilnisite/slovnik/gprs/) Support Node (SGSN) v UMTS/GPRS během procedur připojení (attachment), aktualizace oblasti sledování (tracking area update) nebo žádosti o službu (service request). Uzel core sítě použije tento identifikátor spolu s daty účastníka z Home Subscriber Server ([HSS](/mobilnisite/slovnik/hss/)) k vynucení pravidel přístupu specifických pro danou lokální síť. Například může určit, zda je UE oprávněna přistupovat k dané konkrétní HeNB/HNB a jaké služby nebo tarifní pravidla jsou v rámci této lokální domény aplikovatelné.

Jeho role přesahuje pouhou identifikaci; umožňuje operátorům sítí nabízet lokalizované služby a diferencované účtování. Rozpoznáním LHN-ID může core síť aplikovat specifické konfigurace [APN](/mobilnisite/slovnik/apn/), politiky QoS nebo dokonce směrovat provoz na lokální bránu (např. Local Gateway ([L-GW](/mobilnisite/slovnik/l-gw/)) nebo HeNB Gateway), která poskytuje přímý výstup do internetu nebo přístup k lokálním IP zdrojům v rámci domácí/podnikové sítě. Tento mechanismus je zásadní pro architekturu 3GPP podporující femtobuňky a small buňky, zajišťující, že zařízení mohou bezproblémově přistupovat jak ke službám širokoplošné makro sítě, tak k lokalizovaným službám, při zachování odpovídající bezpečnosti a vynucování politik.

## K čemu slouží

LHN-ID byl zaveden, aby řešil rostoucí nasazení femtobuněk a small buněk v sítích 3GPP, zejména se standardizací Home eNodeBs (HeNB) v Release 9. Před jeho zavedením byla identifikace sítě pro řízení přístupu a lokalizaci služeb primárně založena na Cell Global Identity (CGI) nebo Tracking Area Identity (TAI), které jsou vázány na polohu rádiové buňky, ale ne nutně na logickou, pro účastníka specifickou doménu lokální sítě. To bylo nedostatečné pro rezidenční nebo podniková nasazení, kde více small buněk může patřit do stejné logické 'domácí' sítě, vyžadující společný identifikátor pro konzistentní aplikaci politik.

Primární problém, který řeší, je potřeba operátora sítě identifikovat a spravovat skupinu small buněk jako jedinou logickou entitu pro účastníka nebo skupinu účastníků. Například v domácnosti s více HeNB je třeba, aby je operátor považoval za část stejné 'domácí sítě' pro služby jako jednotné účtování, přístup ke sdílené lokální IP síti (např. tiskárny, NAS) a konzistentní řízení přístupu. LHN-ID poskytuje tento identifikátor logického seskupení, oddělený od fyzické identity buňky. Umožňuje core síti aplikovat účastnicky specifické politiky relevantní pro kontext lokální sítě, jako je povolení přístupu pouze členům Closed Subscriber Group (CSG) asociované s tímto LHN-ID nebo aplikace speciálních tarifů pro hovory/data v rámci domácí sítě.

Historicky bylo jeho vytvoření motivováno prací 3GPP na vylepšené podpoře HeNB v Release 12, zaměřené na mobilitu a kontinuitu služeb mezi makro sítí a subsystémy HeNB. LHN-ID se stal klíčovým prvkem pro funkce jako CSG mobilita, kde UE pohybující se mezi HeNB patřícími do stejné lokální domácí sítě mohlo zažít bezproblémové předávání hovoru (handover) a konzistentní zacházení se službami bez nutnosti opětovné autentizace nebo přehodnocení politik core sítí při každé změně buňky. Vyplnil mezeru ve schopnosti sítě porozumět logické topologii nasazení small buněk, což je nezbytné pro efektivní správu sítě a vylepšený uživatelský zážitek v heterogenních sítích.

## Klíčové vlastnosti

- Jedinečný identifikátor pro logickou doménu lokální domácí sítě
- Přenášen v signalizačních zprávách NAS (např. Attach Request, Tracking Area Update)
- Používán uzly core sítě (MME/SGSN) pro řízení přístupu a vynucování politik
- Umožňuje asociaci více HeNB/HNB k jedné lokální síti účastníka
- Podporuje poskytování lokalizovaných služeb a diferencované účtování
- Usnadňuje správu mobility v rámci stejné lokální domácí sítě

## Související pojmy

- [CSG – Closed Subscriber Group](/mobilnisite/slovnik/csg/)
- [HENB – Home Enhanced Node B](/mobilnisite/slovnik/henb/)
- [NAS – Non-Access Stratum](/mobilnisite/slovnik/nas/)
- [MME – NPC MME Network Product Class](/mobilnisite/slovnik/mme/)

## Definující specifikace

- **TS 24.008** (Rel-19) — 3GPP TS 24008: Core Network Protocols
- **TS 24.301** (Rel-19) — NAS protocol for Evolved Packet System

---

📖 **Anglický originál a plná specifikace:** [LHN-ID na 3GPP Explorer](https://3gpp-explorer.com/glossary/lhn-id/)
