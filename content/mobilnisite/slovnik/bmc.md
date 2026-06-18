---
slug: "bmc"
url: "/mobilnisite/slovnik/bmc/"
type: "slovnik"
title: "BMC – Broadcast/Multicast Control"
date: 2025-01-01
abbr: "BMC"
fullName: "Broadcast/Multicast Control"
category: "Protocol"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/bmc/"
summary: "BMC je podsložka v protokolovém zásobníku UMTS odpovědná za správu doručování vysílacích (broadcast) a skupinových (multicast) dat přes rozhraní vzduchového rozhraní. Zajišťuje plánování, segmentaci a"
---

BMC je podsložka protokolu UMTS, která spravuje doručování vysílacích (broadcast) a skupinových (multicast) dat přes rozhraní vzduchového rozhraní, zajišťuje plánování, segmentaci a opětovné sestavování pro efektivní přenos typu point-to-multipoint.

## Popis

Broadcast/Multicast Control (BMC) funguje jako podsložka uvnitř vrstvy Radio Link Control ([RLC](/mobilnisite/slovnik/rlc/)) v architektuře protokolu UMTS, konkrétně v uživatelské rovině (User Plane). Umístěna nad vrstvou RLC a pod vrstvou Packet Data Convergence Protocol ([PDCP](/mobilnisite/slovnik/pdcp/)) poskytuje BMC specializované funkce pro vysílací (broadcast) a skupinový (multicast) provoz, které se liší od běžného zpracování unicast dat. Protokol je přítomen jak v uživatelském zařízení (UE), tak v [UTRAN](/mobilnisite/slovnik/utran/) (UMTS Terrestrial Radio Access Network), přičemž BMC entita na straně sítě je typicky umístěna v radiovém síťovém řadiči ([RNC](/mobilnisite/slovnik/rnc/)).

Hlavní funkcí BMC je ukládání vysílacích zpráv přijatých od jádra sítě, plánování jejich přenosu přes rozhraní vzduchového rozhraní a zajištění segmentace a opětovného sestavení zpráv. Když vysílací zpráva dorazí z jádra sítě přes rozhraní Iu, BMC entita v RNC ji uloží do fronty vysílacích zpráv. Protokol následně tyto zprávy naplánuje k přenosu přes logický kanál Cell Broadcast Channel ([CTCH](/mobilnisite/slovnik/ctch/)), který je mapován na transportní kanál Forward Access Channel ([FACH](/mobilnisite/slovnik/fach/)). Toto plánování bere v úvahu faktory jako priorita zprávy, periodicita přenosu a zatížení systému za účelem optimalizace využití rádiových prostředků.

Architektura protokolu zahrnuje několik klíčových komponent: samotnou BMC entitu, která spravuje ukládání a plánování zpráv; BMC-SAP (Service Access Point) pro komunikaci s vyššími vrstvami; a rozhraní s RLC pro vlastní přenos dat. BMC podporuje dva hlavní provozní režimy: vysílací režim (broadcast) pro zprávy určené všem UE v buňce a skupinový režim (multicast) pro zprávy cílené na konkrétní skupiny účastníků. Pro služby [MBMS](/mobilnisite/slovnik/mbms/) BMC spolupracuje s dalšími protokolovými vrstvami, aby zajistil efektivní distribuci multimediálního obsahu, včetně podpory procedur selektivního kombinování (selective combining) a sčítání (counting) pro optimalizaci využití prostředků.

BMC implementuje několik důležitých mechanismů pro zajištění spolehlivého a efektivního doručování vysílacích/skupinových zpráv. Mezi ně patří segmentace zpráv pro rozsáhlá vysílání, plánovací algoritmy pro zabránění zahlcení rádiového rozhraní a podpora distribuce zpráv na základě geografické oblasti. Protokol také zpracovává zprávy služby cell broadcast ([CBS](/mobilnisite/slovnik/cbs/)), což jsou krátké textové zprávy vysílané všem UE v určitých geografických oblastech. Návrh BMC minimalizuje spotřebu energie UE tím, že umožňuje zařízením přijímat vysílací zprávy bez nutnosti navázání vyhrazeného spojení, což jej činí zvláště vhodným pro výstražné systémy, služby založené na poloze a multimediální vysílání.

