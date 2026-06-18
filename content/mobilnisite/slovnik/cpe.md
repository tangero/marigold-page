---
slug: "cpe"
url: "/mobilnisite/slovnik/cpe/"
type: "slovnik"
title: "CPE – Customer Premises Equipment"
date: 2025-01-01
abbr: "CPE"
fullName: "Customer Premises Equipment"
category: "Other"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/cpe/"
summary: "Customer Premises Equipment (CPE) označuje telekomunikační zařízení umístěné na straně zákazníka, které jej připojuje k síti operátora. Zahrnuje širokou škálu zařízení, od tradičních modemů a routerů"
---

CPE je telekomunikační zařízení umístěné na straně zákazníka, jako je modem, router nebo 5G brána, které jej připojuje k síti operátora a umožňuje tak poskytování služeb.

## Popis

Customer Premises Equipment (CPE) je základním konceptem v telekomunikacích a označuje jakýkoli koncový bod a s ním spojené zařízení umístěné v prostorách účastníka a připojené k telekomunikačnímu okruhu poskytovatele na demarkačním bodě. Slouží jako rozhraní mezi vnitřní sítí zákazníka (domácí nebo firemní [LAN](/mobilnisite/slovnik/lan/)) a rozlehlou sítí ([WAN](/mobilnisite/slovnik/wan/)) poskytovanou operátorem služeb. V kontextu systémů 3GPP se CPE vyvinulo z jednoduchých zařízení pro mobilní širokopásmový přístup na sofistikované vybavení podporující pevný bezdrátový přístup ([FWA](/mobilnisite/slovnik/fwa/)), síťové segmenty (network slicing) a aplikace IoT.

Architektura CPE se významně liší v závislosti na jeho funkci. Pro mobilní širokopásmový přístup to může být [USB](/mobilnisite/slovnik/usb/) modem nebo mobilní hotspot router obsahující modul 3G/4G/5G modemu, síťový procesor a rozhraní Wi-Fi/Ethernet. Pro pevný bezdrátový přístup (FWA), zejména v 5G, je CPE často venkovní nebo vnitřní jednotka s integrovaným 5G modemem, anténou s vysokým ziskem a funkcí residenční brány. Funguje jako můstek, který převádí signál buněčného rádia (přes NR) na standardní IP provoz pro místní síť. Mezi klíčové vnitřní komponenty patří modem (zajišťující protokolové zásobníky a správu rádiových prostředků), routerová jednotka (pro [NAT](/mobilnisite/slovnik/nat/), firewall, [DHCP](/mobilnisite/slovnik/dhcp/)) a napájecí zdroj. Jeho úlohou je ukončit síťovou službu operátora na hraně zákazníka, poskytovat přístup, vynucovat zásady a často provádět počáteční agregaci provozu.

Provoz CPE zahrnuje několik vrstev. Fyzicky naváže spojení se sítí přes rádiové rozhraní (např. k gNB v 5G) nebo kabelové rozhraní. Běží na něm celý protokolový zásobník od fyzické vrstvy až po IP vrstvu, včetně potenciálně IMS funkcí pro hlas. Zařízení se autentizuje v síti (pomocí přihlašovacích údajů uložených v [SIM](/mobilnisite/slovnik/sim/) nebo vestavěném eSIM), naváže datovou relaci ([PDN](/mobilnisite/slovnik/pdn/) připojení nebo PDU session) a přijímá konfigurační parametry od operátora (např. přes OMA-DM nebo ANDSF). Poté směruje provoz mezi svými vnitřními rozhraními (Wi-Fi, Ethernet) a buněčným uplinkem, aplikuje zásady kvality služeb (QoS), bezpečnostní filtry a někdy i hlášení měření pro správu sítě.

V moderních sítích 3GPP je CPE klíčové pro modely poskytování služeb, jako je 5G FWA, kde nahrazuje tradiční pevné přípojky. Musí podporovat pokročilé funkce, jako je MIMO vyššího řádu pro lepší spolehlivost spojení, beamforming pro směrový zisk a povědomí o síťových segmentech (network slicing) pro izolaci provozu různých služeb (např. oddělení přístupu k internetu od vyhrazeného segmentu pro IoT). Správa CPE je standardizována, aby umožňovala operátorovi vzdálenou konfiguraci, softwarové aktualizace a monitorování poruch, čímž se zajišťuje kvalita služeb a zabezpečení. Jeho vývoj odráží rozšiřující se záběr buněčných sítí mimo mobilní terminály tak, aby zahrnoval pevné a IoT koncové body.

