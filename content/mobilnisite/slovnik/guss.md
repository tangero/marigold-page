---
slug: "guss"
url: "/mobilnisite/slovnik/guss/"
type: "slovnik"
title: "GUSS – GBA User Security Settings"
date: 2025-01-01
abbr: "GUSS"
fullName: "GBA User Security Settings"
category: "Security"
segment: "Security"
canonical: "https://3gpp-explorer.com/glossary/guss/"
summary: "GBA User Security Settings (GUSS) je bezpečnostní profil používaný v rámci architektury Generic Bootstrapping Architecture (GBA). Obsahuje uživatelsky specifické autentizační přihlašovací údaje a bezp"
---

GUSS je uživatelsky specifický bezpečnostní profil v rámci architektury Generic Bootstrapping Architecture, který obsahuje autentizační přihlašovací údaje a parametry a umožňuje zabezpečenou autentizaci mezi uživatelským zařízením (UE) a síťovými aplikačními servery.

## Popis

[GBA](/mobilnisite/slovnik/gba/) User Security Settings (GUSS) je kritická bezpečnostní datová struktura v rámci architektury Generic Bootstrapping Architecture ([GAA](/mobilnisite/slovnik/gaa/)) standardu 3GPP. GAA/GBA poskytuje mechanismus pro vzájemnou autentizaci a dohodu klíčů mezi uživatelským zařízením (UE) a síťovou aplikační funkcí ([NAF](/mobilnisite/slovnik/naf/)), přičemž využívá stávajícího zabezpečeného vztahu mezi UE a jeho domovskou sítí. GUSS je úložištěm uživatelsky specifických bezpečnostních materiálů a konfigurací potřebných pro tento bootstrapovací proces. Je bezpečně uložen ve funkci Bootstrapovacího serveru ([BSF](/mobilnisite/slovnik/bsf/)), což je centrální prvek sítě GBA zodpovědný za provádění bootstrapovacích procedur s UE.

GUSS je v podstatě profil přidružený k soukromé identitě uživatele (např. IMS Private User Identity – [IMPI](/mobilnisite/slovnik/impi/)). Jeho obsah je definován operátorem domovské sítě a může zahrnovat několik klíčových komponent. Primárně obsahuje sdílený tajný klíč (K) spojený s univerzální integrovanou obvodovou kartou uživatele (UICC) nebo softwarovými přihlašovacími údaji, který je kořenem důvěry. Kromě klíče obsahuje uživatelská bezpečnostní nastavení specifická pro GBA, jako je seznam podporovaných verzí GBA (např. GBA_[ME](/mobilnisite/slovnik/me/), GBA_U, GBA_Digest), životnosti klíčů a případně indikace specifické pro služby. BSF využívá informace v GUSS spolu s autentizačními vektory přijatými od Home Subscriber Server ([HSS](/mobilnisite/slovnik/hss/)) k provedení bootstrapovací procedury s UE.

Během běhu GBA bootstrapování se UE a BSF vzájemně autentizují pomocí přihlašovacích údajů odvozených z dat GUSS, typicky prostřednictvím protokolu [HTTP](/mobilnisite/slovnik/http/) Digest AKA. Po úspěšné autentizaci odvodí sdílený, na relaci specifický klíčový materiál (Ks). Klíčovou součástí tohoto odvozeného materiálu je klíč specifický pro NAF (Ks_NAF), který je následně poskytnut BSF žádajícímu NAF (např. serveru multimediální služby). UE nezávisle vypočítá stejný Ks_NAF. To umožňuje UE a NAF navázat zabezpečený kanál, aniž by NAF kdy znal dlouhodobé tajemství uživatele (K). GUSS tedy umožňuje zabezpečené rozšíření autentizace z jádra sítě (HSS/BSF) na více aplikačních serverů a tvoří základ pro možnosti typu single sign-on v servisní vrstvě 3GPP.

## K čemu slouží

