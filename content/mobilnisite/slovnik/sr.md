---
slug: "sr"
url: "/mobilnisite/slovnik/sr/"
type: "slovnik"
title: "SR – Spectrum Reallocation"
date: 2025-01-01
abbr: "SR"
fullName: "Spectrum Reallocation"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/sr/"
summary: "Spectrum Reallocation (SR) označuje proces dynamického přeřazování rádiového kmitočtového spektra mezi různými službami, technologiemi nebo operátory za účelem zlepšení celkového využití a efektivity."
---

SR (Spectrum Reallocation) je proces dynamického přeřazování rádiového kmitočtového spektra mezi službami, technologiemi nebo operátory za účelem zlepšení využití a efektivity, který se přizpůsobuje měnícím se požadavkům v rámci omezených zdrojů.

## Popis

Spectrum Reallocation je široký provozní a regulační proces zahrnující změnu přiřazení konkrétních kmitočtových pásem z jednoho využití na jiné. V kontextu 3GPP zahrnuje technické mechanismy, síťové procedury a politické rámce, které umožňují flexibilní a efektivní využití rádiového kmitočtového spektra. To může nastat na více úrovních: přeřazení spektra mezi různými generacemi mobilních sítí (např. převedení spektra 2G/3G pro 4G/5G), mezi různými operátory nebo mezi mobilními a jinými službami, jako je vysílání. Specifikace 3GPP poskytují technické prostředky v rámci Radio Access Network (RAN) a core networku pro podporu takových přechodů.

Z technického hlediska SR zahrnuje komplexní soubor akcí. Pro síťové operátory vyžaduje pečlivé plánování migrace uživatelských zařízení a síťové infrastruktury z jednoho pásma do druhého s minimálním narušením služeb. To zahrnuje aktualizace konfiguračních databází sítě, vysílaných systémových informací a parametrů předávání spojení. Specifikace jako TS 36.331 ([RRC](/mobilnisite/slovnik/rrc/) protokol) a TS 38.331 definují, jak může síť informovat UE o dostupných kmitočtových pásmech a přesměrovat je na nové nosné. Proces je řízen prostřednictvím systémů Operations, Administration, and Maintenance ([OAM](/mobilnisite/slovnik/oam/)), jak je podrobně popsáno ve specifikacích řad TS 28.xxx a 32.xxx, které orchestrují rekonfiguraci síťových prvků.

Role SR v síti je v zásadě o optimalizaci a vývoji. Umožňuje síťovým operátorům reagovat na technologické posuny a tržní požadavky opětovným využitím jejich nejcennějšího aktiva – spektrálních licencí. Například, protože technologie LTE a NR nabízejí lepší spektrální efektivitu ve srovnání se staršími technologiemi 2G/3G, přeřazení spektra na ně zvyšuje celkovou kapacitu sítě a přenosové rychlosti. Dále je SR nezbytná pro implementaci technik sdílení spektra, jako je Licensed Shared Access ([LSA](/mobilnisite/slovnik/lsa/)) nebo Dynamic Spectrum Sharing (DSS), kde může být spektrum dynamicky přidělováno mezi různými uživateli nebo technologiemi na základě poptávky v reálném čase, jak je zkoumáno ve specifikacích jako TS 37.870.

## K čemu slouží

Spectrum Reallocation existuje k vyřešení základního problému nedostatku spektra a neefektivního využití. Rádiové kmitočtové spektrum je omezený přírodní zdroj a velké části jsou již licencovány pro konkrétní služby. Účelem SR je maximalizovat užitečnost a ekonomickou hodnotu tohoto zdroje tím, že umožní, aby se jeho přiřazení vyvíjelo spolu s technologickým pokrokem a měnícími se požadavky uživatelů. Bez SR by spektrum mohlo zůstat uzamčeno v zastaralém, neefektivním využití, což by bránilo nasazení nových technologií s vyšší kapacitou.

Historicky motivace pro SR rostla s každým generačním přechodem. Přechod z 2G (GSM) na 3G (UMTS) vyžadoval nová kmitočtová pásma, ale také vytvořil příležitost převést GSM spektrum pro UMTS. Tato potřeba se stala výraznější s 4G LTE a 5G NR, které vyžadují širší souvislou šířku pásma pro vysokou propustnost. Regulační orgány po celém světě prosazovaly iniciativy SR k převedení pásem, jako je digitální dividenda (pásmo 700 MHz) z televizního vysílání na mobilní širokopásmový přístup. Standardy 3GPP se musely vyvíjet, aby podporovaly tato přeřazená pásma a mechanismy koexistence vyžadované během přechodných období.

SR řeší omezení statického přidělování spektra. Statický model se nemůže přizpůsobit explozivnímu růstu mobilního datového provozu nebo vzniku nových případů užití, jako je massive IoT nebo ultra-spolehlivá komunikace s nízkou latencí. SR poskytuje rámec – jak regulační, tak technický – pro umožnění dynamičtějšího, tržně řízeného a efektivnějšího spektrálního ekosystému. Je to klíčový nástroj pro síťové operátory k modernizaci jejich sítí, pro regulátory k podpoře konkurence a inovací a pro zajištění, aby spektrum sloužilo největšímu veřejnému prospěchu.

## Klíčové vlastnosti

- Dynamické přeřazení kmitočtových pásem mezi technologiemi (např. z GSM na LTE)
- Umožňuje převedení zastaralého spektra pro novější, efektivnější technologie
- Podporováno aktualizacemi síťové konfigurace prostřednictvím systémů OAM
- Zahrnuje přesměrování UE a rekonfiguraci síťových parametrů
- Základní pro koncepty sdílení spektra jako DSS a LSA
- Řízeno jak technickými standardy, tak národními regulačními politikami

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TR 22.804** (Rel-16) — 5G Automation in Vertical Domains Study
- **TS 25.800** (Rel-12) — UMTS Heterogeneous Networks Study
- **TS 26.114** (Rel-19) — IMS Multimedia Telephony Media Handling
- **TS 26.260** (Rel-19) — Immersive Audio Objective Test Methods
- **TS 26.565** (Rel-19) — Split Rendering Media Service Enabler
- **TS 26.567** (Rel-19) — IMS-based Split Rendering
- **TS 29.549** (Rel-19) — SEAL API Specification for Vertical Applications
- **TS 29.892** (Rel-16) — Study on User Plane Protocol in 5GC
- **TR 33.916** (Rel-19) — 3GPP Security Assurance Methodology (SECAM)
- **TS 36.212** (Rel-19) — LTE Multiplexing and Channel Coding
- **TS 36.213** (Rel-19) — LTE Physical Layer Procedures
- **TS 36.300** (Rel-19) — E-UTRAN Radio Interface Protocol Architecture Overview
- **TS 36.306** (Rel-19) — E-UTRA UE Radio Access Capability Parameters
- **TS 36.321** (Rel-19) — E-UTRA MAC Protocol Specification
- … a dalších 11 specifikací

---

📖 **Anglický originál a plná specifikace:** [SR na 3GPP Explorer](https://3gpp-explorer.com/glossary/sr/)
