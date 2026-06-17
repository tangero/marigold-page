---
slug: "admf"
url: "/mobilnisite/slovnik/admf/"
type: "slovnik"
title: "ADMF – Administration Function"
date: 2025-01-01
abbr: "ADMF"
fullName: "Administration Function"
category: "Security"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/admf/"
summary: "ADMF (Administration Function) je klíčovou součástí architektury zákonného odposlechu (LI) dle 3GPP. Slouží jako centrální administrativní rozhraní pro oprávněné orgány činné v trestním řízení (LEA) k"
---

ADMF je centrální administrativní rozhraní v architektuře zákonného odposlechu 3GPP, kde oprávněné orgány činné v trestním řízení spravují žádosti o odposlech, aby zajistily řádnou autorizaci a kontrolu.

## Popis

Administration Function (ADMF) je standardizovaný a zabezpečený síťový prvek definovaný v rámci architektury zákonného odposlechu (LI) dle 3GPP. Funguje jako jediný centralizovaný kontaktní bod, přes který orgány činné v trestním řízení (LEA) komunikují s telekomunikační sítí za účelem odposlechu. ADMF je zodpovědné za přijímání, ověřování a zabezpečené předávání soudních příkazů k odposlechu od LEA příslušným síťovým prvkům, které provádějí samotný odposlech, jako je Intercepting Control Element (ICE) v jádru sítě nebo Intercepting Access Point (IAP) v přístupové síti. Jeho primární rolí je administrativní kontrola a distribuce příkazů, což zajišťuje, že odposlechové příkazy jsou provedeny pouze na základě řádného zákonného pověření.

Z architektonického hlediska se ADMF nachází v doméně zákonného odposlechu, která je logicky a často i fyzicky oddělena od domény veřejné sítě, kde protéká uživatelský provoz. S LEA komunikuje prostřednictvím předávacího rozhraní (HI), konkrétně rozhraní HI1, které slouží pro výměnu administrativních informací souvisejících s odposlechem (např. údaje o soudním příkazu, identifikátory cíle). Uvnitř sítě ADMF komunikuje s odposlechovými body sítě (např. ICE) prostřednictvím interního síťového rozhraní (INI), konkrétně rozhraní X1. Toto oddělení rozhraní (HI pro externí komunikaci s LEA a X1/INI pro interní síťovou komunikaci) je základním bezpečnostním principem, který brání LEA v přímém přístupu k síťovému zařízení.

Fungování ADMF zahrnuje několik klíčových procesů. Po přijetí žádosti o odposlech přes HI1 provede autentizaci LEA a ověří zákonné pověření. Poté převede obecný soudní příkaz (obsahující cílové identifikátory, jako je MSISDN nebo IMSI) na konkrétní technické odposlechové příkazy určené pro příslušné síťové uzly (např. SGSN nebo MME). Tyto příkazy, odeslané přes rozhraní X1, instruují ICE, aby zahájil odposlech komunikačního obsahu (CC) a informací souvisejících s odposlechem (IRI) určeného cíle. ADMF také spravuje životní cyklus odposlechu, řeší modifikace, obnovy a deaktivace a může poskytovat LEA hlášení o stavu.

Kritickým aspektem ADMF je jeho role při udržování zprostředkování a izolace. Zprostředkovává komunikaci mezi právním/administrativním světem LEA a technickým světem sítě, přičemž zajišťuje správné formátování a cílení příkazů. Zároveň izoluje LEA od interní topologie a konfigurace sítě, čímž poskytuje vrstvu abstrakce pro bezpečnost a jednoduchost. ADMF nezpracovává samotná odposlechnutá data; ta jsou doručována samostatně prvkem ICE/IAP LEA prostřednictvím rozhraní HI2 (pro IRI) a HI3 (pro CC). Tato architektura zajišťuje jasné oddělení odpovědností: správa (ADMF), odposlech (ICE/IAP) a doručení (Mediation Function pro HI2/HI3).

## K čemu slouží

ADMF bylo vytvořeno, aby řešilo kritickou potřebu standardizované, zabezpečené a zákonu odpovídající metody pro zákonný odposlech (LI) v mobilních sítích 3GPP. Před standardizací byly možnosti odposlechu často specifické pro dodavatele, neinteroperabilní a postrádaly jasné oddělení přístupu orgánů činných v trestním řízení od síťových operací, což představovalo riziko pro integritu sítě a soukromí uživatelů. Rozšíření digitální mobilní komunikace si vyžádalo architekturu, kterou by bylo možné jednotně implementovat u různých síťových operátorů a dodavatelů zařízení po celém světě, a zajistit tak, aby orgány činné v trestním řízení mohly efektivně provádět zákonně nařízené odposlechy bez ohledu na podkladovou síťovou technologii.

Hlavním problémem, který ADMF řeší, je zabezpečená a kontrolovaná správa soudních příkazů k odposlechu. Bez centralizované administrativní funkce by LEA musely přímo komunikovat s různými síťovými prvky, což je nebezpečné, neefektivní a mohlo by to odhalit citlivou síťovou infrastrukturu. ADMF poskytuje jedinou kontrolovanou bránu. Zajišťuje, že každá odposlechová akce je předcházena ověřeným zákonným procesem, a tím brání neoprávněnému sledování. To je zásadní pro udržení právního státu, ochranu soukromí účastníků a budování důvěry v systémy digitální komunikace.

ADMF navíc umožňuje škálovatelnost a spravovatelnost. Jak se sítě vyvíjely od 2G/GSM přes 3G/UMTS a dále, rostla složitost síťové architektury. ADMF, zavedené ve verzi 3GPP Release 8 jako součást propracovanější architektury LI, poskytlo model připravený na budoucnost. Odstiňuje od LEA složitost sítě, což umožňuje, aby byly nové síťové funkce (jako MME v LTE nebo AMF v 5G) integrovány do systému LI jednoduše tím, že ADMF komunikuje s jejich odpovídajícím ICE. Tento návrh odstranil omezení dřívějších, více ad-hoc přístupů tím, že vytvořil jasné, modulární a standardy založené rozhraní pro správu zákonného odposlechu.

## Klíčové vlastnosti

- Centralizovaná správa soudních příkazů a správa životního cyklu (aktivace, modifikace, deaktivace)
- Zabezpečené rozhraní (HI1) pro komunikaci s orgány činnými v trestním řízení (LEA)
- Interní rozhraní (X1) pro vydávání příkazů prvkům Intercepting Control Elements (ICE) v síti
- Ověření zákonného pověření a autentizace LEA
- Zprostředkování mezi právními/administrativními požadavky a technickými síťovými příkazy
- Izolace LEA od přímého přístupu k síťové infrastruktuře a topologii

## Definující specifikace

- **TS 33.107** (Rel-19) — Lawful Interception Architecture & Functions
- **TS 33.126** (Rel-19) — Lawful Interception Requirements
- **TS 33.127** (Rel-19) — Lawful Interception Architecture and Functions
- **TS 33.128** (Rel-19) — 3GPP TS 33.128: Lawful Interception Protocols
- **TS 43.033** (Rel-13) — Lawful Interception Stage 2 for GSM/GPRS

---

📖 **Anglický originál a plná specifikace:** [ADMF na 3GPP Explorer](https://3gpp-explorer.com/glossary/admf/)
