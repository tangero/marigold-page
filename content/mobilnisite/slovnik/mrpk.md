---
slug: "mrpk"
url: "/mobilnisite/slovnik/mrpk/"
type: "slovnik"
title: "MRPK – Manufacturer Root Public Key"
date: 2025-01-01
abbr: "MRPK"
fullName: "Manufacturer Root Public Key"
category: "Security"
segment: "User Equipment"
canonical: "https://3gpp-explorer.com/glossary/mrpk/"
summary: "Manufacturer Root Public Key (MRPK) je základní kryptografický klíč používaný v architektuře 3GPP Generic Bootstrapping Architecture (GBA). Patří výrobci zařízení a slouží k autentikaci vestavěného pr"
---

MRPK je základní kryptografický veřejný klíč patřící výrobci zařízení, který autentikuje vestavěný privátní klíč zařízení, aby umožnil bezpečné bootstrapování v architektuře 3GPP Generic Bootstrapping Architecture.

## Popis

Manufacturer Root Public Key (MRPK) je klíčová součást architektury 3GPP Generic Bootstrapping Architecture ([GBA](/mobilnisite/slovnik/gba/)), definovaná v TS 23.057. Jedná se o dlouhodobý asymetrický kryptografický veřejný klíč, který je jedinečně asociován s výrobcem zařízení. Tento klíč je během výrobního procesu vložen do hardwaru zařízení nebo jeho bezpečného prostředí (např. UICC nebo proti manipulaci odolný hardware) společně s odpovídajícím, kryptograficky spárovaným privátním klíčem výrobce (Manufacturer Root Private Key, MRPrK). MRPK se nepoužívá pro přímou autentizaci uživatele nebo sítě, ale slouží jako kotva důvěry pro ověření identity zařízení a jeho držení platného páru klíčů instalovaného výrobcem.

Primární funkcí MRPK je autentikovat veřejný klíč specifický pro zařízení, často označovaný jako Device Public Key (DPK). Během procedury GBA bootstrapování zařízení prokáže síťové funkci Bootstrapping Server Function ([BSF](/mobilnisite/slovnik/bsf/)), že vlastní privátní klíč odpovídající jeho DPK. Tento důkaz má typicky podobu digitálního podpisu vytvořeného pomocí Device Private Key (DPrK). BSF pak může tento podpis ověřit pomocí DPK. BSF však musí nejprvě důvěřovat, že DPK skutečně patří danému zařízení a nebyl pozměněn. Zde přichází na řadu MRPK: DPK je digitálně podepsán privátním klíčem výrobce (MRPrK), čímž vzniká struktura podobná certifikátu. BSF, která je předem vybavena nebo může získat důvěryhodný MRPK pro daného výrobce, může tento podpis ověřit. Tento řetězec důvěry (MRPK podepisuje DPK, DPK podepisuje bootstrapovací požadavek) autentikuje zařízení vůči BSF.

Z architektonického hlediska je MRPK klíčovým prvkem při vytváření sdíleného tajemství v GBA. Po autentizaci zařízení odvodí BSF a zařízení sdílený, na relaci specifický klíč nazvaný Bootstrapping Transaction Identifier ([B-TID](/mobilnisite/slovnik/b-tid/)) a asociovaný klíčový materiál (Ks). Tento Ks je následně používán zařízením a Network Application Function ([NAF](/mobilnisite/slovnik/naf/)) k zabezpečení komunikace na aplikační vrstvě. MRPK tedy umožňuje bezpečnou, automatizovanou a škálovatelnou metodu pro zařízení bez UICC (Universal Integrated Circuit Card) nebo pro aplikace mimo [USIM](/mobilnisite/slovnik/usim/), jak navázat důvěryhodný vztah se síťovými službami. Přesouvá část důvěry z operátorovy [SIM](/mobilnisite/slovnik/sim/) karty na bezpečný proces provisioningu výrobce zařízení.

