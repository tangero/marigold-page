---
slug: "sc-mrb"
url: "/mobilnisite/slovnik/sc-mrb/"
type: "slovnik"
title: "SC-MRB – Single Cell Multicast Radio Bearer"
date: 2025-01-01
abbr: "SC-MRB"
fullName: "Single Cell Multicast Radio Bearer"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/sc-mrb/"
summary: "SC-MRB je rádiový přenosový kanál používaný k doručování multicastového provozu typu Single Cell Point-to-Multipoint (SC-PTM) skupině uživatelských zařízení (UE). Jedná se o logické spojení, které pře"
---

SC-MRB je rádiový přenosový kanál, který doručuje multicastový provoz typu Single Cell Point-to-Multipoint a poskytuje logické spojení pro přenos dat uživatelské roviny ze sítě k více uživatelským zařízením (UE) přes sdílený kanál v rámci jedné buňky.

## Popis

Single Cell Multicast Radio Bearer (SC-MRB, rádiový přenosový kanál pro multicast v jedné buňce) je klíčový koncept v uživatelské rovině LTE pro multicastové služby. Představuje jednosměrný rádiový přenosový kanál typu point-to-multipoint, zřízený mezi eNodeB a skupinou uživatelských zařízení (UE) v rámci jedné buňky za účelem doručování multicastového nebo broadcastového obsahu. SC-MRB je asociován s konkrétní službou [SC-PTM](/mobilnisite/slovnik/sc-ptm/), například proudem zpráv pro veřejnou bezpečnost nebo kanálem mobilní televize. Jedná se o logický kanál, kterým proudí skutečná datová náplň služby, na rozdíl od řídicích informací přenášených na [SC-MCCH](/mobilnisite/slovnik/sc-mcch/). Na vrstvě Packet Data Convergence Protocol ([PDCP](/mobilnisite/slovnik/pdcp/)) jsou data pro SC-MRB zpracována a je jim přiřazen specifický Group-RNTI ([G-RNTI](/mobilnisite/slovnik/g-rnti/)), který identifikuje tento přenosový kanál a službu všem přijímajícím uživatelským zařízením.

Z architektonického hlediska SC-MRB využívá pro efektivitu strukturu sdíleného kanálu. Na úrovni logického kanálu je namapován na specifický Single Cell Multicast Traffic Channel ([SC-MTCH](/mobilnisite/slovnik/sc-mtch/)). SC-MTCH je následně namapován na transportní kanál Downlink Shared Channel ([DL-SCH](/mobilnisite/slovnik/dl-sch/)), který je nakonec vysílán na fyzickém kanálu Physical Downlink Shared Channel ([PDSCH](/mobilnisite/slovnik/pdsch/)). Toto mapování na sdílený kanál je zásadní; namísto vyčleňování samostatných zdrojů pro každé uživatelské zařízení eNodeB data vysílá pouze jednou a všechna uživatelská zařízení zájmové služby monitorují stejné časově-frekvenční zdroje, přičemž ke zjištění paketů určených pro ně používají společný G-RNTI. Vrstva Radio Link Control ([RLC](/mobilnisite/slovnik/rlc/)) pro SC-MRB pracuje v nepotvrzovaném režimu (Unacknowledged Mode, UM), protože neexistuje mechanismus pro hybridní ARQ zpětnou vazbu od množství přijímačů, což odpovídá broadcastové povaze služby.

