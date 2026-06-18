---
slug: "vru"
url: "/mobilnisite/slovnik/vru/"
type: "slovnik"
title: "VRU – Vulnerable Road Users"
date: 2026-01-01
abbr: "VRU"
fullName: "Vulnerable Road Users"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/vru/"
summary: "Termín v 3GPP pro účastníky silničního provozu nejvíce ohrožené v provozu, jako jsou chodci, cyklisté, motocyklisté a jezdci na koloběžkách. Specifikace 3GPP pro služby V2X (Vehicle-to-Everything) def"
---

VRU je termín 3GPP pro zranitelné účastníky silničního provozu, jako jsou chodci a cyklisté, jejichž bezpečnost je zvyšována službami V2X využívajícími přímou komunikaci a komunikaci zprostředkovanou sítí.

## Popis

V rámci architektury 3GPP pro komunikaci Vehicle-to-Everything ([V2X](/mobilnisite/slovnik/v2x/)) označuje termín Vulnerable Road Users (VRU) funkční roli nebo entitu reprezentující účastníky silničního provozu, kteří nejsou uvnitř chráněného vozidla a jsou proto při střetu vystaveni vyššímu riziku zranění. Patří sem především chodci, cyklisté, jezdci na jednostopých motorových vozidlech (např. motocykly, skútry) a potenciálně také uživatelé vozíčků nebo jezdci na koních. Specifikace 3GPP, zejména od Release 14 dále, definují požadavky na služby a technické architektury pro podporu V2X aplikací zaměřených na ochranu VRU. Základní myšlenkou je integrace zařízení VRU (typicky chytrých telefonů, speciálních nositelných zařízení nebo senzorů na kolech) do ekosystému V2X, což jim umožňuje vysílat informaci o své přítomnosti a přijímat varování od vozidel a infrastruktury.

Technický provoz využívá dvě hlavní komunikační rozhraní definovaná pro V2X: rozhraní Uu (prostřednictvím mobilní sítě) a rozhraní PC5 (přímá komunikace mezi zařízeními, známá také jako sidelink). Zařízení VRU může použít jedno nebo obě. Pomocí PC5 může zařízení VRU periodicky vysílat svou základní bezpečnostní zprávu (např. VRU Awareness Message) obsahující svou polohu, rychlost, směr a typ (např. chodec). Vozidla vybavená V2X schopnostmi tyto zprávy přijímají prostřednictvím svých vlastních rozhraní PC5. Palubní aplikace vozidla pak může vyhodnotit riziko kolize a poskytnout varování řidiči nebo iniciovat automatické brzdění. Naopak, vozidlo může vysílat varování (např. o prudkém brzdění), která mohou zařízení VRU přijmout a převést na zvukový nebo vibrační signál pro chodce či cyklistu.

Při použití rozhraní Uu může být poloha a stav zařízení VRU nahlášena aplikačnímu serveru V2X v síti (s využitím Service Enabler Architecture Layer for Verticals - [SEAL](/mobilnisite/slovnik/seal/)). Server může provádět analýzu širší oblasti, detekovat nebezpečné situace zahrnující více entit a rozesílat cílená varování zpět k příslušným vozidlům a VRU prostřednictvím celulárního vysílání nebo unicastu. Tento síťově asistovaný přístup umožňuje varování před nebezpečím na delší vzdálenosti a pokrývá scénáře, kde může být přímá komunikace PC5 omezena dosahem nebo překážkami. Architektura 3GPP definuje potřebné servisní požadavky, struktury zpráv a funkční postupy pro podporu těchto bezpečnostních aplikací VRU, což zajišťuje interoperabilitu mezi zařízeními od různých výrobců a výrobců vozidel.

## K čemu slouží

Formalizace podpory VRU ve standardech 3GPP byla motivována celosvětovou výzvou v oblasti bezpečnosti silničního provozu. Tradiční bezpečnostní systémy zaměřené na vozidlo (jako airbagy, deformační zóny) nechrání osoby mimo vozidlo. Jak se technologie [V2X](/mobilnisite/slovnik/v2x/) vyvíjela, aby umožnila komunikaci vozidlo-vozidlo ([V2V](/mobilnisite/slovnik/v2v/)) a vozidlo-infrastruktura (V2I) pro bezpečnost v automobilovém průmyslu, zůstala významná mezera: začlenění nejzranitelnějších účastníků provozu. Hlavním řešeným problémem je detekce a povědomí o VRU v komplexním městském prostředí, zejména v situacích bez přímé viditelnosti nebo při překrytí, kdy mohou selhat palubní senzory vozidla (kamery, radar).

Komunikace V2X založená na 3GPP poskytuje doplňkový senzor s delším dosahem a schopností 'vidět za roh' prostřednictvím síťového přenosu. Tím, že do bezpečnostního systému zapojí chytré telefony – téměř všudypřítomná zařízení, která nosí chodci a cyklisté – vytvářejí standardy 3GPP škálovatelnou cestu k výraznému zlepšení bezpečnosti VRU. Tato práce, zahájená v Release 14 a vylepšená v pozdějších verzích, byla hnána případy použití definovanými orgány pro automobilové standardy, jako je [ETSI](/mobilnisite/slovnik/etsi/), a snahou vytvořit komplexní ekosystém Cooperative Intelligent Transport Systems (C-ITS) integrovaný s mobilními sítěmi. Řeší omezení předchozích návrhů založených na necelulární dedikované krátkodosahové komunikaci (DSRC) tím, že využívá stávající penetraci celulárních zařízení a schopnost sítě spravovat identity, zabezpečení a služby v široké oblasti.

## Klíčové vlastnosti

- Definuje VRU jako formální entitu v servisní architektuře V2X
- Podporuje bezpečnostní aplikace VRU prostřednictvím přímého sidelink rozhraní PC5 i celulárního rozhraní Uu
- Specifikuje sady zpráv (např. VRU Awareness Messages) pro vysílání informace o přítomnosti
- Umožňuje varování před nebezpečím bez přímé viditelnosti pro vozidla i VRU
- Integruje se se síťovými aplikačními servery V2X pro správu nebezpečí v oblasti
- Využívá všudypřítomné chytré telefony jako potenciální zařízení VRU

## Související pojmy

- [V2X – Vehicle-to-Everything Application Server](/mobilnisite/slovnik/v2x/)
- [BSM – Basic Safety Message](/mobilnisite/slovnik/bsm/)
- [SEAL – Service Enabler Architecture Layer for Verticals](/mobilnisite/slovnik/seal/)

## Definující specifikace

- **TS 22.156** (Rel-19) — Mobile Metaverse Services
- **TR 22.856** (Rel-19) — Feasibility Study on Localized Mobile Metaverse Services
- **TR 22.885** (Rel-14) — LTE support for V2X services
- **TS 23.700** (Rel-20) — XR Services Application Enablement Layer
- **TR 23.776** (Rel-17) — V2X Architecture Enhancements Phase 2
- **TS 24.486** (Rel-19) — V2X Application Enabler (VAE) Protocol Spec
- **TR 38.785** (Rel-17) — UE radio transmission for enhanced NR sidelink

---

📖 **Anglický originál a plná specifikace:** [VRU na 3GPP Explorer](https://3gpp-explorer.com/glossary/vru/)
