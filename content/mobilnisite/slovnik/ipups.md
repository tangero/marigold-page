---
slug: "ipups"
url: "/mobilnisite/slovnik/ipups/"
type: "slovnik"
title: "IPUPS – Inter-PLMN User Plane Security"
date: 2026-01-01
abbr: "IPUPS"
fullName: "Inter-PLMN User Plane Security"
category: "Security"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/ipups/"
summary: "IPUPS je bezpečnostní architektura, která poskytuje ochranu důvěrnosti a integrity dat uživatelské roviny přenášených přes rozhraní N9 mezi dvěma různými veřejnými pozemními mobilními sítěmi (PLMN). Z"
---

IPUPS je bezpečnostní architektura, která poskytuje ochranu důvěrnosti a integrity datové části uživatelské roviny procházejících rozhraním N9 mezi dvěma různými veřejnými pozemními mobilními sítěmi (PLMN).

## Popis

Inter-PLMN User Plane Security (IPUPS) je bezpečnostní mechanismus 3GPP navržený k ochraně dat uživatelské roviny při jejich přenosu mezi dvěma různými veřejnými pozemními mobilními sítěmi (PLMN). Jeho hlavním zaměřením je zabezpečení rozhraní N9, což je referenční bod mezi funkcemi uživatelské roviny ([UPF](/mobilnisite/slovnik/upf/)) dvou samostatných sítí, což je běžný scénář při roamingu nebo když je datová relace uživatele zakotvena v domovské síti, zatímco je připojen přes navštívenou síť. IPUPS zajišťuje jak důvěrnost (ochrana před odposlechem), tak integritu (ochrana před neoprávněnými změnami) uživatelských IP paketů.

Architektura IPUPS zahrnuje bezpečnostní brány (SEG) nebo samotné UPF, které fungují jako bezpečnostní koncové body. Tyto body mezi dvěma PLMN vytvářejí zabezpečený tunel, obvykle pomocí [IPsec](/mobilnisite/slovnik/ipsec/). Systém využívá bezpečnostní sadu protokolů definovanou 3GPP, Network Domain Security ([NDS/IP](/mobilnisite/slovnik/nds-ip/)), která specifikuje způsob implementace IPsec pro síťová rozhraní 3GPP. Správa klíčů je řešena pomocí protokolu Internet Key Exchange verze 2 (IKEv2), často s autentizací na bázi certifikátů k navázání důvěryhodného vztahu mezi sítěmi operátorů. Politiky, pro který provoz je vyžadována ochrana (např. veškerý roamový provoz, provoz pro určité [APN](/mobilnisite/slovnik/apn/)), jsou konfigurovány v síťových funkcích.

Provozně, když je třeba odeslat data uživatelské roviny z navštívené PLMN (VPLMN) do domovské PLMN ([HPLMN](/mobilnisite/slovnik/hplmn/)), zdrojová UPF nebo SEG zapouzdří původní [GTP-U](/mobilnisite/slovnik/gtp-u/) a uživatelské IP pakety do IPsec tunelu Encapsulating Security Payload ([ESP](/mobilnisite/slovnik/esp/)). Tunel je ukončen u partnerské entity v druhé síti, která paket dešifruje a ověří před jeho předáním cílové UPF. Tento proces je pro koncového uživatelského terminál (UE) transparentní. IPUPS je klíčovou součástí bezpečnostní architektury 5G a rozšiřuje princip 'security-by-design' na propojení mezi operátory, která představují potenciální slabá místa v globálně propojeném mobilním ekosystému.

## K čemu slouží

IPUPS byl vytvořen k řešení významné bezpečnostní mezery v propojení mezi operátory. Historicky uživatelský provoz mezi sítěmi různých operátorů (např. pro roamingové uživatele) často procházel přes veřejný internet nebo privátní propojení bez povinného šifrování, spoléhaje se na zabezpečení podkladové přenosové sítě. To činilo data zranitelnými vůči zachycení, manipulaci nebo analýze prostředníky. Rostoucí citlivost uživatelských dat a nástup regulačních požadavků na ochranu dat (jako GDPR) si vynutily standardizované a robustní bezpečnostní řešení.

Motivace pro IPUPS vycházela z konstrukčního principu 5G poskytovat zabezpečení od konce ke konci, které zahrnuje i segment 'síť-síť'. Řeší problém zabezpečení uživatelských dat, jakmile opustí relativně kontrolované prostředí sítě jednoho operátora. Zavedením povinného nebo silně doporučeného [IPsec](/mobilnisite/slovnik/ipsec/) na rozhraní N9 zajišťuje 3GPP, že je soukromí uživatele zachováno i během roamingu, a chrání proti hrozbám, jako jsou útoky typu man-in-the-middle na propojení mezi PLMN. Jeho zavedení ve vydání (Release) 16 je v souladu se zvýšenými bezpečnostními požadavky 5G a podporuje nové případy použití vyžadující vyšší důvěru, jako je síťové segmentování (network slicing) pro podniky a kritické IoT komunikace.

## Klíčové vlastnosti

- Ochrana důvěrnosti a integrity uživatelské roviny mezi PLMN (rozhraní N9)
- Založeno na standardizovaném 3GPP NDS/IP a IPsec architektuře
- Využívá IKEv2 s autentizací na bázi certifikátů pro správu klíčů
- Chrání GTP-U tunely a zapouzdřené uživatelské IP pakety
- Může být implementováno UPF nebo vyhrazenými bezpečnostními branami (SEG)
- Podporuje jak povinné, tak volitelné použití podle politiky operátora

## Související pojmy

- [NDS/IP – Network Domain Security for IP based Protocols](/mobilnisite/slovnik/nds-ip/)
- [UPF – User Plane Function](/mobilnisite/slovnik/upf/)

## Definující specifikace

- **TS 23.501** (Rel-20) — 5G System Architecture Stage 2
- **TS 29.244** (Rel-19) — PFCP Specification for Control/User Plane Separation
- **TS 29.510** (Rel-19) — NRF Service Based Interface Protocol
- **TS 33.501** (Rel-20) — 5G Security Architecture and Procedures

---

📖 **Anglický originál a plná specifikace:** [IPUPS na 3GPP Explorer](https://3gpp-explorer.com/glossary/ipups/)