Provoz zahrnuje koordinaci mezi řídicí a uživatelskou rovinou. eNodeB nejprve nakonfiguruje SC-MRB a jeho asociované parametry (jako je G-RNTI). Poté tuto konfiguraci, včetně G-RNTI a podrobností o plánování, inzeruje na řídicím kanálu SC-MCCH. Uživatelské zařízení, které chce službu přijímat, přečte SC-MCCH, zjistí G-RNTI a způsob plánování SC-MRB a následně nakonfiguruje svou fyzickou vrstvu tak, aby monitorovala PDSCH pro daný G-RNTI. Když eNodeB naplánuje data pro tento SC-MRB, vyšle je na PDSCH s odpovídajícím G-RNTI v downlink control information (DCI). Všechna uživatelská zařízení monitorující tento G-RNTI data přijmou, předají je vzhůru přes své vrstvy RLC a PDCP asociované s tímto SC-MRB a doručí je aplikaci ve vyšší vrstvě. Tento mechanismus umožňuje jediným vysíláním obsloužit neomezený počet uživatelských zařízení v pokrytí buňky, čímž poskytuje optimální spektrální efektivitu pro skupinovou komunikaci.

## K čemu slouží

SC-MRB byl vytvořen, aby poskytl standardizovaný a efektivní mechanismus pro doručování dat uživatelské roviny ve službách Single Cell Point-to-Multipoint (SC-PTM). Před SC-PTM vyžadovalo doručení stejného obsahu více uživatelům v LTE buňce typicky zřízení individuálních unicastových přenosových kanálů (DRB) pro každého uživatele, což znamenalo duplikaci datového proudu pro každé spojení. Tento přístup je vysoce neefektivní z hlediska využití rádiových zdrojů, zejména s rostoucím počtem příjemců, a vytváří v síti významnou zátěž.

SC-MRB řeší tento problém s neefektivitou zdrojů pro lokalizovanou skupinovou komunikaci. Umožňuje skutečný multicast na rádiové úrovni: jediný přenos datových paketů, který může být přijat celou skupinou. To je klíčové pro případy použití, které vyžadují včasné a simultánní doručení mnoha zařízením, jako je vysílání pokynů flotile vozidel, rozesílání nouzových upozornění na všechny telefony v oblasti nebo streamování živého videa divákům na stadionu. Účelem je využít broadcastové povahy rádiového média pro dosažení optimální spektrální efektivity.

Motivována potřebou odlehčených multicastových řešení doplňujících složitější eMBMS/MBSFN, byla SC-PTM a její SC-MRB navržena pro dynamické, buňkově specifické služby. SC-MRB poskytuje základní model přenosového kanálu uživatelské roviny, který se integruje se sdílenou kanálovou architekturou LTE. Umožňuje operátorům nabízet multicastové služby bez režie spojené se správou synchronizované vícebuňkové oblasti MBSFN, čímž činí multicast ekonomicky životaschopným pro širší škálu aplikací, včetně vznikajících scénářů IoT a V2X, kde je skupinové zasílání zpráv základním požadavkem.

## Klíčové vlastnosti

- Jednosměrný rádiový přenosový kanál typu point-to-multipoint pro multicastová data
- Identifikován společným Group RNTI (G-RNTI) pro všechna přijímající uživatelská zařízení (UE)
- Namapován na logický kanál SC-MTCH a transportní/fyzické kanály DL-SCH/PDSCH
- Pro přenos využívá RLC nepotvrzovaný režim (Unacknowledged Mode, UM) bez HARQ zpětné vazby
- Konfigurace je broadcastována k uživatelským zařízením přes řídicí kanál SC-MCCH
- Umožňuje spektrální efektivitu tím, že obsluhuje více uživatelských zařízení jediným rádiovým přenosem

## Související pojmy

- [SC-PTM – Single-Cell Point-to-Multipoint](/mobilnisite/slovnik/sc-ptm/)
- [SC-MCCH – Single Cell Multicast Control Channel](/mobilnisite/slovnik/sc-mcch/)
- [G-RNTI – GERAN Radio Network Temporary Identity](/mobilnisite/slovnik/g-rnti/)
- [PDCP – Packet Data Convergence Protocol](/mobilnisite/slovnik/pdcp/)

## Definující specifikace

- **TS 36.331** (Rel-19) — LTE RRC Protocol Specification

---

📖 **Anglický originál a plná specifikace:** [SC-MRB na 3GPP Explorer](https://3gpp-explorer.com/glossary/sc-mrb/)
