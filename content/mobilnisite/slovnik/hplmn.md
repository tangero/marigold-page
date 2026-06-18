---
slug: "hplmn"
url: "/mobilnisite/slovnik/hplmn/"
type: "slovnik"
title: "HPLMN – Home Public Land Mobile Network"
date: 2025-01-01
abbr: "HPLMN"
fullName: "Home Public Land Mobile Network"
category: "Identifier"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/hplmn/"
summary: "Mobilní síť, ve které jsou uložena trvalá předplatitelská data účastníka. Je to 'domovská' síť účastníka, klíčová pro autentizaci, účtování a poskytování služeb. Umožňuje roaming tím, že odlišuje domo"
---

HPLMN je domovská mobilní síť účastníka, ve které jsou uložena jeho trvalá předplatitelská data pro autentizaci, účtování a poskytování služeb, což umožňuje roaming tím, že ji odlišuje od navštívených sítí.

## Popis

Domovská veřejná pozemní mobilní síť (Home Public Land Mobile Network – HPLMN) je základním konceptem v mobilních telekomunikacích, který identifikuje operátora sítě, u kterého má účastník trvalý smluvní předplatný vztah. Je to klíčový identifikátor v rámci mezinárodního identifikátoru mobilního účastníka (International Mobile Subscriber Identity – [IMSI](/mobilnisite/slovnik/imsi/)), který je uložen na univerzální integrovaném obvodu účastníka (Universal Integrated Circuit Card – UICC) neboli [SIM](/mobilnisite/slovnik/sim/) kartě. IMSI je strukturován jako mobilní kód země (Mobile Country Code – [MCC](/mobilnisite/slovnik/mcc/)), mobilní kód sítě (Mobile Network Code – [MNC](/mobilnisite/slovnik/mnc/)) a identifikační číslo mobilního účastníka (Mobile Subscriber Identification Number – [MSIN](/mobilnisite/slovnik/msin/)). Kombinace MCC a MNC v rámci IMSI jednoznačně identifikuje HPLMN. Tento identifikátor je ústřední pro provoz sítě, protože je to první informace použitá ke směrování požadavků na autentizaci a autorizaci, když se mobilní zařízení připojí k jakékoli síti, ať už v domovské síti nebo při roamingu.

Z architektonického hlediska HPLMN hostuje kritické síťové funkce, které spravují trvalý profil účastníka. Primárním úložištěm je server předplatitelů domovské sítě (Home Subscriber Server – [HSS](/mobilnisite/slovnik/hss/)) v 4G/5G jádrech sítí nebo domovský registr polohy (Home Location Register – [HLR](/mobilnisite/slovnik/hlr/)) v 2G/3G sítích. Tyto databáze uchovávají hlavní kopii dat účastníka včetně přihlašovacích údajů pro autentizaci (klíče Ki), profilů služeb a stavu předplatného. Když se uživatel připojí k síti, obsluhující síť (kterou může být sama HPLMN nebo navštívená [PLMN](/mobilnisite/slovnik/plmn/) – VPLMN) extrahuje identifikátor HPLMN z IMSI. Pokud se zařízení nenachází v HPLMN, obsluhující síť použije signalizační protokoly (jako MAP nebo Diameter) ke kontaktování HSS/HLR v HPLMN za účelem autentizace uživatele a načtení jeho servisního profilu.

Role HPLMN přesahuje rámec počáteční autentizace. Je to kotvící bod pro správu mobility, který zajišťuje plynulou kontinuitu služeb při pohybu uživatele. Pro účtování je zodpovědná za generování záznamů podrobností o hovorech (Call Detail Records – CDR) pro své účastníky, a to i za využití, ke kterému dojde v jiných sítích, prostřednictvím roamingových dohod. Pro pokročilé služby, jako je hlas přes LTE (Voice over LTE – VoLTE) nebo IP multimediální podsystém (IP Multimedia Subsystem – IMS), poskytuje IMS jádro HPLMN a aplikační servery definitivní konfiguraci služeb účastníka. Koncept HPLMN je tedy neoddělitelný od architektury roamingu, neboť umožňuje globální interoperabilitu tím, že poskytuje důvěryhodnou domovskou kotvu pro každé mobilní předplatné.

