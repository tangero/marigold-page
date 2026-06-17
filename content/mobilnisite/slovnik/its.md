---
slug: "its"
url: "/mobilnisite/slovnik/its/"
type: "slovnik"
title: "ITS – Intelligent Transport Systems"
date: 2025-01-01
abbr: "ITS"
fullName: "Intelligent Transport Systems"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/its/"
summary: "Komplexní rámec pro komunikaci vozidel (V2X) umožňující služby bezpečnosti, efektivity provozu a infotainmentu. Definuje komunikaci mezi vozidly (V2V), s infrastrukturou (V2I), s chodci (V2P) a se sít"
---

ITS je komplexní rámec pro komunikaci vozidel (V2X), který umožňuje služby bezpečnosti, efektivity provozu a infotainmentu prostřednictvím spojení V2V, V2I, V2P a V2N s využitím rozhraní PC5 i mobilních sítí.

## Popis

Inteligentní dopravní systémy (ITS) v kontextu 3GPP označují standardizaci schopností mobilních sítí pro podporu komunikace vozidel, běžně známé jako V2X (Vehicle-to-Everything). Jedná se o rámec na aplikační vrstvě, který využívá jak vyvinuté technologie LTE, tak 5G NR pro přístup k rádiovým sítím. Architektura podporuje dva základní komunikační režimy: přímou komunikaci přes rozhraní PC5 (sidelink) a síťovou komunikaci přes rozhraní Uu. Rozhraní PC5 umožňuje přímou komunikaci mezi zařízeními s nízkou latencí, která je klíčová pro bezpečnostní aplikace, jako je zabránění kolizím, a to i mimo pokrytí sítě. Rozhraní Uu využívá tradiční mobilní spojení mezi UE (vozidlem) a základnovou stanicí (gNB nebo [eNB](/mobilnisite/slovnik/enb/)) pro služby s delším dosahem řízené sítí, jako je optimalizace dopravního toku a infotainment.

Rámec ITS definuje celý zásobník, včetně podpory aplikační vrstvy, zabezpečení a správy QoS. Na aplikační vrstvě podporuje standardizované sady zpráv, jako jsou zprávy [ETSI](/mobilnisite/slovnik/etsi/) ITS Cooperative Awareness Messages ([CAM](/mobilnisite/slovnik/cam/)) a Decentralized Environmental Notification Messages ([DENM](/mobilnisite/slovnik/denm/)). Tyto zprávy přenášejí informace jako poloha vozidla, rychlost, směr a varování před událostmi. Systém 3GPP zajišťuje přenos těchto zpráv s přísnými požadavky na spolehlivost a latenci. Pro síťovou komunikaci (V2N) se UE připojuje k aplikačnímu serveru V2X ([AS](/mobilnisite/slovnik/as/)) přes páteřní síť. Pro přímou komunikaci (V2V, V2I, V2P) může UE použít LTE-V2X (založené na LTE sidelink) nebo NR-V2X (založené na 5G NR sidelink) přes rozhraní PC5, s přidělováním zdrojů řízeným sítí (režim 3/4 pro LTE, režim 1/2 pro NR) nebo vybraným autonomně vozidlem.

Mezi klíčové síťové komponenty patří řídicí funkce V2X, která sídlí v páteřní síti a je zodpovědná za autorizaci UE pro služby V2X a jejich vybavení potřebnými parametry, jako je geografické mapování zdrojů pro PC5. Funkce řízení politik ([PCF](/mobilnisite/slovnik/pcf/)) hraje klíčovou roli při prosazování politik specifických pro V2X. Kritickým aspektem je identifikátor ITS aplikace, globálně jednoznačné číslo identifikující konkrétní objekt ITS aplikace (např. konkrétní bezpečnostní službu). Tento identifikátor se v síti používá k aplikaci správných politik, směrování a zacházení s QoS na datové toky spojené s danou aplikací. Vývoj od LTE-V2X ve verzi 14 k rozšířenému V2X (eV2X) ve verzi 15 a NR-V2X ve verzi 16 a novějších kontinuálně rozšiřuje možnosti a podporuje pokročilé případy užití, jako je sdílení senzorů, jízda v koloně a automatizované řízení s ultra vysokou spolehlivostí a nízkou latencí.

