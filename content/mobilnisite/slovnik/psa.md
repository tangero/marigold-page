---
slug: "psa"
url: "/mobilnisite/slovnik/psa/"
type: "slovnik"
title: "PSA – Product Specific Applications"
date: 2026-01-01
abbr: "PSA"
fullName: "Product Specific Applications"
category: "Services"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/psa/"
summary: "Koncept 3GPP pro aplikace specifické pro konkrétní produkt nebo nabídku služby, často s jedinečnými požadavky. Jde o širokou kategorizaci používanou ve specifikacích požadavků na služby a architektury"
---

PSA je koncept 3GPP pro aplikace specifické pro konkrétní produkt nebo nabídku služby, používaný k modelování specializovaných aplikačních funkcí v rámci systému 5G.

## Popis

Product Specific Applications (PSA) je termín používaný v mnoha specifikacích 3GPP k označení aplikačních funkcí nebo služeb, které nejsou obecné, ale jsou vázány na konkrétní komerční produkt, balíček služeb nebo případ užití. Nejde o jediný protokol nebo síťovou funkci, ale o konceptuální entitu používanou při modelování požadavků a architektury. PSAs představují logický koncový bod nebo zdroj provozu a signalizace specifické pro službu, které musí systém 5G (5GS) podporovat. Často jsou diskutovány v kontextu architektury založené na službách, vystavení sítě a diferenciace kvality služby (QoS).

Architektonicky PSA komunikuje s jádrem sítě 5G (5GC) prostřednictvím definovaných rozhraní, primárně přes funkci vystavení sítě ([NEF](/mobilnisite/slovnik/nef/)) nebo přímo s funkcí uživatelské roviny ([UPF](/mobilnisite/slovnik/upf/)) pro směrování provozu. PSA může být aplikační funkce ([AF](/mobilnisite/slovnik/af/)), jak je definována v architektuře 5GC, ale s charakteristickým rysem, že je produktově specifická. To znamená, že její komunikace se sítí nese požadavky jedinečné pro produkt, který umožňuje, jako jsou specifické parametry QoS (např. latence, spolehlivost), zpoplatnění nebo omezení mobility. 5GC využívá informace poskytnuté PSA nebo o PSA k aplikování odpovídajících síťových politik.

Jak to funguje: PSA (nebo entita ji reprezentující, např. AF) poskytuje 5GC informace související se sezením nebo službou. Například PSA pro službu hraní her v reálném čase může prostřednictvím NEF požadovat garantovanou přenosovou rychlost a tok QoS s nízkou latencí pro své uživatele. Funkce řízení politik ([PCF](/mobilnisite/slovnik/pcf/)) by následně vygenerovala politiky na základě této žádosti a předplatného uživatele a funkce správy sezení ([SMF](/mobilnisite/slovnik/smf/)) by je vynutila odpovídající konfigurací UPF. Úlohou konceptu PSA je poskytnout formální model pro tyto produktově specifické interakce, což zajišťuje, že síť může být dynamicky přizpůsobena pro podporu široké škály specializovaných služeb nad rámec základní konektivity, což je ústřední pro vizi 5G 'síť jako služba'.

## K čemu slouží

Koncept Product Specific Applications existuje proto, aby řešil potřebu systému 3GPP podporovat rozmanitý a stále rostoucí ekosystém specializovaných služeb, z nichž každá má jedinečné síťové požadavky. V raných mobilních sítích byly služby převážně monolitické (např. hovor, [SMS](/mobilnisite/slovnik/sms/), základní internet). Jak se sítě vyvíjely, operátoři a třetí strany začali nabízet diferencované produkty, jako jsou streamovací balíčky, řešení IoT a podnikové [VPN](/mobilnisite/slovnik/vpn/), které vyžadovaly, aby síť s jejich provozem zacházela odlišně.

PSA poskytuje standardizovaný způsob, jak tyto služby na míru modelovat v rámci architektury 3GPP. Řeší problém, jak formálně popsat a integrovat požadavky konkrétního komerčního produktu do řídicí a managementové roviny sítě. Před takovým modelováním často vyžadovalo zavedení nové služby proprietární integrace nebo široké, neefektivní konfigurace sítě. Koncept PSA, zejména jak byl upřesněn v architektuře 5G založené na službách, umožňuje dynamické, politikami řízené dělení sítě a správu QoS na bázi jednotlivých aplikací nebo produktů. To operátorům umožňuje efektivně monetizovat své sítě nabídkou šité na míru konektivity jakožto vlastnosti produktu.

## Klíčové vlastnosti

- Představuje aplikační funkce vázané na konkrétní komerční produkty nebo služby
- Komunikuje s jádrem 5G přes funkci vystavení sítě (NEF) nebo jako aplikační funkce (AF)
- Může ovlivňovat síťové politiky pro QoS, zpoplatnění a směrování provozu
- Umožňuje dynamické síťové chování specifické pro službu
- Ústřední pro implementaci dělení sítě pro služby vertikálních segmentů
- Používá se ve specifikacích požadavků k zachycení jedinečných potřeb služeb

## Definující specifikace

- **TS 23.501** (Rel-20) — 5G System Architecture Stage 2
- **TS 23.527** (Rel-19) — 5G System Restoration Procedures
- **TS 23.558** (Rel-20) — Architecture for Edge Applications
- **TS 23.700** (Rel-20) — XR Services Application Enablement Layer
- **TR 23.794** (Rel-17) — Study on enhanced IMS to 5GC integration
- **TR 26.803** (Rel-17) — 5G Media Streaming Extensions for Edge Processing
- **TS 26.804** (Rel-19) — 5G Media Streaming Extensions Study
- **TR 26.806** (Rel-18) — Technical Report on Smartly Tethering AR Glasses
- **TR 28.822** (Rel-17) — Charging for 5G LAN Services Study
- **TR 28.833** (Rel-18) — Technical Report on 5G LAN-type Service Management
- **TS 29.244** (Rel-19) — PFCP Specification for Control/User Plane Separation
- **TS 29.512** (Rel-19) — 5G Session Management Policy Control Service
- **TS 29.513** (Rel-19) — 5G PCC Signalling Flows & QoS Mapping
- **TS 29.514** (Rel-19) — 5G System; Policy Authorization Service; Stage 3
- **TS 29.519** (Rel-19) — UDR Usage for Policy & Exposure Data
- … a dalších 4 specifikací

---

📖 **Anglický originál a plná specifikace:** [PSA na 3GPP Explorer](https://3gpp-explorer.com/glossary/psa/)
