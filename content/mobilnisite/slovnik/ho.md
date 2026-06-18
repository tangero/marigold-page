---
slug: "ho"
url: "/mobilnisite/slovnik/ho/"
type: "slovnik"
title: "HO – Home Operator"
date: 2025-01-01
abbr: "HO"
fullName: "Home Operator"
category: "Security"
segment: "Security"
canonical: "https://3gpp-explorer.com/glossary/ho/"
summary: "Home Operator (HO, domácí operátor) je primární poskytovatel mobilní sítě účastníka, odpovědný za autentizaci, účtování a poskytování služeb. Je to základní koncept v architekturách roamingu a zabezpe"
---

HO (domácí operátor) je primární poskytovatel mobilní sítě účastníka, odpovědný za autentizaci, účtování a poskytování služeb, což umožňuje roaming tím, že povoluje přístup ke službám prostřednictvím jiných navštívených operátorů.

## Popis

Home Operator (HO, domácí operátor) je klíčová administrativní a funkční entita v architekturách sítí 3GPP, která představuje mobilního síťového operátora, u kterého má účastník trvalé předplatné. Je ústřední autoritou pro identitu, přihlašovací údaje a služební profil účastníka. Primární role HO jsou vykonávány prostřednictvím jeho komponent jádra sítě, zejména Home Subscriber Server ([HSS](/mobilnisite/slovnik/hss/)) v 4G/5G Core nebo Home Location Register ([HLR](/mobilnisite/slovnik/hlr/)) ve starších systémech. Tyto databáze uchovávají hlavní kopii dat účastníka, včetně International Mobile Subscriber Identity ([IMSI](/mobilnisite/slovnik/imsi/)), autentizačních vektorů (klíčů a algoritmů), předplacených služeb a QoS profilů.

V bezpečnostních a mobilních procedurách je HO nezbytný. Při počátečním připojení k síti nebo při předání spojení (handover) do nové sítě musí obsluhující (navštívený) operátor uživatele autentizovat. Toho je dosaženo prostřednictvím protokolu autentizace a dohody o klíči ([AKA](/mobilnisite/slovnik/aka/)), kdy navštívená síť požaduje autentizační vektory od HSS HO. HO tyto vektory generuje pomocí sdíleného tajného klíče (K) jedinečného pro modul Universal Subscriber Identity Module ([USIM](/mobilnisite/slovnik/usim/)) účastníka. Tento proces zajišťuje, že pouze legitimní HO může ručit za identitu účastníka, což tvoří základ zabezpečení přístupu k síti a brání podvodům.

Kromě zabezpečení je HO klíčový pro poskytování služeb a správu mobility. Autorizuje služby, ke kterým může roamingový účastník přistupovat, na základě jeho předplatného profilu. V systému 5G interaguje Authentication Server Function (AUD) HO v rámci HSS se Security Anchor Function ([SEAF](/mobilnisite/slovnik/seaf/)) navštívené sítě za účelem správy primární autentizace. HO také hraje kritickou roli v zákonném odposlechu a zprostředkování účtování, generuje záznamy o účtování ([CDR](/mobilnisite/slovnik/cdr/)) za roamingové využití, které jsou vyrovnávány mezi operátory. Jeho architektonická role je definována v rozhraních jako S6a (mezi [MME](/mobilnisite/slovnik/mme/) a HSS) v 4G a Nudm (service-based interface UDM) v 5G, což usnadňuje bezpečné načítání a aktualizace dat.

## K čemu slouží

Koncept Home Operator existuje proto, aby umožnil bezpečnou a bezproblémovou mobilní komunikaci napříč různými administrativními síťovými doménami, primárně pro roaming. Před standardizovanými roamingovými dohodami a architekturami byli účastníci efektivně vázáni na fyzické pokrytí sítě svého poskytovatele. Model HO to řeší tím, že stanoví důvěryhodnou domácí autoritu, která může autentizovat a autorizovat přístup účastníka ke službám v cizí (navštívené) síti. Tím odděluje poskytování služeb od síťového přístupu, což je základem globální mobilní interoperability.

Historicky se potřeba konceptu HO stala akutní s nástupem GSM a touhou po mezinárodním roamingu. Řešil kritický problém, jak může navštívená síť, která nemá s účastníkem přímý vztah, uživateli důvěřovat a poskytovat služby. Řešením bylo centralizovat identitu účastníka a kryptografická tajemství u HO. Tato architektura také řeší obchodní a provozní problémy, jako je vyrovnání účtování mezi operátory a důsledné vynucování služebních politik bez ohledu na polohu uživatele. HO udržuje 'zlatý záznam' o předplatném, což zajišťuje, že změny služeb nebo jejich pozastavení jsou řízeny z jediného bodu.

V moderních sítích se účel rozšiřuje na podporu komplexních servisních architektur, jako je dělení sítě (network slicing) a edge computing v 5G. HO (prostřednictvím svého UDM) poskytuje data o předplatném, která určují, ke kterým síťovým řezům (slices) je uživateli povolen přístup, i když jsou tyto řezy vytvořeny v navštívené síti. HO tedy není jen bezpečnostní kotvou, ale také kotvou pro politiky a řízení služeb, což umožňuje flexibilní, službami řízenou architekturu současných 5G systémů při zachování robustního zabezpečení a komerčních rámců.

## Klíčové vlastnosti

- Vystupuje jako nejvyšší autorita pro autentizaci účastníka a správu bezpečnostních klíčů.
- Hostuje hlavní databázi účastníků (HSS/HLR/UDM) obsahující identitu, služební profily a přihlašovací údaje.
- Generuje a distribuuje autentizační vektory navštíveným sítím prostřednictvím zabezpečených rozhraní.
- Autorizuje přístup účastníka ke konkrétním službám a síťovým řezům (slices) během roamingu.
- Slouží jako kotva pro účtování a generování dat o poplatcích v roamingových scénářích.
- Umožňuje zákonný odposlech pro účastníky tím, že poskytuje údaje o identitě a službách příslušným orgánům.

## Související pojmy

- [HSS – Home Subscriber Server](/mobilnisite/slovnik/hss/)
- [UDM – Unified Data Management](/mobilnisite/slovnik/udm/)
- [IMSI – International Mobile Subscriber Identity](/mobilnisite/slovnik/imsi/)

## Definující specifikace

- **TS 33.401** (Rel-19) — EPS Security Architecture
- **TS 33.812** (Rel-9) — M2M Remote Subscription Management Security
- **TS 33.859** (Rel-11) — UTRAN Key Hierarchy Enhancement Study

---

📖 **Anglický originál a plná specifikace:** [HO na 3GPP Explorer](https://3gpp-explorer.com/glossary/ho/)