## K čemu slouží

Koncept HPLMN byl vytvořen, aby pro každého mobilního účastníka stanovil jasnou, jednoznačnou domovskou autoritu, což je předpokladem pro umožnění bezpečného a účtovatelného roamingu mezi různými síťovými operátory. Před standardizovaným roamingem byli účastníci efektivně vázáni na pokrytí jediné sítě. HPLMN jako globálně jedinečný identifikátor vložený do SIM karty umožňuje jakékoli kompatibilní síti na světě identifikovat domovského operátora účastníka a navázat s ním bezpečné signalizační spojení pro autentizaci a autorizaci. Tím byl vyřešen kritický problém důvěry mezi nezávislými operátory, což jim umožnilo nabízet služby návštěvníkům, a zároveň zajistit, že domovská síť si zachová kontrolu nad platností předplatného a účtováním.

HPLMN navíc poskytuje architektonický základ pro centralizovanou správu účastníků. Kotvením definitivních dat účastníka v domovské síti zjednodušuje poskytování služeb a jejich aktualizace. Operátoři mohou upravit servisní profil účastníka (např. přidání datového tarifu) v jednom centrálním HSS/HLR a tyto změny jsou platné bez ohledu na to, kde se účastník fyzicky nachází. Tento centralizovaný model také usnadňuje implementaci konzistentních servisních politik, jako jsou rodičovské kontroly nebo úrovně služeb pro podniky, které jsou vynucovány na základě profilu načteného z HPLMN. Koncept se vyvinul od základního roamingu v okruhově spínaných sítích 2G až po podporu komplexních IP služeb v sítích 4G a 5G, ale jeho základní účel jako kotvy předplatného zůstává nezměněn.

## Klíčové vlastnosti

- Jednoznačně identifikována kombinací MCC a MNC v IMSI účastníka
- Hostuje hlavní databázi účastníků (HLR/HSS) obsahující autentizační klíče a servisní profily
- Slouží jako kotvící bod pro autentizaci a autorizaci účastníků, a to lokálně i při roamingu
- Centrální bod pro generování záznamů pro účtování (CDR) za aktivitu účastníka napříč všemi sítěmi
- Umožňuje globální roaming tím, že poskytuje důvěryhodnou domovskou síť pro signalizaci mezi operátory
- Kotví poskytování služeb pro IMS a další pokročilé služby na základě domovského předplatného

## Související pojmy

- [IMSI – International Mobile Subscriber Identity](/mobilnisite/slovnik/imsi/)
- [VPLMN – Visited Public Land Mobile Network](/mobilnisite/slovnik/vplmn/)
- [HSS – Home Subscriber Server](/mobilnisite/slovnik/hss/)
- [HLR – Home Location Register](/mobilnisite/slovnik/hlr/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 22.234** (Rel-13) — 3GPP-WLAN Interworking Index Specification
- **TS 22.811** (Rel-7) — Network Selection Mechanisms Overview
- **TR 22.980** (Rel-19) — Network Composition Feasibility Study
- **TS 23.078** (Rel-19) — CAMEL Phase 4 Stage 2 Specification
- **TS 23.110** (Rel-19) — Access Stratum Services Specification
- **TS 23.125** (Rel-7) — Flow Based Charging Architecture
- **TS 23.171** (Rel-4) — LCS Stage 2 Specification for UMTS
- **TS 23.218** (Rel-19) — IMS Call Model Specification
- **TS 23.226** (Rel-19) — Global Text Telephony (GTT) Stage 2
- **TS 23.234** (Rel-13) — 3GPP-WLAN Interworking Index
- **TS 23.240** (Rel-19) — 3GPP Generic User Profile (GUP) Architecture
- **TS 23.271** (Rel-19) — LCS Stage 2 Specification
- **TS 23.278** (Rel-19) — CAMEL for IMS Stage 2 Specification
- **TS 23.722** (Rel-15) — Common API Framework (CAPIF) for 3GPP Northbound APIs
- … a dalších 37 specifikací

---

📖 **Anglický originál a plná specifikace:** [HPLMN na 3GPP Explorer](https://3gpp-explorer.com/glossary/hplmn/)
