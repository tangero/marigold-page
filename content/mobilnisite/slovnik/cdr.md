---
slug: "cdr"
url: "/mobilnisite/slovnik/cdr/"
type: "slovnik"
title: "CDR – Call Detail Record"
date: 2025-01-01
abbr: "CDR"
fullName: "Call Detail Record"
category: "Management"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/cdr/"
summary: "Strukturovaný záznam dat generovaný síťovými prvky za účelem dokumentace podrobností o telekomunikační služební události, jako je hlasový hovor, SMS nebo datová relace. Je základní jednotkou pro faktu"
---

CDR je strukturovaný záznam dat generovaný síťovým prvkem za účelem dokumentace služební události, jako je hovor nebo datová relace, a slouží jako základní jednotka pro fakturaci, účtování a analýzu provozu v sítích 3GPP.

## Popis

Call Detail Record (CDR) je standardizovaný, strojově čitelný záznam, který zachycuje klíčové parametry události využití služby v síti 3GPP. Nejde o jediný monolitický záznam, ale o rodinu typů záznamů definovaných pro různé služby (např. [MOC](/mobilnisite/slovnik/moc/), [MTC](/mobilnisite/slovnik/mtc/), SMS-MO, SMS-MT, [GPRS](/mobilnisite/slovnik/gprs/)) a generovaných různými síťovými funkcemi. Základní síťové prvky zodpovědné za správu relací a přenosových drah, jako je [MSC](/mobilnisite/slovnik/msc/) Server pro přepojování okruhů, SGSN a GGSN pro GPRS, nebo [MME](/mobilnisite/slovnik/mme/), SGW a PGW v EPC, jsou primárními generátory CDR. Tyto uzly shromažďují relevantní informace v reálném čase během instance služby a formátují je podle přísných specifikací definovaných v 3GPP TS 32.250 a souvisejících dokumentech.

Architektura generování a zpracování CDR zahrnuje několik klíčových komponent. Funkce spouštění účtování (Charging Trigger Function, [CTF](/mobilnisite/slovnik/ctf/)), integrovaná v síťovém prvku (např. MSC, PGW), detekuje zpoplatnitelné události a sestaví příslušné účtovací informace do záznamu účtovacích dat (Charging Data Record). Tento CDR je následně předán přes standardizované rozhraní (jako Ga nebo Rf) k funkci účtovacích dat (Charging Data Function, [CDF](/mobilnisite/slovnik/cdf/)) při offline účtování, nebo k systému online účtování (Online Charging System, [OCS](/mobilnisite/slovnik/ocs/)) v reálných scénářích. Samotný CDR obsahuje četná pole, včetně, ale ne pouze: identifikátorů obsluhované strany (MSISDN, IMSI), identity obsluhující sítě, datum a časová razítka začátku a konce relace, doby trvání, objemů dat (vzestupný/sestupný směr), použitých parametrů QoS a identifikátorů konkrétní použité služby. Pro scénáře roamingu bude CDR obsahovat také identifikátory navštívené a domovské PLMN.

Jeho role sahá daleko za prosté fakturace. CDR jsou primárním zdrojem pro systémy následného zpracování, které provádějí mediaci fakturace, detekci podvodů, vypořádání mezisíťových hovorů s jinými operátory a podrobnou analýzu provozu. Formát a obsah CDR se významně vyvinul od jednoduchých záznamů o hovorech s přepojováním okruhů ke komplexním záznamům zahrnujícím IMS relace, VoLTE hovory a hromadné transakce dat IoT. Standardizace zajišťuje interoperabilitu mezi síťovými zařízeními různých dodavatelů a mezi operátory pro vypořádání roamingu. Zpracování CDR zahrnuje sběr, korelaci (např. párování počátečního záznamu s odpovídajícím koncovým záznamem), formátování pro konkrétní fakturační systémy a bezpečné archivování, což tvoří páteř podnikového podpůrného systému (BSS) operátora.

