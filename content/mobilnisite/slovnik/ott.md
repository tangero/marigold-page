---
slug: "ott"
url: "/mobilnisite/slovnik/ott/"
type: "slovnik"
title: "OTT – Over The Top"
date: 2026-01-01
abbr: "OTT"
fullName: "Over The Top"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/ott/"
summary: "Označuje aplikace a služby poskytované přes internet, které obcházejí tradiční servisní platformy řízené telekomunikačním operátorem. Příklady zahrnují VoIP, komunikační aplikace a streamování videa,"
---

OTT je služba poskytovaná přes internet, která obchází vlastní servisní platformy telekomunikačního operátora, využívá jeho IP konektivitu, nikoli však jeho vyhrazenou infrastrukturu, jako je tomu u VoIP nebo streamování videa.

## Popis

Over The Top (OTT) označuje poskytovatele služeb, kteří dodávají obsah, aplikace a komunikační služby koncovým uživatelům přímo prostřednictvím veřejného internetu, využívajíce internetový přístup poskytovaný operátory telekomunikačních sítí. V kontextu 3GPP jsou OTT služby odlišné od služeb řízených operátorem, jako je IMS (IP Multimedia Subsystem), např. VoLTE. Fungují nad transportní IP vrstvou operátora (tzv. 'hloupou trubkou') bez zapojení operátora do řízení služby, účtování nebo zajištění kvality na aplikační vrstvě. Příklady zahrnují Skype, WhatsApp, Netflix a YouTube.

Z architektonického hlediska mobilní síť poskytuje podkladovou IP přístupovou síť ([IP-CAN](/mobilnisite/slovnik/ip-can/)) – jako jsou datové přenosy LTE nebo 5G NR – která nabízí internetový přístup typu best-effort. Poskytovatel OTT služby provozuje vlastní aplikační servery v datových centrech nebo cloudových platformách. Uživatelské zařízení (UE) spouští klientskou aplikaci, která naváže šifrované spojení (např. přes TLS/[HTTPS](/mobilnisite/slovnik/https/), WebRTC) přímo s těmito OTT servery. Jádrová síť 3GPP (EPC nebo 5GC) si konkrétní OTT aplikace neuvědomuje; pouze směruje IP pakety mezi UE a internetem. To je v kontrastu se službami řízenými operátorem, kde jsou prvky jádrové sítě (jako [P-CSCF](/mobilnisite/slovnik/p-cscf/) v IMS) hluboko zapojeny do řízení relace a vynucování politik.

OTT služby fungují využitím standardizované IP konektivity mobilních sítí. UE se připojí k síti, naváže připojení k paketové datové síti (PDN) nebo relaci protokolové datové jednotky (PDU) s přístupovým bodem ([APN](/mobilnisite/slovnik/apn/)) pro internetový přístup a obdrží IP adresu. OTT aplikace na zařízení pak použije tuto IP konektivitu pro komunikaci se svými vzdálenými servery. Klíčovými odlišnostmi jsou absence integrace se systémy účtování 3GPP (místo toho se používá účtování přes app-store nebo kreditní kartu) a typicky žádná garantovaná kvalita služby (QoS) od operátora, ačkoli někteří operátoři nabízejí sponzorovaná data nebo balíčky s diferenciací QoS. 3GPP studuje dopady OTT, aby porozumělo vzorcům provozu, vyvinulo řídicí politiky a prozkoumalo potenciální spolupráci nebo nové obchodní modely, jako jsou partnerství v edge computingu.

## K čemu slouží

Fenomén OTT vznikl díky rozšířenému přijetí IP mobilního širokopásmového připojení (počínaje [HSPA](/mobilnisite/slovnik/hspa/) a LTE), které poskytlo dostatečnou šířku pásma a neustálé připojení pro bohaté internetové aplikace. Vyřešil problém, kdy inovace služeb byla limitována pomalými vývojovými a nasazovacími cykly operátorů. Podnikatelé a technologické společnosti mohly rychle vyvíjet a globálně nasazovat aplikace (jako hlas, video, zasílání zpráv) přímo spotřebitelům, aniž by museli vyjednávat se stovkami operátorů po celém světě nebo se integrovat do složitých telekomunikačních signalizačních systémů.

OTT služby řešily omezení tradičních telekomunikačních služeb, které byly často izolované, drahé (např. mezinárodní SMS) a postrádaly pokročilé funkce. Využily otevřeného, koncové-koncové principu internetu a škálovatelnosti cloudu. Pro 3GPP vzestup OTT vytvořil jak výzvy, tak příležitosti. Mezi výzvy patřil pokles příjmů z legacy služeb (hlas, SMS) a zvýšený, nepředvídatelný datový provoz zatěžující sítě. Příležitosti zahrnovaly zvýšenou poptávku po datových předplatných a potenciální nové role pro operátory, jako je poskytování vylepšené konektivity (např. síťové segmentace), edge hostování pro OTT aplikace nebo vystavení síťových [API](/mobilnisite/slovnik/api/) (přes [NEF](/mobilnisite/slovnik/nef/) v 5G) pro zlepšení kvality služeb.

3GPP začalo formálně studovat OTT ve verzi 12, aby porozumělo jeho technickým a obchodním dopadům, což vedlo k práci na vylepšení politik, detekci provozu a architektonickém vývoji, jako je Service Capability Exposure, které umožňují bezpečnou, standardizovanou interakci mezi sítí a poskytovateli OTT. Toto uznává, že zatímco OTT obchází tradiční servisní vrstvy, spolupráce může v éře 5G vytvořit hodnotu pro obě strany.

## Klíčové vlastnosti

- Služby poskytované nezávisle přes internetový přístup od operátora
- Žádná integrace s řídicími nebo účtovacími systémy 3GPP (např. IMS)
- Typicky používá koncové šifrování mezi aplikací na UE a OTT servery
- Spoléhá se na IP transport typu best-effort, pokud není vylepšen dohodami s operátorem
- Umožňuje rychlé, globální nasazení služeb bez integrace na úrovni jednotlivých operátorů
- Generuje vysoký, proměnlivý datový provoz v mobilních sítích

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [NEF – Network Exposure Function](/mobilnisite/slovnik/nef/)
- [MEC – Multi-Access Edge Computing](/mobilnisite/slovnik/mec/)
- [APN – Access Point Name](/mobilnisite/slovnik/apn/)

## Definující specifikace

- **TS 22.101** (Rel-20) — Service Principles for PLMNs
- **TR 22.816** (Rel-14) — 3GPP TV Service Enhancement Technical Report
- **TS 22.830** (Rel-16) — Business Role Models for Network Slicing
- **TS 23.791** (Rel-16) — NWDAF Data Collection & Analytics Framework
- **TS 26.849** (Rel-12) — MBMS Operation on Demand (MooD)
- **TR 26.909** (Rel-19) — QoE Enhancement for Streaming Services
- **TR 26.922** (Rel-19) — Video Telephony Robustness Improvements Study
- **TR 26.927** (Rel-19) — AI/ML in 5G Media Services Study
- **TS 28.802** (Rel-15) — Management Study for 5G Network Architecture

---

📖 **Anglický originál a plná specifikace:** [OTT na 3GPP Explorer](https://3gpp-explorer.com/glossary/ott/)
