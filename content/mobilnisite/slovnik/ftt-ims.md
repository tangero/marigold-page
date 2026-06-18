---
slug: "ftt-ims"
url: "/mobilnisite/slovnik/ftt-ims/"
type: "slovnik"
title: "FTT-IMS – Firewall Traversal Tunnel to IP network of IMS"
date: 2025-01-01
abbr: "FTT-IMS"
fullName: "Firewall Traversal Tunnel to IP network of IMS"
category: "Core Network"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/ftt-ims/"
summary: "Standardizovaný mechanismus pro bezpečný průchod firewally a NATy pro signalizaci a média v IMS. Zajišťuje spolehlivé poskytování IMS služeb napříč různými síťovými hranicemi, čímž garantuje konektivi"
---

FTT-IMS je standardizovaný mechanismus pro bezpečný průchod firewally a NATy, který zajišťuje spolehlivé signalizační a mediální spojení pro služby založené na SIP napříč různými síťovými hranicemi.

## Popis

Firewall Traversal Tunnel to IP network of IMS (FTT-IMS, Tunel pro průchod firewallem do IP sítě IMS) je řešení definované 3GPP specifikované v TS 24.322. Řeší zásadní problém navázání a udržování relací IP Multimedia Subsystem (IMS) přes síťové hranice obsahující firewally a Network Address Translators ([NAT](/mobilnisite/slovnik/nat/)). Tyto middleboxy často blokují nevyžádané příchozí pakety nebo zastírají skutečnou IP adresu a port uživatelského zařízení (UE), což narušuje předpoklady o end-to-end konektivitě protokolu Session Initiation Protocol ([SIP](/mobilnisite/slovnik/sip/)) a Real-time Transport Protocol ([RTP](/mobilnisite/slovnik/rtp/)). FTT-IMS poskytuje standardizovanou, sítí asistovanou metodu pro vytvoření a udržování zabezpečených pinholes nebo tunelů přes tyto bariéry.

Architektura zahrnuje několik klíčových funkčních entit. UE vybavené FTT-IMS klientem proces iniciuje. Klíčovým síťovým prvkem je FTT-IMS Application Server (FTT-IMS [AS](/mobilnisite/slovnik/as/)), který funguje jako signalizační zprostředkovatel a koncový bod tunelu. [P-CSCF](/mobilnisite/slovnik/p-cscf/) (Proxy-Call Session Control Function) je také obeznámen s postupy FTT-IMS. Mechanismu funguje tak, že UE nejprve naváže zabezpečené, dlouhodobé řídicí spojení (tunel) k FTT-IMS AS. Tento řídicí tunel se používá k výměně potřebných informací pro průchod médií. Když UE iniciuje nebo přijímá IMS relaci, nabídka/odpověď [SDP](/mobilnisite/slovnik/sdp/) (Session Description Protocol) je přenášena tímto řídicím tunelem. FTT-IMS AS poté může instruovat jakýkoli Session Border Controller (SBC) nebo firewall na trase, aby otevřel specifické pinholes pro RTP/[RTCP](/mobilnisite/slovnik/rtcp/) mediální toky spojené s touto relací, s využitím vyjednaných IP adres a portů.

Tento proces zajišťuje obousměrný tok mediálních paketů. Pro signalizaci jsou zprávy SIP také typicky směrovány přes FTT-IMS AS, který funguje jako odchozí proxy, a zajišťuje tak, že veškerá signalizace pochází ze stabilní, dosažitelné adresy. Řešení podporuje jak IPv4, tak IPv6 a je navrženo pro spolupráci s IMS Authentication and Key Agreement ([AKA](/mobilnisite/slovnik/aka/)) z důvodu zabezpečení. Jeho role je klíčová ve scénářích, kde je UE připojeno přes privátní nebo carrier-grade NAT, například v mnoha pevných širokopásmových nebo podnikových sítích, a garantuje spolehlivé fungování hlasových, video a messagingových služeb založených na IMS bez ohledu na topologii podkladové IP sítě.

## K čemu slouží

FTT-IMS byl vytvořen, aby vyřešil všudypřítomný problém selhání IMS služeb v sítích chráněných firewally a NATy. Původní IMS architektura předpokládala relativně otevřenou IP konektivitu, ale reálná nasazení, zejména když operátoři začali služby poskytovat přes třetí strany nebo nespravované přístupové sítě (jako je domácí Wi-Fi), čelila významným problémům s konektivitou. NATy porušují end-to-end princip internetu, což znemožňuje vzdálené straně iniciovat spojení k UE za NATem bez explicitních mechanismů. Firewally často blokují UDP porty používané protokoly SIP a RTP.

Před standardizací byly zkoušeny proprietární řešení a nestandardizované použití technik jako Interactive Connectivity Establishment (ICE) a Traversal Using Relays around NAT (TURN), ty však postrádaly interoperabilitu a síťovou kontrolu. Motivací pro FTT-IMS bylo poskytnout standardizované, operátorem spravované řešení, které garantuje doručení služby. Poskytuje síťovému operátorovi viditelnost a kontrolu nad procesem průchodu firewallem, což je zásadní pro zajištění kvality služby, zákonného odposlechu a konzistentního uživatelského zážitku pro služby kritické pro fungování, jako jsou tísňová volání přes IMS.

Jeho zavedení ve Release 12 bylo hnací silou potřeby upevnit IMS jako jedinou platformu pro hlasové a komunikační služby pro LTE (VoLTE) a budoucí sítě. Vyřešením problému s průchodem odstranil FTT-IMS hlavní překážku nasazení, což umožnilo vizi "IMS všude" a usnadnilo konvergenci pevných a mobilních služeb na společném IMS core.

## Klíčové vlastnosti

- Standardizovaný průchod firewally a NATy pro IMS signalizaci (SIP)
- Zabezpečené tunelování pro navázání mediálních (RTP/RTCP) toků
- Síťově řízená správa pinholes přes FTT-IMS AS
- Podpora pro IPv4 i IPv6 síťová prostředí
- Integrace s IMS AKA pro autentizaci a zabezpečení
- Umožňuje spolehlivé IMS služby pro UE v privátních/NATovaných sítích

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [P-CSCF – Proxy Call Session Control Function](/mobilnisite/slovnik/p-cscf/)
- [SIP – Session Initiation Protocol](/mobilnisite/slovnik/sip/)
- [NAT – Network Address Translation](/mobilnisite/slovnik/nat/)

## Definující specifikace

- **TS 24.322** (Rel-19) — IMS Tunneling over Restrictive Networks

---

📖 **Anglický originál a plná specifikace:** [FTT-IMS na 3GPP Explorer](https://3gpp-explorer.com/glossary/ftt-ims/)
