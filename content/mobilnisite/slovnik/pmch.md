---
slug: "pmch"
url: "/mobilnisite/slovnik/pmch/"
type: "slovnik"
title: "PMCH – Physical Multicast Channel"
date: 2025-01-01
abbr: "PMCH"
fullName: "Physical Multicast Channel"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/pmch/"
summary: "Fyzický multicastový kanál (PMCH) je downlinkový fyzický kanál v LTE používaný výhradně pro službu Multimedia Broadcast Multicast Service (MBMS). Přenáší multicastová uživatelská data (MTCH) a řídicí"
---

PMCH je downlinkový fyzický kanál v LTE, který přenáší multicastový provoz a řídicí informace pro službu Multimedia Broadcast Multicast Service (MBMS) a umožňuje efektivní přenos dat z jednoho bodu do více bodů.

## Popis

Fyzický multicastový kanál (PMCH) je klíčovou součástí fyzické vrstvy rozhraní LTE, specifikovanou v 3GPP TS 36.211 (Fyzické kanály a modulace). Je to downlinkový transportní kanál, který existuje speciálně v buňkách nakonfigurovaných pro službu Multimedia Broadcast Multicast Service ([MBMS](/mobilnisite/slovnik/mbms/)), známých jako oblasti [MBSFN](/mobilnisite/slovnik/mbsfn/) (MBMS Single Frequency Network). Na rozdíl od unicastových kanálů ([PDSCH](/mobilnisite/slovnik/pdsch/)) vyhrazených pro jedno koncové zařízení (UE) je PMCH vysílán všem UE v oblasti MBSFN, což umožňuje efektivní využití spektra pro skupinovou komunikaci.

Z pohledu struktury je PMCH mapován na specifické časově-frekvenční zdroje v rámci rámce LTE. Využívá strukturu MBSFN subrámců, která se liší od běžných unicastových subrámců. V MBSFN subrámcích je cyklická předpona delší a v datové oblasti chybí některé referenční signály ([CRS](/mobilnisite/slovnik/crs/)), což umožňuje robustnější přenos vhodný pro velké pokrytí buňky a kombinování v [SFN](/mobilnisite/slovnik/sfn/). PMCH přenáší dva typy logických kanálů: Multicast Traffic Channel ([MTCH](/mobilnisite/slovnik/mtch/)), který obsahuje skutečný multimediální obsah (např. video streamy), a Multicast Control Channel ([MCCH](/mobilnisite/slovnik/mcch/)), který poskytuje potřebné řídicí informace pro službu MBMS, jako jsou informace o plánování.

Provoz spočívá v tom, že eNodeB vysílá stejný PMCH signál synchronně přes všechny buňky patřící do oblasti MBSFN. Koncová zařízení (UE) přijímající služby MBMS se na tento signál synchronizují a kombinují identické vlnové formy přijaté z více eNodeB, čímž efektivně považují přenosy z více buněk za jediný, silný signál se zlepšeným pokrytím a kvalitou. Tento provoz SFN snižuje interference a zlepšuje spektrální účinnost pro vysílací služby. Modulační a kódovací schéma ([MCS](/mobilnisite/slovnik/mcs/)) pro PMCH je obvykle robustnější (např. použití QPSK) ve srovnání s unicastem, aby bylo zajištěno přijetí na okraji buňky.

Role PMCH je ústřední pro vysílací funkci LTE, eMBMS (evolved MBMS). Poskytuje fyzickou vrstvu pro doručování oblíbeného obsahu, jako je živé TV, rádio nebo aktualizace softwaru, mnoha uživatelům bez zahlcení unicastových kanálů. V pozdějších vydáních byl jeho rámec zvažován i pro komunikace V2X a systémy veřejného varování, což ukazuje jeho užitečnost pro šíření informací od jednoho k mnoha.

## K čemu slouží

