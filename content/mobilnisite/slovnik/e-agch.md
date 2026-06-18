---
slug: "e-agch"
url: "/mobilnisite/slovnik/e-agch/"
type: "slovnik"
title: "E-AGCH – EDCH – Absolute Grant Channel"
date: 2025-01-01
abbr: "E-AGCH"
fullName: "EDCH – Absolute Grant Channel"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/e-agch/"
summary: "Downlinkový fyzický kanál v UMTS/HSPA, který Node B používá k vysílání příkazů absolutního povolení (absolute grant) k uživatelským zařízením (UE). Tyto příkazy přímo nastavují maximální povolený výko"
---

E-AGCH je downlinkový kanál v UMTS/HSPA, který Node B používá k vysílání příkazů absolutního povolení (absolute grant), které přímo nastavují maximální výkon pro uplinkový E-DCH uživatelského zařízení (UE) za účelem řízení interference a datových rychlostí.

## Popis

Kanál absolutního povolení pro [E-DCH](/mobilnisite/slovnik/e-dch/) (E-AGCH) je vyhrazený downlinkový fyzický řídicí kanál v rámci funkce High-Speed Uplink Packet Access ([HSUPA](/mobilnisite/slovnik/hsupa/)) v UMTS (3G). Funguje jako součást architektury rozšířeného vyhrazeného kanálu (E-DCH), která výrazně zlepšuje datové rychlosti a kapacitu v uplinku. Primární funkcí E-AGCH je přenos příkazů absolutního povolení (Absolute Grant) z Node B (základnové stanice) ke konkrétnímu uživatelskému zařízení (UE). Absolutní povolení je příkaz, který explicitně nastavuje maximální povolený poměr výkonů [E-DPDCH](/mobilnisite/slovnik/e-dpdch/)/[DPCCH](/mobilnisite/slovnik/dpcch/) pro uživatelské zařízení, což přímo určuje maximální datovou rychlost uplinkového přenosu, kterou může uživatelské zařízení použít.

Z architektonického hlediska je E-AGCH sdílený kanál mapovaný na sekundární společný řídicí fyzický kanál ([S-CCPCH](/mobilnisite/slovnik/s-ccpch/)) v downlinku. Používá specifický kanalizační kód a je asociován s dočasným identifikátorem rádiové sítě pro E-DCH ([E-RNTI](/mobilnisite/slovnik/e-rnti/)) pro adresování jednotlivých uživatelských zařízení nebo jejich skupin. Kanál přenáší malý transportní blok pevné velikosti obsahující hodnotu absolutního povolení a důležitý příznak „Primary/Secondary“ (primární/sekundární). Tento příznak udává, zda se povolení vztahuje na obsluhující buňku E-DCH uživatelského zařízení (primární povolení), nebo na neobsluhující buňku při měkčím/měkkém předání spojení (sekundární povolení), což umožňuje koordinované řízení interference mezi více buňkami.

Během provozu plánovač v Node B průběžně monitoruje interferenci v uplinku (měřenou jako Rise Over Thermal – RoT) a hlášení o stavu vyrovnávací paměti od uživatelských zařízení. Na základě těchto informací a požadavků na kvalitu služeb (QoS) plánovač rozhodne o vhodné datové rychlosti pro každé uživatelské zařízení. Poté vyšle příkaz absolutního povolení na kanálu E-AGCH. Po přijetí svého povolení uživatelské zařízení okamžitě odpovídajícím způsobem upraví svůj uplinkový vysílací výkon a vybere kombinaci transportních formátů ([TFC](/mobilnisite/slovnik/tfc/)), která nepřekračuje povolený poměr výkonů. Tento proces probíhá velmi rychle (každých 2 ms nebo 10 ms přenosový časový interval – [TTI](/mobilnisite/slovnik/tti/)), což umožňuje velmi rychlé plánování řízené Node B.

Role E-AGCH je klíčová pro výkon HSUPA. Poskytuje Node B přímou a rychlou kontrolu nad uplinkem, což je zásadní pro řízení interference v CDMA rádiovém rozhraní UMTS. Řízením maximálního výkonu, který může každé uživatelské zařízení použít, může Node B zabránit přetížení buňky, upřednostnit uživatele s vysokými nároky na QoS a maximalizovat celkovou propustnost buňky. To je v kontrastu s pomalejším plánováním řízeným RNC používaným v UMTS před zavedením HSUPA. E-AGCH spolupracuje s kanálem relativního povolení (E-RGCH) pro jemné doladění a s kanálem indikátoru HARQ (E-HICH) pro potvrzení, čímž tvoří jádro mechanismu rychlého plánování a hybridního ARQ v HSUPA.

