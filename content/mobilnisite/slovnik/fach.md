---
slug: "fach"
url: "/mobilnisite/slovnik/fach/"
type: "slovnik"
title: "FACH – Forward Access Channel"
date: 2025-01-01
abbr: "FACH"
fullName: "Forward Access Channel"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/fach/"
summary: "Společný downlinkový transportní kanál v UMTS používaný pro přenos řídicích informací a malého množství uživatelských dat do mobilních zařízení. Je klíčovým kanálem pro počáteční přístup k síti, odpov"
---

FACH je společný (common) downlinkový transportní kanál v UMTS pro vysílání řídicích informací a malých paketů uživatelských dat do mobilních zařízení. Používá se pro přístup k síti, odpovědi na paging a přenos dat s nízkým objemem bez uzavřené smyčky řízení výkonu.

## Popis

Forward Access Channel (FACH) je základní downlinkový transportní kanál v UMTS (WCDMA) rádiové přístupové síti (UTRAN). Je to společný kanál (common channel), což znamená, že není vyhrazen pro jediného uživatele, ale mohou jej přijímat vícečetná uživatelská zařízení (UE) v rámci buňky. FACH je mapován na fyzický kanál Secondary Common Control Physical Channel (S-CCPCH) ve fyzické vrstvě. Jeho primární rolí je přenášet řídicí signalizaci ze sítě k UE, zejména pro procedury, které nevyžadují zřízení vyhrazeného kanálu ([DCH](/mobilnisite/slovnik/dch/)), jako je nastavení hovoru, odpověď na paging nebo procedury aktualizace buňky. Může také přenášet malá množství dat uživatelské roviny, což jej činí vhodným pro služby paketové komunikace s nízkou přenosovou rychlostí a bursty charakterem.

Z architektonického hlediska je FACH ukončen v radiovém síťovém řadiči (RNC). RNC používá FACH ke komunikaci s UE ve stavu Cell_FACH, což je jeden z několika stavů spojení řízení rádiových prostředků ([RRC](/mobilnisite/slovnik/rrc/)). V tomto stavu je UE síti známo na úrovni buňky, ale nemá mu přidělen vyhrazený kanál. FACH je vysílán přes celou buňku nebo konkrétní sektor a nepoužívá rychlé řízení výkonu. Místo toho je typicky vysílán s pevnou, relativně vysokou úrovní výkonu, aby bylo zajištěno, že jej mohou přijímat UE na okraji buňky, což při rozsáhlém použití ovlivňuje celkovou kapacitu buňky.

Jak funguje, zahrnuje adresování. Zprávy na FACH obsahují identifikátor UE (jako U-RNTI nebo [C-RNTI](/mobilnisite/slovnik/c-rnti/)), takže vícečetná UE naslouchající stejnému kanálu mohou rozpoznat, které zprávy jsou určeny pro ně. Když UE potřebuje odeslat uplinková data nebo signalizaci ve stavu Cell_FACH, používá pro uplink náhodný přístupový kanál (RACH), čímž vytváří spárovanou kombinaci FACH/RACH pro komunikaci s nízkou aktivitou. FACH hraje klíčovou roli v přechodech mezi stavy; například při zvýšení datové aktivity může síť pomocí zprávy odeslané na samotném FACH nařídit UE přejít do stavu Cell_DCH. Jeho návrh představuje kompromis mezi režií signalizace, efektivitou alokace prostředků a spotřebou baterie UE pro zařízení s nízkou aktivitou.

## K čemu slouží

FACH byl vytvořen jako klíčová komponenta UMTS pro efektivní správu rádiových prostředků pro velkou populaci mobilních zařízení s různorodými a často sporadickými komunikačními potřebami. Ve světě 2G, dominovaném přepojováním okruhů, byly pro jakékoli aktivní spojení normou vyhrazené kanály. Pro paketová data a mnoho signalizačních scénářů je udržování vyhrazeného kanálu s rychlým řízením výkonu pro každé UE z hlediska kódových a výkonových prostředků vysoce neefektivní. FACH tento problém řeší tím, že poskytuje sdílenou, vždy dostupnou downlinkovou cestu pro řídicí informace a malé datové bursty.

Řeší problém, jak udržet UE registrované a dosažitelné sítí bez spotřeby vyhrazených prostředků. Umožňuje stav Cell_FACH, což je stav s nízkou režií, ale zároveň připojený, který překlenuje propast mezi režimem nečinnosti (Cell_PCH, URA_PCH) a režimem vyhrazeného kanálu s vysokou aktivitou (Cell_[DCH](/mobilnisite/slovnik/dch/)). Tento stavový stroj je zásadní pro optimalizaci výdrže baterie a správu kapacity sítě. FACH umožňuje síti pagovat UE, doručovat broadcastové systémové informace a zvládat počáteční přístupové procedury, čímž tvoří páteř správy spojení v UMTS. Jeho podpora malých paketových dat byla zvláště důležitá pro rané služby mobilních dat v režimu 'vždy zapnuto', což umožňovalo efektivní přenos keep-alive zpráv nebo malých TCP potvrzení bez latence spojené se zřizováním DCH.

## Klíčové vlastnosti

- Společný downlinkový transportní kanál pro vícečetná UE
- Mapován na fyzický kanál S-CCPCH
- Podporuje UE ve stavu RRC Cell_FACH
- Přenáší jak signalizaci řídicí roviny, tak malé pakety uživatelských dat
- Funguje bez rychlého (uzavřené smyčky) řízení výkonu
- Pro adresování zpráv používá identifikátory specifické pro UE

## Související pojmy

- [DCH – Dedicated Channel](/mobilnisite/slovnik/dch/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 25.101** (Rel-19) — UTRA FDD UE RF Requirements
- **TS 25.171** (Rel-19) — A-GPS Minimum Performance Requirements for UTRA FDD UE
- **TS 25.202** (Rel-19) — 7.68Mcps TDD Option Technical Specification
- **TS 25.211** (Rel-19) — UTRA FDD Layer 1: Transport & Physical Channels
- **TS 25.212** (Rel-19) — UTRA FDD Layer 1 Multiplexing & Channel Coding
- **TS 25.214** (Rel-19) — UTRA FDD Physical Layer Procedures
- **TS 25.221** (Rel-19) — UTRA TDD Physical Layer Specification
- **TS 25.222** (Rel-19) — UTRA TDD Multiplexing & Channel Coding
- **TS 25.224** (Rel-19) — UTRA TDD Physical Layer Procedures
- **TS 25.225** (Rel-19) — UTRA TDD Physical Layer Measurements
- **TS 25.301** (Rel-19) — UE-UTRAN Radio Interface Protocol Architecture
- **TS 25.302** (Rel-19) — UTRA Physical Layer Services
- **TS 25.321** (Rel-19) — MAC Protocol Specification for UTRAN
- **TS 25.322** (Rel-19) — RLC Protocol Specification
- … a dalších 14 specifikací

---

📖 **Anglický originál a plná specifikace:** [FACH na 3GPP Explorer](https://3gpp-explorer.com/glossary/fach/)
