---
slug: "mecn"
url: "/mobilnisite/slovnik/mecn/"
type: "slovnik"
title: "MECN – Monitoring Event Charging Node"
date: 2025-01-01
abbr: "MECN"
fullName: "Monitoring Event Charging Node"
category: "Management"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/mecn/"
summary: "Síťová funkce odpovědná za sběr a hlášení monitorovacích událostí pro účely účtování. Je implementována v rámci uzlů, jako jsou MME, SGSN nebo IWK-SCEF, aby poskytla podrobné údaje o využití pro faktu"
---

MECN je síťová funkce odpovědná za sběr a hlášení monitorovacích událostí pro účely účtování, aby poskytla podrobné údaje o využití pro fakturaci a vynucování politik.

## Popis

Monitoring Event Charging Node (MECN) je funkční entita definovaná v rámci architektury 3GPP za účelem sběru, zpracování a hlášení monitorovacích událostí relevantních pro účtování. Nejde o samostatný fyzický uzel, ale o logickou funkci integrovanou do stávajících prvků jádra sítě, především Mobility Management Entity ([MME](/mobilnisite/slovnik/mme/)), Serving [GPRS](/mobilnisite/slovnik/gprs/) Support Node ([SGSN](/mobilnisite/slovnik/sgsn/)) a Interworking [SCEF](/mobilnisite/slovnik/scef/) ([IWK-SCEF](/mobilnisite/slovnik/iwk-scef/)). Jejím hlavním úkolem je sloužit jako zdroj podrobných informací o využití založených na událostech, které jsou předávány do offline a online účtovacích systémů ([OFCS](/mobilnisite/slovnik/ofcs/) a [OCS](/mobilnisite/slovnik/ocs/)). MECN monitoruje specifické aktivity uživatele a sítě, jako je zřízení relace, události mobility nebo využití služby, a generuje odpovídající Charging Data Records ([CDR](/mobilnisite/slovnik/cdr/)) nebo hlášení událostí. Tyto záznamy jsou následně předávány funkci Charging Data Function (CDF) nebo Online Charging Function (OCF) přes standardizovaná rozhraní, jako jsou referenční body Ga nebo Gy.

Architektonicky funkce MECN funguje tak, že zachycuje a analyzuje signalizační a uživatelské zprávy ve svém hostitelském uzlu. Například v rámci MME monitoruje signalizační procedury Non-Access Stratum (NAS), jako je Attach, Tracking Area Update a Service Request. Extrahuje relevantní informace, jako je identita uživatele, časová razítka, údaje o poloze a parametry kvality služby. Tato data jsou následně formátována podle specifikací 3GPP (např. 3GPP TS 32.298 pro popis účtovacích dat) do strukturovaného hlášení události. Integrace MECN umožňuje podrobné účtování na úrovni jednotlivých událostí namísto pouhé agregace na úrovni relace, což umožňuje flexibilnější fakturační modely, jako je účtování na základě událostí nebo kontroly výdajových limitů.

Fungování MECN je úzce spojeno s řízením politik. Může být aktivována politikami přijatými od funkce Policy and Charging Rules Function (PCRF) přes rozhraní Gx MME (nebo ekvivalentní). Například pravidlo politiky může nařídit MME hlásit každou událost předání spojení pro konkrétního účastníka. Funkce MECN v rámci MME by pak pro každé předání spojení vygenerovala monitorovací událost včetně podrobností, jako jsou ID zdrojové a cílové buňky. Tato schopnost je klíčová pro implementaci pokročilých účtovacích scénářů v sítích 4G a 5G, jako je účtování za mobilitu jako službu, služby založené na poloze nebo hlášení událostí IoT zařízení. Její specifikace napříč releasy 13 až 19 zajišťuje zpětnou kompatibilitu a vývoj pro podporu nových síťových funkcí a služeb.

## K čemu slouží

MECN byl zaveden, aby řešil rostoucí potřebu podrobného, událostmi řízeného účtování v moderních mobilních sítích. Tradiční účtovací systémy se často spoléhaly na záznamy o účtování (CDR) generované bránami (jako PGW nebo GGSN) na úrovni relace, které poskytovaly souhrn datového využití, ale postrádaly podrobnosti o konkrétních síťových událostech nebo aktivitách účastníků odehrávajících se v uzlech řídicí roviny. Jak se sítě vyvíjely, aby nabízely složitější služby (např. IoT, M2M, služby řízené politikami), operátoři potřebovali schopnost účtovat na základě diskrétních událostí – jako je připojení zařízení, aktualizace mobility nebo vyvolání konkrétní služby – nejen na základě objemu dat. MECN tuto potřebu naplňuje tím, že mění uzly řídicí roviny ve zdroje zpoplatnitelných událostí.

Historicky, před standardizací MECN, měli operátoři omezenou viditelnost událostí relevantních pro účtování, které se odehrávaly v MME nebo SGSN. Jakékoli účtování na základě událostí vyžadovalo proprietární implementace nebo nepřímé odvozování ze záznamů brány, což bylo neefektivní a nepřesné. MECN, standardizovaný od Release 13 dále, poskytl jednotnou, standardy založenou metodu, jak se tyto uzly mohou přímo účastnit účtovacího ekosystému. To bylo motivováno zejména vzestupem IoT a Machine-Type Communication (MTC), kde četné malé, událostmi řízené transakce (jako odečty senzorů) činí účtování založené na objemu nepraktickým. MECN umožňuje monetizaci těchto transakcí tím, že každou nahlásí jako samostatnou zpoplatnitelnou událost.

Dále MECN podporuje vylepšené řízení politik a účtování (PCC) tím, že poskytuje hlášení událostí v reálném čase, které lze použít pro okamžitou kontrolu kreditu nebo vynucování politik. Například operátor může definovat politiku, kde prvních deset událostí mobility denně je zdarma, ale následné jsou zpoplatněny. MECN v MME může tyto události počítat a interagovat s OCS, aby aplikoval správnou účtovací logiku. Tím se řeší problém implementace sofistikovaných, real-time účtovacích schémat, která jsou těsně integrována se síťovou politikou, což bylo omezení dřívějších architektur, kde byly účtování a politika volněji provázány.

## Klíčové vlastnosti

- Integrována v rámci MME, SGSN a IWK-SCEF jako logická funkce
- Generuje podrobná hlášení monitorovacích událostí pro účtování
- Podporuje jak offline (na základě CDR), tak online (na základě událostí) modely účtování
- Spouštěna na základě síťových událostí, jako je připojení (attach), předání spojení (handover) nebo požadavky na službu
- Formátuje data podle specifikací 3GPP pro účtování (např. TS 32.298)
- Spolupracuje s PCRF pro hlášení událostí řízené politikami

## Související pojmy

- [MME – NPC MME Network Product Class](/mobilnisite/slovnik/mme/)
- [SGSN – Serving GPRS Support Node](/mobilnisite/slovnik/sgsn/)
- [IWK-SCEF – InterWorking - Service Capability Exposure Function](/mobilnisite/slovnik/iwk-scef/)

## Definující specifikace

- **TR 28.816** (Rel-17) — Charging for 5G Cellular IoT
- **TS 32.278** (Rel-19) — Monitoring Events Offline Charging Specification

---

📖 **Anglický originál a plná specifikace:** [MECN na 3GPP Explorer](https://3gpp-explorer.com/glossary/mecn/)
