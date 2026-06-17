---
slug: "5g-brg"
url: "/mobilnisite/slovnik/5g-brg/"
type: "slovnik"
title: "5G-BRG – 5G Broadband Residential Gateway"
date: 2026-01-01
abbr: "5G-BRG"
fullName: "5G Broadband Residential Gateway"
category: "Services"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/5g-brg/"
summary: "Rezidenční brána pro 5G, která poskytuje pevný bezdrátový přístup (FWA) pro domácnosti a malé kanceláře pomocí 5G NR. Funguje jako můstek mezi 5G sítí a místní Wi-Fi/Ethernet, umožňuje vysokorychlostn"
---

5G-BRG je rezidenční brána, která poskytuje pevný bezdrátový přístup (FWA) pro domácnosti a malé kanceláře pomocí 5G NR, propojuje 5G síť s místní Wi-Fi/Ethernet pro vysokorychlostní širokopásmový přístup.

## Popis

5G Broadband Residential Gateway (5G-BRG) je zařízení typu customer premises equipment (CPE), které funguje jako rezidenční brána pro služby pevného bezdrátového přístupu (FWA) založené na 5G. Připojuje se k 5G síti prostřednictvím 5G New Radio (NR) rozhraní, typicky pomocí 5G modemu se SIM kartou nebo vestavěnou univerzální integrovanou obvodovou kartou (eUICC). 5G-BRG naváže s 5G core sítí (5GC) Packet Data Unit (PDU) session pro získání IP konektivity a z pohledu sítě se chová jako User Equipment (UE). Uvnitř obsahuje funkce směrování, Network Address Translation (NAT), firewall a často i server Dynamic Host Configuration Protocol (DHCP) pro distribuci konektivity místním zařízením přes Wi-Fi (např. Wi-Fi 6/6E) a Ethernet porty. Může podporovat dvoupásmovou nebo třípásmovou Wi-Fi, vícevstupní/výstupní (MIMO) antény pro lepší příjem 5G a správu kvality služeb (QoS) pro upřednostnění provozu, jako je streamování videa nebo hraní her.

Z architektonického hlediska 5G-BRG komunikuje s 5G sítí přes Next Generation Radio Access Network (NG-RAN) a 5GC za použití standardních 5G protokolů, jako je Non-Access Stratum (NAS) pro signalizaci. Je spravována funkcí 5GC Access and Mobility Management Function (AMF) pro registraci a mobilitu a funkcí Session Management Function (SMF) pro správu PDU session. 5G-BRG může také komunikovat s funkcí User Plane Function (UPF) pro přeposílání dat. Pro poskytování služeb a správu může používat 5G Network Exposure Function (NEF) nebo protokoly pro správu zařízení jako TR-069 nebo OMA-DM, jak je specifikováno ve standardech 3GPP pro rozhraní správy (např. v TS 29.525). Brána podporuje různé typy PDU session, jako IPv4, IPv6 nebo Ethernet, aby vyhověla různým konfiguracím domácích sítí.

Během provozu 5G-BRG provádí autentizaci a autorizaci pomocí metod 5G Authentication and Key Agreement (5G-AKA) nebo Extensible Authentication Protocol (EAP), čímž zajišťuje zabezpečený přístup k síti. Může implementovat 5G QoS mechanismy, mapováním místního provozu na 5G QoS Flows na základě QoS Identifiers (QCIs) nebo 5G QoS Indicators (5QIs), aby garantovala výkon pro aplikace jako ultra-spolehlivá nízkolatenční komunikace (URLLC) nebo vylepšené mobilní širokopásmové připojení (eMBB). Brána také zvládá události mobility, jako je předávání spojení mezi 5G buňkami, pro udržení plynulého připojení. Její role sahá až k podpoře síťového řezání (network slicing), kde může být nakonfigurována pro použití specifických síťových řezů pro diferencované služby, například řez optimalizovaný pro rezidenční broadband versus řez pro IoT. Díky tomu je 5G-BRG klíčovým prvkem pro nasazení 5G FWA, efektivně propojující mobilní a místní sítě.

## K čemu slouží

5G-BRG byl představen ve 3GPP Release 16, aby uspokojil rostoucí poptávku po vysokorychlostním širokopásmovém připojení v oblastech, kde je tradiční pevná infrastruktura (jako optika nebo kabel) nákladná nebo nepraktická na nasazení. Využívá vylepšené schopnosti 5G, jako jsou vyšší datové rychlosti, nižší latence a lepší kapacita, aby poskytl konkurenceschopnou alternativu k drátovému broadbandu. To podporuje strategie operátorů pro konvergenci pevných a mobilních služeb (FMC), umožňuje jim nabízet balíčkované služby a rozšiřovat tržní dosah bez rozsáhlých zemních prací. Historicky dřívější rezidenční brány pro 4G LTE poskytovaly FWA, ale byly limitovány nižšími špičkovými rychlostmi a vyšší latencí LTE, což je činilo méně vhodnými pro aplikace náročné na šířku pásma, jako je streamování 4K nebo cloudové hraní her.

Využitím 5G NR 5G-BRG tyto limity překonává, umožňuje rychlosti na úrovni gigabitů a podporu nových případů užití, jako je virtuální realita (VR) a aplikace pro chytré domácnosti. Také řeší potřebu flexibilního nasazení v městských, příměstských a venkovských oblastech, kde lze 5G sítě rozšířit rychleji než optiku. 5G-BRG se integruje s funkcemi 5GC, jako je síťové řezání (network slicing) a edge computing, což operátorům umožňuje nabízet přizpůsobené služby, například řezy s nízkou latencí pro hraní her nebo upřednostněné streamování videa. Tento vývoj od 4G k 5G FWA zařízením odráží posun odvětví ke konvergovaným sítím, které plynule propojují pevné a mobilní služby, poháněný spotřebitelskou poptávkou po všudypřítomném kvalitním připojení.

## Klíčové vlastnosti

- Konektivita 5G NR pro pevný bezdrátový přístup (FWA)
- Integrovaná Wi-Fi 6/6E a Ethernet pro místní síťování
- Podpora síťového řezání (network slicing) a správy QoS v 5G
- Autentizace pomocí 5G-AKA nebo EAP pro zabezpečený přístup
- Správa PDU session s typy IPv4/IPv6/Ethernet
- Vzdálená správa pomocí protokolů TR-069 nebo OMA-DM

## Definující specifikace

- **TS 23.003** (Rel-19) — Numbering, addressing and identification in 3GPP
- **TS 23.316** (Rel-19) — Wireline and Wireless Convergence Access Support
- **TS 23.501** (Rel-20) — 5G System Architecture Stage 2
- **TS 24.501** (Rel-19) — 5G NAS Protocols Specification
- **TS 29.507** (Rel-19) — 5G Access & Mobility Policy Control Service
- **TS 29.525** (Rel-19) — 5G UE Policy Control Service Stage 3
- **TS 29.561** (Rel-19) — 5G Interworking with External Data Networks

---

📖 **Anglický originál a plná specifikace:** [5G-BRG na 3GPP Explorer](https://3gpp-explorer.com/glossary/5g-brg/)
