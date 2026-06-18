---
slug: "ip-m"
url: "/mobilnisite/slovnik/ip-m/"
type: "slovnik"
title: "IP-M – Internet Protocol Multicast"
date: 2025-01-01
abbr: "IP-M"
fullName: "Internet Protocol Multicast"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/ip-m/"
summary: "Síťová služba pro efektivní distribuci IP datových toků od jednoho k mnoha nebo od mnoha k mnoha (např. živé video nebo aktualizace softwaru) skupině zájemců. Optimalizuje využití šířky pásma tím, že"
---

IP-M je síťová služba 3GPP pro efektivní distribuci IP datových toků od jednoho k mnoha, která optimalizuje šířku pásma tím, že síť replikuje pakety pouze v bodcích větvení.

## Popis

Internet Protocol Multicast (IP-M) je metoda směrování a doručování IP datagramů z jednoho zdroje (nebo více zdrojů) do skupiny cílů současně. Funguje na síťové vrstvě (vrstva 3) a používá specifický rozsah IP adres (224.0.0.0 až 239.255.255.255) určených jako skupinové multicastové adresy. Na rozdíl od unicastu, který vytváří samostatný datový tok pro každého příjemce, nebo broadcastu, který vysílá všem uzlům v podsíti, multicast vysílá jeden tok paketů, který je směrovači inteligentně duplikován pouze tam, kde se síťové cesty k více příjemcům rozcházejí. Tím vzniká efektivní distribuční strom.

V mobilní síti 3GPP představuje implementace IP-M jedinečné výzvy kvůli sdílenému rádiovému médiu a mobilitě uživatelů. Jádrová síť musí spravovat členství ve skupině (multicast group membership, s využitím protokolů jako [IGMP](/mobilnisite/slovnik/igmp/) nebo [MLD](/mobilnisite/slovnik/mld/)) a vytvářet efektivní cesty pro multicastový provoz. V kontextu 3GPP je IP-M primárně spojováno se službou Multimedia Broadcast Multicast Service ([MBMS](/mobilnisite/slovnik/mbms/)), zavedenou ve vydání 6 (Release 6). MBMS rozšiřuje základní IP multicast o funkce specifické pro buněčné sítě pro správu zdrojů na rádiovém rozhraní. Síť zahrnuje funkční entity jako Broadcast Multicast-Service Center ([BM-SC](/mobilnisite/slovnik/bm-sc/)), který slouží jako vstupní bod pro multicastový obsah, plánuje přenosy a spravuje oznámení služeb.

Doručování IP-M provozu přes rádiovou přístupovou síť (RAN) může využívat dva režimy: MBMS Broadcast mode, kde je obsah odesílán přes vyhrazený point-to-multipoint rádiový bearer pokrývající celou buňku, a MBMS Multicast mode, který může zahrnovat předplatné a správu klíčů pro zabezpečené doručení konkrétní skupině. V jádrové síti se MBMS Gateway ([MBMS-GW](/mobilnisite/slovnik/mbms-gw/)) stará o distribuci IP multicastu k RAN, přičemž používá multicastové směrovací protokoly jako [PIM](/mobilnisite/slovnik/pim/) (Protocol Independent Multicast). Pro uživatelské zařízení (UE) přijímání IP-M provozu typicky vyžaduje připojení se k multicastové skupině a aplikaci, která dokáže dekódovat datový tok. Specifikace 3GPP definují procedury pro zahájení/ukončení MBMS relace, registraci/odregistraci UE u multicastových služeb a řešení mobility pro zajištění nepřetržitého příjmu při pohybu uživatelů mezi buňkami.

## K čemu slouží

IP Multicast byl vyvinut k řešení inherentní neefektivity použití unicastu nebo broadcastu pro skupinovou komunikaci na internetu a privátních sítích. Pro služby jako živé televizní vysílání, burzovní tickery nebo distribuce softwaru ve velkém měřítku vyžaduje unicast, aby zdroj odeslal samostatnou kopii dat pro každého příjemce, což spotřebovává obrovské množství šířky pásma zdroje i sítě. Broadcast, ačkoli je efektivní v lokálním segmentu, plýtvá šířkou pásma a výpočetním výkonem na všech uzlech, včetně těch, které o obsah nemají zájem, a nelze jej škálovat za jedinou podsíť.

3GPP přijalo a rozšířilo IP-M, aby umožnilo efektivní doručování multimediálních služeb přes buněčné sítě, což je klíčová schopnost pro operátory usilující o nabídku vysílacích služeb (např. mobilní [TV](/mobilnisite/slovnik/tv/)) bez zahlcení jejich cenného rádiového spektra. Tradiční unicastový model by se pod zátěží tisíců uživatelů sledujících stejnou živou událost zhroutil. [MBMS](/mobilnisite/slovnik/mbms/), postavený na principech IP-M, byl řešením, které umožňuje, aby jeden rádiový přenos byl přijímán mnoha uživateli současně v buňce, což dramaticky zlepšuje spektrální účinnost.

Motivace byla jak technická, tak komerční: vytvořit životaschopnou platformu pro vysílání obsahu do mobilních zařízení, což umožňuje nové zdroje příjmů, a poskytnout mechanismus pro efektivní skupinovou komunikaci pro aplikace veřejné bezpečnosti a podnikové sféry. Slouží také jako základ pro pozdější technologie, jako je evolved MBMS (eMBMS) v LTE a další vylepšení v 5G pro komunikaci Vehicle-to-Everything (V2X) a systémy veřejného varování.

## Klíčové vlastnosti

- Používá IP adresy třídy D (224.0.0.0/4) pro identifikaci skupiny
- Vytváří efektivní distribuční stromy pomocí protokolů jako PIM (Protocol Independent Multicast)
- Podporuje dynamické členství ve skupině prostřednictvím IGMP (IPv4) nebo MLD (IPv6)
- Integrováno do 3GPP jako základní síťová vrstva pro služby MBMS
- Umožňuje významné úspory šířky pásma pro distribuci dat od jednoho k mnoha
- Vyžaduje, aby síťová infrastruktura (směrovače, BM-SC) podporovala multicastové směrování a správu služeb

## Související pojmy

- [MBMS – Multimedia Broadcast Multicast Service](/mobilnisite/slovnik/mbms/)
- [BM-SC – Broadcast-Multicast Service Centre](/mobilnisite/slovnik/bm-sc/)
- [MBSFN – Multimedia Broadcast multicast service Single Frequency Network](/mobilnisite/slovnik/mbsfn/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 22.060** (Rel-19) — GPRS Stage 1 Service Description

---

📖 **Anglický originál a plná specifikace:** [IP-M na 3GPP Explorer](https://3gpp-explorer.com/glossary/ip-m/)
