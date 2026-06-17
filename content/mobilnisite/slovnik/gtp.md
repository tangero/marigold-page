---
slug: "gtp"
url: "/mobilnisite/slovnik/gtp/"
type: "slovnik"
title: "GTP – GPRS Tunnelling Protocols"
date: 2025-01-01
abbr: "GTP"
fullName: "GPRS Tunnelling Protocols"
category: "Protocol"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/gtp/"
summary: "Soubor IP protokolů používaných v mobilních sítích 3GPP pro zapouzdření a tunelování uživatelských dat a signalizace řídicí roviny mezi síťovými uzly, primárně mezi jádrem sítě a rádiovou přístupovou"
---

GTP je soubor IP protokolů používaných v mobilních sítích 3GPP pro zapouzdření a tunelování uživatelských dat a signalizace řídicí roviny mezi síťovými uzly, což umožňuje mobilitu a správu relací.

## Popis

Protokoly pro tunelování [GPRS](/mobilnisite/slovnik/gprs/) (GTP) jsou základní sadou protokolů definovaných 3GPP pro paketově přepínané mobilní sítě, včetně GPRS, UMTS, LTE a 5G. GTP funguje nad IP sítěmi a používá se především k přenosu uživatelských dat a signalizace řídicí roviny mezi prvky jádra sítě, jako je Serving GPRS Support Node (SGSN) a Gateway GPRS Support Node (GGSN) v 3G, nebo Serving Gateway (SGW), Packet Data Network Gateway (PGW) a Mobility Management Entity ([MME](/mobilnisite/slovnik/mme/)) v LTE/EPC. Sada protokolů se dělí na odlišné varianty: [GTP-C](/mobilnisite/slovnik/gtp-c/) pro signalizaci řídicí roviny a [GTP-U](/mobilnisite/slovnik/gtp-u/) pro tunelování dat v uživatelské rovině. GTP vytváří logické tunely identifikované identifikátory koncových bodů tunelu (TEID), které jsou dynamicky přidělovány během procedur navazování relace, jako je aktivace PDP kontextu nebo nastavení EPS přenosového kanálu. Tyto tunely zapouzdřují původní IP pakety z uživatelského zařízení (UE) a přidávají hlavičky GTP obsahující TEID, pořadová čísla a informace o typu zprávy, což síti umožňuje směrovat provoz na správný koncový bod a bezproblémově zvládat události mobility, jako je předávání hovoru.

Z architektonického hlediska je GTP protokolem typu klient-server, kde iniciátor GTP (např. SGSN nebo SGW) odesílá požadavky odpovídači GTP (např. GGSN nebo PGW). Řídicí rovina, GTP-C, zajišťuje funkce správy relací, jako je vytváření, modifikace a rušení tunelů, a také správu mobility, například aktualizaci koncových bodů tunelu při předávání hovoru. Používá mechanismus požadavek-odpověď se zprávami jako Create PDP Context Request/Response. Uživatelská rovina, GTP-U, je zodpovědná za přeposílání vlastních paketů uživatelských dat v rámci těchto zavedených tunelů. Obsahuje mechanismy pro doručování ve správném pořadí a detekci ztrát pomocí pořadových čísel, ačkoli opětovný přenos obvykle zajišťují protokoly vyšších vrstev. Pakety GTP-U jsou přenášeny přes UDP/IP, což poskytuje odlehčený a efektivní mechanismus pro přenos dat.

V systémech 5G hraje GTP i nadále klíčovou roli, zejména v uživatelské rovině mezi funkcí uživatelské roviny ([UPF](/mobilnisite/slovnik/upf/)) a (R)[AN](/mobilnisite/slovnik/an/), jak je definováno v architektuře 5G Core (5GC). Zatímco řídicí rovina v 5GC primárně používá rozhraní založené na službách (SBI) využívající [HTTP](/mobilnisite/slovnik/http/)/2, GTP-U zůstává dominantním protokolem pro tunelování uživatelské roviny díky své osvědčené efektivitě a kompatibilitě. Protokol se vyvinul, aby podporoval nové požadavky, jako je síťové dělení (network slicing), kde více logických sítí sdílí stejnou fyzickou infrastrukturu, a tunely GTP mohou být asociovány s konkrétními identifikátory řezů. GTP dále podporuje různé rozšíření a volby, jako jsou identifikátory účtování, parametry kvality služby (QoS) a podporu různých přístupových technologií, což z něj činí univerzální a trvalou součást mobilních paketových jader sítě.

## K čemu slouží