## K čemu slouží

CPE existuje proto, aby rozšířilo dosah síťových služeb operátora na místo zákazníka a poskytlo potřebné hardwarové a softwarové rozhraní pro využívání služeb. Řeší základní problém připojení koncových uživatelských zařízení (počítačů, telefonů, IoT senzorů) k rozlehlé telekomunikační síti. Historicky, před standardizovaným CPE, vedla proprietární zařízení k problémům s interoperabilitou, omezené přenositelnosti služeb a zvýšeným nákladům pro operátory i zákazníky. Standardizace v rámci 3GPP zajišťuje, že zařízení CPE se mohou spolehlivě připojovat k sítím po celém světě, podporovat automatizované zřizování a dodržovat bezpečnostní protokoly.

Motivací pro jeho pokračující vývoj v rámci vydání 3GPP jsou nové paradigmaty služeb. Zpočátku zaměřené na mobilní přístup k datům přes USB modemy se objevila potřeba integrovanějších zařízení (mobilních routerů) pro sdílení konektivity. Tlak na pevný bezdrátový přístup (FWA) jako konkurenční alternativu k vláknu/DSL vyžadoval vývoj robustních, vysoce výkonných CPE schopných poskytovat širokopásmový přístup na úrovni operátora přes buněčné spoje. Dále, rozmach IoT vyžadoval varianty CPE s nízkými náklady a nízkou spotřebou pro připojení senzorů. Každá evoluce řeší omezení: zlepšuje přenosové rychlosti, zvyšuje spolehlivost v náročných rádiových podmínkách, snižuje cenu zařízení a spotřebu energie a přidává podporu pro nové síťové funkce, jako je segmentace sítí (slicing) a edge computing. Standardizace CPE umožňuje hromadné nasazení, efektivní správu operátorem a konzistentní uživatelský zážitek napříč různými službami.

## Klíčové vlastnosti

- Fyzické ukončení sítě na straně zákazníka
- Rozhraní mezi buněčnou sítí a místní IP sítí (Wi-Fi/Ethernet)
- Vestavěný modem prováděcí 3GPP protokolový zásobník (NAS, RRC atd.)
- Podpora vzdálené správy a konfigurace operátorem (TR-069, OMA-DM)
- Autentizace a zabezpečené navázání relace (pomocí SIM/eSIM)
- Schopnosti vynucení QoS a směrování provozu

## Související pojmy

- [FWA – Fixed Wireless Access](/mobilnisite/slovnik/fwa/)
- [SIM – Subscriber Identity Module / Universal Subscriber Identity Module](/mobilnisite/slovnik/sim/)

## Definující specifikace

- **TR 22.978** (Rel-19) — Feasibility of All-IP Network (AIPN) in 3GPP
- **TS 23.716** (Rel-16) — Wireline and Trusted Non-3GPP Access to 5G Core
- **TS 26.253** (Rel-19) — IVAS Codec Algorithmic Description
- **TS 26.254** (Rel-19) — IVAS Rendering Functions Specification
- **TS 26.255** (Rel-19) — IVAS Frame Loss Concealment Procedure
- **TR 26.942** (Rel-19) — Study on Media Energy Consumption Exposure & Evaluation
- **TS 28.318** (Rel-19) — Management and Orchestration for Energy Utilities
- **TR 28.829** (Rel-18) — Technical Report on Network and Service Operations for Energy Utilities
- **TS 32.808** (Rel-8) — Common User Profile Storage Framework
- **TS 32.821** (Rel-9) — SON OAM Architecture for Home NodeB
- **TS 32.854** (Rel-11) — FMC Federated Network Information Model
- **TS 33.320** (Rel-19) — H(e)NB Subsystem Security Architecture
- **TS 36.101** (Rel-19) — LTE UE Radio Transmission & Reception Requirements
- **TS 36.783** (Rel-15) — Study on 1024QAM for LTE Downlink
- **TS 36.807** (Rel-10) — LTE Advanced UE Radio Requirements Study
- … a dalších 7 specifikací

---

📖 **Anglický originál a plná specifikace:** [CPE na 3GPP Explorer](https://3gpp-explorer.com/glossary/cpe/)
