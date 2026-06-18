---
slug: "sepp"
url: "/mobilnisite/slovnik/sepp/"
type: "slovnik"
title: "SEPP – Security Edge Protection Proxy"
date: 2026-01-01
abbr: "SEPP"
fullName: "Security Edge Protection Proxy"
category: "Security"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/sepp/"
summary: "SEPP je bezpečnostní proxy nasazená na okraji sítě, která chrání rozhraní založené na službách (SBI) uvnitř a mezi jádry sítí 5G. Autentizuje a autorizuje všechny zprávy SBI, uplatňuje bezpečnostní po"
---

SEPP je bezpečnostní proxy nasazená na okraji sítě, která chrání rozhraní založené na službách (Service-Based Interface) uvnitř a mezi jádry sítí 5G (5G Core) tím, že autentizuje, autorizuje a zabezpečuje všechny signalizační zprávy mezi různými veřejnými pozemními mobilními sítěmi (PLMN).

## Popis

Security Edge Protection Proxy (SEPP) je základní bezpečnostní uzel zavedený v architektuře jádra 5G (5GC). Funguje jako netransparentní proxy pro všechny zprávy rozhraní založeného na službách ([SBI](/mobilnisite/slovnik/sbi/)) na bázi [HTTP](/mobilnisite/slovnik/http/)/2, které překračují hranice sítí, primárně mezi různými veřejnými pozemními mobilními sítěmi ([PLMN](/mobilnisite/slovnik/plmn/)) v roamovacích scénářích. Primární funkcí SEPP je chránit rozhraní N32, což je referenční bod pro propojení mezi SEPP různých operátorů. Nachází se na perimetru sítě a kontroluje veškerý příchozí a odchozí provoz SBI do a ze síťových funkcí ([NF](/mobilnisite/slovnik/nf/)), jako jsou [AMF](/mobilnisite/slovnik/amf/), [SMF](/mobilnisite/slovnik/smf/) a [NRF](/mobilnisite/slovnik/nrf/).

Architektonicky je SEPP dedikovaná síťová funkce, která implementuje zabezpečení na aplikační vrstvě. Spolupracuje se síťovou repozitářovou funkcí (NRF) pro zjišťování služeb a řízení politik. Pro odchozí zprávy určené do jiné PLMN přijímá domácí SEPP požadavek SBI od producentské NF, provede bezpečnostní zpracování (včetně potenciálního šifrování a ochrany integrity) a přepošle jej do SEPP navštívené PLMN. Navštívený SEPP následně zprávu ověří, odstraní bezpečnostní zapouzdření a směruje ji k příslušné konzumentské NF ve své síti. Tento model zabezpečení skok po skoku zajišťuje, že interní topologie sítě a identity NF jsou skryty před externími subjekty.

SEPP využívá pro rozhraní N32 dva hlavní bezpečnostní mechanismy: N32-c a N32-f. N32-c je řídicí rozhraní používané pro vytvoření bezpečnostního kontextu a vyjednávání parametrů mezi dvěma SEPP před výměnou dat. N32-f je přenosové rozhraní, které přenáší skutečné chráněné zprávy SBI. Ochrana může být aplikována pomocí [JSON](/mobilnisite/slovnik/json/) Web Encryption (JWE) pro důvěrnost a JSON Web Signature (JWS) pro integritu a autentizaci HTTP zpráv. SEPP také provádí filtrování zpráv a skrývání topologie, odstraněním nebo úpravou citlivých směrovacích informací v hlavičkách, aby zabránil externím sítím v mapování interního nasazení NF. Jeho role je klíčová pro umožnění bezpečného roamování, síťového řezání napříč operátory a vystavení síťových schopností poskytovatelům aplikací třetích stran prostřednictvím funkce pro vystavení sítě (NEF).

## K čemu slouží

SEPP byl vytvořen, aby řešil významné bezpečnostní výzvy zavedené architekturou založenou na službách (SBA) jádra 5G a její závislostí na API HTTP/2 (SBI). V předchozích generacích (4G EPC) používala signalizace mezi operátory protokoly na bázi Diameter, jako S6a a S8, které měly vlastní bezpečnostní mechanismy (např. IPsec, zabezpečení Diameter). Přechod na RESTful API a potřeba flexibilnějšího vystavení sítě vytvořily novou útočnou plochu. Bez dedikované okrajové proxy by byly zprávy HTTP/2 mezi operátory zranitelné vůči odposlechu, manipulaci a falšování a odhalovaly by interní strukturu sítě.

Hlavní problémy, které SEPP řeší, jsou zabezpečení komunikace mezi PLMN pro roamování a umožnění bezpečného přístupu třetích stran. Roaming v 5G vyžaduje, aby mezi domácí a navštívenou sítí proudilo množství zpráv SBI pro autentizaci, správu relací a řízení politik. SEPP zajišťuje, že tyto zprávy jsou mezi síťovými perimetry autentizovány, autorizovány a chráněny end-to-end. Dále usnadňuje skrývání topologie, což je regulatorní a bezpečnostní požadavek operátorů na utajení jejich interní konfigurace sítě před partnery a potenciálními útočníky.

K jeho vytvoření vedl tlak 3GPP na cloud-nativní, webově přívětivé jádro sítě. SBA umožňuje agilní nasazování služeb, ale přebírá také bezpečnostní obavy webových technologií. SEPP je standardizovanou odpovědí na aplikaci robustního zabezpečení na aplikační vrstvě šitého na míru telekomunikačním potřebám, nahrazující ad-hoc bezpečnostní brány a zajišťující konzistentní, interoperabilní bezpečnostní základ pro globální nasazení 5G, zejména pro síťové řezy napříč administrativními doménami.

## Klíčové vlastnosti

- Zabezpečení na aplikační vrstvě pro zprávy SBI na bázi HTTP/2
- Ochrana skok po skoku pro mezi-PLMN rozhraní N32
- Podpora JSON Web Encryption (JWE) a JSON Web Signature (JWS)
- Skrývání topologie interních identit a konfigurace síťových funkcí
- Filtrování zpráv a vynucování politik na síťovém perimetru
- Integrace s NRF pro zjišťování a řízení bezpečnostních politik

## Definující specifikace

- **TS 23.501** (Rel-20) — 5G System Architecture Stage 2
- **TR 26.930** (Rel-19) — WebRTC Enhancements for Immersive RTC over 5G
- **TS 29.500** (Rel-19) — 5GC Service Based Architecture Specification
- **TS 29.513** (Rel-19) — 5G PCC Signalling Flows & QoS Mapping
- **TS 29.573** (Rel-19) — PLMN/SNPN Interconnection Interface Stage 3
- **TS 33.117** (Rel-20) — Catalogue of General Security Assurance Requirements
- **TS 33.501** (Rel-20) — 5G Security Architecture and Procedures
- **TS 33.517** (Rel-20) — 5G Security Assurance Specification (SCAS)
- **TS 33.776** (Rel-19) — Study of ACME for 5G SBA
- **TR 33.841** (Rel-16) — Security aspects; Study on 256-bit algorithms for 5G

---

📖 **Anglický originál a plná specifikace:** [SEPP na 3GPP Explorer](https://3gpp-explorer.com/glossary/sepp/)
