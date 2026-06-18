---
slug: "scm-s"
url: "/mobilnisite/slovnik/scm-s/"
type: "slovnik"
title: "SCM-S – SEAL Configuration Management Server"
date: 2025-01-01
abbr: "SCM-S"
fullName: "SEAL Configuration Management Server"
category: "Management"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/scm-s/"
summary: "SCM-S je síťová funkce, která spravuje konfiguraci klientů SEAL (Service Enabler Architecture Layer). Je zodpovědná za zřizování, aktualizaci a údržbu konfiguračních dat služeb, která potřebují aplika"
---

SCM-S je SEAL Configuration Management Server (server správy konfigurace SEAL), síťová funkce, která spravuje konfiguraci klientů SEAL prostřednictvím zřizování, aktualizace a údržby jejich konfiguračních dat služeb.

## Popis

[SEAL](/mobilnisite/slovnik/seal/) Configuration Management Server (SCM-S) je klíčová komponenta v rámci architektury 3GPP Service Enabler Architecture Layer (SEAL), standardizovaná od Release 16. Funguje jako centralizované úložiště konfigurace a řídicí entita pro klienty SEAL, kterými jsou typicky aplikační servery nebo uživatelská zařízení (UE) využívající běžné síťové služby, jako je správa identity, správa skupin nebo samotná správa konfigurace. SCM-S ukládá a poskytuje specifická konfigurační data, známá jako SEAL Configuration Data ([SCD](/mobilnisite/slovnik/scd/)), autorizovaným klientům SEAL. Tato data zahrnují parametry potřebné pro to, aby klient mohl objevovat a komunikovat s dalšími službami SEAL, jako jsou koncové adresy, podporované verze služeb a bezpečnostní politiky.

Architektonicky je SCM-S definován jako síťová funkce, která vystavuje severovýchodní [API](/mobilnisite/slovnik/api/) specifikované v 3GPP TS 24.257 pro správu konfigurace. Interaguje s Network Exposure Function ([NEF](/mobilnisite/slovnik/nef/)) nebo přímo s aplikačními funkcemi v závislosti na modelu nasazení. Server ověřuje a autorizuje konfigurační požadavky od klientů SEAL na základě síťových politik. Spravuje životní cyklus konfiguračních dat a podporuje operace jako vytváření, načítání, úpravy a mazání SCD. SCM-S zajišťuje, že klienti dostávají konzistentní a aktuální konfiguraci, což je klíčové pro spolehlivý provoz služeb postavených na architektuře SEAL.

Jeho provoz využívá mechanismus požadavek-odpověď. Klient SEAL při inicializaci nebo když jeho konfigurace zastará, odešle požadavek na SCM-S. Požadavek obsahuje identitu klienta a typ požadovaných konfiguračních dat. SCM-S požadavek ověří, načte příslušná SCD ze své databáze a vrátí je klientovi ve standardizovaném formátu. Server může také proaktivně zasílat aktualizace konfigurace klientům v případě změn v síti. Oddělením aplikační logiky od parametrů konfigurace SCM-S zjednodušuje nasazení služeb, zvyšuje škálovatelnost a zajišťuje, že změny konfigurace lze efektivně šířit po síti bez nutnosti aktualizovat jednotlivé klientské aplikace.

## K čemu slouží

SCM-S byl zaveden, aby řešil rostoucí složitost správy konfigurace pro síťově vystavené služby, zejména s nástupem 5G a potřebou standardizovaných služeb. Před [SEAL](/mobilnisite/slovnik/seal/) aplikace komunikující se síťovými schopnostmi často spoléhaly na proprietární nebo ad-hoc metody konfigurace, což vedlo k problémům s integrací, nekonzistentnímu chování a vysoké provozní zátěži. Nedostatek jednotného mechanismu správy konfigurace ztěžoval nasazování, aktualizaci a škálování služeb napříč různými operátory a dodavateli.

Vznik SCM-S byl motivován prací 3GPP na společných službách v Release 16, jejímž cílem bylo poskytnout opakovaně použitelné stavební bloky pro aplikace. Řeší problém, jak efektivně a bezpečně distribuovat potřebné parametry připojení a politik různorodým klientům SEAL. Centralizací správy konfigurace zajišťuje, že všichni klienti pracují se správnými parametry, což snižuje chyby a chybné konfigurace. To je obzvláště důležité v prostředích s více dodavateli a pro scénáře edge computingu, kde je třeba služby dynamicky orchestraovat.

Historicky byla konfigurace často pevně zakódována nebo spravována prostřednictvím operátorsky specifických systémů zřizování, které nebyly navrženy pro agilní, [API](/mobilnisite/slovnik/api/) řízené interakce vyžadované moderními aplikacemi. SCM-S poskytuje standardizované webové rozhraní (RESTful API), které je v souladu s principy cloud-nativních aplikací. Umožňuje automatizaci, podporuje zřizování bez zásahu obsluhy a usnadňuje správu životního cyklu síťově vystavených služeb, čímž urychluje inovace služeb a snižuje čas uvedení nových nabídek na trh.

## Klíčové vlastnosti

- Centralizované úložiště pro SEAL Configuration Data (SCD)
- Standardizované severovýchodní RESTful API pro správu konfigurace (TS 24.257)
- Podpora CRUD operací (vytvořit, načíst, aktualizovat, smazat) nad konfiguračními daty
- Ověřování a autorizace požadavků klientů SEAL
- Schopnost proaktivního zasílání konfigurace pro dynamické aktualizace
- Odděluje aplikační logiku od konfiguračních parametrů pro agilní nasazení

## Související pojmy

- [SEAL – Service Enabler Architecture Layer for Verticals](/mobilnisite/slovnik/seal/)
- [NEF – Network Exposure Function](/mobilnisite/slovnik/nef/)
- [SCD – Signal Conditioning Device](/mobilnisite/slovnik/scd/)

## Definující specifikace

- **TS 24.257** (Rel-19) — UAS Application Enabler (UAE) Layer
- **TS 24.546** (Rel-19) — SEAL Configuration Management Protocol Specification

---

📖 **Anglický originál a plná specifikace:** [SCM-S na 3GPP Explorer](https://3gpp-explorer.com/glossary/scm-s/)
