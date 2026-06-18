---
slug: "pim-sm"
url: "/mobilnisite/slovnik/pim-sm/"
type: "slovnik"
title: "PIM-SM – Protocol Independent Multicast – Sparse Mode"
date: 2025-01-01
abbr: "PIM-SM"
fullName: "Protocol Independent Multicast – Sparse Mode"
category: "Protocol"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/pim-sm/"
summary: "Multicastový směrovací protokol používaný v sítích 3GPP pro efektivní skupinovou komunikaci. Funguje v řídkém režimu (sparse mode), což znamená, že vytváří distribuční stromy pouze tam, kde jsou příto"
---

PIM-SM je protokolně nezávislý multicastový směrovací protokol používaný v sítích 3GPP, který vytváří distribuční stromy pouze tam, kde jsou přítomni příjemci, aby optimalizoval šířku pásma pro efektivní skupinovou komunikaci.

## Popis

Protocol Independent Multicast – Sparse Mode (PIM-SM) je multicastový směrovací protokol definovaný ve specifikacích 3GPP pro použití v IP sítích, zejména v kontextu paketových datových služeb a propojování s externími sítěmi. Na rozdíl od multicastových protokolů v hustém režimu (dense-mode), které zpočátku zaplavují síť provozem, je PIM-SM navržen pro prostředí, kde jsou členové multicastové skupiny rozptýleni a řídce rozmístěni po síti. Jeho činnost začíná volbou bodu setkání (Rendezvous Point, [RP](/mobilnisite/slovnik/rp/)) pro každou multicastovou skupinu, který funguje jako centrální místo setkávání. Příjemci, kteří si přejí připojit se k multicastové skupině, odesílají explicitní zprávy Join směrem vzhůru k RP, čímž vytvářejí sdílený strom (RP-tree) od RP k příjemcům. Zdroje odesílají svůj multicastový provoz na RP, který jej následně distribuuje tímto sdíleným stromem. Pro zvýšení efektivity mohou směrovače na cestě od zdroje k příjemci iniciovat přechod ze sdíleného RP-stromu na strom nejkratší cesty (shortest-path tree, [SPT](/mobilnisite/slovnik/spt/)) přímo od zdroje, čímž optimalizují směrovací cestu. PIM-SM je protokolně nezávislý, protože nespoléhá na konkrétní unicastový směrovací protokol pro získávání topologických informací; využívá stávající unicastovou směrovací tabulku k určení sousedů na dalším skoku a pro kontrolu zpětné cesty (reverse-path forwarding, RPF). Mezi klíčové komponenty patří RP, určený směrovač (Designated Router, [DR](/mobilnisite/slovnik/dr/)) na podsíti pro zpracování zpráv Join/Prune a zprávy protokolu [PIM](/mobilnisite/slovnik/pim/) (Join, Prune, Register, Register-Stop), které spravují distribuční stromy. V architekturách 3GPP umožňuje PIM-SM efektivní doručování multicastových služeb, jako je propojení služby Multimedia Broadcast Multicast Service ([MBMS](/mobilnisite/slovnik/mbms/)) nebo distribuce [IPTV](/mobilnisite/slovnik/iptv/), v rámci paketové jádrové sítě a na rozhraních k externím IP sítím.

## K čemu slouží

PIM-SM byl zaveden, aby poskytl škálovatelnou a efektivní metodu pro multicastové směrování uvnitř a směrem k paketově přepínaným sítím 3GPP. Tradiční multicastové protokoly v hustém režimu byly neefektivní pro rozsáhlé sítě velkého rozsahu, kde je členů skupiny málo a jsou rozptýleni, protože způsobovaly počáteční zaplavování sítě a vysokou režii řízení. Přístup řídkého režimu (sparse-mode) tento problém řeší vytvářením distribučních stromů pouze tam, kde existuje explicitní členství, čímž šetří síťové zdroje. Jeho protokolová nezávislost umožňuje nasazení v různých síťových infrastrukturách používajících OSPF, IS-IS, BGP nebo statické směrování, což zajišťuje flexibilitu a integraci se stávajícími sítěmi operátorů. V kontextu 3GPP služby jako vysílání [TV](/mobilnisite/slovnik/tv/) nebo skupinová komunikace vyžadují efektivní směrování v jádrové síti bez zatížení všech uzlů, což motivovalo přijetí PIM-SM ve specifikacích jako 29.061 (Interworking with external networks) a 29.561 (Protocols for home network).

## Klíčové vlastnosti

- Provoz v řídkém režimu (sparse mode) vytvářející stromy pouze k explicitním příjemcům
- Protokolová nezávislost na podkladovém unicastovém směrování
- Použití bodu setkání (Rendezvous Point, RP) pro počáteční vytvoření stromu
- Schopnost přepnout ze sdíleného RP-stromu na strom nejkratší cesty (SPT) specifický pro zdroj
- Explicitní zprávy Join/Prune pro správu členství ve skupině
- Kontrola zpětné cesty (Reverse Path Forwarding, RPF) využívající unicastovou směrovací tabulku

## Související pojmy

- [MBMS – Multimedia Broadcast Multicast Service](/mobilnisite/slovnik/mbms/)
- [EPC – Evolved Packet Core Network](/mobilnisite/slovnik/epc/)

## Definující specifikace

- **TS 29.061** (Rel-19) — Packet Domain Interworking for PLMN
- **TS 29.561** (Rel-19) — 5G Interworking with External Data Networks

---

📖 **Anglický originál a plná specifikace:** [PIM-SM na 3GPP Explorer](https://3gpp-explorer.com/glossary/pim-sm/)
