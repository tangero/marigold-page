---
slug: "oma"
url: "/mobilnisite/slovnik/oma/"
type: "slovnik"
title: "OMA – Open Mobile Alliance"
date: 2026-01-01
abbr: "OMA"
fullName: "Open Mobile Alliance"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/oma/"
summary: "Open Mobile Alliance (OMA) je standardizační organizace, která vyvíjí otevřené, interoperabilní technické specifikace pro mobilní služby a aplikace. Původně vznikla sloučením různých fór pro mobilní s"
---

OMA je standardizační organizace, která vyvíjí otevřené, interoperabilní technické specifikace pro mobilní služby a aplikace, aby zajistila globální interoperabilitu služeb napříč různými sítěmi a zařízeními.

## Popis

Open Mobile Alliance (OMA) není jednotlivá technologie, ale průmyslové konsorcium, které vytváří specifikace pro tzv. "enablery" (umožňující komponenty) mobilních služeb. Vznikla sloučením několika již existujících fór, jako například [WAP](/mobilnisite/slovnik/wap/) Forum, Location Interoperability Forum ([LIF](/mobilnisite/slovnik/lif/)), SyncML Initiative a dalších. Hlavním výstupem OMA je soubor technických specifikací, které definují protokoly, datové formáty a architektury pro standardizovanou implementaci různých mobilních služeb. Tyto specifikace jsou navrženy tak, aby byly nezávislé na typu sítě a fungovaly přes 2G, 3G, 4G i 5G. Jsou přijímány organizací 3GPP jako součást standardizace servisní vrstvy, zejména pro služby mimo základní spojové funkce.

Z architektonického hlediska specifikace OMA často definují modely klient-server, [API](/mobilnisite/slovnik/api/) a formáty datových objektů. Klíčovými komponentami napříč mnoha "enablery" OMA jsou server enableru (např. [DM](/mobilnisite/slovnik/dm/) Server pro OMA Device Management), klient na uživatelském zařízení (UE) a standardizované protokoly pro komunikaci mezi nimi, jako jsou XML-based protokoly přes [HTTP](/mobilnisite/slovnik/http/). Například OMA Device Management (OMA DM) využívá objektový model "management tree" a protokol SyncML, aby umožnil serveru konfigurovat, aktualizovat a spravovat nastavení na mobilním zařízení. Podobně OMA Client Provisioning definuje mechanismy pro dálkovou provizi síťových a aplikačních nastavení na zařízení.

V rámci ekosystému 3GPP jsou specifikace OMA referencovány a integrovány, aby poskytly kompletní popisy služeb. Specifikace 3GPP (jako například TS 22.340, TS 23.222) uvádějí "enablery" OMA jako technickou realizaci konkrétních servisních schopností. Tato spolupráce umožňuje 3GPP soustředit se na síťovou architekturu a základní protokoly, zatímco využívá odborné znalosti OMA v oblasti "enablerů" na aplikační vrstvě. "Enablery" OMA se tedy nacházejí v aplikační/servisní vrstvě a rozhraní s síťovými schopnostmi definovanými 3GPP probíhá přes standardizované referenční body.

## K čemu slouží

OMA byla vytvořena, aby vyřešila kritický problém fragmentace a nedostatku interoperability v mobilních nadstandardních službách. Před jejím vznikem vyvíjelo více konkurenčních a překrývajících se průmyslových konsorcií (jako [WAP](/mobilnisite/slovnik/wap/) Forum, [LIF](/mobilnisite/slovnik/lif/), MMS-IOP) proprietární nebo nekompatibilní specifikace pro podobné služby. Tato fragmentace brzdila rozvoj globálního trhu mobilních služeb, zvyšovala náklady pro operátory a výrobce a vytvářela špatný uživatelský zážitek kvůli nekompatibilitě služeb mezi zařízeními a sítěmi.

Sloučení do OMA poskytlo jediné, otevřené fórum, kde klíčoví hráči v oboru mohli spolupracovat na jednotných, bezlicenčních specifikacích. Jejím účelem je urychlit adopci mobilních služeb tím, že zajišťuje, aby služby jako zasílání zpráv (OMA Instant Messaging), správa zařízení (OMA [DM](/mobilnisite/slovnik/dm/)), správa digitálních práv (OMA DRM) a lokalizační služby (OMA SUPL) fungovaly konzistentně na všech kompatibilních zařízeních a sítích operátorů. Poskytnutím těchto standardizovaných "stavebních bloků" neboli "enablerů" umožňuje OMA vývojářům aplikací a poskytovatelům služeb vytvářet interoperabilní služby bez nutnosti řešit heterogenitu podkladové sítě nebo zařízení.

Historicky byla práce OMA obzvláště zásadní během éry 2.5G a 3G, kdy se mobilní sítě vyvíjely od základního hlasu k datovým a multimediálním službám. Odstranila omezení předchozích proprietárních přístupů vytvořením rovných podmínek. Zatímco některé "enablery" OMA se vyvinuly nebo byly nahrazeny novějšími technologiemi (např. Rich Communication Services (RCS) navazují na dřívější práci OMA v oblasti zasílání zpráv), princip otevřených specifikací "enablerů" služeb, který OMA zavedla, zůstává v mobilním průmyslu vlivný.

## Klíčové vlastnosti

- Vývoj otevřených, interoperabilních specifikací pro "enablery" služeb
- Návrh nezávislý na typu sítě pro použití napříč 2G, 3G, 4G a 5G
- Definuje architektury klient-server, protokoly a datové formáty
- Umožňuje standardizovanou správu zařízení a provizi
- Poskytuje frameworky pro služby založené na poloze (např. SUPL)
- Specifikuje "enablery" pro zasílání zpráv, službu přítomnosti a správu digitálních práv

## Související pojmy

- [SUPL – Secure User Plane for Location](/mobilnisite/slovnik/supl/)
- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [MMS – Multimedia Messaging Service](/mobilnisite/slovnik/mms/)

## Definující specifikace

- **TS 22.340** (Rel-19) — IMS Messaging Stage 1 Requirements
- **TR 22.940** (Rel-19) — IMS Messaging Requirements Analysis
- **TR 22.949** (Rel-19) — Privacy Requirements Study for 3GPP Services
- **TS 23.222** (Rel-19) — Common API Framework for 3GPP Northbound APIs
- **TS 23.271** (Rel-19) — LCS Stage 2 Specification
- **TS 23.392** (Rel-19) — MMTel Application Enablement
- **TS 23.700** (Rel-20) — XR Services Application Enablement Layer
- **TS 23.722** (Rel-15) — Common API Framework (CAPIF) for 3GPP Northbound APIs
- **TR 23.976** (Rel-19) — Push Service Requirements Analysis
- **TR 23.979** (Rel-19) — PoC over 3GPP Systems Architectural Requirements
- **TR 23.981** (Rel-19) — IPv4 IMS Interworking and Migration Study
- **TS 24.166** (Rel-19) — IMS Conferencing Management Object
- **TS 24.167** (Rel-19) — 3GPP IMS Management Object Specification
- **TS 24.216** (Rel-19) — Communication Continuity Management Object
- **TS 24.235** (Rel-12) — I-WLAN Interworking Management Object
- … a dalších 29 specifikací

---

📖 **Anglický originál a plná specifikace:** [OMA na 3GPP Explorer](https://3gpp-explorer.com/glossary/oma/)
