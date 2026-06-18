---
slug: "ni"
url: "/mobilnisite/slovnik/ni/"
type: "slovnik"
title: "NI – Network Identifier"
date: 2025-01-01
abbr: "NI"
fullName: "Network Identifier"
category: "Identifier"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/ni/"
summary: "Povinná část názvu přístupového bodu (APN), která identifikuje externí paketovou datovou síť (PDN) nebo službu, ke které se chce UE připojit, například internet nebo síť IMS. Jedná se o doménovou znač"
---

NI je povinná doménová značka v názvu přístupového bodu (APN), která identifikuje externí paketovou datovou síť nebo službu, jako je 'internet' nebo 'ims', pro výběr brány a zřízení relace.

## Popis

Identifikátor sítě (NI) je základní součástí názvu přístupového bodu ([APN](/mobilnisite/slovnik/apn/)), což je plně kvalifikovaný název domény ([FQDN](/mobilnisite/slovnik/fqdn/)) používaný v paketových jádrech sítí 3GPP k určení přenosové cesty pro datovou relaci UE. APN se skládá ze dvou hlavních částí: identifikátoru sítě (NI) a identifikátoru operátora ([OI](/mobilnisite/slovnik/oi/)). NI je nejlevější částí APN FQDN a je jedinou povinnou složkou. Je to značka, která konkrétně identifikuje externí paketovou datovou síť ([PDN](/mobilnisite/slovnik/pdn/)) nebo konkrétní službu v síti operátora, ke které má UE v úmyslu přistupovat. Mezi běžné příklady patří 'internet', 'ims', 'mms' nebo název podnikové sítě jako 'companyvpn'. Když UE zahájí aktivaci kontextu [PDP](/mobilnisite/slovnik/pdp/) (ve 2G/3G) nebo žádost o připojení k PDN (ve 4G/5G), zahrne APN, což síti umožní pochopit požadovaný cíl uživatele.

Po přijetí žádosti síťový prvek ([SGSN](/mobilnisite/slovnik/sgsn/) v 2G/3G nebo [MME](/mobilnisite/slovnik/mme/) ve 4G) použije APN pro překlad [DNS](/mobilnisite/slovnik/dns/). NI hraje v tomto procesu překladu klíčovou roli. Síť vytvoří dotaz DNS pomocí APN FQDN, aby našla IP adresu(y) příslušné brány paketové datové sítě (PGW ve 4G, PCF+UPF v 5G), která obsluhuje tuto konkrétní externí síť nebo službu. Výběr PGW je zásadní, protože různé PGW mohou být vyhrazeny pro různé služby (např. jedna pro běžný internetový provoz, jiná pro hlasový provoz IMS s nízkou latencí) nebo se mohou připojovat k různým externím IP sítím. Vybraná brána se pak stane ukotvovacím bodem pro IP relaci UE.

Dále se NI používá ve spojení s informacemi profilu účastníka k aplikaci konkrétních pravidel řízení politiky a účtování (PCC). Síť dokáže na základě NI identifikovat přistupovanou službu a použít odpovídající parametry kvality služby (QoS), sazby účtování a zásady správy provozu. Například provoz z APN s NI 'ims' bude obvykle přiřazen třídě QoS s vysokou prioritou pro hlas, zatímco provoz 'internet' může mít třídu best-effort. NI tedy není pouze směrovací značkou, ale také klíčem pro spuštění správného chování sítě pro danou datovou relaci, což ovlivňuje uživatelský zážitek, účtování a správu síťových zdrojů.

## K čemu slouží

Koncept identifikátoru sítě (NI) byl vytvořen k vyřešení základního problému směrování datové relace mobilního uživatele do správné externí sítě škálovatelným a standardizovaným způsobem. V raných sítích GPRS, když operátoři začali nabízet přístup k více externím sítím (např. podniková intranet, brána WAP a veřejný internet), byl potřebný mechanismus k rozlišení těchto cílů. Bez standardizovaného identifikátoru by byly vyžadovány proprietární konfigurace, což by bránilo interoperabilitě mezi UE a sítěmi od různých výrobců a operátorů.

NI jako součást APN poskytuje tento standardizovaný vyhledávací mechanismus. Abstrahuje složitou topologii sítě od UE. UE potřebuje znát pouze logický název (např. 'internet'), nikoli konkrétní IP adresu brány. To umožňuje operátorům měnit jejich vnitřní síťovou architekturu, upgradovat nebo přesouvat brány a zavádět nové služby bez nutnosti aktualizace konfigurace každého UE. Také umožňuje bezproblémový roaming; navštěvující UE může použít známý APN NI (jako 'internet' nebo APN IMS partnerské sítě pro roaming) k získání služby a překlad DNS navštívené sítě směruje relaci na správnou místní nebo do domácí sítě směrovanou bránu na základě roamingových dohod. NI je tedy základním kamenem flexibilní, na služby orientované architektury paketového jádra, která se vyvinula od GPRS až po 5G.

## Klíčové vlastnosti

- Povinná součást plně kvalifikovaného názvu domény (FQDN) názvu přístupového bodu (APN)
- Identifikuje externí paketovou datovou síť (PDN) nebo službu (např. internet, IMS)
- Používá se pro výběr brány paketové datové sítě (PGW/UPF) založený na DNS
- Spouští konkrétní pravidla řízení politiky a účtování (PCC) a profily QoS
- Umožňuje diferenciaci služeb a alokaci síťových zdrojů
- Podporuje roaming účastníků prostřednictvím standardizovaných logických názvů

## Související pojmy

- [APN – Access Point Name](/mobilnisite/slovnik/apn/)
- [DNN – Data Network Name](/mobilnisite/slovnik/dnn/)
- [PGW – PDN Gateway](/mobilnisite/slovnik/pgw/)
- [PCC – Performance-oriented Congestion Control](/mobilnisite/slovnik/pcc/)

## Definující specifikace

- **TS 24.234** (Rel-12) — 3GPP-WLAN Interworking Network Selection
- **TS 25.211** (Rel-19) — UTRA FDD Layer 1: Transport & Physical Channels
- **TS 25.221** (Rel-19) — UTRA TDD Physical Layer Specification
- **TS 25.346** (Rel-19) — MBMS in UTRA Technical Specification
- **TS 25.433** (Rel-19) — Node B Application Part (NBAP) Protocol
- **TS 32.251** (Rel-19) — PS Domain Charging Management
- **TS 32.272** (Rel-19) — Charging for Push-to-Talk over Cellular (PoC)
- **TS 32.278** (Rel-19) — Monitoring Events Offline Charging Specification

---

📖 **Anglický originál a plná specifikace:** [NI na 3GPP Explorer](https://3gpp-explorer.com/glossary/ni/)
