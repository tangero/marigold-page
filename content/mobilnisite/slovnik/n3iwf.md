---
slug: "n3iwf"
url: "/mobilnisite/slovnik/n3iwf/"
type: "slovnik"
title: "N3IWF – Non-3GPP access InterWorking Function"
date: 2026-01-01
abbr: "N3IWF"
fullName: "Non-3GPP access InterWorking Function"
category: "Core Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/n3iwf/"
summary: "N3IWF je funkce jádra sítě, která umožňuje bezpečnou a plynulou integraci přístupových sítí mimo 3GPP (non-3GPP), jako je Wi-Fi, do 5G Core. Funguje jako důvěryhodná brána, která ukončuje IPsec tunely"
---

N3IWF je funkce jádra sítě, která umožňuje bezpečnou integraci přístupových sítí mimo 3GPP (non-3GPP) do 5G Core tím, že funguje jako brána, která ukončuje IPsec tunely a přeposílá provoz.

## Popis

Funkce pro propojení s přístupem mimo 3GPP (Non-3GPP InterWorking Function, N3IWF) je klíčová síťová funkce v architektuře 5G Core (5GC), konkrétně definovaná pro integraci nedůvěryhodných přístupových sítí mimo 3GPP. Nedůvěryhodný přístup mimo 3GPP označuje primárně přístupové technologie nespecifikované 3GPP, jako je Wi-Fi, které jsou z pohledu zabezpečení 5G Core považovány za nedůvěryhodné. N3IWF slouží jako bezpečný vstupní bod pro uživatelské zařízení (UE) připojené přes takový přístup, přičemž se sama etabluje jako koncový bod v důvěryhodné doméně operátora.

Architektonicky rozhraní N3IWF komunikuje s UE přes referenční bod NWu, který využívá protokoly IKEv2 a [IPsec](/mobilnisite/slovnik/ipsec/) k vytváření zabezpečených tunelů. Tím je zajištěna důvěrnost a integrita provozu v uživatelské rovině a signalizace mezi UE a 5GC. Na straně sítě se N3IWF připojuje k ostatním síťovým funkcím 5GC přes standardní rozhraní: k funkci pro správu přístupu a mobility ([AMF](/mobilnisite/slovnik/amf/)) přes rozhraní [N2](/mobilnisite/slovnik/n2/) pro signalizaci v řídicí rovině (např. registrace, autentizace) a k funkci uživatelské roviny ([UPF](/mobilnisite/slovnik/upf/)) přes rozhraní N3 pro přenos uživatelských dat. To umožňuje, aby bylo s UE zacházeno, jako by bylo připojeno přes 3GPP rádiový přístup, což zajišťuje konzistentní kontinuitu služeb a vynucování politik.

Činnost N3IWF zahrnuje několik klíčových procedur. Při počátečním připojení UE objeví N3IWF a provede autentizaci IKEv2 a vytvoření zabezpečené asociace IPsec (SA), často s využitím přihlašovacích údajů pro 5G autentizaci (např. z USIM). N3IWF poté přeposílá [NAS](/mobilnisite/slovnik/nas/) zprávy UE (zapouzdřené v IPsec tunelu) k AMF přes N2. V uživatelské rovině N3IWF dekapsuluje příchozí IPsec pakety od UE a přeposílá vnitřní IP pakety k UPF přes [GTP-U](/mobilnisite/slovnik/gtp-u/) tunel na N3 a naopak. Hraje také roli při podpoře událostí mobility, jako jsou předávání spojení mezi přístupem 3GPP a mimo 3GPP.

Klíčové komponenty v logickém návrhu N3IWF zahrnují koncové body pro IKEv2 a IPsec, přeposílací funkci pro signalizaci NAS N1/N2 a koncový bod GTP-U pro rozhraní N3. Její role je zásadní pro naplnění vize 5G o poskytování služeb nezávislých na přístupu, což operátorům umožňuje využívat stávající infrastrukturu Wi-Fi pro odlehčení provozu, rozšíření pokrytí a poskytnutí plynulého uživatelského zážitku bez kompromisů v zabezpečení a standardech služeb 5G.

## K čemu slouží

N3IWF byla představena ve vydání 3GPP Release 15 jako součást nové architektury 5G System (5GS) za účelem řešení kritického problému integrace přístupových sítí mimo 3GPP do jádra 5G bezpečným a standardizovaným způsobem. Před 5G byla integrace Wi-Fi s mobilními sítěmi řešena prostřednictvím samostatných, často proprietárních bran (jako ePDG v EPS pro nedůvěryhodné Wi-Fi), které nebyly plně sladěné s cloud-nativními a službami založenými principy 5GC. Motivací bylo vytvořit jednotné jádro, které by mohlo poskytovat konzistentní služby, zabezpečení a politiky bez ohledu na podkladovou přístupovou technologii (3GPP nebo mimo 3GPP).