## K čemu slouží

CDR existuje za účelem poskytnutí přesného, ověřitelného a standardizovaného záznamu o využití služeb, který je nepostradatelný pro komerční telekomunikační provoz. Jeho primárním účelem je umožnit fakturaci a účtování, tedy transformaci spotřeby síťových zdrojů na zpoplatnitelné události pro účastníky (postpaid) nebo pro řízení kreditu v reálném čase (prepaid). Bez CDR by operátoři neměli žádný objektivní mechanismus, jak služby účtovat, což by komerční mobilní sítě činilo finančně neudržitelnými. Řeší základní problém měření využití sítě v prostředí s více dodavateli a více operátory.

Historicky tento koncept předchází 3GPP a pochází z pevné telefonie (jak odkazuje ITU-T). V raných mobilních sítích se potřeba stala ještě kritičtější kvůli mobilitě, roamingu a širšímu spektru služeb mimo prosté hlasové hovory. Omezení proprietárních, nestandardizovaných mechanismů protokolování byla významnou překážkou interoperability, zejména pro roaming, kde musí domovský operátor účtovat svému účastníkovi na základě záznamů generovaných navštívenou zahraniční sítí. Standardizace formátů CDR, pravidel jejich generování a přenosových protokolů v rámci 3GPP poskytla tento nezbytný společný jazyk.

CDR dále řeší provozní a obchodně-inteligentní problémy přesahující čistou fakturaci. Poskytují surová data pro inženýring provozu, plánování sítě, správu podvodů (detekcí neobvyklých vzorců volání) a dodržování regulatorních požadavků (např. protokolování pro legální odposlech). Vývoj CDR směrem k zahrnutí podrobných parametrů QoS, informací o poloze a atributů specifických pro služby umožňuje operátorům implementovat sofistikované tarifní plány, záruky kvality služeb a nové obchodní modely, což z nich činí základní kámen jak správy sítě, tak obchodních operací.

## Klíčové vlastnosti

- Standardizovaný formát pro interoperabilitu mezi dodavateli a operátory
- Generování spouštěné zpoplatnitelnými událostmi (začátek/ukončení relace, dosažení prahové hodnoty objemu)
- Obsahuje komplexní data o službě (identity, časová razítka, doba trvání, objemy, QoS)
- Podporuje scénáře offline (fakturace po události) i online (účtování v reálném čase)
- Nezbytný pro fakturaci roamingu a vypořádání mezisíťových hovorů
- Slouží jako primární zdroj dat pro mediaci fakturace, detekci podvodů a analýzu provozu

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 22.115** (Rel-19) — Service Aspects; Charging and Billing
- **TS 22.121** (Rel-5) — Virtual Home Environment Requirements
- **TS 22.234** (Rel-13) — 3GPP-WLAN Interworking Index Specification
- **TR 22.950** (Rel-19) — Feasibility Study on Priority Service
- **TR 22.976** (Rel-2) — Release 2000 Services Overview
- **TS 23.039** (Rel-5) — SMSC to SME Interface Protocols
- **TS 23.060** (Rel-19) — GPRS Service Description Stage 2
- **TS 23.125** (Rel-7) — Flow Based Charging Architecture
- **TS 23.140** (Rel-6) — MMS Non-Realtime Service Definition
- **TS 23.167** (Rel-19) — IMS Emergency Sessions
- **TS 23.218** (Rel-19) — IMS Call Model Specification
- **TS 23.222** (Rel-19) — Common API Framework for 3GPP Northbound APIs
- **TS 23.228** (Rel-19) — IMS Stage-2 Service Description
- **TS 23.682** (Rel-19) — 3GPP TS 23682: MTC Architecture Enhancements
- … a dalších 35 specifikací

---

📖 **Anglický originál a plná specifikace:** [CDR na 3GPP Explorer](https://3gpp-explorer.com/glossary/cdr/)
