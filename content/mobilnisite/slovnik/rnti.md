---
slug: "rnti"
url: "/mobilnisite/slovnik/rnti/"
type: "slovnik"
title: "RNTI – Radio Network Temporary Identifier"
date: 2025-01-01
abbr: "RNTI"
fullName: "Radio Network Temporary Identifier"
category: "Identifier"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/rnti/"
summary: "Dočasný identifikátor přiřazený rádiovou přístupovou sítí (RAN) uživatelskému zařízení (UE) pro komunikaci přes rozhraní Uu (vzdušné rozhraní). Je klíčový pro adresování a rozlišení uživatelů v buňce,"
---

RNTI je dočasný identifikátor přiřazený rádiovou přístupovou sítí (RAN) uživatelskému zařízení (UE) pro jeho adresování a rozlišení v buňce za účelem plánování a zabezpečeného přenosu dat v LTE a 5G NR.

## Popis

Radio Network Temporary Identifier (RNTI) je základní adresovací mechanismus v sítích 3GPP LTE ([E-UTRA](/mobilnisite/slovnik/e-utra/)) a 5G NR (New Radio). Jedná se o 16bitovou nebo 24bitovou hodnotu, kterou gNB (v NR) nebo [eNB](/mobilnisite/slovnik/enb/) (v LTE) přiřadí konkrétnímu uživatelskému zařízení (UE) nebo skupině UE na dobu trvání spojení nebo konkrétní procedury. RNTI není trvalá identita účastníka jako [IMSI](/mobilnisite/slovnik/imsi/); jde o dočasný, kontextově specifický identifikátor používaný výhradně přes rádiové rozhraní Uu mezi UE a základnovou stanicí. Jeho primární role je skramblovat kontrolní součet [CRC](/mobilnisite/slovnik/crc/) (Cyclic Redundancy Check) připojený ke zprávám [DCI](/mobilnisite/slovnik/dci/) (Downlink Control Information) přenášeným na kanálu [PDCCH](/mobilnisite/slovnik/pdcch/) (Physical Downlink Control Channel). Když UE úspěšně deskrambluje CRC zprávy DCI pomocí svého přiřazeného RNTI, ví, že následující plánovací informace na [PDSCH](/mobilnisite/slovnik/pdsch/) nebo [PUSCH](/mobilnisite/slovnik/pusch/) jsou určeny právě jí.

Z architektonického hlediska RNTI funguje v rámci vrstev MAC (Medium Access Control) a PHY (Physical). Plánovač základnové stanice používá různé typy RNTI pro správu různých kanálů a procedur. Například C-RNTI (Cell-RNTI) je jednoznačně přiřazeno UE ve stavu RRC_CONNECTED pro plánování dat uživatelské roviny. Dočasné C-RNTI (Temporary C-RNTI) se používá během náhodného přístupu. Jiná RNTI, jako P-RNTI (Paging RNTI) a SI-RNTI (System Information RNTI), jsou společná všem UE v buňce pro vysílání stránkovacích zpráv a systémových informačních bloků (SIB). Proces je dynamický: UE monitoruje PDCCH pro formáty DCI skramblované pomocí RNTI relevantních pro její stav. Po detekci dekóduje přidružený datový kanál (PDSCH pro downlink, PUSCH pro uplink) podle pokynů v DCI.

Mechanismus RNTI je klíčový pro efektivitu a zabezpečení sítě. Umožňuje přesné plánování a multiplexování více UE na sdílených časově-frekvenčních zdrojích. Použitím různých typů RNTI může síť efektivně spravovat společné procedury (vysílání, paging, náhodný přístup) a vyhrazená spojení bez vystavování trvalých identit přes vzdušné rozhraní, čímž zvyšuje soukromí uživatelů. V 5G NR byl koncept rozšířen o další typy RNTI, jako je CS-RNTI (Configured Scheduling RNTI) pro grant-free uplink přenos a MCS-C-RNTI (Modulation and Coding Scheme Cell RNTI) pro indikaci specifických MCS tabulek, což podporuje pokročilejší funkce a případy užití.

## K čemu slouží

