---
slug: "supi"
url: "/mobilnisite/slovnik/supi/"
type: "slovnik"
title: "SUPI – Subscription Permanent Identifier"
date: 2026-01-01
abbr: "SUPI"
fullName: "Subscription Permanent Identifier"
category: "Identifier"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/supi/"
summary: "Subscription Permanent Identifier (SUPI, trvalý identifikátor předplatného) je globálně jedinečný, trvalý identifikátor předplatného 3GPP v systémech 5G. Slouží jako základní identita předplatného, po"
---

SUPI je globálně jedinečný, trvalý identifikátor předplatného 3GPP v systémech 5G, který slouží jako základní identita pro autentizaci a správu předplatného.

## Popis

Subscription Permanent Identifier (SUPI, trvalý identifikátor předplatného) je klíčový koncept v architektuře systému 5G, definovaný poprvé ve verzi 3GPP Release 15. Jedná se o globálně jedinečný, neměnný identifikátor, který trvale reprezentuje uživatelovo předplatné v rámci ekosystému 3GPP. Síť používá SUPI pro účely identifikace, autentizace, autorizace a účtování. Je bezpečně uložen ve funkci Unified Data Management ([UDM](/mobilnisite/slovnik/udm/)) a na univerzálním modulu identifikace účastníka ([USIM](/mobilnisite/slovnik/usim/)) v zařízení uživatele. Samotný SUPI se nikdy nepřenáší v čitelné podobě přes rozhraní vzduchu, aby byla chráněno soukromí uživatele; místo toho je skryt pomocí identifikátoru chránícího soukromí zvaného Subscription Concealed Identifier ([SUCI](/mobilnisite/slovnik/suci/)).

Z architektonického hlediska je SUPI klíčovým vstupem do procedur 5G Authentication and Key Agreement (5G [AKA](/mobilnisite/slovnik/aka/)) a Extensible Authentication Protocol ([EAP](/mobilnisite/slovnik/eap/))-AKA'. Při počáteční registri vygeneruje uživatelské zařízení (UE) SUCI zašifrováním SUPI veřejným klíčem domovské sítě pomocí schématu Elliptic Curve Integrated Encryption Scheme ([ECIES](/mobilnisite/slovnik/ecies/)). Tento SUCI je odeslán do obsluhující sítě (např. navštívené sítě v roamingu). Obsluhující síť přepošle SUCI do funkce Authentication Server Function ([AUSF](/mobilnisite/slovnik/ausf/)) domovské sítě, která s pomocí funkce Subscription Identifier De-concealing Function ([SIDF](/mobilnisite/slovnik/sidf/)) v UDM dešifruje SUCI a získá zpět SUPI. SUPI je poté použit k načtení autentizačního vektoru a profilu předplatného z UDM.

SUPI může mít dva hlavní formáty: formát založený na IMSI nebo formát Network Access Identifier (NAI). SUPI založený na IMSI následuje strukturu International Mobile Subscriber Identity (IMSI), která se skládá z mobilního kódu země (MCC), mobilního kódu sítě (MNC) a čísla identifikace mobilního předplatného (MSIN). To zajišťuje zpětnou kompatibilitu se staršími systémy. SUPI založený na NAI se používá pro přístup mimo 3GPP (např. Wi-Fi) a následuje formát uživatelské_jméno@doména. Role SUPI přesahuje rámec autentizace; používá se v řízení politik (prostřednictvím Policy Control Function (PCF)), účtování (prostřednictvím Charging Function (CHF)) a výběru síťových řezů (prostřednictvím Network Slice Selection Function (NSSF)). Jeho trvalá povaha zajišťuje konzistentní identifikaci napříč relacemi a událostmi mobility a tvoří páteř správy předplatného v 5G.

## K čemu slouží

