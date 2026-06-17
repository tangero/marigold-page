---
slug: "cbss"
url: "/mobilnisite/slovnik/cbss/"
type: "slovnik"
title: "CBSS – Controlling Base Station Sub-system"
date: 2025-01-01
abbr: "CBSS"
fullName: "Controlling Base Station Sub-system"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/cbss/"
summary: "CBSS je hlavní řídicí entita v architektuře UTRAN, konkrétně v kontextu rozhraní Iur-g pro GERAN. Spravuje klíčové funkce jako řízení rádiových prostředků, správu mobility a koordinaci přechodů mezi z"
---

CBSS (řídicí subsystém základnové stanice) je hlavní řídicí entita UTRAN pro rozhraní Iur-g, která spravuje rádiové prostředky, mobilitu a přechody mezi základnovými stanicemi (handover) za účelem zajištění plynulé spolupráce mezi BSS v sítích 2G/3G.

## Popis

Řídicí subsystém základnové stanice (CBSS) je základní logická entita definovaná ve specifikacích 3GPP pro GSM/[EDGE](/mobilnisite/slovnik/edge/) Radio Access Network ([GERAN](/mobilnisite/slovnik/geran/)) a její interakci s UMTS Terrestrial Radio Access Network (UTRAN). Funguje v rámci rozhraní Iur-g, což je rozhraní mezi [BSS](/mobilnisite/slovnik/bss/) standardizované pro přímou komunikaci a koordinaci prostředků mezi subsystémy základnových stanic. Architektonicky CBSS není samostatný fyzický uzel, ale určená funkční role, kterou přebírá jeden BSS ve vztahu s jedním nebo více dalšími BSS, které se označují jako řízené BSS. Tento hierarchický řídicí vztah se vytváří za účelem správy procedur vyžadujících koordinaci, jako jsou přechody mezi základnovými stanicemi (handover) a některé úlohy řízení rádiových prostředků.

Během provozu CBSS funguje jako řídicí bod pro konkrétní připojení uživatelského zařízení (UE), která zahrnují prostředky napříč více BSS. Když uživatelské zařízení (UE) je ve scénáři vyžadujícím prostředky z řízeného BSS nebo mobilitu k němu, CBSS si udržuje kontrolu nad hlavní signalizací připojení (jako je připojení řízení rádiových prostředků – [RRC](/mobilnisite/slovnik/rrc/)). Spravuje přidělování rádiových prostředků v řízeném BSS zasíláním řídicích zpráv přes rozhraní Iur-g. To zahrnuje příkazy k zřízení, změně a uvolnění rádiových přenosových kanálů (radio bearers) v buňkách řízeného BSS. CBSS také zajišťuje správu mobility pro UE v rámci domény řízených BSS, rozhoduje o přechodech mezi základnovými stanicemi (handover) a provádí potřebnou signalizaci k přenosu kontextu a provozu UE.

Klíčovými komponentami zapojenými do funkce CBSS jsou softwarové funkce [BSC](/mobilnisite/slovnik/bsc/) (Base Station Controller), které implementují protokolový zásobník rozhraní Iur-g, jak je definováno v 3GPP TS 25.423 a TS 43.130. Tyto protokoly přenášejí řídicí zprávy aplikační části podsystému rádiové sítě (RNSAP) upravené pro kontext GERAN. Role CBSS je klíčová pro funkce jako přímé přechody (Direct Transfer handovers), při kterých je hovor předán přímo mezi dvěma BSS bez zapojení jádra sítě ([MSC](/mobilnisite/slovnik/msc/)) pro přepnutí rádiové cesty, čímž se snižuje latence přechodu a signalizační zátěž jádra sítě. Umožňuje efektivnější využití rádiových prostředků a lepší uživatelský zážitek díky rychlejším, sítí řízeným přechodům mezi různými pokrytími BSS.

## K čemu slouží

Koncept CBSS byl zaveden, aby řešil omezení starších architektur GSM, kde přechody mezi základnovými stanicemi (handover) a koordinace mezi [BSS](/mobilnisite/slovnik/bss/) byly silně závislé na ústředně jádra sítě (Mobile Switching Centre – [MSC](/mobilnisite/slovnik/msc/)). V architekturách před Release 8 vyžadoval přechod mezi BSS, aby MSC fungovala jako centrální kotva: přijímala měřicí reporty, rozhodovala o přechodu a zřizovala novou okruhově spínanou cestu k cílovému BSS. Tento proces, známý jako základní přechod (basic handover), měl za následek významnou latenci a signalizační režii v jádře sítě, což mohlo ovlivnit kvalitu služeb, zejména u služeb citlivých na zpoždění, jako je hlas.

Vytvoření rozhraní Iur-g a role CBSS, standardizovaných od 3GPP Release 8, bylo motivováno potřebou přesunout tuto řídicí funkcionalitu z jádra sítě do rádiové přístupové sítě (RAN). Tím, že umožnilo BSS komunikovat přímo a umožnilo jednomu BSS (CBSS) řídit prostředky v jiném, mohly být přechody mezi základnovými stanicemi provedeny rychleji a efektivněji. Tento přístup, často označovaný jako přímý přenos (Direct Transfer) nebo síťově řízený přechod (Network Controlled handover), snižuje dobu přerušení při přechodu a minimalizuje zapojení MSC. Byl to krok k plošší, inteligentnější architektuře RAN, která zlepšuje celkový výkon sítě a škálovatelnost s rostoucími nároky na datový provoz a mobilitu. Také usnadnil lepší integraci a správu mobility mezi sítěmi GERAN a UTRAN.

## Klíčové vlastnosti

- Slouží jako řídicí entita pro připojení UE přes více BSS prostřednictvím rozhraní Iur-g
- Spravuje přidělování rádiových prostředků a řízení přenosových kanálů (bearer control) v jednom nebo více řízených BSS
- Provádí přímé přechody (Direct Transfer handovers), čímž snižuje latenci díky obcházení jádra sítě při přepínání rádiové cesty
- Udržuje kontrolu nad připojením řízení rádiových prostředků (RRC) pro UE během procedur mezi BSS
- Využívá protokol RNSAP přes Iur-g pro signalizaci a koordinaci mezi BSS
- Zlepšuje správu mobility a kontinuitu služeb v přístupové vrstvě GERAN/UTRAN

## Definující specifikace

- **TS 25.423** (Rel-19) — UTRAN RNSAP Specification
- **TS 43.130** (Rel-19) — Iur-g Interface Overview

---

📖 **Anglický originál a plná specifikace:** [CBSS na 3GPP Explorer](https://3gpp-explorer.com/glossary/cbss/)
