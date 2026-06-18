---
slug: "seaf"
url: "/mobilnisite/slovnik/seaf/"
type: "slovnik"
title: "SEAF – Security Anchor Functionality"
date: 2026-01-01
abbr: "SEAF"
fullName: "Security Anchor Functionality"
category: "Security"
segment: "Security"
canonical: "https://3gpp-explorer.com/glossary/seaf/"
summary: "SEAF je klíčová bezpečnostní funkce v 5G Core síti, součást Authentication Server Function (AUSF). Působí jako primární bezpečnostní kotva v rámci servisní sítě, řídí procedury autentizace a dohody o"
---

SEAF je primární bezpečnostní kotva v rámci servisní sítě 5G, je součástí AUSF a spravuje procedury autentizace a dohody o klíčích s UE.

## Popis

Funkce bezpečnostní kotvy (SEAF) je základní bezpečnostní komponenta v architektuře systému 5G (5GS), definovaná jako podfunkce Authentication Server Function ([AUSF](/mobilnisite/slovnik/ausf/)). Její primární role spočívá v tom, že slouží jako bezpečnostní koncový bod v servisní síti během procedur primární autentizace a dohody o klíčích ([AKA](/mobilnisite/slovnik/aka/)). SEAF sama neprovádí autentizační výpočty, ale celý proces řídí prostřednictvím komunikace s funkcí [ARPF](/mobilnisite/slovnik/arpf/)/[UDM](/mobilnisite/slovnik/udm/) domovské sítě. Přijímá od domovské sítě autentizační vektory a používá je k autentizaci uživatelského zařízení (UE). Po úspěšné autentizaci SEAF odvodí kotvený klíč (K_SEAF) z klíče domovské sítě (K_AUSF), čímž vytvoří bezpečnostní asociaci ukotvenou v servisní síti. Tento K_SEAF je následně použit k odvození dalších klíčů pro zabezpečení signalizace ne-přístupové vrstvy ([NAS](/mobilnisite/slovnik/nas/)) mezi UE a funkcí [AMF](/mobilnisite/slovnik/amf/). Umístění SEAF v servisní síti je klíčové pro lokalizaci bezpečnosti, což snižuje latenci a závislost na domovské síti pro následné bezpečnostní procedury, jako je re-autentizace a obnova klíčů. Architektonicky je SEAF kolidována s AUSF a její rozhraní, jako je Nausf, se používají pro komunikaci s AMF. Její činnost je ústřední pro bezpečnostní rámec 5G, poskytuje jasné oddělení bezpečnostních odpovědností mezi domovskou a servisní sítí a umožňuje funkce jako bezproblémová mobilita a síťové segmenty (network slicing) s izolovanými bezpečnostními kontexty.

## K čemu slouží

SEAF byla zavedena ve specifikaci 3GPP Release 15 jako součást nové bezpečnostní architektury 5G, aby odstranila omezení předchozích generací, zejména 4G EPS. V EPS fungoval [MME](/mobilnisite/slovnik/mme/) v servisní síti jako bezpečnostní koncový bod, což vytvářelo složitou hierarchii klíčů a potenciální zranitelnosti při předávání mezi MME. Hlavním motivem pro SEAF bylo poskytnout vyhrazenou, stabilní bezpečnostní kotvu v servisní síti, která je oddělena od funkce správy mobility ([AMF](/mobilnisite/slovnik/amf/)). Toto oddělení zodpovědností zvyšuje bezpečnost izolací dlouhodobého kotveného klíče (K_SEAF) a zjednodušuje správu klíčů při událostech mobility. Řeší problém řetězení klíčů a snižuje prostor pro útoky lokalizací primárního bezpečnostního kontextu. Dále návrh SEAF podporuje požadavek 5G na viditelnost a kontrolu autentizace ze strany servisní sítě, což je nezbytné pro regulace a umožnění nových obchodních modelů, jako je síťové segmentování (network slicing), kde každý segment může vyžadovat nezávislou bezpečnostní kotvu z pohledu servisní sítě.

## Klíčové vlastnosti

- Působí jako bezpečnostní koncový bod v servisní síti pro 5G AKA
- Odvozuje kotvený klíč (K_SEAF) z klíče domovské sítě (K_AUSF)
- Řídí primární autentizaci prostřednictvím komunikace s ARPF/UDM domovské sítě
- Umožňuje odvození klíčů pro zabezpečení NAS (K_AMF) pro zabezpečení signalizace s AMF
- Podporuje procedury re-autentizace a obnovy klíčů lokálně v rámci servisní sítě
- Usnadňuje oddělení bezpečnostního kontextu pro síťové segmentování (network slicing)

## Související pojmy

- [AUSF – Authentication Server Function](/mobilnisite/slovnik/ausf/)
- [AMF – Access and Mobility Management Function](/mobilnisite/slovnik/amf/)

## Definující specifikace

- **TS 23.501** (Rel-20) — 5G System Architecture Stage 2
- **TS 29.509** (Rel-19) — AUSF Service Based Interface Protocol
- **TS 33.501** (Rel-20) — 5G Security Architecture and Procedures
- **TR 33.741** (Rel-18) — Home Network Triggered Authentication
- **TS 33.835** (Rel-16) — Study on authentication and key management for apps
- **TR 33.841** (Rel-16) — Security aspects; Study on 256-bit algorithms for 5G

---

📖 **Anglický originál a plná specifikace:** [SEAF na 3GPP Explorer](https://3gpp-explorer.com/glossary/seaf/)