SUPI byl zaveden ve verzi 5G Release 15, aby řešil nedostatky v oblasti soukromí a bezpečnosti u předchozích identifikátorů předplatného, zejména IMSI používaného v 4G LTE. V LTE se IMSI někdy přenášel v čitelné podobě během počátečních procedur připojení, což jej činilo zranitelným vůči odposlechu a útokům na sledování. To umožňovalo škodlivým aktérům identifikovat a lokalizovat uživatele a narušovat tak jejich soukromí. SUPI v kombinaci s mechanismem SUCI byl navržen tak, aby poskytoval silné soukromí identity účastníka tím, že zajišťuje, že trvalý identifikátor není nikdy vystaven přes rozhraní vzduchu.

Další motivací bylo vytvořit jednotný identifikátor předplatného, který bezproblémově funguje napříč různými typy přístupu (3GPP a mimo 3GPP) a podporuje nové služby, jako jsou síťové řezy a IoT. Starší IMSI bylo primárně navrženo pro buněčný přístup, zatímco 5G předpokládá konvergenci s pevnými a bezdrátovými lokálními sítěmi. Flexibilní formáty SUPI (založené na IMSI a NAI) tuto konvergenci umožňují a zajišťují konzistentní správu předplatného v heterogenních sítích.

SUPI dále podporuje vylepšené bezpečnostní protokoly a modely směrování provozu přes domovskou síť v roamingu. Tím, že je SUPI skrytý, dokud nedosáhne domovské sítě, snižuje nároky na důvěru vůči navštíveným sítím a zmírňuje rizika spojená s mezinárodním roamingem. To je v souladu s principy návrhu 5G, které kladou důraz na zabudovanou bezpečnost a ochranu soukromí, a řeší tak regulatorní požadavky, jako je Obecné nařízení o ochraně osobních údajů (GDPR). SUPI tak řeší dvojí problém: poskytuje robustní, trvalou kotvu předplatného a zároveň zajišťuje soukromí uživatele ve stále více propojeném a sledovaném digitálním prostředí.

## Klíčové vlastnosti

- Globálně jedinečný a trvalý identifikátor předplatného 3GPP
- Nikdy se nepřenáší v čitelné podobě přes rozhraní vzduchu; je vždy skryt jako SUCI z důvodu ochrany soukromí
- Podporuje dva formáty: založený na IMSI (pro buněčný přístup) a založený na NAI (pro přístup mimo 3GPP)
- Základní vstup pro autentizační procedury 5G AKA a EAP-AKA'
- Používá se pro profilování předplatného, řízení politik a výběr síťových řezů
- Bezpečně uložen v UDM a USIM, přičemž dešifrování je možné pouze v domovské síti

## Související pojmy

- [SUCI – Subscription Concealed Identifier](/mobilnisite/slovnik/suci/)
- [IMSI – International Mobile Subscriber Identity](/mobilnisite/slovnik/imsi/)
- [UDM – Unified Data Management](/mobilnisite/slovnik/udm/)

## Definující specifikace

- **TS 23.003** (Rel-19) — Numbering, addressing and identification in 3GPP
- **TS 23.501** (Rel-20) — 5G System Architecture Stage 2
- **TS 23.700** (Rel-20) — XR Services Application Enablement Layer
- **TS 24.501** (Rel-19) — 5G NAS Protocols Specification
- **TS 24.502** (Rel-19) — 5G Core Access via Non-3GPP Networks; Stage 3
- **TS 24.526** (Rel-19) — UE Policies for 5GS; Stage 3
- **TS 28.204** (Rel-18) — Charging management
- **TR 28.840** (Rel-18) — Technical Report
- **TS 29.503** (Rel-19) — UDM Service Based Interface Stage 3
- **TS 29.504** (Rel-19) — Nudr Service Based Interface Stage 3 Protocol
- **TS 29.505** (Rel-19) — UDR Service for Subscription Data Usage
- **TS 29.507** (Rel-19) — 5G Access & Mobility Policy Control Service
- **TS 29.508** (Rel-19) — 5G Session Management Event Exposure Service
- **TS 29.514** (Rel-19) — 5G System; Policy Authorization Service; Stage 3
- **TS 29.515** (Rel-19) — Ngmlc Service Based Interface Protocol
- … a dalších 26 specifikací

---

📖 **Anglický originál a plná specifikace:** [SUPI na 3GPP Explorer](https://3gpp-explorer.com/glossary/supi/)
