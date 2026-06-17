---
slug: "lipa"
url: "/mobilnisite/slovnik/lipa/"
type: "slovnik"
title: "LIPA – Local IP Access"
date: 2025-01-01
abbr: "LIPA"
fullName: "Local IP Access"
category: "Services"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/lipa/"
summary: "LIPA umožňuje uživatelskému zařízení (UE) přistupovat k místní IP síti, jako je domácí nebo podniková síť, přímo přes femtobuňku nebo Home NodeB/eNodeB, bez směrování provozu přes jádrovou síť mobilní"
---

LIPA je funkce, která umožňuje mobilnímu zařízení přistupovat k místní IP síti přímo přes femtobuňku bez směrování provozu přes jádrovou síť operátora.

## Popis

Local IP Access (LIPA) je standardizovaná funkce 3GPP, která umožňuje mobilnímu zařízení připojenému přes femtobuňku (Home NodeB nebo Home eNodeB) přímo přistupovat k jiným IP zařízením ve stejné místní síti areálu. Architektura je založena na Lokální bráně ([L-GW](/mobilnisite/slovnik/l-gw/)), což je logická funkce typicky umístěná společně s femtobuňkou. Když UE zahájí připojení k paketové datové síti (PDN) pro LIPA, femtobuňka a její přidružená L-GW vytvoří přímou IP cestu mezi UE a místní sítí. L-GW pro toto konkrétní PDN připojení funguje jako výchozí IP směrovač pro UE a vykonává funkce jako přidělování IP adres (pomocí [DHCP](/mobilnisite/slovnik/dhcp/)) a přeposílání provozu. Jádrová síť mobilního operátora, konkrétně Serving Gateway (S-GW) a Packet Data Network Gateway ([P-GW](/mobilnisite/slovnik/p-gw/)), je pro tento místní provoz obcházena, přičemž zůstává zapojena do řídicí roviny, například při navazování spojení a správě mobility pro buněčný přenos.

Funkce LIPA je úzce integrována s podsystémem femtobuňky a jejím bezpečnostním bránovým prvkem (SeGW). L-GW může být implementována jako samostatná fyzická entita nebo, častěji, jako logická funkce integrovaná do hardwaru femtobuňky. Aby UE mohlo používat LIPA, musí být v dosahu femtobuňky, která LIPA podporuje a je pro takový přístup autorizována. UE žádá o PDN připojení pro LIPA použitím konkrétního Access Point Name ([APN](/mobilnisite/slovnik/apn/)) nakonfigurovaného pro místní přístup. Femtobuňka po přijetí této žádosti komunikuje s Mobility Management Entity ([MME](/mobilnisite/slovnik/mme/)) v jádrové síti za účelem autorizace. Po autorizaci je datová cesta nastavena přímo mezi UE a L-GW. Všechny IP pakety určené pro místní síť směruje L-GW, zatímco pakety určené pro veřejný internet by typicky vyžadovaly samostatné, ne-LIPA PDN připojení, které je směrováno přes operátorovou jádrovou P-GW.

Role LIPA je významná při odlehčování lokalizovaného, datově náročného provozu. Umožňuje případy použití, jako je přístup k místnímu síťovému úložišti ([NAS](/mobilnisite/slovnik/nas/)), tisk na místní tiskárně nebo streamování z místního mediálního serveru bez spotřeby často omezené kapacity přenosové trasy (backhaul) femtobuňky k jádrové síti operátora. Tato architektura zachovává uživatelský komfort pro místní služby, i když je širokopásmové internetové připojení přetížené nebo nedostupné. Zabezpečení pro místní přístup je spravováno na IP vrstvě uvnitř místní sítě, protože zabezpečení rádiového rozhraní buněčné sítě končí na femtobuňce. LIPA představuje konvergenci buněčných a lokálních sítí ([LAN](/mobilnisite/slovnik/lan/)), rozšiřující koncept důvěryhodné místní sítě na zařízení používající technologii buněčného rádiového přenosu.

## K čemu slouží

LIPA byla vytvořena, aby řešila rostoucí využití femtobuněk a malých buněk (small cells) v rezidenčních a podnikových prostředích. Klíčovým problémem bylo, že veškerý datový provoz UE, dokonce i provoz určený pro tiskárnu ve stejné místnosti, byl tradičně směrován přes bránu jádrové sítě mobilního operátora ([P-GW](/mobilnisite/slovnik/p-gw/)), která je často umístěna stovky kilometrů daleko. Toto 'trombónování' místního provozu zvyšovalo latenci, spotřebovávalo cennou šířku pásma přenosové trasy (backhaul) (což může být nákladové úzké hrdlo pro nasazení femtobuněk) a nepřinášelo žádný výkonnostní benefit pro čistě místní komunikaci. Také to omezovalo užitečnost femtobuněk pro vytváření efektivních lokálních sítí pro buněčná zařízení.

Historicky, před LIPA, mohlo UE přistupovat ke službám pouze přes jádrovou síť operátora. To bylo neefektivní pro vznikající model nasazení malých buněk. Motivací pro LIPA bylo umožnit efektivnější architekturu, kde by lokalizovaná komunikace mohla zůstat místní, což odpovídá chování Wi-Fi v lokální síti. Řeší problém s přetížením přenosové trasy (backhaul) pro malé buňky, snižuje latenci pro místní služby a umožňuje operátorům nabízet nové balíčky služeb zahrnující bezproblémový přístup k zařízením na straně zákazníka. Řešila omezení předchozích buněčných architektur, které byly navrženy primárně pro přístup k rozlehlé síti (WAN), nikoli pro optimalizovaný přístup k lokální síti (LAN) prostřednictvím infrastruktury nasazené operátorem.

## Klíčové vlastnosti

- Umožňuje přímý přístup UE k místním IP sítím přes femtobuňku
- Odlehčení provozu z jádrové sítě mobilního operátora pro místní destinace
- Využívá spolulokalizovanou funkci Lokální brány (L-GW)
- Vyžaduje specifický Access Point Name (APN) s podporou LIPA
- Podporuje mobilitu v rámci pokrytí femtobuňky (kontinuita LIPA)
- Nezávislá správa IP adres pro segment místní sítě

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.060** (Rel-19) — GPRS Service Description Stage 2
- **TS 23.401** (Rel-19) — Evolved Packet System (EPS) Stage 2 Description
- **TS 24.008** (Rel-19) — 3GPP TS 24008: Core Network Protocols
- **TS 24.301** (Rel-19) — NAS protocol for Evolved Packet System
- **TS 25.413** (Rel-19) — Radio Access Network Application Part (RANAP)
- **TS 25.467** (Rel-19) — UTRAN Architecture for 3G Home Node B
- **TS 29.060** (Rel-19) — GPRS Tunnelling Protocol (GTP) version 1
- **TS 29.274** (Rel-19) — GTPv2-C Control Plane Protocol Specification
- **TS 29.303** (Rel-19) — DNS Procedures for Evolved Packet System
- **TS 33.107** (Rel-19) — Lawful Interception Architecture & Functions
- **TS 33.320** (Rel-19) — H(e)NB Subsystem Security Architecture
- **TS 36.300** (Rel-19) — E-UTRAN Radio Interface Protocol Architecture Overview
- **TS 36.413** (Rel-19) — S1 Application Protocol (S1AP)
- **TS 36.875** (Rel-13) — Dual Connectivity Extension Requirements

---

📖 **Anglický originál a plná specifikace:** [LIPA na 3GPP Explorer](https://3gpp-explorer.com/glossary/lipa/)
