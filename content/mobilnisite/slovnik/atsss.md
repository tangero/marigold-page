---
slug: "atsss"
url: "/mobilnisite/slovnik/atsss/"
type: "slovnik"
title: "ATSSS – Access Traffic Steering, Switching, and Splitting"
date: 2026-01-01
abbr: "ATSSS"
fullName: "Access Traffic Steering, Switching, and Splitting"
category: "Services"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/atsss/"
summary: "ATSSS je rámec 3GPP umožňující současné využití více přístupových sítí (3GPP i ne-3GPP) pro jednu PDU relaci. Inteligentně směruje, přepíná a rozděluje provoz přes dostupné cesty pro optimalizaci výko"
---

ATSSS je rámec 3GPP pro jednu datovou relaci, který umožňuje současné a inteligentní směrování, přepínání a rozdělování provozu přes více přístupových sítí za účelem optimalizace výkonu a spolehlivosti.

## Popis

ATSSS je komplexní rámec standardizovaný ve specifikacích 3GPP Release 16 a novějších, který umožňuje uživatelskému zařízení (UE) zřídit a využívat jednu relaci protokolové datové jednotky (PDU) přes více přístupových sítí současně. Tyto přístupové sítě mohou zahrnovat 3GPP přístupy (jako 5G NR nebo LTE) i ne-3GPP přístupy (jako Wi-Fi nebo pevné sítě). Základním architektonickým principem je funkce ATSSS, která sídlí ve funkci uživatelské roviny ([UPF](/mobilnisite/slovnik/upf/)) a v UE a spolupracuje s funkcí správy relací ([SMF](/mobilnisite/slovnik/smf/)) v řídicí rovině.

Systém funguje prostřednictvím tří základních mechanismů pro zpracování provozu: Směrování (Steering), Přepínání (Switching) a Rozdělení (Splitting). Směrování zahrnuje výběr nejvhodnější přístupové sítě pro nový tok provozu na základě politik (např. citlivý na latenci poslat na 5G, hromadné stahování na Wi-Fi). Přepínání zahrnuje dynamický přesun probíhajícího toku z jednoho přístupu na jiný, typicky pro zachování kontinuity služeb při zhoršení kvality aktuálního přístupu. Rozdělení zahrnuje distribuci paketů jednoho IP toku přes více přístupových sítí, což lze provést na úrovni paketů (na bázi [MPTCP](/mobilnisite/slovnik/mptcp/)) nebo na IP vrstvě (na bázi [ATSSS-LL](/mobilnisite/slovnik/atsss-ll/)), za účelem agregace přenosové kapacity a zvýšení spolehlivosti.

Klíčové součásti zahrnují Řídicí funkci ATSSS (součást SMF), která spravuje politiky a pravidla ATSSS, a Funkci uživatelské roviny ATSSS (v rámci UPF a UE), která provádí skutečné rozdělování provozu. Rámec využívá rozhraní N4 pro poskytnutí těchto pravidel ze SMF do UPF. Politiky vycházejí z funkce řízení politik ([PCF](/mobilnisite/slovnik/pcf/)) a mohou zohledňovat podmínky přístupových sítí v reálném čase, uživatelský tarif a požadavky aplikací. Schopnost ATSSS v UE je vyjednána během zřizování PDU relace.

ATSSS hraje klíčovou roli v architektuře 5G tím, že naplňuje skutečnou konvergenci více přístupů. Posouvá se nad rámec prostého výběru přístupu (jako [ANDSF](/mobilnisite/slovnik/andsf/)/MPTCP) a poskytuje plynulé, politikami řízené a detailní řízení toho, jak uživatelský provoz využívá heterogenní přístupové prostředky. To operátorům umožňuje poskytovat vylepšený kvalitativní uživatelský zážitek (QoE) tím, že pro danou službu vždy využívají nejlepší dostupné síťové cesty, čímž zlepšují celkovou efektivitu sítě a využití prostředků.

## K čemu slouží

