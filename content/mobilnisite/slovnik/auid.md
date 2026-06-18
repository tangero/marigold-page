---
slug: "auid"
url: "/mobilnisite/slovnik/auid/"
type: "slovnik"
title: "AUID – Application Unique IDentity"
date: 2025-01-01
abbr: "AUID"
fullName: "Application Unique IDentity"
category: "Identifier"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/auid/"
summary: "AUID je globálně jednoznačný identifikátor pro aplikace v sítích 3GPP, standardizovaný pro umožnění bezpečného zjišťování, registrace a vyvolávání služeb aplikací. Poskytuje standardizovaný adresní me"
---

AUID je globálně jednoznačný identifikátor, standardizovaný v sítích 3GPP, který umožňuje aplikacím jejich bezpečné zjišťování, registraci a vyvolávání služeb napříč různými prostředími operátorů.

## Popis

Application Unique IDentity (AUID) je základní identifikátor definovaný v architektuře vrstvy služeb 3GPP, konkrétně v rámci Open Service Access ([OSA](/mobilnisite/slovnik/osa/)) a pozdějších funkcí pro vystavování schopností sítě. Slouží jako trvalý, globálně jednoznačný název aplikace, který je nezávislý na fyzickém umístění aplikace, instanci jejího nasazení nebo konkrétním síťovém uzlu, který ji hostuje. AUID je klíčovou součástí pro registraci aplikací, jejich zjišťování a bezpečné vyvolávání služeb v prostředí sítě 3GPP.

Z architektonického hlediska je AUID spravován a využíván Serverem schopností služeb ([SCS](/mobilnisite/slovnik/scs/)) nebo Aplikačním serverem ([AS](/mobilnisite/slovnik/as/)) a síťovou funkcí pro vystavování služeb, historicky OSA Gateway (OSA-GW) nebo modernější Network Exposure Function ([NEF](/mobilnisite/slovnik/nef/)). Když se chce aplikace zaregistrovat v síti za účelem využívání síťových schopností (jako je odeslání [SMS](/mobilnisite/slovnik/sms/), dotaz na polohu uživatele nebo zahájení hovoru), předloží svůj AUID jako součást registrační procedury. Vrstva služeb sítě používá tento AUID k jednoznačné identifikaci aplikační entity ve všech následných interakcích. AUID není adresou pro směrování zpráv; jedná se spíše o logický název používaný pro identifikaci, autorizaci a asociaci se servisní logikou. Během registrační relace aplikace je typicky svázán s fyzickou adresou koncového bodu (např. IP adresou a portem).

Struktura a formát AUID jsou definovány tak, aby zajišťovaly globální jednoznačnost. Často se řídí hierarchickým schématem pojmenování, podobným [URI](/mobilnisite/slovnik/uri/) nebo jménu založenému na doméně, které může zahrnovat prvky identifikující poskytovatele aplikace, název aplikace a případně i identifikátor verze. Tento strukturovaný formát umožňuje federovanou správu a zabraňuje kolizím. Uvnitř sítě je AUID klíčem používaným v databázích politik k určení, ke kterým síťovým službám a aplikačním rozhraním ([API](/mobilnisite/slovnik/api/)) má aplikace autorizovaný přístup, jaké úrovně kvality služby může požadovat a jaké zpoplatňovací modely se uplatňují. Jeho role je tedy klíčová pro bezpečnostní, správní a komerční aspekty nabídek sítě jako služby.

Při provozu se AUID používá v celém životním cyklu aplikace. Při počátečním uzavření servisní smlouvy mezi poskytovatelem aplikace a síťovým operátorem je AUID přidělen. Aplikace poté tento AUID používá ve veškeré signalizaci s vystavující vrstvou sítě. Například když aplikace odešle požadavek `sendSms` přes Parlay X API, je AUID zahrnuto v hlavičce zprávy. Síťová brána ověří, že poskytnutý AUID odpovídá aktivní, autorizované relaci aplikace, než požadavek zpracuje. Tento mechanismus brání neautorizovaným aplikacím, aby se vydávaly za legitimní, a tvoří základ pro přesné zaznamenávání využití služeb a jejich zpoplatnění.

## K čemu slouží

AUID byl vytvořen, aby vyřešil základní problém jednoznačné identifikace a správy aplikací třetích stran standardizovaným a bezpečným způsobem v telekomunikačních sítích. Před jeho standardizací používali různí výrobci a operátoři proprietární mechanismy, což vedlo k fragmentaci, bránilo přenositelnosti aplikací a komplikovalo bezpečnostní modely. Aplikace napsaná pro síť jednoho operátora nemohla být snadno nasazena v síti jiného bez výrazných úprav kvůli odlišným schématům identifikace a autentizace.

Zavedení AUID, zejména v rámci 3GPP Open Service Access ([OSA](/mobilnisite/slovnik/osa/)) ve vydání 6, bylo klíčovým kamenem přechodu k otevřeným, programovatelným sítím. Umožnilo vizi, že síťové schopnosti jsou vystavovány jako znovupoužitelné, zjistitelné služby. AUID poskytuje potřebný ukotvující bod pro implementaci konzistentních bezpečnostních politik na úrovni aplikací, správu smluv o úrovni služeb (SLA) a umožňuje přesné účtování za spotřebu API. Bez globálně jednoznačného identifikátoru aplikace by nebylo možné spolehlivě sledovat, která aplikace iniciovala síťovou akci, což by vedlo k bezpečnostním slabinám, nepřesnostem v účtování a neschopnosti vynucovat politiky spravedlivého využívání.

Dále AUID podporuje nezbytné provozní procesy, jako je správa životního cyklu aplikace (registrace, zrušení registrace, aktualizace) a správa poruch. Umožňuje síťovým operátorům zablokovat nebo pozastavit konkrétní problematické aplikace bez dopadu na ostatní. V podstatě AUID přeměnil aplikace z neprůhledných externích entit na plnohodnotné, identifikovatelné a spravovatelné subjekty v rámci domény služeb operátora, což byla nezbytná podmínka pro úspěšnou komercializaci síťových API a ekosystému vývojářů aplikací třetích stran.

## Klíčové vlastnosti

- Globálně jednoznačný identifikátor pro aplikace, zajišťující absenci konfliktů v pojmenování
- Umožňuje bezpečnou registraci a autentizaci aplikací u síťových vrstev služeb
- Slouží jako klíč pro vynucování politik, autorizaci a řízení přístupu k síťovým API
- Umožňuje přesné účtování a fakturaci díky jednoznačnému označení servisních požadavků jejich zdrojovou aplikací
- Podporuje přenositelnost aplikací napříč různými síťovými prostředími operátorů díky standardizovanému identifikačnímu schématu
- Nezbytný pro správu životního cyklu aplikace, včetně zjišťování, aktivace a vyřazení

## Definující specifikace

- **TS 24.141** (Rel-19) — Presence Service Protocol Details
- **TS 24.423** (Rel-8) — PSTN/ISDN Simulation Services XCAP Protocol
- **TS 24.484** (Rel-19) — MCS Configuration Management
- **TS 24.623** (Rel-19) — XCAP Protocol for Supplementary Services
- **TS 24.841** (Rel-6) — Presence Service IP Multimedia Subsystem
- **TS 32.808** (Rel-8) — Common User Profile Storage Framework

---

📖 **Anglický originál a plná specifikace:** [AUID na 3GPP Explorer](https://3gpp-explorer.com/glossary/auid/)
