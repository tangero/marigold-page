---
slug: "n3qai"
url: "/mobilnisite/slovnik/n3qai/"
type: "slovnik"
title: "N3QAI – Non-3GPP QoS Assistance Information"
date: 2026-01-01
abbr: "N3QAI"
fullName: "Non-3GPP QoS Assistance Information"
category: "QoS"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/n3qai/"
summary: "N3QAI je sada parametrů poskytovaných UE síti pro pomoc při mapování QoS toků a vynucování politik pro provoz směrovaný přes non-3GPP přístup (např. Wi-Fi). Přenáší požadavky na QoS na aplikační úrovn"
---

N3QAI je sada parametrů od UE, která pomáhá síti při mapování QoS toků a vynucování politik pro provoz přes non-3GPP přístup, jako je Wi-Fi.

## Popis

Non-3GPP QoS Assistance Information (N3QAI) je koncept zavedený ve specifikaci 3GPP Release 18 pro zlepšení zpracování Quality of Service (QoS) pro User Equipment (UE) připojené přes nedůvěryhodný non-3GPP přístup, jako je Wi-Fi, prostřednictvím Non-3GPP InterWorking Function ([N3IWF](/mobilnisite/slovnik/n3iwf/)). V čistě 3GPP přístupovém scénáři je Radio Access Network (RAN) plně obeznámena s 5G QoS toky a dokáže je mapovat na příslušné rádiové přenašeče. Když však UE využívá non-3GPP přístup jako Wi-Fi, podkladová přístupová síť typicky nezná 5G QoS konstrukty. Mechanismus N3QAI umožňuje UE poskytnout 5G Core informace o charakteristikách QoS svého uplinkového provozu, což umožňuje lepší vynucování QoS na N3IWF a dále.

N3QAI jsou informace odesílané UE, typicky jako součást přenosu uplinkových dat v uživatelské rovině nebo prostřednictvím přidruženého řídicího signalizačního provozu při vytváření PDU session nebo QoS Flow přes non-3GPP přístup. Tyto informace zahrnují parametry popisující požadavky na QoS odesílaných aplikačních dat. Tyto parametry mohou odpovídat nebo být odvozeny od charakteristik 5G QoS, jako je 5G QoS Identifier ([5QI](/mobilnisite/slovnik/5qi/)), Allocation and Retention Priority ([ARP](/mobilnisite/slovnik/arp/)), Guaranteed Flow Bit Rate (GFBR), Maximum Flow Bit Rate ([MFBR](/mobilnisite/slovnik/mfbr/)), nebo jiné deskriptory provozu. Aplikační vrstva UE nebo její vrstva pro správu QoS generuje tyto pomocné informace na základě požadavků služby.

Po přijetí paketů označených N3QAI od UE přes NWu [IPsec](/mobilnisite/slovnik/ipsec/) tunel může N3IWF tyto informace využít. Hlavní role N3IWF je interpretovat N3QAI a provádět dvě klíčové funkce: za prvé mapovat příchozí provoz na příslušný 5G QoS Flow v rámci existující PDU session pro rozhraní N3 směrem k [UPF](/mobilnisite/slovnik/upf/); za druhé potenciálně aplikovat lokální QoS politiky nebo označení na provoz před jeho přeposláním. Toto pomáhá Session Management Function ([SMF](/mobilnisite/slovnik/smf/)) a Policy Control Function ([PCF](/mobilnisite/slovnik/pcf/)) 5G Core vynucovat správné QoS politiky end-to-end, i když samotný segment non-3GPP přístupu nativně nepodporuje signalizaci 5G QoS.

Architektonicky N3QAI funguje v rámci cesty uživatelské roviny mezi UE a N3IWF. Je to forma QoS signalizace, která doplňuje standardní signalizaci N1 NAS používanou pro zřizování QoS Flow. Jeho zavedení uznává, že v mnoha non-3GPP nasazeních, zejména Wi-Fi, jsou charakteristiky posledního segmentu linky (např. podmínky Wi-Fi kanálu, kongesce) pro 5G Core neprůhledné. Poskytnutím pomocných informací od UE – koncového bodu, který zažívá lokální přístupové podmínky – může síť činit informovanější rozhodnutí o prioritizaci provozu a alokaci zdrojů, čímž se zlepšuje celková konzistence kvality uživatelského zážitku pro služby jako hlas, video nebo hraní her při přístupu přes Wi-Fi.

