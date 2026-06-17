---
slug: "grx"
url: "/mobilnisite/slovnik/grx/"
type: "slovnik"
title: "GRX – GPRS Roaming eXchange"
date: 2025-01-01
abbr: "GRX"
fullName: "GPRS Roaming eXchange"
category: "Core Network"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/grx/"
summary: "Privátní, zabezpečená páteřní síť IP propojující paketová jádra GPRS/UMTS různých mobilních operátorů po celém světě. Umožňuje plynulý datový roaming přenosem GTP-C a GTP-U provozu mezi domácí a navšt"
---

GRX je privátní páteřní síť využívající protokol IP, která propojuje jádrové sítě GPRS/UMTS mobilních operátorů za účelem zajištění bezpečného globálního datového roamingu přenosem GTP provozu mezi domácí a navštívenou sítí.

## Popis

[GPRS](/mobilnisite/slovnik/gprs/) Roaming eXchange (GRX) je vyhrazená, privátní síťová infrastruktura IP, která funguje jako rozbočovací uzel pro propojení paketově přepínaných jádrových sítí (GPRS, UMTS) různých mobilních síťových operátorů ([MNO](/mobilnisite/slovnik/mno/)) po celém světě. Není to jedna síť, ale koncept a soubor vzájemně propojených sítí provozovaných specializovanými GRX přepravci. Jejím hlavním úkolem je přenášet signalizační ([GTP-C](/mobilnisite/slovnik/gtp-c/)) a uživatelský ([GTP-U](/mobilnisite/slovnik/gtp-u/)) provoz protokolu GPRS Tunneling Protocol ([GTP](/mobilnisite/slovnik/gtp/)) mezi domácí veřejnou pozemní mobilní sítí ([HPLMN](/mobilnisite/slovnik/hplmn/)) roamujícího účastníka a navštívenou PLMN (VPLMN). Když účastník přejde do roamingu v cizí síti, jeho mobilní zařízení se připojí k místnímu radiovému přístupu a jádrové síti VPLMN. Pro paketové datové služby Serving GPRS Support Node (SGSN) ve VPLMN naváže přes GRX GTP tunely s Gateway GPRS Support Node (GGSN) v účastníkově HPLMN. Veškerý uživatelský datový provoz je směrován zpět do GGSN domácí sítě, který poskytuje přístup k internetu nebo jiným paketovým datovým sítím (PDN).

Z architektonického hlediska je GRX založen na IP technologii, konkrétně IPv4, a pro směrování mezi různými sítěmi GRX přepravců a páteřními sítěmi GPRS operátorů (často označovanými jako rozhraní Gp) používá Border Gateway Protocol (BGP-4). Každý MNO nebo GRX přepravce se připojuje k jednomu nebo více GRX rozbočovacím uzlům na specifických peeringových bodech. Bezpečnost je prvořadá; sítě GRX implementují přísné politiky firewallů, seznamy řízení přístupu ([ACL](/mobilnisite/slovnik/acl/)) a často používají tunely IP Security ([IPsec](/mobilnisite/slovnik/ipsec/)) k vytvoření důvěryhodného společenství. Tím je provoz GRX oddělen od veřejného internetu, což chrání signalizaci GTP před odposlechem a zajišťuje kvalitu služeb (QoS) a spolehlivost roamujících datových relací. Infrastruktura GRX také typicky zahrnuje Domain Name System (DNS) a někdy Diameter Routing Agents (DRA) pro překlad názvů APN na správné IP adresy GGSN napříč různými operátory, což je kritická funkce známá jako GPRS Roaming Exchange DNS (GRX DNS).

GRX funguje transparentně pro koncového uživatele i protokoly GTP. Z pohledu SGSN a GGSN se GRX jeví jako směrovaná IP síť spojující jejich rozhraní Gp. GTP tunely jsou navázány end-to-end mezi SGSN a GGSN, přičemž GRX pouze přeposílá IP pakety, které zapouzdřují hlavičky GTP a uživatelská data. Tento model centralizuje připojení účastníka k PDN a účtování v domácí síti, což zjednodušuje poskytování služeb a účtování pro roamujícího partnera. GRX byla základní architekturou pro globální datový roaming GPRS a UMTS, která se později vyvinula v model IPX (IP eXchange) pro podporu širší škály služeb, jako je IMS roaming, datový roaming LTE (S8HR) a propojení pro voice over LTE (VoLTE). Nicméně základní principy privátní, spravované páteřní sítě IP pro provoz mezi operátory zůstávají konzistentní.