GUSS byl vytvořen k řešení problému roztříštěné a těžkopádné autentizace pro přidané služby v mobilních sítích. Před GBA a GUSS musely aplikační servery (jako ty pro multimediální zprávy, služby přítomnosti nebo lokalizační služby) často udržovat vlastní samostatné uživatelské databáze a autentizační mechanismy. To vyžadovalo od uživatelů správu více přihlašovacích údajů, zvyšovalo provozní složitost pro operátory a vytvářelo bezpečnostní slabiny prostřednictvím množení přihlašovacích údajů. Potřeba byla využít silnou autentizaci založenou na SIM kartě mobilní sítě pro zabezpečení služeb na aplikační vrstvě.

Architektura Generic Bootstrapping Architecture (GBA) byla odpovědí a GUSS je její základní komponentou. Jejím účelem je centralizovat správu uživatelsky specifických bezpečnostních parametrů vyžadovaných pro GBA uvnitř domény důvěry sítě (BSF). Tento návrh umožňuje domovskému operátorovi udržovat kontrolu nad autentizačními politikami, silou klíčů a životnostmi přihlašovacích údajů. Odděluje zodpovědnost za základní autentizaci (řešenou BSF/HSS pomocí GUSS) od poskytování služeb (řešeného NAF).

Poskytnutím standardizovaného kontejneru pro tato nastavení GUSS umožňuje interoperabilitu a konzistentní vynucování zabezpečení napříč různými službami a dodavateli kompatibilními s GBA. Je klíčovým prvkem pro zabezpečený přístup ke službám v IMS a dalších službách založených na IP, což operátorům umožňuje nabízet bezproblémový a bezpečný uživatelský zážitek, kdy autentizace na síťové úrovni transparentně poskytuje přístup k sadě aplikací, což významně zvyšuje jak zabezpečení, tak použitelnost.

## Klíčové vlastnosti

- Ukládá uživatelsky specifický dlouhodobý tajný klíč (K) a parametry zabezpečení GBA ve funkci Bootstrapovacího serveru (BSF)
- Nezbytný pro bootstrapovací proceduru GBA mezi UE a BSF
- Obsahuje konfiguraci pro podporované varianty GBA (GBA_ME, GBA_U) a životnosti klíčů
- Umožňuje odvození relací specifických klíčů pro NAF (Ks_NAF) pro zabezpečený přístup na aplikační vrstvě
- Centralizuje správu zabezpečení pro operátora a zabraňuje množení přihlašovacích údajů
- Základní prvek pro poskytování možností single sign-on napříč různými aplikačními službami 3GPP

## Související pojmy

- [GBA – Generic Bootstrapping Architecture](/mobilnisite/slovnik/gba/)
- [BSF – Bootstrapping Server Function](/mobilnisite/slovnik/bsf/)
- [NAF – Network Application Function](/mobilnisite/slovnik/naf/)
- [AKA – Authentication and Key Agreement](/mobilnisite/slovnik/aka/)
- [IMPI – IP Multimedia CN subsystem Private Identity](/mobilnisite/slovnik/impi/)

## Definující specifikace

- **TS 24.109** (Rel-19) — HTTP Digest AKA & GAA Stage 3
- **TS 29.109** (Rel-19) — GAA Bootstrapping Interfaces (Zh, Dz, Zn, Zpn)
- **TS 29.309** (Rel-19) — Nbsp Service Based Interface for GBA BSF
- **TS 32.808** (Rel-8) — Common User Profile Storage Framework
- **TS 33.220** (Rel-19) — Generic Authentication Architecture (GAA); Generic Bootstrapping Architecture (GBA)
- **TS 33.223** (Rel-19) — GBA Push Function Specification
- **TS 33.804** (Rel-12) — Non-UICC SSO using SIP Digest credentials
- **TR 33.924** (Rel-19) — GBA-OpenID Interworking Specification
- **TR 33.980** (Rel-19) — GAA & Liberty Alliance Interworking Guidelines

---

📖 **Anglický originál a plná specifikace:** [GUSS na 3GPP Explorer](https://3gpp-explorer.com/glossary/guss/)