RNTI bylo zavedeno, aby řešilo kritické problémy efektivního řízení rádiových zdrojů a soukromí uživatelů v paketově přepínaných mobilních systémech, a vyvinulo se z TLLI (Temporary Logical Link Identifier) v GPRS. V dřívějších okruhově přepínaných systémech byl kanál vyhrazen na dobu volání, což vyžadovalo méně dynamické adresování. S příchodem all-IP architektury LTE se sdílenými kanály byl potřebný mechanismus pro rychlé a jednoznačné adresování konkrétního UE mezi stovkami v buňce pro každý přenosový časový interval (TTI), aniž by se používaly trvalé identifikátory ohrožující zabezpečení.

Jeho vytvoření bylo motivováno potřebou plánovacího identifikátoru s nízkou režií a vysokou rychlostí. RNTI umožňuje plánovači základnové stanice směrovat řídicí informace ke správnému UE s minimálním počtem bitů. Skramblováním CRC v DCI poskytuje jak adresování, tak lehkou kontrolu integrity. Tento návrh je mnohem efektivnější než vkládání plné adresy do každé řídicí zprávy. Řeší také problém kolizí na společných kanálech; například RA-RNTI (Random Access RNTI) identifikuje, na kterém časově-frekvenčním zdroji byl odeslán preambule náhodného přístupu, což umožňuje síti odpovědět správnému UE ještě před přiřazením vyhrazeného C-RNTI.

RNTI dále řeší omezení statického adresování ve vysoce mobilním prostředí. Když se UE pohybuje, mění se její obsluhující buňka a s ní může změnit i své C-RNTI. Tato dočasná, buňkově specifická povaha zjednodušuje procedury předávání spojení a převýběr buňky. Evoluce do 5G NR si vyžádala nové typy RNTI pro podporu funkcí jako části šířky pásma (bandwidth parts), komunikace s ultra-spolehlivým nízkým zpožděním (URLLC) a síťové řezy (network slicing), což demonstruje flexibilitu RNTI jako základního stavebního kamene pro dynamické přidělování rádiových zdrojů v moderních mobilních sítích.

## Klíčové vlastnosti

- 16bitový (LTE) nebo 24bitový (5G NR) dočasný identifikátor přiřazený RAN
- Skrambluje CRC (kontrolní součet) DCI (Downlink Control Information) na PDCCH
- Více typů pro různé účely (C-RNTI, P-RNTI, SI-RNTI, RA-RNTI)
- Umožňuje efektivní plánování a multiplexování UE na sdílených kanálech
- Zvyšuje zabezpečení vzdušného rozhraní tím, že se vyhne přenosu trvalých ID
- Dynamické přiřazení a změna během předávání spojení a změn stavů připojení

## Související pojmy

- [C-RNTI – Cell Radio Network Temporary Identifier](/mobilnisite/slovnik/c-rnti/)
- [PDCCH – Physical Downlink Control Channel](/mobilnisite/slovnik/pdcch/)
- [DCI – Downlink Control Information](/mobilnisite/slovnik/dci/)
- [MAC – Message Authentication Code](/mobilnisite/slovnik/mac/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.060** (Rel-19) — GPRS Service Description Stage 2
- **TS 23.221** (Rel-19) — 3GPP System Architectural Requirements
- **TR 23.923** (Rel-4) — Mobile IP+ Feasibility Study for UMTS/GPRS
- **TS 25.301** (Rel-19) — UE-UTRAN Radio Interface Protocol Architecture
- **TS 25.302** (Rel-19) — UTRA Physical Layer Services
- **TS 25.303** (Rel-19) — Radio Resource Control Procedures
- **TS 25.321** (Rel-19) — MAC Protocol Specification for UTRAN
- **TS 25.322** (Rel-19) — RLC Protocol Specification
- **TS 25.331** (Rel-19) — UTRAN RRC Protocol Specification
- **TS 25.401** (Rel-19) — UTRAN Overall Architecture
- **TS 25.423** (Rel-19) — UTRAN RNSAP Specification
- **TS 25.425** (Rel-19) — UTRAN Iur Interface User Plane Protocols
- **TR 25.931** (Rel-19) — UTRAN Signalling Procedures Examples
- **TS 36.133** (Rel-19) — E-UTRA RRM Requirements
- … a dalších 11 specifikací

---

📖 **Anglický originál a plná specifikace:** [RNTI na 3GPP Explorer](https://3gpp-explorer.com/glossary/rnti/)