## K čemu slouží

GRX byla vytvořena za účelem vyřešení kritického problému zajištění bezpečného a spolehlivého paketového datového roamingu pro mobilní účastníky. Před zavedením GRX operátoři pro GPRS roaming vytvářeli přímé bilaterální spoje (rozhraní Gp), což nebylo škálovatelné; operátor by potřeboval přímé spojení s každým potenciálním roamovacím partnerem, což vedlo ke složité síti propojení. To bylo ekonomicky i technicky neproveditelné pro globální pokrytí. GRX zavedla model hub-and-spoke (centrum a paprsky), kde se operátoři připojují ke společné, důvěryhodné zprostředkovatelské síti (GRX), která pak směruje provoz ke všem ostatním připojeným operátorům. To dramaticky snížilo počet potřebných spojení a zjednodušilo provozní složitost navazování roamových dohod.

Motivace vycházela z komerčního nasazení GPRS a později UMTS, které slibovaly 'vždy připojený' mobilní internet. Aby tento slib platil i mezinárodně, byla nezbytná robustní roamová infrastruktura. Veřejný internet byl pro tuto roli považován za nevhodný kvůli nedostatku zabezpečení, nepředvídatelné latenci, zpoždění (jitteru) a neschopnosti garantovat integritu signalizace GTP – která je citlivá a nese informace pro účtování. GRX poskytla řízené prostředí s garantovanou kvalitou a smlouvami o úrovni služeb (SLA) týkající se dostupnosti a výkonu. Zajistila, že citlivá účastnická data a signalizace nejsou vystavena veřejnému internetu, čímž zmírnila rizika podvodů a odposlechu.

Dále GRX vyřešila problém s objevováním sítě prostřednictvím systému GRX DNS. Když roamující účastník aktivuje datovou relaci s Access Point Name (APN), například 'internet', SGSN navštívené sítě potřebuje najít IP adresu GGSN v účastníkově domácí síti, která daný APN obsluhuje. Hierarchické GRX DNS umožňuje VPLMN dotazovat se na tuto informaci na základě APN Network Identifier (např. 'internet.mnc001.mcc234.gprs'), což umožňuje dynamické a škálovatelné překlad napříč stovkami operátorů. GRX se tak stala nepostradatelnou páteří globálního ekosystému mobilních dat, která umožnila zážitek 'roam like home' pro miliardy účastníků a připravila cestu pro pokročilejší sítě IPX, které dnes podporují roaming 4G a 5G.

## Klíčové vlastnosti

- Privátní, zabezpečená páteřní síť IP pro roamový provoz GPRS/UMTS mezi operátory
- Přenáší protokoly GTP-C a GTP-U mezi SGSN a GGSN napříč sítěmi
- Pro směrování mezi GRX přepravci a sítěmi operátorů používá BGP-4
- Poskytuje centralizované GRX DNS pro překlad APN na IP adresy GGSN
- Implementuje přísné bezpečnostní politiky (firewally, IPsec) k vytvoření důvěryhodného společenství
- Umožňuje škálovatelné propojení typu hub-and-spoke, čímž odstraňuje potřebu plně propojených bilaterálních spojů (full-mesh)

## Související pojmy

- [GPRS – CSI GPRS CAMEL Subscription Information](/mobilnisite/slovnik/gprs/)
- [GTP – GPRS Tunnelling Protocols](/mobilnisite/slovnik/gtp/)
- [IPX – Internetwork Packet Exchange](/mobilnisite/slovnik/ipx/)
- [APN – Access Point Name](/mobilnisite/slovnik/apn/)

## Definující specifikace

- **TR 22.893** (Rel-10) — IP Service Interconnection Requirements Study
- **TR 22.980** (Rel-19) — Network Composition Feasibility Study

---

📖 **Anglický originál a plná specifikace:** [GRX na 3GPP Explorer](https://3gpp-explorer.com/glossary/grx/)