## K čemu slouží

ITS bylo standardizováno 3GPP, aby reagovalo na rostoucí globální potřebu bezpečnější, efektivnější a automatizované silniční dopravy. Tradiční bezpečnostní systémy vozidel (jako radar) byly omezeny na přímou viditelnost a sadu senzorů jednotlivého vozidla. Motivací bylo vytvořit standardizovaný komunikační systém založený na mobilních sítích, který by mohl rozšířit povědomí vozidla daleko za jeho vlastní senzory a umožnit kooperativní vnímání. Tím se řeší omezení, jako je detekce mrtvého úhlu, varování před kolizí na křižovatkách a varování nouzového brzdového světla sdělované od vozidel vpředu.

Vytvoření 3GPP ITS bylo také hnací silou snahy využít všudypřítomné nasazení a kontinuální vývoj mobilních sítí. Zatímco standardy pro vyhrazenou krátkou komunikaci (DSRC) existovaly, 3GPP poskytlo cestu pro integraci se službami mobilních sítí široké oblasti, nabízející delší dosah prostřednictvím sítě (V2N), zvýšené zabezpečení díky ekosystému mobilních sítí a jasnou cestu vývoje směrem k 5G. Počínaje verzí 14 se základními bezpečnostními službami V2X založenými na LTE se rozsah rozšířil na podporu stále náročnějších případů užití pro automatizované řízení, které vyžadují extrémní spolehlivost, velmi nízkou latenci a vysoké přenosové rychlosti – schopnosti poskytované sidelinkem NR-V2X zavedeným v pozdějších verzích. Tato práce řeší problém roztříštěných standardů pro komunikaci vozidel tím, že poskytuje jednotnou, globálně škálovatelnou platformu podporující jak okamžité bezpečnostní aplikace, tak dlouhodobou vizi propojené a automatizované mobility.

## Klíčové vlastnosti

- Podporuje duální komunikační režimy: přímé rozhraní PC5 (sidelink) a síťové rozhraní Uu
- Definuje identifikátory aplikací pro globálně jednoznačné rozpoznání služeb ITS
- Umožňuje komunikační scénáře V2V, V2I, V2P a V2N
- Specifikuje přísné požadavky na QoS pro bezpečnostní zprávy s nízkou latencí a vysokou spolehlivostí
- Vyvinuto z LTE-V2X (Rel-14/15) na NR-V2X (Rel-16+) pro pokročilé případy užití
- Zahrnuje síťové řídicí funkce pro autorizaci a správu zdrojů

## Definující specifikace

- **TS 22.186** (Rel-19) — Service requirements for enhanced V2X support
- **TR 22.885** (Rel-14) — LTE support for V2X services
- **TR 22.890** (Rel-19) — Study on Railway Smart Station Services
- **TR 22.967** (Rel-19) — eCall Emergency Data Transmission
- **TS 23.256** (Rel-19) — UAS Support Architecture Enhancements
- **TS 23.285** (Rel-19) — V2X Architecture Enhancements for LTE
- **TS 23.287** (Rel-19) — 5G V2X Architecture Enhancements
- **TS 23.795** (Rel-16) — V2X Application Architecture Study
- **TS 24.386** (Rel-19) — V2X Communication Protocols and Procedures
- **TS 24.486** (Rel-19) — V2X Application Enabler (VAE) Protocol Spec
- **TS 24.587** (Rel-19) — V2X Services Protocols for 5G System
- **TS 33.185** (Rel-19) — V2X Security in LTE
- **TS 33.836** (Rel-16) — Security Study for Advanced V2X Services
- **TS 33.885** (Rel-14) — Security Study for V2X Services
- **TS 36.101** (Rel-19) — LTE UE Radio Transmission & Reception Requirements
- … a dalších 15 specifikací

---

📖 **Anglický originál a plná specifikace:** [ITS na 3GPP Explorer](https://3gpp-explorer.com/glossary/its/)
