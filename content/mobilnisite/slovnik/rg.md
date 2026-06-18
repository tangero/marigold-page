---
slug: "rg"
url: "/mobilnisite/slovnik/rg/"
type: "slovnik"
title: "RG – Residential Gateway"
date: 2026-01-01
abbr: "RG"
fullName: "Residential Gateway"
category: "Other"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/rg/"
summary: "Síťové zařízení umístěné v prostorách zákazníka, například v domácnosti nebo malé kanceláři, které zajišťuje konektivitu mezi místními sítěmi (jako Wi-Fi nebo Ethernet) a širokopásmovou sítí poskytova"
---

RG (Residential Gateway) je síťové zařízení v prostorách zákazníka, které propojuje místní sítě se širokopásmovou sítí poskytovatele služeb a funguje jako centrální rozbočovač pro přístup k internetu do sítě 3GPP.

## Popis

Residential Gateway (RG) je zařízení typu [CPE](/mobilnisite/slovnik/cpe/) (customer-premises equipment), které slouží jako demarkační bod mezi vnitřní místní sítí ([LAN](/mobilnisite/slovnik/lan/)) účastníka a přístupovou sítí poskytovatele služeb. V architekturách 3GPP, zejména pro konvergenci pevných a mobilních sítí a širokopásmový přístup, RG zprostředkovává konektivitu přes různé přístupové technologie včetně [DSL](/mobilnisite/slovnik/dsl/), optických vláken ([PON](/mobilnisite/slovnik/pon/)) nebo bezdrátových rozhraní (např. přes 3GPP radiová rozhraní). Typicky zahrnuje router s funkcí [NAT](/mobilnisite/slovnik/nat/) (Network Address Translation) a firewallem, server [DHCP](/mobilnisite/slovnik/dhcp/) pro přidělování IP adres připojeným zařízením a často i integrovaný bezdrátový přístupový bod pro Wi-Fi konektivitu. RG spravuje politiky QoS (Quality of Service) pro priorizaci provozu, podporuje více služebních toků pro různé aplikace (jako hlas, video a data) a může implementovat bezpečnostní funkce jako WPA2/WPA3 pro Wi-Fi. Ve specifikacích 3GPP rozhraní RG komunikuje s síťovými prvky jako Broadband Network Gateway ([BNG](/mobilnisite/slovnik/bng/)) nebo User Plane Function ([UPF](/mobilnisite/slovnik/upf/)) v systémech 5G s využitím protokolů jako PPPoE nebo IPoE pro autentizaci a správu relací. Jeho role je klíčová pro poskytování triple-play služeb (internet, TV, hlas) a pro umožnění aplikací chytré domácnosti díky poskytování spolehlivé, spravované konektivity.

## K čemu slouží

Residential Gateway byl zaveden, aby poskytoval standardizovaný, spravovaný koncový bod pro širokopásmové služby v domácím a malém firemním prostředí. Řeší problém různorodého, nespravovaného zákaznického vybavení, které mohlo vést k nekonzistentní kvalitě služeb, bezpečnostním rizikům a složitému odstraňování závad pro operátory. Nasazením spravovaného RG mohou operátoři zajistit konzistentní výkon, vynutit politiky QoS, vzdáleně diagnostikovat problémy a nabízet služby s přidanou hodnotou, jako je spravované Wi-Fi nebo rodičovské kontroly. Historicky, jak se širokopásmové služby vyvíjely od jednoduchého přístupu k internetu k balíčkovým nabídkám zahrnujícím IPTV a VoIP, vznikla potřeba robustní, funkčně bohaté brány, která by zvládala více služebních toků s různými požadavky na latenci a šířku pásma. RG řeší omezení základních modemů integrací funkcí směrování, přepínání a často i bezdrátových schopností do jediného zařízení, čímž zjednodušuje instalaci u zákazníka a snižuje náklady na podporu.

## Klíčové vlastnosti

- Integrovaná funkce směrování a NAT pro připojení více zařízení k jedinému WAN připojení
- Vestavěný přístupový bod Wi-Fi podporující nejnovější standardy IEEE 802.11 (např. Wi-Fi 6)
- Správa kvality služeb (QoS) pro priorizaci typů provozu (hlas, video, data)
- Podpora více WAN technologií včetně DSL, optických vláken (PON) a bezdrátových technologií 3GPP
- Možnosti vzdálené správy prostřednictvím protokolu TR-069 nebo jiných protokolů pro správu
- Integrovaný firewall a bezpečnostní funkce pro ochranu sítě

## Související pojmy

- [BNG – Broadband Network Gateway](/mobilnisite/slovnik/bng/)
- [UPF – User Plane Function](/mobilnisite/slovnik/upf/)
- [CPE – Customer Premises Equipment](/mobilnisite/slovnik/cpe/)
- [PON – Passive Optical Network](/mobilnisite/slovnik/pon/)

## Definující specifikace

- **TS 23.003** (Rel-19) — Numbering, addressing and identification in 3GPP
- **TS 23.008** (Rel-19) — Organization of Subscriber Data
- **TS 23.139** (Rel-19) — 3GPP-Fixed Broadband Interworking Stage 2
- **TS 23.203** (Rel-19) — Policy and charging control architecture
- **TS 23.316** (Rel-19) — Wireline and Wireless Convergence Access Support
- **TS 23.501** (Rel-20) — 5G System Architecture Stage 2
- **TS 23.716** (Rel-16) — Wireline and Trusted Non-3GPP Access to 5G Core
- **TS 23.725** (Rel-16) — Study on URLLC Architecture Enhancements
- **TS 23.839** (Rel-12) — Fixed-Mobile Convergence Architecture Study
- **TS 23.896** (Rel-12) — Policy & Charging Control for Fixed Broadband Convergence
- **TS 24.501** (Rel-19) — 5G NAS Protocols Specification
- **TS 24.524** (Rel-19) — Hosted Enterprise Services Architecture
- **TS 25.309** (Rel-6) — FDD Enhanced Uplink Support
- **TS 25.319** (Rel-19) — Enhanced Uplink for UTRA FDD/TDD
- **TS 25.321** (Rel-19) — MAC Protocol Specification for UTRAN
- … a dalších 12 specifikací

---

📖 **Anglický originál a plná specifikace:** [RG na 3GPP Explorer](https://3gpp-explorer.com/glossary/rg/)
