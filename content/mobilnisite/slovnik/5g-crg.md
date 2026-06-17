---
slug: "5g-crg"
url: "/mobilnisite/slovnik/5g-crg/"
type: "slovnik"
title: "5G-CRG – 5G Cable Residential Gateway"
date: 2026-01-01
abbr: "5G-CRG"
fullName: "5G Cable Residential Gateway"
category: "Other"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/5g-crg/"
summary: "5G Cable Residential Gateway (5G-CRG) je konvergované síťové zařízení, které integruje 5G přístup s tradiční infrastrukturou kabelového širokopásmového připojení. Slouží jako most mezi 5G sítěmi a pev"
---

5G-CRG je konvergované síťové zařízení, které integruje 5G přístup s infrastrukturou kabelového širokopásmového připojení a slouží jako most pro zajištění residenčních 5G služeb přes stávající kabelové rozvody.

## Popis

5G Cable Residential Gateway je standardizovaná síťová funkce definovaná v 3GPP, která kombinuje schopnosti 5G uživatelského zařízení (UE) se schopnostmi tradičního klienta systému pro ukončení kabelových modemů (CMTS) nebo DOCSIS modemu. Z architektonického hlediska se nachází u zákazníka a obsahuje jak 5G modem, tak kabelovou modemovou komponentu. 5G-CRG navazuje spojení k 5G Core Network (5GC) prostřednictvím 5G Radio Access Network (NG-RAN) za použití standardních 5G protokolů a rozhraní, jako je rozhraní N1 pro signalizaci řídicí roviny a rozhraní N3/N6 pro data uživatelské roviny. Současně se připojuje ke kabelové síti, typicky za použití protokolů DOCSIS (Data Over Cable Service Interface Specification), aby poskytovalo širokopásmové připojení zařízením v domácnosti přes Ethernet nebo Wi-Fi.

Interně 5G-CRG implementuje konvergenční vrstvu, která spravuje integraci mezi 5G a kabelovou doménou. To zahrnuje funkce směrování provozu, mapování kvality služeb (QoS) a správy relací. Brána slouží jako jednotný bod autentizace a vynucování politik pro uživatele a vůči 5G síti se prezentuje jako UE s konkrétními předplatitelskými přihlašovacími údaji (SUPI/SUCI). Pro kabelovou síť se jeví jako standardní kabelový modem. 5G-CRG podporuje scénáře duální konektivity, kdy může být provoz směrován přes 5G nebo kabelovou cestu na základě síťových podmínek, politik nebo požadavků aplikace, což umožňuje vyrovnávání zatížení a redundanci.

Klíčové komponenty v architektuře 5G-CRG zahrnují 5G protokolový zásobník (NAS, RRC), zásobník kabelového modemu (DOCSIS MAC a PHY vrstvy), funkci konvergence a směrování a rozhraní pro místní síť (LAN switch, přístupový bod Wi-Fi). Zařízení je spravováno jak prostřednictvím systémů správy 5G sítě (jako je Network Slice Selection Function - NSSF a Policy Control Function - PCF), tak systémů správy kabelové sítě (jako je Cable Modem Termination System - CMTS). Jeho úlohou v síti je usnadňovat Fixed Mobile Convergence (FMC), což operátorům umožňuje využít jejich 5G spektrum a infrastrukturu k doručování vysokorychlostního internetu do domácností bez nutnosti kompletního nasazení vláken, a tím urychlit nasazení gigabitových širokopásmových služeb.

## K čemu slouží

5G-CRG bylo vytvořeno, aby řešilo rostoucí poptávku po vysokokapacitních residenčních internetových službách a potřebu efektivnějších strategií nasazování sítí. Tradiční přístupy k poskytování domácího širokopásmového připojení, jako je nasazování nové infrastruktury Fiber-to-the-Home (FTTH), jsou často nákladné a časově náročné, zejména v příměstských nebo venkovských oblastech. 5G-CRG umožňuje operátorům použít jejich 5G bezdrátové sítě jako řešení 'poslední míle', doručovat širokopásmové připojení do domácností vzduchem a poté využívat stávající koaxiální kabelové rozvody v domě pro distribuci. Tím se řeší problém 'posledního metru' uvnitř domu a odpadá nutnost instalace nového Ethernetového nebo Wi-Fi vybavení v každé místnosti.

Historicky fungovaly pevné a mobilní sítě odděleně, s vlastními core sítěmi, systémy správy a zařízeními u zákazníka. 5G-CRG, zavedené v 3GPP Release 16 jako součást širšího vylepšení 5G System (5GS) pro konvergenci s pevnými sítěmi, tyto bariéry odstraňuje. Řeší omezení předchozích řešení fixed-wireless, která byla často proprietární nebo vyžadovala samostatné modemy pro mobilní a domácí síťování, což vedlo ke složitým nastavením a neoptimálnímu uživatelskému zážitku. Standardizací konvergované brány umožňuje 3GPP bezproblémovou, operátorem spravovanou službu, která kombinuje vysokou kapacitu a nízkou latenci 5G s spolehlivostí a všudypřítomností kabelových sítí. To je motivováno zejména vzestupem Fixed Wireless Access (FWA) jako primárního případu užití 5G, což umožňuje mobilním operátorům přímou konkurenci tradičním poskytovatelům internetových služeb (ISP) o zákazníky residenčního širokopásmového připojení.

## Klíčové vlastnosti

- Konverguje 5G bezdrátový přístup s kabelovým širokopásmovým připojením založeným na DOCSIS
- Funguje zároveň jako 5G UE a jako kabelový modem pro připojení k duální síti
- Podporuje směrování provozu a mapování QoS mezi 5G a kabelovou doménou
- Umožňuje Fixed Mobile Convergence (FMC) pro residenční služby
- Usnadňuje nasazení 5G Fixed Wireless Access (FWA) využitím stávajících domácích kabelových rozvodů
- Spravováno prostřednictvím funkcí 5G core sítě i systémů správy kabelové sítě

## Definující specifikace

- **TS 23.003** (Rel-19) — Numbering, addressing and identification in 3GPP
- **TS 23.316** (Rel-19) — Wireline and Wireless Convergence Access Support
- **TS 23.501** (Rel-20) — 5G System Architecture Stage 2
- **TS 23.716** (Rel-16) — Wireline and Trusted Non-3GPP Access to 5G Core
- **TS 24.501** (Rel-19) — 5G NAS Protocols Specification
- **TS 29.507** (Rel-19) — 5G Access & Mobility Policy Control Service
- **TS 29.525** (Rel-19) — 5G UE Policy Control Service Stage 3
- **TS 29.561** (Rel-19) — 5G Interworking with External Data Networks

---

📖 **Anglický originál a plná specifikace:** [5G-CRG na 3GPP Explorer](https://3gpp-explorer.com/glossary/5g-crg/)
