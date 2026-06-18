---
slug: "pii"
url: "/mobilnisite/slovnik/pii/"
type: "slovnik"
title: "PII – Personally Identifiable Information"
date: 2022-01-01
abbr: "PII"
fullName: "Personally Identifiable Information"
category: "Security"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/pii/"
summary: "PII (osobně identifikovatelné údaje) jsou jakákoliv data, která lze samostatně nebo v kombinaci s dalšími informacemi použít k identifikaci, kontaktování nebo lokalizaci konkrétní osoby, nebo k identi"
---

PII (osobně identifikovatelné údaje) jsou jakákoliv data, která lze samostatně nebo v kombinaci s dalšími informacemi použít k identifikaci, kontaktování nebo lokalizaci osoby, jako jsou IMSI, MSISDN, IMEI nebo lokalizační údaje v mobilních sítích.

## Popis

V kontextu standardů 3GPP se termín PII (osobně identifikovatelné údaje) vztahuje k podmnožině uživatelských a abonentních dat, která lze přímo nebo nepřímo spojit s konkrétní fyzickou osobou. Systém 3GPP ze své podstaty zpracovává velké objemy PII za účelem poskytování mobilních služeb. Mezi klíčové kategorie PII patří: Identifikátory předplatného (např. [IMSI](/mobilnisite/slovnik/imsi/) (International Mobile Subscriber Identity), [MSISDN](/mobilnisite/slovnik/msisdn/) (Mobile Subscriber Integrated Services Digital Network Number)), Identifikátory zařízení (např. [IMEI](/mobilnisite/slovnik/imei/) (International Mobile Equipment Identity), [PEI](/mobilnisite/slovnik/pei/) (Permanent Equipment Identifier)), Trvalé identifikátory používané na vrstvách služeb (např. [SIP](/mobilnisite/slovnik/sip/) [URI](/mobilnisite/slovnik/uri/), Private User Identity) a Uživatelský provoz a lokalizační data (např. [GPS](/mobilnisite/slovnik/gps/) souřadnice, identifikátor buňky, obsah komunikace).

Architektura pro ochranu PII je do návrhu systému 3GPP vpletena. Zahrnuje několik klíčových principů a funkcí: Anonymita, kdy se po rozhraní pro rádiový přenos používají dočasné identifikátory jako [TMSI](/mobilnisite/slovnik/tmsi/) (Temporary Mobile Subscriber Identity) nebo 5G-GUTI, aby se zabránilo vystavení trvalých identifikátorů; Důvěrnost, dosažená šifrováním dat uživatelské a řídicí roviny (pomocí algoritmů jako 128-EEA3 v 4G nebo NEA v 5G) a ochranou integrity; a Řízení přístupu, vynucované prostřednictvím protokolu AKA (Authentication and Key Agreement) a profilů předplatného v HSS (Home Subscriber Server) nebo UDM (Unified Data Management).

Síťové funkce, které zpracovávají PII, jako je UDR (User Data Repository), NEF (Network Exposure Function) a systémy LI (Lawful Interception), mají specifické bezpečnostní požadavky definované v 3GPP TS 33.867. NEF například funguje jako bezpečnostní brána pro PII při vystavování síťových schopností třetím stranám prostřednictvím AF (Application Functions). Před sdílením dat anonymizuje, agreguje nebo aplikuje zásady ochrany soukromí. Dále 3GPP definuje PRI (Privacy Requirement Indicators), které může UE signalizovat síti, aby vyjádřilo uživatelské preference týkající se vystavení určitých PII, jako je jeho IMEI. Celý životní cyklus PII – sběr, ukládání, zpracování, přenos a odstranění – podléhá principům ochrany soukromí již při návrhu, které vyžadují předpisy jako GDPR, a tyto principy jsou zohledněny v technických specifikacích 3GPP.

## K čemu slouží

Formální definice a přístup k PII ve specifikacích 3GPP byly hnací silou rostoucího globálního regulačního prostředí pro ochranu dat a zvyšující se hodnoty (a rizika) uživatelských dat v digitálním věku. Rané mobilní systémy byly navrženy především pro funkčnost a zabezpečení se zaměřením na řízení přístupu k síti (např. zabránění klonování). I když chránily před některými hrozbami, komplexní ochrana soukromí uživatelských informací nebyla primárním architektonickým zájmem.

Rozšíření mobilního internetu, služeb založených na poloze a IoT zvýšilo objem a citlivost PII zpracovávaných sítěmi. To přitáhlo pozornost regulátorů a vedlo k přijetí zákonů jako obecné nařízení o ochraně osobních údajů (GDPR) EU. 3GPP jako globální normalizační orgán muselo vyvinout své specifikace, aby poskytlo technický rámec umožňující operátorům dodržovat takové předpisy. Standardizace nakládání s PII zajišťuje interoperabilitu nejen pro služby, ale také pro zákonné a z hlediska ochrany soukromí kompatibilní operace napříč více-dodavatelskými mezinárodními sítěmi.

Navíc obchodní model vystavování síťových API vývojářům třetích stran (např. prostřednictvím SCEF/NEF) vytvořil novou útočnou plochu pro PII. Bez standardizovaných mechanismů pro anonymizaci a řízení zásad by operátoři riskovali narušení dat a nedodržování předpisů. Práce 3GPP na PII, zejména od verze Rel-12 dále, poskytuje nezbytné technické kontroly – jako je zprostředkovatelská role NEF a PRI – které umožňují inovace prostřednictvím vystavení síťových schopností a zároveň zásadně chrání soukromí účastníků. Řeší tak základní problém vyvážení personalizace služeb a síťové funkcionality se základním právem jednotlivce na soukromí.

## Klíčové vlastnosti

- Zahrnuje identifikátory jako IMSI, MSISDN, IMEI/PEI, IP adresu a lokalizační informace
- Ochrana prostřednictvím šifrování (uživatelské/řídicí roviny), ochrany integrity a používání dočasných identifikátorů (TMSI/GUTI)
- PRI (Privacy Requirement Indicators) umožňují UE signalizovat síti preference ohledně ochrany soukromí
- NEF (Network Exposure Function) anonymizuje/agreguje PII před vystavením externím AF
- Řízeno přísnými bezpečnostními požadavky v TS 33.867 pro UDR, LI a další NF zpracovávající data
- Nedílná součást sladění 3GPP s globálními předpisy na ochranu soukromí (např. GDPR, CCPA)

## Související pojmy

- [SUPI – Subscription Permanent Identifier](/mobilnisite/slovnik/supi/)
- [NEF – Network Exposure Function](/mobilnisite/slovnik/nef/)
- [AKA – Authentication and Key Agreement](/mobilnisite/slovnik/aka/)

## Definující specifikace

- **TS 22.864** (Rel-15) — 5G Network Operation Use Cases & Requirements
- **TS 33.849** (Rel-14) — 3GPP Privacy Principles and Guidelines
- **TR 33.867** (Rel-17) — User Consent for 3GPP Services

---

📖 **Anglický originál a plná specifikace:** [PII na 3GPP Explorer](https://3gpp-explorer.com/glossary/pii/)
