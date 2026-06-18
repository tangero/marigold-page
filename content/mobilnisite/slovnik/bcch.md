---
slug: "bcch"
url: "/mobilnisite/slovnik/bcch/"
type: "slovnik"
title: "BCCH – Broadcast Control Channel"
date: 2025-01-01
abbr: "BCCH"
fullName: "Broadcast Control Channel"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/bcch/"
summary: "Broadcast Control Channel (BCCH) je sestupný logický kanál, který síť používá k vysílání základních systémových informací všem mobilním zařízením v buňce. Přenáší klíčové parametry, jako je identita s"
---

BCCH je sestupný logický kanál používaný k vysílání základních systémových informací, jako je identita sítě a konfigurace buňky, všem mobilním zařízením v buňce.

## Popis

Broadcast Control Channel (BCCH) je základní logický kanál v architektuře protokolů rádiového rozhraní 3GPP, konkrétně součást vrstvy Radio Resource Control ([RRC](/mobilnisite/slovnik/rrc/)). Funguje jako bod-vícebodový, pouze sestupný kanál od základnové stanice (NodeB, eNodeB, gNB) ke všem uživatelským zařízením (UE) v její pokryté oblasti. BCCH nepřenáší uživatelská data, ale je vyhrazen pro vysílání systémových informací ([SI](/mobilnisite/slovnik/si/)), což je strukturovaná sada zpráv nezbytných pro fungování UE v síti. Tyto informace jsou organizovány do hlavních informačních bloků ([MIB](/mobilnisite/slovnik/mib/)) a několika bloků systémových informací ([SIB](/mobilnisite/slovnik/sib/)), z nichž každý obsahuje specifické sady parametrů. Primární úlohou BCCH je poskytnout UE nezbytné informace pro přístup k síti, provedení (re)výběru buňky a pochopení schopností a konfigurace buňky.

Z architektonického hlediska je BCCH logický kanál mapovaný na transportní a fyzické kanály. V GSM je logický kanál BCCH přenášen na specifických časových úsecích. V UMTS je mapován na transportní kanál Broadcast Channel ([BCH](/mobilnisite/slovnik/bch/)), který je následně mapován na fyzický kanál Primary Common Control Physical Channel ([P-CCPCH](/mobilnisite/slovnik/p-ccpch/)). V LTE a NR přenáší BCCH dva odlišné typy zpráv: MIB je přenášen na fyzickém kanálu Physical Broadcast Channel ([PBCH](/mobilnisite/slovnik/pbch/)), zatímco SIBy (kromě [SIB1](/mobilnisite/slovnik/sib1/) v NR) jsou přenášeny na sdíleném sestupném kanálu (DL-SCH), mapovaném na fyzický sdílený sestupný kanál (PDSCH). Toto rozdělení umožňuje, aby byly kritické minimální informace (MIB) přenášeny s robustním, neřízeným dekódováním, zatímco podrobnější SIBy mohou být plánovány flexibilněji.

Provoz BCCH je charakterizován periodickým a opakovaným vysíláním. Síť nepřetržitě vysílá systémové informace a UE je musí přečíst při zapnutí, vstupu do nové oblasti nebo periodicky, aby zůstala aktuální. MIB obsahuje nejdůležitější parametry pro počáteční přístup, jako je šířka pásma systému a číslo systémového rámce (SFN). SIB1 (nebo jeho ekvivalent) obsahuje plánovací informace pro další SIBy a parametry související s přístupem k buňce, jako je identita PLMN. Ostatní SIBy přenášejí informace pro převýběr buňky, seznamy sousedních buněk, konfigurace společných kanálů a informace specifické pro služby. UE používá pro každý SIB platnostní časovač; pokud časovač vyprší, musí UE tento SIB znovu získat, čímž je zajištěno, že pracuje s aktuálními síťovými daty.

Jeho role v síti je zásadní. Bez BCCH by UE nebylo schopno identifikovat síť, synchronizovat se v čase a frekvenci nebo zjistit postupy a prostředky potřebné k vyžádání spojení. Je to první kanál, který UE dekóduje při hledání služby. Spolehlivost a efektivita přenosu BCCH přímo ovlivňuje dobu objevení sítě, zpoždění při navazování hovoru a úspěšnost mobilních procedur, jako je předávání (handover) a převýběr buňky. Je to kritická součást pro transparentnost sítě, která zajišťuje, že všechna UE mají konzistentní a přesný pohled na rádiové prostředí a síťové politiky.

