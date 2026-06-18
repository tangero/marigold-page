---
slug: "nsp"
url: "/mobilnisite/slovnik/nsp/"
type: "slovnik"
title: "NSP – Network Service Provider"
date: 2026-01-01
abbr: "NSP"
fullName: "Network Service Provider"
category: "Other"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/nsp/"
summary: "Poskytovatel síťových služeb (Network Service Provider, NSP) je subjekt, který uživatelům poskytuje síťové služby, například IP konektivitu. V kontextu 3GPP často odkazuje na externí IP síť (např. int"
---

NSP je externí IP síť, například internet nebo podniková síť, ke které se zařízení uživatele připojuje prostřednictvím 3GPP mobilní sítě za účelem získání služeb, jako je IP konektivita.

## Popis

Termín Poskytovatel síťových služeb (Network Service Provider, NSP) ve standardech 3GPP, na který odkazují dokumenty jako TS 23.435 a TS 24.302, označuje subjekt, který nabízí služby síťové konektivity. V architektuře mobilních sítí, zejména od vydání Release 8 se systémovou architekturou [SAE](/mobilnisite/slovnik/sae/) (System Architecture Evolution), je NSP typicky poskytovatelem služeb externí paketové datové sítě ([PDN](/mobilnisite/slovnik/pdn/)). Nejběžnějším příkladem je poskytovatel internetových služeb ([ISP](/mobilnisite/slovnik/isp/)). 3GPP mobilní síť (veřejná pozemní mobilní síť – [PLMN](/mobilnisite/slovnik/plmn/)) funguje jako přístupová síť a poskytuje rádiové a jádrové síťové připojení, které umožňuje uživatelskému zařízení (UE) dosáhnout na služby NSP.

Interakce je řízena prostřednictvím brány paketové datové sítě ([PGW](/mobilnisite/slovnik/pgw/) v 4G, kotvy [PDU](/mobilnisite/slovnik/pdu/) sezení v 5G). Když UE naváže datové spojení (připojení k PDN v 4G, PDU sezení v 5G), specifikuje název přístupového bodu ([APN](/mobilnisite/slovnik/apn/)). APN je reference, která pomáhá síti vybrat příslušnou PGW/[UPF](/mobilnisite/slovnik/upf/) a určuje cestu k externí síti NSP. Síť mobilního operátora na základě předplatitelských dat ověří a autorizuje přístup UE ke konkrétnímu NSP. Samotný NSP je zodpovědný za přidělení IP adresy UE (často prostřednictvím DHCP), poskytnutí dalších služeb na IP úrovni (jako je webhosting, e-mail) a implementaci vlastních politik pro provoz ve své doméně.

Ve pokročilejších scénářích, jako je síťové krájení (network slicing), může být NSP podnik, který si pronajímá vyhrazený síťový řez od mobilního operátora. V tomto případě NSP (podnik) poskytuje své interní služby (např. privátní cloudovou aplikaci) prostřednictvím izolovaného řezu. Standardy 3GPP definují rozhraní a procedury (např. v řízení politik – TS 26.941) pro usnadnění servisní interakce mezi sítí mobilního operátora a NSP, což zajišťuje správnou kvalitu služeb (QoS), účtování a řízení přístupu.

## K čemu slouží

Koncept NSP je základním kamenem architektury mobilních dat, neboť vytváří jasné oddělení mezi poskytovatelem přístupu (mobilním operátorem) a poskytovatelem služeb (NSP). Toto oddělení umožňuje diverzifikovaný ekosystém. Jeden mobilní operátor může poskytovat přístup k více NSP (např. k internetu, poskytovateli služeb IMS, podnikovému VPN) a uživatel si mezi nimi může vybírat. Tento model existoval již před vydáním Release 8, ale byl upevněn s čistým oddělením řídicí a uživatelské roviny v architektuře EPC (Evolved Packet Core).

Historicky byly mobilní sítě uzavřenými zahradami nabízejícími pouze služby pod kontrolou operátora. Model NSP otevřel síť službám třetích stran, což podpořilo inovace a ekonomiku mobilního internetu. Řeší omezení, kdy byl operátor jediným zdrojem služeb. Architektura umožňuje mobilnímu operátorovi soustředit se na poskytování spolehlivého, výkonného přístupu a správy konektivity, zatímco se NSP může zaměřit na tvorbu a poskytování inovativních aplikací a obsahu založených na IP. Toto rozdělení úkolů je klíčové pro škálovatelnost a specializaci v telekomunikačním průmyslu.

## Klíčové vlastnosti

- Poskytuje IP konektivitu a aplikační služby externí vůči 3GPP mobilní síti
- Identifikován a vybrán uživatelským zařízením (UE) prostřednictvím parametru Název přístupového bodu (APN)
- Zodpovědný za konečné přidělení IP adresy uživatelskému zařízení (např. prostřednictvím DHCP)
- Implementuje vlastní servisní politiky, zabezpečení a účtování ve své doméně
- Může jím být poskytovatel internetových služeb (ISP), podniková síť nebo poskytovatel služeb IMS
- Spolupracuje se sítí 3GPP prostřednictvím standardizovaných rozhraní na úrovni PGW/UPF

## Související pojmy

- [APN – Access Point Name](/mobilnisite/slovnik/apn/)
- [PDN – Packet Data Network](/mobilnisite/slovnik/pdn/)
- [PLMN – Public Land Mobile Network](/mobilnisite/slovnik/plmn/)
- [PGW – PDN Gateway](/mobilnisite/slovnik/pgw/)

## Definující specifikace

- **TS 23.435** (Rel-19) — Network Slice Capability Exposure Procedures
- **TS 23.700** (Rel-20) — XR Services Application Enablement Layer
- **TS 24.302** (Rel-19) — Access to EPC via non-3GPP networks; Stage 3
- **TR 26.941** (Rel-19) — 5G Media Slicing Extensions
- **TS 28.530** (Rel-19) — Network Slicing Concepts & Requirements
- **TS 28.531** (Rel-20) — Management and Orchestration
- **TS 28.535** (Rel-19) — Closed Control Loop Assurance Management
- **TR 28.836** (Rel-18) — Technical Report on Intent Driven Management
- **TR 28.843** (Rel-18) — Technical Report on Charging Aspects for Vertical Scenarios
- **TR 32.847** (Rel-18) — Technical Report

---

📖 **Anglický originál a plná specifikace:** [NSP na 3GPP Explorer](https://3gpp-explorer.com/glossary/nsp/)
