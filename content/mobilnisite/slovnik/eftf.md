---
slug: "eftf"
url: "/mobilnisite/slovnik/eftf/"
type: "slovnik"
title: "EFTF – Enhanced Firewall Traversal Function"
date: 2025-01-01
abbr: "EFTF"
fullName: "Enhanced Firewall Traversal Function"
category: "Core Network"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/eftf/"
summary: "Síťová funkce, která usnadňuje bezpečné a efektivní překonávání hranic firewallů a NAT pro IP komunikační služby. Umožňuje službám, jako je IMS hlas a video, spolehlivě fungovat v různých síťových dom"
---

EFTF je síťová funkce, která umožňuje bezpečné a efektivní překonávání hranic firewallů a NAT pro podporu spolehlivých IP služeb, jako je IMS hlas a video, napříč síťovými doménami.

## Popis

Enhanced Firewall Traversal Function (EFTF) je prvek jádra sítě definovaný v architektuře 3GPP, konkrétně v TS 24.322. Funguje jako funkční entita navržená pro správu a optimalizaci toku IP provozu, zejména pro služby reálného času jako IMS (IP Multimedia Subsystem) hlas a video, přes síťové hranice obsahující firewally a překladače síťových adres ([NAT](/mobilnisite/slovnik/nat/)). Tyto hranice často komunikaci brání blokováním nevyžádaných příchozích paketů nebo změnou IP adres a čísel portů, což narušuje protokoly závislé na end-to-end konektivitě.

Architektonicky se EFTF typicky nachází v domácí síti uživatele nebo v důvěryhodné síti poskytovatele služeb. Funguje ve spolupráci s dalšími IMS entitami, jako je [P-CSCF](/mobilnisite/slovnik/p-cscf/) (Proxy-Call Session Control Function). Jeho hlavní mechanismus spočívá v roli zprostředkovatele nebo přenosového bodu. Pro odchozí provoz z UE za NAT/firewallem jej EFTF může přijmout a přeposlat, čímž vytvoří vazbu (binding) nebo otvor (pinhole) ve firewallu. Pro příchozí provoz určený pro dané UE může EFTF tento provoz přesměrovat přes vytvořenou cestu nebo použít techniky jako překlad paketů, aby zajistil jeho doručení na správnou privátní IP adresu a port uvnitř lokální sítě.

Klíčové součásti jeho fungování zahrnují vazby správy relací, kde udržuje mapování mezi privátní transportní adresou UE (IP:port) a veřejnou transportní adresou, a funkce přenosu provozu. Může také implementovat aplikační brány (ALGs) nebo využívat protokoly jako [ICE](/mobilnisite/slovnik/ice/) (Interactive Connectivity Establishment) ve spolupráci s UE k nalezení optimální komunikační cesty. Jeho role je klíčová pro zajištění kontinuity relace, udržování NAT připojení (keep-alive) a podporu různých typů NAT (např. full-cone, symmetric), čímž zaručuje, že kritické IMS služby fungují bezproblémově bez ohledu na omezení základní IP konektivity uložená mezilehlými síťovými zařízeními.

## K čemu slouží

EFTF byl vytvořen k řešení základního problému poskytování spolehlivých IP multimediálních služeb v reálných sítích plných privátního adresování a bezpečnostních bariér. Rozšíření [NAT](/mobilnisite/slovnik/nat/) a stavových firewallů, nezbytných pro šetření IPv4 adresami a síťovou bezpečnost, inherentně narušuje end-to-end princip internetu. To představovalo vážnou výzvu pro IMS a další služby založené na SIP, protože signalizace pro sestavení hovoru a mediální toky mohly být blokovány nebo špatně směrovány, což vedlo k neúspěšným relacím nebo jednosměrnému audiu.

Před standardizovanými funkcemi, jako je EFTF, byla řešení často proprietární, spoléhala pouze na klientské protokoly STUN/TURN/[ICE](/mobilnisite/slovnik/ice/) (které mohly selhat ve složitých scénářích s NAT) nebo vyžadovala invazivní konfiguraci firewallů. EFTF poskytuje standardizované, síťově asistované řešení. Odstraňuje omezení čistě koncových metod zavedením důvěryhodné síťové funkce, která dokáže spravovat otvory ve firewallech, provádět překlad adres, je-li to nutné, a zajistit, že jak signalizace, tak mediální toky mohou předvídatelně a bezpečně překonávat síťové hranice.

Jeho zavedení v 3GPP Release 12 bylo motivováno potřebou robustnějšího a operátorsky vhodného nasazení IMS, zejména pro VoLTE (Voice over LTE). Umožňuje mobilním operátorům garantovat kvalitu a spolehlivost služeb pro hlasové a videohovory, když se uživatelé pohybují mezi různými přístupovými sítěmi (např. z mobilní sítě na Wi-Fi) nebo jsou obsluhováni CGNAT (Carrier-Grade NAT) v jádrech mobilních sítí, a tím zajišťuje konzistentní uživatelský zážitek.

## Klíčové vlastnosti

- Usnadňuje překonávání NAT a firewallů pro SIP a RTP/RTCP provoz
- Udržuje vazby mezi privátními a veřejnými transportními adresami pro UE
- Slouží jako přenosový bod nebo zprostředkovatel pro mediální pakety, když jsou přímé end-to-end cesty blokovány
- Podporuje různé typy NAT včetně symmetric a full-cone
- Integruje se s IMS architekturou a spolupracuje s P-CSCF
- Umožňuje mechanizmy NAT keep-alive pro udržení kontinuity relace

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [P-CSCF – Proxy Call Session Control Function](/mobilnisite/slovnik/p-cscf/)
- [NAT – Network Address Translation](/mobilnisite/slovnik/nat/)
- [ICE – Interactivity Connectivity Establishment](/mobilnisite/slovnik/ice/)

## Definující specifikace

- **TS 24.322** (Rel-19) — IMS Tunneling over Restrictive Networks

---

📖 **Anglický originál a plná specifikace:** [EFTF na 3GPP Explorer](https://3gpp-explorer.com/glossary/eftf/)