PMCH byl vytvořen, aby řešil neefektivitu používání více unicastových spojení (bod-bod) pro doručování identického obsahu mnoha uživatelům, jako je mobilní TV nebo živé sportovní události. Tento unicastový přístup spotřebovává nadměrné síťové zdroje (rádiové přenosové kanály, plánovací povolení, výkon) a může vést k zahlcení v oblíbených buňkách. Potřeba vysílací schopnosti z jednoho bodu do více bodů byla rozpoznána již od 3G UMTS (MBMS), ale architektura PMCH a MBSFN v LTE poskytla výrazně efektivnější a výkonnější implementaci.

Primární problém, který řeší, je optimalizace spektra a síťové kapacity pro hromadné doručování obsahu. Vyčleněním specifických subrámců (MBSFN subrámců) pro vysílací provoz může síť obsloužit neomezený počet zainteresovaných uživatelů v oblasti jediným přenosem, čímž uvolní zbývající subrámy pro vyhrazený unicastový provoz. Toto oddělení zajišťuje, že vysílací služby negativně neovlivňují zážitek jednotlivých datových uživatelů.

Historicky existovaly dedikované vysílací sítě (např. DVB-H) vedle celulárních sítí. PMCH/eMBMS integroval vysílací schopnosti přímo do standardu celulární sítě LTE, což umožnilo operátorům flexibilně využívat jejich licencované spektrum pro interaktivní i vysílací služby na stejné infrastruktuře. Tato konvergence snížila náklady a umožnila nové servisní modely. Vytvoření PMCH bylo motivováno komerčním potenciálem mobilní televize a technickým požadavkem na efektivní skupinovou komunikaci pro veřejnou bezpečnost a automobilové aplikace (V2X) v pozdějších vydáních.

## Klíčové vlastnosti

- Využívá MBSFN (Multicast-Broadcast Single Frequency Network) subrámy pro robustní přenos v široké oblasti
- Přenáší jak uživatelská data (MTCH), tak řídicí informace (MCCH) pro služby MBMS
- Umožňuje provoz SFN, při kterém se identické signály z více buněk kombinují a zlepšují pokrytí
- Používá robustní modulační schéma (typicky QPSK) vhodné pro příjem na okraji buňky
- Vyhrazené přidělení fyzických zdrojů oddělené od unicastového PDSCH, které zabraňuje interferenci
- Základ pro služby LTE Broadcast (eMBMS), jako je mobilní TV a veřejná varování

## Související pojmy

- [MBMS – Multimedia Broadcast Multicast Service](/mobilnisite/slovnik/mbms/)
- [MBSFN – Multimedia Broadcast multicast service Single Frequency Network](/mobilnisite/slovnik/mbsfn/)
- [MTCH – MBMS point-to-multipoint Traffic Channel](/mobilnisite/slovnik/mtch/)
- [MCCH – MBMS point-to-multipoint Control Channel](/mobilnisite/slovnik/mcch/)
- [PDSCH – Physical Downlink Shared Channel](/mobilnisite/slovnik/pdsch/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 36.101** (Rel-19) — LTE UE Radio Transmission & Reception Requirements
- **TS 36.104** (Rel-19) — Base Station (BS) radio transmission and reception
- **TS 36.201** (Rel-19) — LTE Physical Layer General Description
- **TS 36.211** (Rel-19) — LTE Physical Layer Specification
- **TS 36.212** (Rel-19) — LTE Multiplexing and Channel Coding
- **TS 36.213** (Rel-19) — LTE Physical Layer Procedures
- **TS 36.300** (Rel-19) — E-UTRAN Radio Interface Protocol Architecture Overview
- **TS 36.302** (Rel-19) — E-UTRA Physical Layer Services
- **TS 36.443** (Rel-19) — M2 Application Protocol (M2AP) for E-UTRAN
- **TR 36.976** (Rel-19) — LTE-based 5G Terrestrial Broadcast Overview
- **TR 38.889** (Rel-16) — NR-based access to unlicensed spectrum study

---

📖 **Anglický originál a plná specifikace:** [PMCH na 3GPP Explorer](https://3gpp-explorer.com/glossary/pmch/)
