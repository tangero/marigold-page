---
slug: "mospf"
url: "/mobilnisite/slovnik/mospf/"
type: "slovnik"
title: "MOSPF – Multicast Open Shortest Path First"
date: 2025-01-01
abbr: "MOSPF"
fullName: "Multicast Open Shortest Path First"
category: "Protocol"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/mospf/"
summary: "Rozšíření multicastového směrovacího protokolu pro OSPF používané v paketových sítích 3GPP, primárně pro správu IP multicast skupin a výpočet distribučních stromů. Umožňuje efektivní doručování multic"
---

MOSPF je rozšíření multicastového směrovacího protokolu pro OSPF používané v paketových sítích 3GPP pro správu IP multicast skupin a výpočet distribučních stromů, které umožňují efektivní doručování multicastového provozu.

## Popis

Multicast Open Shortest Path First (MOSPF) je rozšíření unicastového směrovacího protokolu Open Shortest Path First (OSPF), definované [IETF](/mobilnisite/slovnik/ietf/) a začleněné do specifikací 3GPP pro použití v paketových doménách. Funguje jako multicastový směrovací protokol typu link-state. V MOSPF si směrovače vyměňují informace o členství ve skupinách prostřednictvím nového typu Link State Advertisement ([LSA](/mobilnisite/slovnik/lsa/)), tzv. group-membership-LSA. To umožňuje každému směrovači v oblasti OSPF vytvořit si úplný obraz o členství v multicastových skupinách a topologii sítě. Pomocí těchto informací může směrovač na vyžádání vypočítat strom nejkratších cest pro každou dvojici zdroj a multicastová skupina (S, G). Strom je zakořeněn ve zdroji a rozprostírá se ke všem směrovačům, které mají lokální členy skupiny, přičemž využívá Dijkstrův algoritmus aplikovaný na databázi topologie.

Fungování protokolu je úzce integrováno se základním unicastovým směrováním OSPF. Směrovače musí být schopné MOSPF, aby se mohly účastnit multicastového směrování. Designated Router ([DR](/mobilnisite/slovnik/dr/)) na segmentu sítě s více přístupy je zodpovědný za vytváření group-membership-LSA jménem lokálních členů skupiny nahlášených prostřednictvím protokolu Internet Group Management Protocol ([IGMP](/mobilnisite/slovnik/igmp/)). Tyto LSA jsou rozesílány (floodovány) po celé oblasti OSPF, což zajišťuje, že všechny směrovače mají synchronizované informace o multicastové topologii. Když na směrovač dorazí paket pro multicastovou skupinu a směrovač nemá pro tuto dvojici (S, G) uložený strom v mezipaměti, provede Dijkstrův výpočet pro určení výstupních rozhraní pro přeposílání. Tento výpočet využívá běžnou link-state databázi OSPF rozšířenou o informace o členství ve skupinách.

V rámci architektury 3GPP je MOSPF zmíněn v kontextu Packet Data Network Gateway ([P-GW](/mobilnisite/slovnik/p-gw/)) a páteřní IP přenosové sítě. Jeho úlohou je usnadňovat efektivní doručování multicastových služeb, jako jsou multicastové služby IP Multimedia Subsystem (IMS) nebo distribuce obsahu, napříč IP páteří operátora. Poskytuje mechanismus pro vytváření multicastových distribučních stromů bez nutnosti spoléhat se pouze na flooding nebo kontroly reverzní cesty (RPF) založené na unicastových směrovacích tabulkách. Jeho škálovatelnost je však omezena na jednu oblast OSPF, protože group-membership-LSA nejsou rozesílány do jiných oblastí; multicast mezi oblastmi vyžaduje jiné mechanismy.

## K čemu slouží

MOSPF byl vyvinut pro řešení potřeby efektivního, na topologii založeného multicastového směrování v rámci autonomních systémů, konkrétně těch, které používají OSPF jako svůj Interior Gateway Protocol (IGP). Před protokoly jako MOSPF se multicast často spoléhal na jednodušší, ale méně efektivní metody, jako je flooding nebo Distance Vector Multicast Routing Protocol ([DVMRP](/mobilnisite/slovnik/dvmrp/)), což mohlo vést k neoptimálním cestám a smyčkám provozu. Integrace multicastového směrování se spolehlivými, rychle konvergujícími principy link-state protokolu OSPF byla významnou motivací.

V kontextu 3GPP, jak se mobilní sítě vyvíjely pro podporu bohatých paketových služeb, jako je multimediální vysílání a skupinová komunikace, se efektivní multicast v páteřní síti stal nezbytným. MOSPF poskytl standardizovanou metodu pro operátory používající OSPF ve své páteři, aby nativně podporovali IP multicast, což umožnilo službám jako Multimedia Broadcast Multicast Service ([MBMS](/mobilnisite/slovnik/mbms/)) efektivní přenos od zdrojů obsahu k více základnovým stanicím nebo přímo k uživatelským zařízením. Řešil problém výpočtu optimálních multicastových distribučních stromů na základě skutečné síťové topologie a členství ve skupinách, čímž oproti unicastové replikaci nebo naivnímu multicastovému floodingu snížil redundantní provoz a zlepšil využití šířky pásma.

## Klíčové vlastnosti

- Multicastové směrování typu link-state integrované s OSPF
- Pro oznamování členství v multicastových skupinách používá Group-Membership-LSA
- Výpočet stromů nejkratších cest zakořeněných ve zdroji (Dijkstra) na vyžádání
- Vyžaduje synchronizovanou link-state databázi OSPF v celé oblasti
- Designated Router (DR) je zodpovědný za vytváření členských LSA na sdílených segmentech
- Poskytuje efektivní multicastové přeposílání v rámci jedné oblasti OSPF

## Související pojmy

- [MBMS – Multimedia Broadcast Multicast Service](/mobilnisite/slovnik/mbms/)
- [P-GW – Packet Data Network Gateway](/mobilnisite/slovnik/p-gw/)

## Definující specifikace

- **TS 29.061** (Rel-19) — Packet Domain Interworking for PLMN

---

📖 **Anglický originál a plná specifikace:** [MOSPF na 3GPP Explorer](https://3gpp-explorer.com/glossary/mospf/)