## K čemu slouží

N3QAI bylo vytvořeno k řešení významné mezery v rámci 5G QoS při aplikaci na nedůvěryhodné non-3GPP přístupové sítě. Jádrem problému je asymetrie povědomí o QoS: zatímco 5G Core definuje přesné QoS toky s konkrétními parametry, non-3GPP přístupová síť (např. komerční nebo domácí Wi-Fi router) těmto 5G-specifickým konstruktům nerozumí. Před zavedením N3QAI se vynucování QoS pro provoz z UE přes non-3GPP přístup silně spoléhalo na statické politiky nakonfigurované na N3IWF nebo hlubokou inspekci paketů (DPI), což mohlo být neefektivní, nepřesné nebo dynamicky nezarovnané s potřebami aplikace.

Motivace pro N3QAI vychází z rostoucí závislosti na Wi-Fi pro poskytování vysoce kvalitních 5G služeb, zejména ve scénářích konvergence indoorových a fixních bezdrátových sítí. Bez mechanismu, kterým by UE mohlo komunikovat své požadavky na QoS v reálném čase, by síť mohla zacházet se vším provozem z Wi-Fi připojení s výchozím, potenciálně nízkoprioritním QoS profilem, což by degradovalo výkon aplikací citlivých na latenci nebo vyžadujících vysokou šířku pásma. N3QAI to řeší tím, že umožňuje UE, které má nejlepší znalost požadavků aplikace, tyto požadavky explicitně signalizovat interworking funkci.

Historicky existovaly podobné koncepty v omezené formě (jako značení DSCP přes IPsec), ale nebyly standardizovány v rámci architektury 3GPP pro non-3GPP přístup. N3QAI poskytuje standardizovanou metodu pro pomoc s QoS zarovnanou s 3GPP. Umožňuje dynamičtější a přesnější mapování QoS, což je zásadní pro podporu pokročilých 5G služeb jako network slicing, Ultra-Reliable Low Latency Communications (URLLC) a enhanced Mobile Broadband (eMBB) přes konvergované přístupové sítě. Představuje vývoj od síťově-centrického předpokladu QoS k více spolupracujícímu modelu QoS s asistencí koncového bodu pro heterogenní přístup.

## Klíčové vlastnosti

- Poskytuje podněty pro QoS pro uplinkový provoz přes nedůvěryhodný non-3GPP přístup, které pocházejí od UE
- Nese parametry analogické charakteristikám 5G QoS (např. 5QI, ARP, přenosové rychlosti)
- Umožňuje N3IWF provádět přesné mapování QoS Flow pro N3 tunel uživatelské roviny
- Napomáhá konzistentnímu vynucování QoS politik napříč 3GPP a non-3GPP přístupovými cestami
- Pomáhá udržovat kvalitu služby pro aplikace, když podkladový non-3GPP spoj je QoS-neuvědomělý
- Standardizovaný mechanismus zlepšující podporu network slicingu a pokročilých služeb přes Wi-Fi

## Související pojmy

- [5QI – 5G QoS Identifier](/mobilnisite/slovnik/5qi/)
- [N3IWF – Non-3GPP access InterWorking Function](/mobilnisite/slovnik/n3iwf/)
- [PCF – Positioning Calculation Function](/mobilnisite/slovnik/pcf/)
- [SMF – Service Management Function](/mobilnisite/slovnik/smf/)
- [ATSSS – Access Traffic Steering, Switching, and Splitting](/mobilnisite/slovnik/atsss/)

## Definující specifikace

- **TS 23.501** (Rel-20) — 5G System Architecture Stage 2
- **TS 24.501** (Rel-19) — 5G NAS Protocols Specification
- **TS 29.502** (Rel-19) — 5G System; Nsmf Service Based Interface; Stage 3

---

📖 **Anglický originál a plná specifikace:** [N3QAI na 3GPP Explorer](https://3gpp-explorer.com/glossary/n3qai/)
