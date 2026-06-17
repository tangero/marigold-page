---
slug: "5g-guti"
url: "/mobilnisite/slovnik/5g-guti/"
type: "slovnik"
title: "5G-GUTI – 5G Globally Unique Temporary Identifier"
date: 2026-01-01
abbr: "5G-GUTI"
fullName: "5G Globally Unique Temporary Identifier"
category: "Identifier"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/5g-guti/"
summary: "Dočasný identifikátor přidělený UE v sítích 5G, který chrání trvalou identitu předplatitele uživatele (SUPI). Používá se v procedurách přístupu k síti, pagingu a žádostech o služby, umožňuje efektivní"
---

5G-GUTI je dočasný identifikátor přidělený UE v sítích 5G, který chrání trvalou identitu předplatitele uživatele a používá se pro přístup k síti, paging a žádosti o služby.

## Popis

5G-GUTI je základní identifikátor v architektuře systému 5G, navržený pro jedinečnou a dočasnou identifikaci uživatelského zařízení (UE) v rámci sítě. Slouží jako alias chránící soukromí pro trvalý identifikátor předplatitele (SUPI), a zajišťuje, že dlouhodobá identita uživatele není vystavena během rádiové komunikace, čímž snižuje riziko sledování a odposlechu. Identifikátor je strukturován tak, aby podporoval efektivní síťové operace včetně registrace, žádostí o služby a správy mobility, protože síť může korelovat relace a kontext bez opakovaného dotazování na SUPI.

Architektonicky je 5G-GUTI přidělen funkcí pro správu přístupu a mobility ([AMF](/mobilnisite/slovnik/amf/)) během počátečních registračních procedur. Skládá se ze dvou hlavních komponent: [GUAMI](/mobilnisite/slovnik/guami/) (Globálně jedinečný identifikátor AMF) a [5G-TMSI](/mobilnisite/slovnik/5g-tmsi/) (Dočasná identita mobilního účastníka 5G). GUAMI jednoznačně identifikuje AMF, která 5G-GUTI přidělila, a zahrnuje mobilní kód země ([MCC](/mobilnisite/slovnik/mcc/)), mobilní kód sítě ([MNC](/mobilnisite/slovnik/mnc/)), ID oblasti AMF, ID sady AMF a ukazatel AMF. 5G-TMSI je jedinečný identifikátor v rámci této AMF, používaný k lokálnímu rozlišení UE. Tato hierarchická struktura umožňuje škálovatelné směrování a správu, protože síť může z GUAMI určit obsluhující AMF a následně použít 5G-TMSI k nalezení konkrétního kontextu UE.

Během provozu UE zahrne 5G-GUTI do signalizačních zpráv, jako jsou žádosti o registraci nebo služby, aby se identifikovala síti. AMF ověří 5G-GUTI, aby načetla bezpečnostní kontext UE a data předplatného ze svého lokálního úložiště nebo z Unified Data Management ([UDM](/mobilnisite/slovnik/udm/)). Pokud je 5G-GUTI neplatný nebo jeho platnost vypršela, síť může zahájit proceduru přeauthientikace a případně bezpečně vyžádat SUPI. Identifikátor může být přepřidělen nebo aktualizován během událostí mobility, jako jsou předání nebo přesuny mezi AMF, aby odrážel změny v obsluhující síťové entitě. Toto dynamické přidělování podporuje plynulou mobilitu napříč různými AMF a síťovými řezy.

Role 5G-GUTI přesahuje ochranu identity; je nedílnou součástí efektivity a škálovatelnosti sítě. Použitím dočasného identifikátoru síť snižuje signalizační režii, protože AMF může rychle vyřešit kontext UE bez rozsáhlých databázových dotazů. Také usnadňuje procedury pagingu a oznámení, kde se 5G-TMSI používá k pagingu UE v určité oblasti. Ve scénářích zahrnujících síťové řezy pomáhá 5G-GUTI asociovat UE s příslušnou instancí řezu, což zajišťuje zachování mobility a kontinuity služeb napříč hranicemi řezů. Celkově je 5G-GUTI základním kamenem bezpečnostního a provozního návrhu 5G, který vyvažuje soukromí, výkon a flexibilitu.