## K čemu slouží

BCCH byl vytvořen k řešení základního problému objevování sítě a počátečního přístupu v celulárním systému. V raných mobilních sítích byl potřebný mechanismus, který by náhodně příchozí mobilní zařízení informoval o identitě a konfiguraci obslužné buňky bez nutnosti předchozího nastavení signalizace. BCCH poskytuje tuto základní vysílací službu, umožňující jakémukoli zařízení autonomně najít a přihlásit se (camp) k vhodné buňce. Řeší omezení spočívající v nutnosti předkonfigurovat zařízení rozsáhlými síťovými daty nebo navázat individuální signalizační spoje pro základní systémové parametry, což by bylo neefektivní a nepraktické pro hromadný celulární provoz.

Historicky jeho koncept vznikl v GSM (jak je uvedeno v původní definici) a byl základním kamenem všech následujících technologií 3GPP (UMTS, LTE, 5G NR). Motivací pro jeho pokračující vývoj byla podpora stále složitějších sítí s více funkcemi, širšími šířkami pásma a různorodými službami. BCCH přenáší informace potřebné k podpoře pokročilých funkcí, jako je agregace nosných, indikace síťového řezání (network slicing) (v 5G), služby multimediálního vysílání a sofistikované schémata mobility a úspory energie. Řeší problém škálovatelné distribuce systémových informací v dynamickém rádiovém prostředí.

Dále BCCH umožňuje efektivní provoz a správu sítě. Vysíláním společných parametrů odstraňuje potřebu, aby síť individuálně informovala každé UE o statických nebo polostatických informacích o buňce, čímž šetří významnou signalizační režii na vyhrazených kanálech. Hraje také klíčovou roli v oblasti veřejné bezpečnosti, vysíláním informací o varování před zemětřesením a tsunami (ETWS) a informací služby komerčního mobilního varování (CMAS). Jeho návrh zajišťuje, že i UE v nečinném režimu (idle mode) mohou přijímat kritické aktualizace a nouzová varování bez navázání stavu spojení, což je zásadní pro bezpečnost a dodržování předpisů.

## Klíčové vlastnosti

- Vysílá základní systémové informace (MIB a SIBy) všem UE v buňce
- Umožňuje UE autonomní vyhledání, výběr a převýběr buňky
- Přenáší kritické parametry pro identifikaci sítě (PLMN ID) a řízení přístupu
- Podporuje plánovací mechanismy pro různé typy bloků systémových informací
- Poskytuje informace pro konfiguraci rádiových prostředků a seznamy sousedních buněk
- Slouží k vysílání zpráv veřejného varování a nouzových výstrah (např. ETWS, CMAS)

## Související pojmy

- [SIB – System Information Block](/mobilnisite/slovnik/sib/)
- [MIB – Management Information Base](/mobilnisite/slovnik/mib/)
- [RRC – Radio Resource Control](/mobilnisite/slovnik/rrc/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.171** (Rel-4) — LCS Stage 2 Specification for UMTS
- **TS 23.271** (Rel-19) — LCS Stage 2 Specification
- **TS 23.851** (Rel-6) — Network Sharing Architecture for 3G Systems
- **TS 25.222** (Rel-19) — UTRA TDD Multiplexing & Channel Coding
- **TS 25.224** (Rel-19) — UTRA TDD Physical Layer Procedures
- **TS 25.225** (Rel-19) — UTRA TDD Physical Layer Measurements
- **TS 25.301** (Rel-19) — UE-UTRAN Radio Interface Protocol Architecture
- **TS 25.302** (Rel-19) — UTRA Physical Layer Services
- **TS 25.304** (Rel-19) — UTRA Idle Mode Procedures Specification
- **TS 25.321** (Rel-19) — MAC Protocol Specification for UTRAN
- **TS 25.322** (Rel-19) — RLC Protocol Specification
- **TS 25.331** (Rel-19) — UTRAN RRC Protocol Specification
- **TS 25.367** (Rel-19) — Home NodeB Mobility Procedures
- **TS 25.430** (Rel-19) — Introduction to Iub Interface Specifications
- … a dalších 23 specifikací

---

📖 **Anglický originál a plná specifikace:** [BCCH na 3GPP Explorer](https://3gpp-explorer.com/glossary/bcch/)