ATSSS byl vytvořen k řešení základní výzvy efektivního a inteligentního využití více dostupných přístupových sítí (buněčných i nebuněčných), ke kterým se může moderní UE připojit. Před ATSSS řešení jako funkce pro zjišťování a výběr přístupové sítě ([ANDSF](/mobilnisite/slovnik/andsf/)) poskytovala výběr přístupu na základě politik, ale postrádala schopnost používat více přístupů současně pro jednu relaci nebo dynamicky přepínat/rozdělovat provoz v rámci toku. Multi-Path TCP ([MPTCP](/mobilnisite/slovnik/mptcp/)) nabízelo rozdělování na aplikační vrstvě, ale vyžadovalo podporu aplikace a nebylo těsně integrováno s rámcem politik jádrové sítě.

Primární motivací bylo zlepšit uživatelský zážitek prostřednictvím lepšího výkonu, spolehlivosti a plynulé mobility. Tím, že umožňuje směrování, přepínání a rozdělování provozu, ATSSS zajišťuje, že kritické aplikace vždy využívají nejlepší dostupnou cestu, mohou přežít výpadek jednoho typu přístupu bez přerušení služby a mohou agregovat přenosovou kapacitu z více přístupů. To je obzvláště důležité pro vizi 5G podporovat rozmanité služby (eMBB, URLLC, mMTC), kde se požadavky na latenci, přenosovou kapacitu a spolehlivost dramaticky liší.

ATSSS navíc poskytuje operátorům standardizovaný, sítí řízený mechanismus pro správu provozu přes heterogenní přístupy. Umožňuje nové obchodní modely, jako je konvergence pevných a mobilních sítí, tím, že zachází s Wi-Fi a 5G jako s komplementárními prostředky pod jednotným řízením politik. Řeší omezení předchozích fragmentovaných přístupů hlubokou integrací do servisně orientované architektury 5G jádra a poskytuje škálovatelný a flexibilní rámec nezbytný pro budoucnost konvergovaných sítí.

## Klíčové vlastnosti

- Umožňuje jednu PDU relaci přes více 3GPP a ne-3GPP přístupů
- Poskytuje tři provozní režimy: Směrování (Steering), Přepínání (Switching) a Rozdělení (Splitting)
- Podporuje dvě metody rozdělování: na bázi MPTCP a na bázi nižší vrstvy ATSSS (ATSSS-LL)
- Řízeno sítí prostřednictvím politik z PCF, vynucováno SMF a UPF
- Zvyšuje kontinuitu služeb a spolehlivost prostřednictvím dynamického přepínání přístupů
- Umožňuje agregaci přenosové kapacity a optimalizovaný výběr cesty pro každý tok provozu

## Související pojmy

- [MPTCP – Multi-Path TCP Protocol](/mobilnisite/slovnik/mptcp/)
- [UPF – User Plane Function](/mobilnisite/slovnik/upf/)
- [SMF – Service Management Function](/mobilnisite/slovnik/smf/)

## Definující specifikace

- **TS 23.501** (Rel-20) — 5G System Architecture Stage 2
- **TS 23.793** (Rel-16) — 5G ATSSS Study
- **TS 24.193** (Rel-19) — ATSSS Procedures Specification
- **TS 24.301** (Rel-19) — NAS protocol for Evolved Packet System
- **TS 24.501** (Rel-19) — 5G NAS Protocols Specification
- **TS 26.804** (Rel-19) — 5G Media Streaming Extensions Study
- **TS 28.104** (Rel-19) — Management Data Analytics (MDA)
- **TS 29.214** (Rel-19) — Policy and Charging Control over Rx
- **TS 29.244** (Rel-19) — PFCP Specification for Control/User Plane Separation
- **TS 29.512** (Rel-19) — 5G Session Management Policy Control Service
- **TS 29.514** (Rel-19) — 5G System; Policy Authorization Service; Stage 3
- **TS 29.519** (Rel-19) — UDR Usage for Policy & Exposure Data
- **TS 29.523** (Rel-19) — 5G Policy Control Event Exposure Service
- **TS 32.255** (Rel-20) — Telecom Management; Charging for 5G Data Connectivity
- **TS 32.291** (Rel-19) — Charging Management: Service-Based Interface Protocol
- … a dalších 1 specifikací

---

📖 **Anglický originál a plná specifikace:** [ATSSS na 3GPP Explorer](https://3gpp-explorer.com/glossary/atsss/)
