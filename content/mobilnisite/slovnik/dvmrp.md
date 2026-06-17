---
slug: "dvmrp"
url: "/mobilnisite/slovnik/dvmrp/"
type: "slovnik"
title: "DVMRP – Distance Vector Multicast Routing Protocol"
date: 2025-01-01
abbr: "DVMRP"
fullName: "Distance Vector Multicast Routing Protocol"
category: "Protocol"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/dvmrp/"
summary: "DVMRP je vnitřní bránový multicastový směrovací protokol, který vytváří stromy distribuce specifické pro zdroj pomocí distance-vector algoritmu. V 3GPP je zmíněn pro IP multicastové směrování ve scéná"
---

DVMRP je vnitřní bránový multicastový směrovací protokol, který vytváří stromy distribuce specifické pro zdroj pomocí distance-vector algoritmu pro efektivní IP multicastové směrování ve scénářích propojení 3GPP s externími sítěmi.

## Popis

Distance Vector Multicast Routing Protocol (DVMRP) je internetový protokol používaný pro směrování multicastových datagramů v rámci autonomního systému. Jeho architektura je založena na směrovačích, které si vyměňují informace o směrování s přímo připojenými sousedy pomocí distance-vector algoritmu, podobně jako RIP, ale rozšířeného pro multicast. Mezi klíčové komponenty patří DVMRP směrovače, které udržují směrovací tabulky s metrikami (počtem skoků) k multicastovým zdrojům, a mechanismus protokolu pro vytváření multicastových distribučních stromů zakořeněných ve zdroji pomocí techniky zvané Reverse Path Forwarding (RPF).

DVMRP funguje v několika fázích. Nejprve si DVMRP sousedé navzájem objeví a vymění si reklamy tras. Tyto reklamy informují směrovače o nejkratší cestě zpět ke zdroji multicastové skupiny. Když dorazí multicastový paket, směrovač provede kontrolu RPF: ověří, zda paket dorazil na rozhraní, které je nejkratší cestou zpět k adrese zdroje paketu (podle své unicastové směrovací tabulky odvozené z DVMRP reklam). Pokud kontrola projde, paket je přeposlán na všechna následná rozhraní kromě toho, na které dorazil; jinak je zahoděn. Pro ořezání nežádoucího provozu používá DVMRP zprávy typu graft a prune pro dynamickou úpravu distribučního stromu, odřezávajíce větve, kde nejsou žádní členové skupiny.

V architektuře 3GPP je DVMRP zmíněn v kontextu propojení mezi Gateway [GPRS](/mobilnisite/slovnik/gprs/) Support Node (GGSN) nebo Packet Data Network Gateway (PGW) a externími IP sítěmi (např. internetem nebo sítí poskytovatele obsahu). Když se UE přihlásí k multicastové službě (jako je [MBMS](/mobilnisite/slovnik/mbms/)), může síť potřebovat směrovat multicastový provoz z externího zdroje. DVMRP je jedním z protokolů, které by mohly být použity v této externí směrovací doméně. Specifikace 3GPP definují, jak GGSN/PGW interaguje s takovými externími multicastovými směrovači, včetně proxy [IGMP](/mobilnisite/slovnik/igmp/)/[MLD](/mobilnisite/slovnik/mld/) a vytváření tunelů, ale vnitřní mechanika samotného DVMRP je definována [IETF](/mobilnisite/slovnik/ietf/).

## K čemu slouží

Účelem zmínky DVMRP ve standardech 3GPP je uznat a umožnit propojení se zastaralými infrastrukturami multicastového směrování, které mohou existovat v externích IP sítích připojených k mobilnímu jádru. Řeší problém doručování IP multicastového provozu ze zdrojů umístěných v tradičních, směrovači založených IP sítích k mobilním účastníkům přes 3GPP paketové jádro. Bez podpory takových propojovacích protokolů by byly multicastové služby omezeny na zdroje uvnitř vlastní sítě operátora.

Historicky byl DVMRP jedním z prvních široce nasazených multicastových směrovacích protokolů pro internet (Mbone). Ačkoli jsou dnes rozšířenější pokročilejší protokoly jako Protocol Independent Multicast (PIM), DVMRP existoval v mnoha sítích. Začlenění DVMRP do 3GPP od verze Rel-8 zajistilo zpětnou kompatibilitu a širokou interoperabilitu pro [MBMS](/mobilnisite/slovnik/mbms/) a další IP multicastové služby. Vyřešilo omezení, kdy je mobilní jádro multicastovým 'ostrovem', specifikací, jak se bránový uzel účastní nebo rozhraní s externími doménami multicastového směrování, bez ohledu na konkrétní protokol (DVMRP, PIM-SM atd.) v nich používaný, což umožnilo širší ekosystém pro doručování multicastového obsahu.

## Klíčové vlastnosti

- Používá distance-vector algoritmus s metrikou počtu skoků pro výpočet multicastové trasy
- Implementuje Reverse Path Forwarding (RPF) pro vytváření multicastových distribučních stromů specifických pro zdroj
- Podporuje dynamické ořezávání a přidávání větví stromu na základě členství ve skupině
- Navržen pro použití v rámci jedné administrativní domény (směrování uvnitř AS)
- Zahrnuje mechanismy objevování sousedů a periodické výměny informací o trasách
- Umí tunelovat multicastový provoz přes sítě, které multicast nepodporují (DVMRP tunel)

## Související pojmy

- [MBMS – Multimedia Broadcast Multicast Service](/mobilnisite/slovnik/mbms/)

## Definující specifikace

- **TS 29.061** (Rel-19) — Packet Domain Interworking for PLMN

---

📖 **Anglický originál a plná specifikace:** [DVMRP na 3GPP Explorer](https://3gpp-explorer.com/glossary/dvmrp/)