## K čemu slouží

E-AGCH byl vytvořen jako součást HSUPA (3GPP Release 6) k řešení základních omezení původního uplinku UMTS Release 99. V Release 99 byly datové rychlosti v uplinku na vyhrazeném kanálu (DCH) řízeny výhradně řadičem rádiové sítě (RNC), který byl příliš pomalý a vzdálený od rádiového rozhraní, aby mohl rychle reagovat na měnící se rádiové podmínky a úrovně interference. To vedlo k neefektivnímu využití uplinkových zdrojů, nestabilním úrovním interference a neschopnosti efektivně podporovat paketové služby s vysokou datovou rychlostí.

Primární motivací bylo přesunout pravomoc pro uplinkové plánování na Node B, tedy entitu, která přímo zaznamenává uplinkovou interferenci. Tento koncept, známý jako plánování v Node B nebo rychlé plánování, vyžadoval nízkolatenční, spolehlivý signalizační kanál z Node B k uživatelskému zařízení – a proto byl vytvořen E-AGCH. Absolutní povolení poskytuje „tvrdý“ limit, což dává Node B deterministickou kontrolu pro rychlé zvýšení nebo zastavení uplinkového přenosu uživatelského zařízení za účelem řízení celkového nárůstu šumu v buňce.

Řešil tak problém „near-far“ efektu v CDMA, kde jedno uživatelské zařízení vysílající na vysoký výkon mohlo přehlušit signály mnoha dalších uživatelů a způsobit kolaps kapacity buňky. Použitím E-AGCH mohl Node B vynucovat přísné limity, čímž zajišťoval spravedlnost a stabilitu. To bylo nezbytné pro umožnění vysokorychlostního uplinku s nízkou latencí, vyžadovaného aplikacemi jako videokonference, nahrávání velkých souborů a interaktivní hry přes 3G sítě, což představovalo zásadní vývoj od služeb dominovaných přepojováním okruhů k dominanci přepojování paketů.

## Klíčové vlastnosti

- Přenáší příkazy absolutního povolení (Absolute Grant), které nastavují maximální poměr uplinkového výkonu uživatelského zařízení (UE).
- Umožňuje rychlé (2ms/10ms TTI) plánování v uplinku řízené Node B.
- Pro adresování konkrétních uživatelských zařízení (UE) nebo jejich skupin používá E-RNTI.
- Obsahuje příznak Primary/Secondary (primární/sekundární) pro povolení pro obsluhující a neobsluhující buňku.
- Je mapován na downlinkový fyzický kanál S-CCPCH.
- Je zásadní pro řízení interference a maximalizaci kapacity v HSUPA.

## Související pojmy

- [E-DCH – Enhanced Dedicated Channel](/mobilnisite/slovnik/e-dch/)
- [E-RGCH – E-DCH Relative Grant Channel](/mobilnisite/slovnik/e-rgch/)
- [E-HICH – EDCH HARQ Acknowledgement Indicator Channel](/mobilnisite/slovnik/e-hich/)
- [HSUPA – High Speed Uplink Packet Access](/mobilnisite/slovnik/hsupa/)

## Definující specifikace

- **TS 25.101** (Rel-19) — UTRA FDD UE RF Requirements
- **TS 25.102** (Rel-19) — UTRA TDD RF Characteristics
- **TS 25.202** (Rel-19) — 7.68Mcps TDD Option Technical Specification
- **TS 25.211** (Rel-19) — UTRA FDD Layer 1: Transport & Physical Channels
- **TS 25.212** (Rel-19) — UTRA FDD Layer 1 Multiplexing & Channel Coding
- **TS 25.213** (Rel-19) — UTRA FDD Spreading and Modulation
- **TS 25.214** (Rel-19) — UTRA FDD Physical Layer Procedures
- **TS 25.221** (Rel-19) — UTRA TDD Physical Layer Specification
- **TS 25.222** (Rel-19) — UTRA TDD Multiplexing & Channel Coding
- **TS 25.224** (Rel-19) — UTRA TDD Physical Layer Procedures
- **TS 25.225** (Rel-19) — UTRA TDD Physical Layer Measurements
- **TS 25.302** (Rel-19) — UTRA Physical Layer Services
- **TS 25.309** (Rel-6) — FDD Enhanced Uplink Support
- **TS 25.319** (Rel-19) — Enhanced Uplink for UTRA FDD/TDD
- **TS 25.321** (Rel-19) — MAC Protocol Specification for UTRAN
- … a dalších 8 specifikací

---

📖 **Anglický originál a plná specifikace:** [E-AGCH na 3GPP Explorer](https://3gpp-explorer.com/glossary/e-agch/)