GTP bylo vytvořeno, aby řešilo základní výzvu poskytování bezproblémových IP služeb paketových dat v mobilních sítích, což umožňuje mobilitu uživatelů a kontinuitu relací. Před GTP dominovaly sítě s přepojováním okruhů, ale rozmach internetu si vyžádal efektivní architektury s přepojováním paketů. GTP vyřešilo problém tunelování uživatelských IP paketů mezi distribuovanými síťovými uzly přes IP páteř, což umožnilo jádru sítě spravovat účastnické relace nezávisle na podkladové rádiové přístupové technologii. Poskytlo standardizovaný mechanismus pro zapouzdření dat, který zajišťoval, že pakety mohou být správně směrovány k mobilním uživatelům a od nich, když se pohybují, aniž by to vyžadovalo změny ve vnějších paketových datových sítích (PDN), jako je internet.

Návrh protokolu byl motivován potřebou oddělení řídicí a uživatelské roviny, což je klíčový princip v telekomunikačních sítích. [GTP-C](/mobilnisite/slovnik/gtp-c/) zajišťuje signalizaci pro zřizování, modifikaci a rušení relací, zatímco GTP-U efektivně přeposílá uživatelská data. Toto oddělení umožňuje škálovatelná a flexibilní nasazení sítě, kde řídicí prvky mohou být centralizovány a prvky uživatelské roviny distribuovány blíže k okraji sítě. GTP také zavedlo klíčové funkce mobility, které umožňují předávání hovoru mezi základnovými stanicemi a uzly jádra bez přerušení aktivních datových relací, což bylo nezbytné pro podporu služeb v reálném čase a neustálého připojení.

Historicky GTP vzniklo ve specifikacích GPRS pro sítě 2.5G a bylo průběžně vylepšováno v rámci vydání pro 3G, 4G a 5G. Jeho dlouhověkost je dokladem jeho účinnosti při řešení základních požadavků na mobilitu a tunelování. Ačkoli byly zvažovány alternativní protokoly, jednoduchost, robustnost a rozsáhlá základna nasazení GTP zajistily jeho další použití, zejména v uživatelské rovině, a to i přesto, že se rozhraní řídicí roviny v 5G vyvíjejí směrem ke službám založeným na HTTP/2. Odstraňuje omezení dřívějších, rigidnějších architektur tím, že poskytuje dynamický, na tunely orientovaný přístup, který se přizpůsobuje měnícím se síťovým podmínkám a polohám účastníka.

## Klíčové vlastnosti

- IP protokol pro tunelování určený k zapouzdření uživatelských dat a signalizace řídicí roviny
- Rozdělení na varianty GTP-C (řídicí rovina) a GTP-U (uživatelská rovina)
- Používá identifikátory koncových bodů tunelu (TEID) pro dynamickou správu tunelů
- Podporuje funkce mobility, jako je předávání hovoru a kontinuita relace
- Přenos přes UDP/IP pro efektivitu a nízkou režii
- Rozšiřitelný formát hlavičky s volbami pro účtování, QoS a síťové dělení

## Související pojmy

- [UPF – User Plane Function](/mobilnisite/slovnik/upf/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.060** (Rel-19) — GPRS Service Description Stage 2
- **TS 23.221** (Rel-19) — 3GPP System Architectural Requirements
- **TS 23.228** (Rel-19) — IMS Stage-2 Service Description
- **TS 23.234** (Rel-13) — 3GPP-WLAN Interworking Index
- **TS 23.327** (Rel-13) — 3GPP-WLAN Mobility Stage 2 Description
- **TS 23.804** (Rel-7) — SMS/MMS over IP Access Support
- **TS 23.857** (Rel-11) — EPC Node Failure & Restoration Study
- **TS 24.161** (Rel-19) — Network-Based IP Flow Mobility (NBIFOM)
- **TS 25.401** (Rel-19) — UTRAN Overall Architecture
- **TS 25.413** (Rel-19) — Radio Access Network Application Part (RANAP)
- **TS 25.414** (Rel-19) — UTRAN Iu Interface User Plane Transport Protocols
- **TS 26.804** (Rel-19) — 5G Media Streaming Extensions Study
- **TR 26.806** (Rel-18) — Technical Report on Smartly Tethering AR Glasses
- **TR 26.937** (Rel-19) — 3GPP PSS Characterization
- … a dalších 22 specifikací

---

📖 **Anglický originál a plná specifikace:** [GTP na 3GPP Explorer](https://3gpp-explorer.com/glossary/gtp/)