## K čemu slouží

BMC byl vytvořen, aby vyřešil základní výzvu efektivního doručování stejného obsahu více uživatelům současně v mobilních sítích. Před BMC se mobilní systémy primárně spoléhaly na point-to-point (unicast) spojení, která se stala vysoce neefektivními, když stejný obsah potřeboval být doručen mnoha uživatelům ve stejné geografické oblasti. Tato neefektivita spotřebovávala nadměrné rádiové prostředky a kapacitu jádra sítě, zejména pro populární obsah jako aktualizace zpráv, výstražné systémy nebo multimediální streamy.

Protokol byl představen ve 3GPP Release 4 jako součást vývoje architektury UMTS pro nativní podporu vysílacích (broadcast) a skupinových (multicast) služeb v rámci mobilního systému. Předchozí přístupy buď využívaly opakované unicast přenosy (plýtvavé vůči prostředkům), nebo se spoléhaly na externí vysílací systémy jako Digital Audio Broadcasting (DAB) nebo Digital Video Broadcasting (DVB), které vyžadovaly samostatnou infrastrukturu a zařízení. BMC umožnil integrované vysílací/skupinové schopnosti v rámci stávající infrastruktury UMTS, což operátorům dovolilo nabízet nové služby bez nutnosti nasazení zcela oddělených sítí.

BMC konkrétně vyřešil několik technických problémů: poskytl standardizované mechanismy plánování pro vysílací provoz, umožnil efektivní využití rádiových prostředků prostřednictvím sdílených kanálů a podporoval jak služby cell broadcast (pro krátké zprávy), tak multimediální vysílací/skupinové služby (MBMS) (pro bohatší obsah). Návrh protokolu zohledňoval jedinečné požadavky vysílacího přenosu, včetně podpory nespojitého příjmu (discontinuous reception) pro šetření baterie UE, možností geografického cílení a integrace s existujícími funkcemi správy mobility UMTS. To umožnilo služby jako výstražné systémy, distribuce informací založená na poloze a nakonec vysílání multimediálního obsahu prostřednictvím MBMS.

## Klíčové vlastnosti

- Ukládání a plánování vysílacích zpráv v RNC
- Podpora zpráv služby Cell Broadcast Service (CBS)
- Efektivní využití rádiových prostředků prostřednictvím přenosu sdíleným kanálem
- Možnosti distribuce zpráv na základě geografické oblasti
- Integrace s Multimedia Broadcast/Multicast Service (MBMS)
- Podpora nespojitého příjmu (discontinuous reception) pro šetření energie UE

## Související pojmy

- [MBMS – Multimedia Broadcast Multicast Service](/mobilnisite/slovnik/mbms/)
- [RLC – Radio Link Control](/mobilnisite/slovnik/rlc/)
- [CTCH – Common Traffic Channel](/mobilnisite/slovnik/ctch/)
- [CBS – Cell Broadcast Service](/mobilnisite/slovnik/cbs/)
- [FACH – Forward Access Channel](/mobilnisite/slovnik/fach/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 25.301** (Rel-19) — UE-UTRAN Radio Interface Protocol Architecture
- **TS 25.324** (Rel-19) — Broadcast/Multicast Control Protocol
- **TS 25.401** (Rel-19) — UTRAN Overall Architecture
- **TR 25.931** (Rel-19) — UTRAN Signalling Procedures Examples

---

📖 **Anglický originál a plná specifikace:** [BMC na 3GPP Explorer](https://3gpp-explorer.com/glossary/bmc/)
