---
slug: "w-5gcan"
url: "/mobilnisite/slovnik/w-5gcan/"
type: "slovnik"
title: "W-5GCAN – Wireline 5G Cable Access Network"
date: 2026-01-01
abbr: "W-5GCAN"
fullName: "Wireline 5G Cable Access Network"
category: "Other"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/w-5gcan/"
summary: "3GPP architektura pro integraci kabelových širokopásmových sítí založených na DOCSIS s 5G Core. Umožňuje kabelovým modemům a CPE připojit se jako 5G uživatelská zařízení (UE), což kabelovým operátorům"
---

W-5GCAN je 3GPP architektura pro integraci kabelových sítí založených na DOCSIS s 5G Core, která umožňuje kabelovým modemům připojit se jako 5G zařízení přes stávající HFC infrastrukturu.

## Popis

Wireline 5G Cable Access Network (W-5GCAN) je standardizovaná architektura v rámci 3GPP, která usnadňuje konvergenci kabelových širokopásmových sítí, zejména těch založených na standardech Data Over Cable Service Interface Specification ([DOCSIS](/mobilnisite/slovnik/docsis/)), se sítí 5G Core. Podobně jako [W-5GAN](/mobilnisite/slovnik/w-5gan/) a [W-5GBAN](/mobilnisite/slovnik/w-5gban/) klasifikuje kabelový přístup jako důvěryhodný non-3GPP přístup. Klíčovou síťovou funkcí umožňující tuto integraci je Cable Access Gateway Function, která plní zásadní roli adaptace protokolů mezi doménou DOCSIS kabelové sítě a doménou 5G Core.

Tato bránová funkce komunikuje se systémem Cable Modem Termination System (CMTS) nebo Converged Cable Access Platform (CCAP) v kabelové síti. Zachycuje řídicí a datový provoz z kabelových modemů ([CM](/mobilnisite/slovnik/cm/)) a vestavěných Multimedia Terminal Adapters (eMTA). Brána překládá kabelově specifické protokoly pro provisioning, autentizaci a správu (jako jsou zprávy správy DOCSIS [MAC](/mobilnisite/slovnik/mac/) a signalizace PacketCable) do nativní 5G signalizace přes rozhraní [N2](/mobilnisite/slovnik/n2/) k [AMF](/mobilnisite/slovnik/amf/). V uživatelské rovině navazuje [GTP-U](/mobilnisite/slovnik/gtp-u/) tunely přes rozhraní N3 k UPF, čímž efektivně směruje datový provoz účastníků přímo do datové sítě 5G Core, obcházejíce tradiční směrovací funkce systému ukončení kabelových modemů.

Technický proces zahrnuje, že kabelový modem nebo brána je rozpoznána jako 5G UE s předplatným v UDM. Během počátečního provisioningu nebo vytváření služebního toku funkce Cable Access Gateway Function usnadňuje 5G-AKA autentizaci. Po autentizaci SMF pro zařízení zřídí PDU Session. Parametry QoS kabelové sítě (např. DOCSIS služební toky se specifickými zárukami latence a šířky pásma) jsou mapovány na 5G QoS Flows pod kontrolou PCF. To umožňuje kabelovému operátorovi aplikovat bohaté možnosti řízení politik, účtování a síťového řezání 5G Core na své pevné širokopásmové účastníky, čímž vytváří bezproblémový servisní zážitek napříč kabelovým a mobilním přístupem.

## K čemu slouží

W-5GCAN byl vytvořen, aby řešil strategickou potřebu kabelových síťových operátorů (Multi-System Operators nebo MSO) zapojit se do 5G ekosystému s využitím jejich rozsáhlé Hybrid Fiber-Coaxial (HFC) infrastruktury. Historicky poskytovaly kabelové sítě širokopásmový internet, hlas a video pomocí zcela oddělených core sítí (PacketCable pro hlas, DOCSIS pro data) od mobilních operátorů. Toto oddělení bránilo nabídce konvergovaných služeb a vedlo k duplikaci síťových funkcí pro autentizaci, politiky a účtování.

Primární problém, který W-5GCAN řeší, je technologická izolace mezi světem DOCSIS/PacketCable a 3GPP mobilním světem. Poskytuje jasnou, standardy založenou cestu pro kabelové operátory k modernizaci jejich sítí přijetím 5G Core, čímž získávají přístup k pokročilým 5G schopnostem, jako je síťové řezání pro podnikové služby, integrace edge computingu a jednotné rámce politik. To je motivováno zejména expanzí kabelových operátorů do mobilních služeb (přes MVNO nebo vlastní rádiovou síť) a snahou nabídnout konzistentní "bezdrátový" zážitek přes jejich pevnou síť.

Zavedený ve Release 16, W-5GCAN využívá stejné principy konvergence jako W-5GAN, ale přizpůsobuje je specifickým protokolům, modelům QoS a provozním postupům kabelového průmyslu. Řeší omezení předchozích pokusů o konvergenci poskytnutím nativní podpory pro kabelově specifické funkce, jako je doručování multicastového videa v kontextu 5G PDU Session. To umožňuje kabelovým operátorům efektivně konkurovat vláknovým a mobilním operátorům nabídkou jednotného portfolia služeb nové generace ukotveného v jejich stávajícím koaxiálním vedení.

## Klíčové vlastnosti

- Integrace kabelových sítí HFC založených na DOCSIS jako důvěryhodný non-3GPP přístup k 5GC
- Definuje vzájemné propojení mezi protokoly DOCSIS/PacketCable a rozhraními 5G Core (N2, N3)
- Umožňuje kabelovým modemům a zařízením eMTA registrovat se jako 5G uživatelská zařízení (UE)
- Podporuje mapování DOCSIS služebních toků a parametrů QoS na 5G QoS Flows
- Umožňuje využití kabelového přístupu jako podkladové přenosové technologie pro 5G síťové řezy
- Usnadňuje jednotnou autentizaci a správu politik pro provoz pocházející z kabelové sítě prostřednictvím funkcí 5G Core

## Související pojmy

- [DOCSIS – Data Over Cable Service Interface Specification](/mobilnisite/slovnik/docsis/)
- [W-5GAN – Wireline 5G Access Network](/mobilnisite/slovnik/w-5gan/)

## Definující specifikace

- **TS 23.003** (Rel-19) — Numbering, addressing and identification in 3GPP
- **TS 23.316** (Rel-19) — Wireline and Wireless Convergence Access Support
- **TS 23.501** (Rel-20) — 5G System Architecture Stage 2
- **TS 23.716** (Rel-16) — Wireline and Trusted Non-3GPP Access to 5G Core
- **TS 29.507** (Rel-19) — 5G Access & Mobility Policy Control Service
- **TS 29.512** (Rel-19) — 5G Session Management Policy Control Service
- **TS 29.514** (Rel-19) — 5G System; Policy Authorization Service; Stage 3
- **TS 29.525** (Rel-19) — 5G UE Policy Control Service Stage 3

---

📖 **Anglický originál a plná specifikace:** [W-5GCAN na 3GPP Explorer](https://3gpp-explorer.com/glossary/w-5gcan/)
