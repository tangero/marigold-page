---
slug: "s-smt-cdr"
url: "/mobilnisite/slovnik/s-smt-cdr/"
type: "slovnik"
title: "S-SMT-CDR – SGSN delivered Short message Mobile Terminated – Charging Data Record"
date: 2025-01-01
abbr: "S-SMT-CDR"
fullName: "SGSN delivered Short message Mobile Terminated – Charging Data Record"
category: "Management"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/s-smt-cdr/"
summary: "Záznam o účtovaných datech (Charging Data Record) generovaný SGSN pro doručení SMS zprávy (mobile-terminated). Poskytuje potřebná data pro účtování a účetní účely, zachycuje podrobnosti pokusu o doruč"
---

S-SMT-CDR je záznam o účtovaných datech (Charging Data Record) generovaný SGSN pro účtování doručené SMS zprávy (mobile-terminated), který zachycuje podrobnosti jako stav úspěchu či neúspěchu pokusu o doručení pro zajištění příjmů operátora.

## Popis

S-SMT-CDR ([SGSN](/mobilnisite/slovnik/sgsn/) delivered Short message Mobile Terminated – Charging Data Record) je standardizovaný datový záznam definovaný v rámci architektury účtování 3GPP. Generuje jej Serving [GPRS](/mobilnisite/slovnik/gprs/) Support Node (SGSN) v paketově spínané síti 2G/3G při zpracování doručení [SMS](/mobilnisite/slovnik/sms/) zprávy (SMS-MT) účastníkovi. Tento záznam je specifickým typem Charging Data Record ([CDR](/mobilnisite/slovnik/cdr/)), který tvoří část systému offline účtování (Offline Charging System, [OFCS](/mobilnisite/slovnik/ofcs/)). Jeho vytvoření je spuštěno specifickými událostmi v procesu doručení SMS, jako je úspěšné předání zprávy mobilní stanici nebo selhání doručení. SGSN, který vystupuje jako funkce spouštějící účtování (Charging Trigger Function, [CTF](/mobilnisite/slovnik/ctf/)), shromažďuje relevantní informace o události, formátuje je dle specifikací v 3GPP TS 32.251 a TS 32.272 a předává S-SMT-CDR funkci pro sběr účtovacích dat (Charging Data Function, [CDF](/mobilnisite/slovnik/cdf/)) přes referenční bod Ga.

Architektura pro generování S-SMT-CDR je integrována do účtovacích funkcí SGSN. Když pro účastníka dorazí SMS-MT, SGSN komunikuje přes rozhraní Gd s Mobile Switching Centre ([MSC](/mobilnisite/slovnik/msc/)) a SMS Gateway MSC (SMS-GMSC) pro doručení SMS přes síť GPRS. Během tohoto postupu SGSN identifikuje parametry relevantní pro účtování. Mezi ně patří identita obslužného uzlu (adresa SGSN), identifikátor účastníka (např. IMSI, MSISDN), adresa odesílatele SMS, čas pokusu o doručení, příčina ukončení záznamu (např. úspěšné doručení, důvod selhání) a ukazatele objemu dat související s přenosem signalizační zprávy. Tato data jsou zkompilována do CDR se specifickým identifikátorem typu záznamu.

S-SMT-CDR hraje klíčovou roli v systému účtování operátora. Po vygenerování je přenesen do fakturační domény sítě. Zde je použit pro aplikaci příslušného tarifu za službu SMS-MT, který se může lišit na základě tarifního plánu účastníka, původu zprávy (např. tuzemská, mezinárodní) nebo politiky sítě. Záznam poskytuje auditovatelnou stopu pro každou fakturační událost, což umožňuje fakturaci zákazníkům, vypořádání mezi operátory (pokud zpráva pocházela z jiné sítě) a zajištění příjmů korelací poskytnutí služby s vygenerovanými poplatky. Jeho standardizovaný formát zajišťuje interoperabilitu mezi síťovými prvky různých výrobců a fakturačními systémy operátora.

## K čemu slouží

S-SMT-CDR byl zaveden, aby poskytl standardizovaný a spolehlivý mechanismus pro účtování mobilních SMS zpráv (mobile-terminated) doručovaných přes paketově spínanou páteřní síť GPRS (prostřednictvím SGSN). Před zavedením standardizovaných účtovacích záznamů čelili operátoři výzvám v přesném účtování za datové služby, včetně SMS přes GPRS, což mohlo vést k úniku příjmů nebo fakturačním sporům. Vytvoření specifických typů CDR pro různé scénáře služeb bylo klíčovou součástí snahy 3GPP definovat komplexní a flexibilní účtovací rámec (Charging and Billing) pro všechny síťové služby.

Jeho účelem je řešit problém služebně specifického účtování v rámci paketově spínané domény. Zatímco hovory v okruhově spínaných sítích měly dobře zavedené účtovací modely, vzestup paketových služeb, jako je SMS přes GPRS, vyžadoval nové datové struktury pro zachycení jedinečných atributů těchto transakcí. S-SMT-CDR to řeší přesným zaznamenáním pokusu o doručení SMS-MT, včetně stavu úspěchu/selhání, což je zásadní pro spravedlivé a přesné účtování. Umožňuje operátorům implementovat složité tarifní modely, podporovat předplacené účtování prostřednictvím integrace se systémy online účtování a generovat podrobné zákaznické faktury. Motivací byla komerční nutnost monetizovat rychle rostoucí službu SMS a zajistit konzistentní přístup k účtování napříč nasazeními sítí od více výrobců.

## Klíčové vlastnosti

- Generován SGSN pro události doručení mobilní SMS zprávy (mobile-terminated)
- Standardizovaný formát dle 3GPP TS 32.251 a TS 32.272
- Obsahuje klíčová pole jako IMSI, MSISDN, adresa odesílatele, časová značka události a příčina ukončení
- Používá se pro offline účtování a fakturační vyrovnání
- Podporuje vypořádání mezi operátory pro SMS mezi sítěmi
- Poskytuje auditovatelnou stopu pro zajištění příjmů a správu podvodů

## Související pojmy

- [SGSN – Serving GPRS Support Node](/mobilnisite/slovnik/sgsn/)

## Definující specifikace

- **TS 32.251** (Rel-19) — PS Domain Charging Management
- **TS 32.272** (Rel-19) — Charging for Push-to-Talk over Cellular (PoC)

---

📖 **Anglický originál a plná specifikace:** [S-SMT-CDR na 3GPP Explorer](https://3gpp-explorer.com/glossary/s-smt-cdr/)