Správa a zabezpečení MRPK jsou prvořadé. Odpovídající privátní klíč (MRPrK) musí být výrobcem vysoce zabezpečen, protože jeho kompromitace by útočníkovi umožnila generovat platné přihlašovací údaje pro falešná zařízení. Veřejný MRPK musí být distribuován všem BSF v sítích, které chtějí podporovat zařízení od daného výrobce. Tato distribuce může probíhat prostřednictvím bilaterálních dohod nebo potenciálně přes centralizovaný repozitář. Použití MRPK umožňuje funkce jako bezpečné poskytování služeb, správu zařízení (např. pro IoT zařízení) a autentizaci pro aplikace IP Multimedia Subsystem (IMS) a další služby využívající GBA.

## K čemu slouží

Manufacturer Root Public Key byl zaveden, aby řešil klíčovou výzvu v mobilní bezpečnosti: jak autentizovat zařízení a bootstrapovat bezpečná spojení pro aplikace, které fungují nezávisle na autentizaci založené na [USIM](/mobilnisite/slovnik/usim/). Tradiční buněčná autentizace se výlučně spoléhá na přihlašovací údaje uložené na kartě USIM/[SIM](/mobilnisite/slovnik/sim/), která je pod kontrolou síťového operátora. Tento model je nedostatečný pro výrobce zařízení nebo poskytovatele služeb třetích stran, kteří potřebují navázat vlastní zabezpečené kanály se zařízením pro služby jako aktualizace firmwaru, správa zařízení nebo na operátora nezávislé aplikace.

Historicky, bez GBA a MRPK, byly alternativní metody autentizace zařízení ad-hoc, méně bezpečné nebo vyžadovaly složitou správu předem sdílených klíčů. MRPK poskytuje standardizované, škálovatelné a kryptograficky robustní řešení. Vytváří model důvěry, kde výrobce zařízení vystupuje jako kořen důvěry (Root of Trust). Toto bylo zvláště motivováno růstem komunikace mezi stroji (M2M) a internetem věcí (IoT), kde mohou být zařízení nasazena bez tradiční interaktivní SIM karty uživatele nebo mohou potřebovat autentizaci vůči více poskytovatelům služeb.

MRPK řeší problém počátečního navázání důvěry škálovatelným způsobem. Umožňuje BSF síťového operátora důvěřovat zařízení od daného výrobce bez nutnosti předem provisionovat tajemství pro každé jednotlivé zařízení. Podpis výrobce na klíči zařízení slouží jako ověřitelný přihlašovací údaj. To umožňuje bezpečné provisioning a správu typu 'zero-touch', což je klíčové pro rozsáhlá nasazení IoT. Také zajišťuje budoucí odolnost architektury tím, že poskytuje základ pro bezpečné služby v 5G a dalších generacích, kde rozmanitý ekosystém zařízení a služeb vyžaduje flexibilní autentizační mechanismy mimo tradiční SIM.

## Klíčové vlastnosti

- Slouží jako kryptograficky zabezpečený kořen důvěry (root of trust) pro výrobce zařízení v rámci architektury GBA.
- Používá se k ověření autenticity vestavěného veřejného klíče zařízení (Device Public Key).
- Umožňuje bezpečné bootstrapování aplikačních klíčů (Ks) pro zařízení bez autentizace založené na USIM.
- Usnadňuje škálovatelnou a automatizovanou autentizaci zařízení pro služby IoT a M2M.
- Podporuje model důvěry oddělený od přihlašovacích údajů na SIM kartě mobilního operátora.
- Nezbytný pro bezpečné operace správy zařízení a provisioningu služeb.

## Definující specifikace

- **TS 23.057** (Rel-19) — Mobile Execution Environment (MExE) Specification

---

📖 **Anglický originál a plná specifikace:** [MRPK na 3GPP Explorer](https://3gpp-explorer.com/glossary/mrpk/)