## K čemu slouží

5G-GUTI byl vytvořen, aby řešil kritické nedostatky v oblasti soukromí a bezpečnosti přítomné v předchozích mobilních generacích, jako je 4G/LTE, kde mohly být dočasné identifikátory jako [GUTI](/mobilnisite/slovnik/guti/) v čase stále spojovány s trvalými identitami, což umožňovalo potenciální sledování. V 5G je vylepšené soukromí klíčovým požadavkem, hnaným regulacemi jako GDPR a zvýšeným povědomím uživatelů. 5G-GUTI to řeší tím, že poskytuje robustní mechanismus pro zakrytí SUPI během rádiových přenosů, což brání pasivním útočníkům v korelaci aktivit nebo polohy uživatele s jeho trvalou identitou. Toto oddělení zajišťuje, že i když jsou dočasné identifikátory zachyceny, nelze je snadno namapovat na dlouhodobé předplatné uživatele.

Historicky měly identifikátory v sítích 2G/3G/4G, jako [IMSI](/mobilnisite/slovnik/imsi/) nebo 4G-GUTI, omezení v ochraně soukromí a škálovatelnosti. Například 4G-GUTI mohl být použit ke sledování uživatelů, pokud nebyl často obnovován, a jeho struktura byla méně optimalizovaná pro distribuované architektury, jako je službami řízené rozhraní 5G. 5G-GUTI zavádí více hierarchický a globálně jedinečný design, který je v souladu s cloud-nativním prostředím a prostředím řezů sítě 5G. Podporuje efektivní správu mobility napříč různými scénáři nasazení, včetně neveřejných sítí a edge computingu, tím, že umožňuje jasné směrování ke správné instanci AMF.

Dále 5G-GUTI řeší provozní výzvy ve velkých sítích tím, že snižuje závislost na centrálních databázích pro každou interakci s UE. Tím, že umožňuje AMF spravovat dočasné identifikátory lokálně, snižuje latenci a signalizační zátěž, což je klíčové pro případy použití 5G s nízkou latencí, jako je URLLC. Identifikátor také usnadňuje síťové řezy tím, že v sobě nese informace specifické pro AMF, což zajišťuje, že kontexty UE jsou zpracovávány v rámci příslušného řezu. Celkově 5G-GUTI ztělesňuje principy 5G: vylepšenou bezpečnost, soukromí integrované do návrhu a škálovatelnou architekturu, řeší problémy dědictví minulosti a zároveň umožňuje budoucí inovace.

## Klíčové vlastnosti

- Globálně jedinečná struktura s komponentami GUAMI a 5G-TMSI
- Ochrana soukromí skrytím SUPI během rádiového přenosu
- Hierarchický návrh pro efektivní směrování AMF a škálovatelnost
- Podpora dynamického přepřidělení během mobility a předávání
- Integrace se síťovými řezy pro správu UE specifickou pro řez
- Snížení signalizační režie prostřednictvím lokálního řešení kontextu

## Související pojmy

- [AMF – Access and Mobility Management Function](/mobilnisite/slovnik/amf/)
- [GUAMI – Globally Unique AMF Identifier](/mobilnisite/slovnik/guami/)
- [5G-TMSI – 5G Temporary Mobile Subscription Identifier](/mobilnisite/slovnik/5g-tmsi/)

## Definující specifikace

- **TS 23.003** (Rel-19) — Numbering, addressing and identification in 3GPP
- **TS 23.501** (Rel-20) — 5G System Architecture Stage 2
- **TS 24.301** (Rel-19) — NAS protocol for Evolved Packet System
- **TS 24.501** (Rel-19) — 5G NAS Protocols Specification
- **TS 24.890** (Rel-16) — 5G NAS Protocol for 5GS Stage 3
- **TS 29.518** (Rel-19) — AMF Service Based Interface Protocol

---

📖 **Anglický originál a plná specifikace:** [5G-GUTI na 3GPP Explorer](https://3gpp-explorer.com/glossary/5g-guti/)
