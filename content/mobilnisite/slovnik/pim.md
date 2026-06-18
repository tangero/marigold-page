---
slug: "pim"
url: "/mobilnisite/slovnik/pim/"
type: "slovnik"
title: "PIM – Protocol-Independent Multicast"
date: 2025-01-01
abbr: "PIM"
fullName: "Protocol-Independent Multicast"
category: "Protocol"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/pim/"
summary: "Protocol-Independent Multicast (PIM) je rodina směrovacích protokolů pro multicast používaná k vytváření distribučních stromů pro efektivní doručování dat více destinacím v IP sítích. Je 'protokolově"
---

PIM je rodina směrovacích protokolů pro multicast používaná k vytváření efektivních distribučních stromů pro doručování dat více destinacím v IP sítích, která funguje nezávisle na podkladovém unicastovém směrovacím protokolu.

## Popis

Protocol-Independent Multicast (PIM) není jediný protokol, ale sada směrovacích protokolů pro multicast definovaná [IETF](/mobilnisite/slovnik/ietf/) a přijatá v rámci architektur 3GPP pro IP Multimedia Subsystem (IMS) a multicastové doručování v 5G core sítích. Základním principem PIM je jeho nezávislost na podkladovém unicastovém směrovacím protokolu (např. OSPF, IS-IS, BGP). PIM neudržuje samostatnou databázi topologie; místo toho využívá existující unicastovou směrovací tabulku ([RIB](/mobilnisite/slovnik/rib/) - Routing Information Base) k rozhodování o zpětné cestě (RPF - Reverse Path Forwarding). Tento návrh zjednodušuje nasazení a provoz.

PIM funguje tak, že si routery vyměňují zprávy protokolu PIM za účelem vytváření multicastových distribučních stromů. Tyto stromy definují cestu od multicastového zdroje ke všem zainteresovaným příjemcům. Existují dva hlavní režimy provozu: PIM Sparse Mode ([PIM-SM](/mobilnisite/slovnik/pim-sm/)) a PIM Dense Mode ([PIM-DM](/mobilnisite/slovnik/pim-dm/)), přičemž PIM-SM je nejrozšířenější. V PIM-SM příjemci explicitně signalizují svůj zájem o multicastovou skupinu odesíláním PIM Join zpráv směrem k centrálnímu bodu setkání (Rendezvous Point - [RP](/mobilnisite/slovnik/rp/)) nebo přímo ke zdroji. Tím se vytvoří sdílený strom (zakořeněný v RP) nebo zdrojový strom (zakořeněný ve zdroji). PIM spoléhá na unicastovou směrovací tabulku při určování RPF rozhraní pro příchozí multicastová data a správného nadřazeného souseda, kterému posílat Join/Prune zprávy.

Klíčovými komponentami v PIM síti jsou Designated Router ([DR](/mobilnisite/slovnik/dr/)) na sítích s vícenásobným přístupem (jako je Ethernet), který je zodpovědný za odesílání joinů jménem podřízených příjemců, a Rendezvous Point (RP) v PIM-SM, který slouží jako počáteční místo setkání zdrojů a příjemců. PIM routery udržují záznamy multicastového směrovacího stavu, které uvádějí příchozí (nadřazená) a odchozí (podřízená) rozhraní pro každou dvojici zdroj-skupina (S,G) nebo záznam skupiny (*,G).

V rámci ekosystému 3GPP je PIM zmíněn ve specifikacích jako TS 29.561 pro vystavení 5G core sítě, TS 26.140 pro multimediální multicastovou službu a TS 37.808 pro vylepšení architektury [MBMS](/mobilnisite/slovnik/mbms/). Jeho úlohou je poskytnout multicastovou směrovací infrastrukturu na IP vrstvě, která umožňuje efektivní doručování broadcastového/multicastového obsahu, jako je [IPTV](/mobilnisite/slovnik/iptv/) nebo skupinová komunikace, od zdrojů obsahu uvnitř paketové datové sítě k okraji mobilní sítě (např. k UPF nebo MBMS-GW). Je to kritická komponenta pro umožnění škálovatelných služeb typu point-to-multipoint.

## K čemu slouží

PIM byl vytvořen, aby vyřešil problémy škálovatelnosti a nasazení u starších multicastových směrovacích protokolů. Předchozí multicastové protokoly jako Distance Vector Multicast Routing Protocol (DVMRP) byly často vázány na konkrétní unicastový protokol a vyžadovaly udržování samostatných multicastových směrovacích tabulek, což bylo složité a náročné na zdroje. Potřeba byla robustní, škálovatelná metoda pro doručování dat více příjemcům bez zatížení zdroje nebo sítě více unicastovými proudy.

Základním účelem PIM je poskytnout efektivní distribuci dat typu many-to-many nebo one-to-many na síťové vrstvě. Řeší problém zaplavování sítě a neefektivního využití šířky pásma pro skupinové aplikace. Vytvářením distribučních stromů PIM zajišťuje, že pakety jsou replikovány pouze v nezbytných větvicích bodech sítě, čímž šetří šířku pásma ve srovnání s unicastovou replikací. Jeho protokolová nezávislost byla klíčovou motivací, protože umožňuje nasazení nad jakoukoliv existující unicastovou infrastrukturou bez nutnosti paralelního multicastového směrovacího protokolu, čímž se snižují provozní bariéry.

V kontextu 3GPP je přijetí PIM motivováno potřebou standardizovaného, interoperabilního IP multicastu pro podporu služeb jako Multimedia Broadcast/Multicast Service (MBMS), evolved MBMS (eMBMS) a multicastových služeb založených na IMS. Poskytuje podkladový transportní mechanismus na IP vrstvě, který umožňuje mobilní core síti bezproblémově rozhraní s externími IP sítěmi podporujícími multicast, a tím umožňuje efektivní doručování živého videa, softwarových aktualizací a varovných zpráv pro veřejnost velkému počtu uživatelů.

## Klíčové vlastnosti

- Nezávislost na podkladovém unicastovém směrovacím protokolu (OSPF, BGP, statické cesty atd.).
- Využívá kontrolu zpětné cesty (Reverse Path Forwarding - RPF) založenou na unicastové směrovací tabulce.
- Podporuje provoz jak ve sparse módu (PIM-SM), tak v dense módu (PIM-DM).
- Vytváří efektivní zdrojové stromy (S,G) a/nebo sdílené stromy (*,G) pro multicastový přenos.
- Definuje body setkání (Rendezvous Points - RP) pro inicializaci a setkání v PIM-SM.
- Obsahuje mechanismy pro volbu určeného routeru (Designated Router) na spojích s vícenásobným přístupem.

## Související pojmy

- [PIM-SM – Protocol Independent Multicast – Sparse Mode](/mobilnisite/slovnik/pim-sm/)
- [PIM-DM – Protocol-Independent Multicast - Dense Mode](/mobilnisite/slovnik/pim-dm/)
- [MBMS – Multimedia Broadcast Multicast Service](/mobilnisite/slovnik/mbms/)

## Definující specifikace

- **TS 26.140** (Rel-19) — MMS Media Formats and Codecs Specification
- **TS 29.561** (Rel-19) — 5G Interworking with External Data Networks
- **TS 37.808** (Rel-12) — PIM Handling for Base Stations Study

---

📖 **Anglický originál a plná specifikace:** [PIM na 3GPP Explorer](https://3gpp-explorer.com/glossary/pim/)
