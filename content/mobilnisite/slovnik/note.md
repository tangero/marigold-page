---
slug: "note"
url: "/mobilnisite/slovnik/note/"
type: "slovnik"
title: "NOTE – Network Operator Tunneling Exchange"
date: 2026-01-01
abbr: "NOTE"
fullName: "Network Operator Tunneling Exchange"
category: "Core Network"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/note/"
summary: "Funkční entita nebo referenční bod usnadňující zabezpečené tunelování a výměnu dat mezi síťovými operátory, zejména pro služby jako SMS, MMS nebo služby založené na poloze. Umožňuje poskytování služeb"
---

NOTE je funkční entita nebo referenční bod, který umožňuje zabezpečené tunelování a výměnu dat mezi síťovými operátory pro služby jako SMS, MMS nebo služby založené na poloze.

## Popis

Network Operator Tunneling Exchange (NOTE) je koncept architektury 3GPP, který poskytuje standardizovaný mechanismus pro zabezpečený přístup a využívání služeb hostovaných v síťové doméně jiného operátora. Funguje jako brána nebo výměnný bod, který zapouzdřuje servisní požadavky a data do zabezpečeného tunelu, čímž zajišťuje soukromí, integritu a řízený přístup. Zatímco uvedená definice je neúplná, kontext termínu napříč specifikacemi jako TS 22.261 (servisní požadavky) a TS 29.238 (signalizace založená na [SIP](/mobilnisite/slovnik/sip/)) naznačuje jeho roli při umožnění poskytování služeb mezi různými [PLMN](/mobilnisite/slovnik/plmn/) pro multimediální a zprávové služby.

Architektonicky lze NOTE implementovat jako dedikovaný síťový uzel nebo logickou funkci, často umístěnou na hranici mezi sítěmi dvou operátorů. Typicky komunikuje s prvky jádra sítě, jako je IP Multimedia Subsystem (IMS) nebo zprávové brány. Například pro službu Multimedia Messaging Service ([MMS](/mobilnisite/slovnik/mms/)): pokud účastník u Operátora A odešle MMS zprávu účastníkovi u Operátora B, může MMS server Operátora A použít rozhraní NOTE k předání zprávy přes síť Operátora B příjemci. Funkce NOTE zajišťuje potřebnou adaptaci protokolu, zabezpečení (např. pomocí [IPsec](/mobilnisite/slovnik/ipsec/) nebo [TLS](/mobilnisite/slovnik/tls/)) a směrování, čímž zaručuje, že servisní požadavek je správně formátován a autorizován pro cizí síť.

Jeho provoz zahrnuje několik klíčových komponent: zásobník tunelovacího protokolu pro vytvoření zabezpečeného spojení, mechanismy autentizace a autorizace pro ověření identity operátora žádajícího o službu a servisní logiku pro překlad nebo směrování zapouzdřených servisních datových jednotek. NOTE abstrahuje složitou topologii a interní konfigurace sítě partnerského operátora. Z pohledu servisního uzlu domovského operátora jednoduše předává data na adresu NOTE; entita NOTE pak přebírá odpovědnost za jejich doručení ke správnému internímu koncovému bodu v navštívené síti. Tento model zjednodušuje partnerské dohody a integraci služeb mezi operátory, protože operátoři potřebují spravovat pouze jeden standardizovaný výměnný bod namísto více bod-od-bodu spojení k různým interním síťovým prvkům.

## K čemu slouží

NOTE byl vytvořen k řešení problému škálovatelného a zabezpečeného poskytování služeb mezi operátory. V raných mobilních sítích vyžadovalo umožnění služeb jako [MMS](/mobilnisite/slovnik/mms/) nebo služeb založených na poloze napříč různými operátory často složité bilaterální integrace mezi konkrétními síťovými prvky (např. MMS centry), což nebylo škálovatelné s rostoucím počtem operátorů a služeb. Účelem NOTE je poskytnout jednotnou, standardizovanou funkci brány, která odděluje interní síťovou architekturu jednoho operátora od servisních požadavků druhého.

Tím se řeší významná omezení předchozích ad-hoc přístupů, které byly nákladné na zavedení a údržbu a mohly vytvářet bezpečnostní rizika kvůli vystavení interních síťových rozhraní. Směrováním provozu mezi operátory přes dedikovaný tunelovací výměnný bod mohou operátoři vynucovat konzistentní bezpečnostní politiky, provádět centralizované logování a účtování transakcí mezi operátory a snadněji spravovat roamingové a partnerské dohody. Jeho zavedení, zvláště zaznamenané kolem Rel-4 s nástupem paketově přepínaných služeb a IMS, bylo motivováno posunem odvětví k all-IP sítím a bohatším ekosystémem multimediálních služeb, které inherentně vyžadovaly bezproblémovou funkčnost napříč operátory, aby byly pro koncové uživatele hodnotné.

## Klíčové vlastnosti

- Poskytuje zabezpečený tunelovací mechanismus pro výměnu dat mezi operátory
- Slouží jako standardizovaná brána nebo referenční bod mezi sítěmi operátorů
- Abstrahuje interní topologii sítě poskytujícího operátora
- Podporuje poskytování služeb pro zprávové (SMS/MMS) a multimediální služby
- Zahrnuje autentizaci a autorizaci pro partnerské operátory
- Umožňuje centralizovanou správu a účtování provozu služeb mezi operátory

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [MMS – Multimedia Messaging Service](/mobilnisite/slovnik/mms/)
- [PLMN – Public Land Mobile Network](/mobilnisite/slovnik/plmn/)

## Definující specifikace

- **TS 22.261** (Rel-20) — 5G System Service Requirements
- **TR 22.975** (Rel-4) — UMTS Numbering and Addressing Requirements
- **TS 24.229** (Rel-19) — IMS call control protocol based on SIP and SDP
- **TR 28.836** (Rel-18) — Technical Report on Intent Driven Management
- **TS 29.238** (Rel-19) — H.248 Profile for IBCF-TrGW Interface
- **TS 32.602** (Rel-19) — Basic Configuration Management IRP Information Service
- **TS 32.612** (Rel-19) — Bulk Configuration Management IRP: Information Service
- **TS 32.662** (Rel-19) — Configuration Management (CM); Kernel CM IRP
- **TS 32.690** (Rel-19) — Inventory Management IRP Requirements

---

📖 **Anglický originál a plná specifikace:** [NOTE na 3GPP Explorer](https://3gpp-explorer.com/glossary/note/)
