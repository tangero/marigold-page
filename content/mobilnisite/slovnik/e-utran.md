---
slug: "e-utran"
url: "/mobilnisite/slovnik/e-utran/"
type: "slovnik"
title: "E-UTRAN – Evolved Universal Terrestrial Radio Access Network"
date: 2026-01-01
abbr: "E-UTRAN"
fullName: "Evolved Universal Terrestrial Radio Access Network"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/e-utran/"
summary: "Rádiová přístupová síť pro systémy 4G LTE, skládající se z eNodeB, které připojují uživatelská zařízení k Evolved Packet Core. Zavedla plochou, čistě IP architekturu se zjednodušenými síťovými uzly, c"
---

E-UTRAN je rádiová přístupová síť pro systémy 4G LTE, která se skládá z eNodeB, jež připojují uživatelská zařízení k Evolved Packet Core.

## Popis

E-UTRAN je rádiová přístupová síť definovaná standardem 3GPP pro systém Long-Term Evolution (LTE), počínaje Release 8. Její architektura je radikálním odklonem od hierarchické struktury ovlivněné přepojováním okruhů, kterou měl její předchůdce [UTRAN](/mobilnisite/slovnik/utran/) (3G). Hlavním síťovým prvkem je evolved NodeB (eNodeB nebo [eNB](/mobilnisite/slovnik/enb/)), který integruje funkce radiového síťového kontroléru ([RNC](/mobilnisite/slovnik/rnc/)) ze sítí 3G do jediné stanice. Tím vzniká plochá, distribuovaná architektura, kde se eNodeB přímo připojují k Evolved Packet Core (EPC) přes rozhraní S1 a k sobě navzájem přes rozhraní [X2](/mobilnisite/slovnik/x2/) pro přímou koordinaci mezi buňkami a správu předávání spojení. Toto zjednodušení snižuje latenci a zlepšuje efektivitu pro paketově přepínaný provoz.

Z funkčního hlediska eNodeB zajišťuje všechny rádiové funkce pro buňky, které obsluhuje. To zahrnuje správu rádiových prostředků ([RRM](/mobilnisite/slovnik/rrm/)), jako je plánování, adaptace spojení a řízení výkonu; kompresi hlaviček a šifrování uživatelských dat; a také kompletní sadu protokolů Radio Resource Control ([RRC](/mobilnisite/slovnik/rrc/)) pro vytváření spojení, mobilitu a aktivaci zabezpečení. Uživatelská protokolová zásobník mezi uživatelským zařízením (UE) a eNodeB se skládá z vrstev Packet Data Convergence Protocol ([PDCP](/mobilnisite/slovnik/pdcp/)), Radio Link Control ([RLC](/mobilnisite/slovnik/rlc/)) a Medium Access Control (MAC), které jsou ukončeny v eNB. Řídicí zásobník zahrnuje protokoly RRC a Non-Access Stratum (NAS), přičemž zprávy NAS jsou transparentně přeposílány mezi UE a Mobility Management Entity (MME) v páteřní síti.

E-UTRAN podporuje duplexní režimy Frequency Division Duplex (FDD) a Time Division Duplex (TDD), což nabízí flexibilitu ve využití spektra. Zavedl pokročilé technologie fyzické vrstvy, jako je Orthogonal Frequency Division Multiple Access (OFDMA) pro downlink a Single-Carrier FDMA (SC-FDMA) pro uplink, které poskytují vysokou spektrální účinnost a odolnost vůči vícecestnému útlumu. Klíčové výkonnostní cíle pro E-UTRAN zahrnovaly špičkové datové rychlosti přesahující 100 Mbps pro stahování a 50 Mbps pro nahrávání, latenci uživatelské roviny pod 10 ms a škálovatelné šířky pásma od 1,4 MHz do 20 MHz. Její koncepce jako čistě paketově přepínané sítě od základů byla klíčová pro umožnění revoluce mobilního broadbandu, poskytující vysokorychlostní připojení s nízkou latencí potřebné pro moderní internetové služby a aplikace.

## K čemu slouží