Historicky představoval přístup mimo 3GPP (zejména nedůvěryhodné Wi-Fi) bezpečnostní rizika a správní složitosti. N3IWF je řeší tím, že poskytuje standardizovanou, bezpečnou funkci pro vzájemné propojení, která aplikuje stejné robustní mechanismy autentizace a zabezpečení 5G (jako 5G-AKA nebo EAP-AKA') i na připojení mimo 3GPP. Řeší problém fragmentace přístupu a umožňuje plynulou kontinuitu relací a architekturu založenou na službách pro zařízení připojená přes Wi-Fi. To bylo hnací silou potřeby průmyslu využít hustá nasazení Wi-Fi pro zvýšení kapacity, vnitřní pokrytí a scénáře pevného bezdrátového přístupu v rámci rámce služeb 5G.

Dále bylo vytvoření N3IWF motivováno omezeními předchozích řešení pro vzájemné propojení, která byla často pouze přílepky k jádru sítě. V 5G je N3IWF plnohodnotnou součástí architektury založené na službách (SBA), která komunikuje s [AMF](/mobilnisite/slovnik/amf/) a [UPF](/mobilnisite/slovnik/upf/) přes rozhraní založená na službách. To umožňuje flexibilnější nasazení, lepší škálovatelnost a integrované řízení politik, naplňující tak požadavek 5G na konvergenci pevných a mobilních sítí.

## Klíčové vlastnosti

- Ukončuje tunely IKEv2 a IPsec od UE přes rozhraní NWu pro zabezpečený nedůvěryhodný přístup mimo 3GPP
- Přeposílá signalizační zprávy NAS N1 (UE-AMF) a N2 (AMF-UE) mezi UE a AMF
- Poskytuje funkci přeposílání v uživatelské rovině, přeposílá data mezi IPsec tunely od UE a GTP-U tunely na N3 k/od UPF
- Podporuje procedury autentizace 5G (např. 5G-AKA, EAP-AKA') pro UE připojená mimo 3GPP
- Umožňuje politiky mobility a kontinuity relací mezi typy přístupu 3GPP a mimo 3GPP
- Komunikuje s ostatními síťovými funkcemi 5GC (AMF, UPF) přes rozhraní založená na službách (N2, N3)

## Související pojmy

- [AMF – Access and Mobility Management Function](/mobilnisite/slovnik/amf/)
- [UPF – User Plane Function](/mobilnisite/slovnik/upf/)
- [ATSSS – Access Traffic Steering, Switching, and Splitting](/mobilnisite/slovnik/atsss/)
- [IPSec – Internet Protocol Security](/mobilnisite/slovnik/ipsec/)

## Definující specifikace

- **TS 23.501** (Rel-20) — 5G System Architecture Stage 2
- **TS 24.501** (Rel-19) — 5G NAS Protocols Specification
- **TS 24.502** (Rel-19) — 5G Core Access via Non-3GPP Networks; Stage 3
- **TS 24.526** (Rel-19) — UE Policies for 5GS; Stage 3
- **TS 24.890** (Rel-16) — 5G NAS Protocol for 5GS Stage 3
- **TR 28.828** (Rel-18) — Charging Aspects for Non-Public Networks
- **TS 29.214** (Rel-19) — Policy and Charging Control over Rx
- **TS 29.413** (Rel-19) — NGAP for Non-3GPP Access
- **TS 29.518** (Rel-19) — AMF Service Based Interface Protocol
- **TS 29.525** (Rel-19) — 5G UE Policy Control Service Stage 3
- **TS 29.561** (Rel-19) — 5G Interworking with External Data Networks
- **TS 32.255** (Rel-20) — Telecom Management; Charging for 5G Data Connectivity
- **TS 32.256** (Rel-19) — 5G Connection & Mobility Charging Spec
- **TS 33.127** (Rel-19) — Lawful Interception Architecture and Functions
- **TS 33.501** (Rel-20) — 5G Security Architecture and Procedures
- … a dalších 1 specifikací

---

📖 **Anglický originál a plná specifikace:** [N3IWF na 3GPP Explorer](https://3gpp-explorer.com/glossary/n3iwf/)