E-UTRAN byl vytvořen, aby řešil rostoucí poptávku po mobilních datových službách a omezení sítí 3G UMTS/UTRAN, které byly původně navrženy s důrazem na přepojování okruhů pro hlas. Hlavními motivy bylo dosáhnout výrazného skoku v datových rychlostech, snížit latenci, zlepšit spektrální účinnost a snížit náklady na přenesený bit pro operátory. Stávající architektura UTRAN s oddělenými NodeB a radiovými síťovými kontroléry (RNC) vytvářela úzká místa a složitost pro zpracování objemového IP provozu. Cílem bylo navrhnout síť optimalizovanou pro IP služby od samého počátku.

Vývoj LTE a E-UTRAN byl hnán potřebou konkurovat jiným vyvíjejícím se bezdrátovým broadbandovým technologiím a splnit uživatelská očekávání pro internetové zážitky srovnatelné s pevným broadbandem. Plochá, čistě IP architektura E-UTRAN odstranila RNC a distribuovala jeho inteligenci do eNodeB. Toto zjednodušení snížilo počet síťových prvků zapojených do přenosu dat, čímž se snížila latence – kritický faktor pro interaktivní služby, jako je hraní her a VoIP. Nové rozhraní založené na OFDMA navíc poskytovalo lepší výkon v náročných rádiových podmínkách a efektivnější využití spektra, což je pro operátory vzácný a drahý zdroj.

E-UTRAN nakonec posloužil jako základ pro skutečný 4G mobilní broadband. Vyřešil problém škálování sítí pro exponenciální růst dat při zachování kvality služeb. Jeho konstrukční principy jednoduchosti, účinnosti a čistě IP provozu nejen definovaly éru LTE, ale také významně ovlivnily následnou architekturu 5G NR (New Radio), kde se z monolitického konceptu eNB vyvinul podobný disagregovaný model RAN s centrálními a distribuovanými jednotkami (CU/DU).

## Klíčové vlastnosti

- Plochá, čistě IP architektura s integrovaným eNodeB nahrazujícím NodeB a RNC
- Podpora duplexních režimů FDD i TDD se škálovatelnou šířkou kanálu
- Využití OFDMA v downlinku a SC-FDMA v uplinku pro vysokou spektrální účinnost
- Přímá komunikace mezi eNodeB přes rozhraní X2 pro rychlé předávání spojení a koordinaci interference
- Integrovaná správa rádiových prostředků (RRM) včetně plánování, adaptace spojení a řízení výkonu
- Podpora pokročilých MIMO (Multiple-Input Multiple-Output) anténních technologií

## Související pojmy

- [LTE – Local Terminal Emulator](/mobilnisite/slovnik/lte/)
- [EPC – Evolved Packet Core Network](/mobilnisite/slovnik/epc/)
- [OFDMA – Orthogonal Frequency Division Multiple Access](/mobilnisite/slovnik/ofdma/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.009** (Rel-19) — Handover Procedures in PLMNs
- **TS 23.060** (Rel-19) — GPRS Service Description Stage 2
- **TS 23.179** (Rel-13) — MCPTT Functional Architecture
- **TS 23.203** (Rel-19) — Policy and charging control architecture
- **TS 23.221** (Rel-19) — 3GPP System Architectural Requirements
- **TS 23.251** (Rel-19) — Network Sharing Stage 2 Specification
- **TS 23.280** (Rel-20) — Common Architecture for Mission Critical Services
- **TS 23.281** (Rel-20) — MCVideo Functional Architecture and Flows
- **TS 23.286** (Rel-19) — V2X Application Enabler Architecture
- **TS 23.379** (Rel-20) — MCPTT Functional Architecture
- **TS 23.401** (Rel-19) — Evolved Packet System (EPS) Stage 2 Description
- **TS 23.479** (Rel-19) — MBMS API for Mission Critical Services
- **TR 23.758** (Rel-17) — Study on Edge Application Architecture
- **TS 23.795** (Rel-16) — V2X Application Architecture Study
- … a dalších 116 specifikací

---

📖 **Anglický originál a plná specifikace:** [E-UTRAN na 3GPP Explorer](https://3gpp-explorer.com/glossary/e-utran/)
