---
slug: "b2b"
url: "/mobilnisite/slovnik/b2b/"
type: "slovnik"
title: "B2B – Business to Business"
date: 2025-01-01
abbr: "B2B"
fullName: "Business to Business"
category: "Management"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/b2b/"
summary: "B2B označuje rámec pro vztahy mezi podniky (business-to-business) v rámci účtovacích a fakturačních systémů 3GPP. Umožňuje poskytovatelům služeb spravovat a vypořádávat poplatky za služby vyměňované m"
---

B2B je rámec pro vztahy mezi podniky (business-to-business) v rámci účtovacích systémů 3GPP, který poskytovatelům služeb umožňuje spravovat a vypořádávat poplatky za služby vyměňované mezi různými obchodními subjekty.

## Popis

Rámec Business to Business (B2B) v 3GPP je komplexní systém pro správu finančních transakcí a vypořádání služeb mezi různými obchodními subjekty v rámci telekomunikačního ekosystému. Funguje v širším kontextu účtovací architektury 3GPP a je konkrétně definován v řadě specifikací Telecommunication Management (TM), včetně TS 28.843, TS 32.101, TS 32.140 a TS 32.141. Rámec poskytuje protokoly, datové modely a postupy nezbytné pro sledování využití služeb, výpočet poplatků a generování záznamů pro vypořádání mezi operátory.

Z architektonického hlediska rozhraní B2B komunikuje se základními síťovými funkcemi, jako je Charging Data Function ([CDF](/mobilnisite/slovnik/cdf/)) a Charging Gateway Function ([CGF](/mobilnisite/slovnik/cgf/)), za účelem sběru dat o využití. Rozšiřuje standardní účtovací mechanismy tak, aby zvládly scénáře, kdy je spotřebitel služby a její poskytovatel samostatný právní nebo obchodní subjekt. Systém využívá specifické B2B účtovací záznamy, které obsahují pole identifikující zapojené strany, typ služby, objem využití, použité tarify a částky k vypořádání. Tyto záznamy jsou formátovány podle standardů 3GPP (např. kódování ASN.1) a přenášeny standardizovanými rozhraními do fakturačních systémů ke zpracování.

Klíčové součásti rámce B2B zahrnují B2B Charging Function, která koreluje události využití ze sítě s konkrétními obchodními dohodami; Settlement Function, která vypočítává finanční závazky na základě dohodnutých tarifů a smluv o úrovni služeb (SLA); a B2B Mediation Function, která převádí účtovací datové záznamy ([CDR](/mobilnisite/slovnik/cdr/)) do formátů vhodných pro vypořádání. Rámec podporuje různé modely vypořádání včetně velkoobchodního, sdílení výnosů a modelu poplatku za službu. Integruje se s offline a online účtovacími systémy ([OFCS](/mobilnisite/slovnik/ofcs/) a [OCS](/mobilnisite/slovnik/ocs/)), aby poskytoval řízení kreditu pro služby B2B v reálném čase, je-li to vyžadováno.

Úlohou B2B v síti je umožnit komerční vrstvu, která stojí nad technickým poskytováním služeb. Bez něj by operátoři neměli standardizovaný, automatizovaný způsob, jak si navzájem účtovat služby roamingu, propojení sítí, služby pro [MVNO](/mobilnisite/slovnik/mvno/) nebo služby založené na [API](/mobilnisite/slovnik/api/). Zajišťuje správný tok výnosů mezi partnery, možnost řešení sporů prostřednictvím auditovatelných záznamů a rychlé nasazení nových obchodních modelů. Tento rámec je zásadní pro ekonomickou udržitelnost celého ekosystému, protože umožňuje operátorům zpeněžit své sítě a služby, když je využívají jiné podniky, nikoli přímo koncoví uživatelé.

## K čemu slouží

Rámec B2B byl vytvořen, aby řešil rostoucí složitost obchodních vztahů v telekomunikačním průmyslu. Jak se mobilní sítě vyvíjely za hranice jednoduchých hlasových služeb, začali operátoři nabízet velkoobchodní přístup, roamingové dohody a partnerské služby, které vyžadovaly robustní mechanismy pro vypořádání mezi operátory. Před standardizovanými systémy B2B se operátoři spoléhali na bilaterální dohody a manuální procesy pro vzájemné účtování, které byly náchylné k chybám, pomalé a obtížně škálovatelné. Nedostatek automatizace brzdil vývoj nových služeb a vytvářel problémy se slaďováním.

Historicky zavedení GSM roamingu zvýraznilo potřebu automatizovaného vypořádání, ale rané systémy byly často proprietární. S příchodem 3G a růstem datových služeb objem a rozmanitost transakcí mezi operátory explodovaly, včetně velkoobchodu s přenosovou kapacitou, interoperability zpráv a později služeb konektivity pro IoT. Rámec 3GPP B2B, zavedený ve verzi 8, poskytl standardizovaný přístup k definování účtovacích datových záznamů, postupů vypořádání a rozhraní specificky pro scénáře mezi podniky. To umožnilo operátorům implementovat konzistentní systémy bez ohledu na jejich partnery, čímž se snížily integrační náklady a provozní režie.

Rámec řeší problém zpeněžení síťových aktiv v prostředí více operátorů. Umožňuje operátorům nabízet své síťové schopnosti (jako je konektivita, QoS nebo lokalizační služby) jiným podnikům měřitelným a účtovatelným způsobem. To usnadnilo růst mobilních virtuálních síťových operátorů ([MVNO](/mobilnisite/slovnik/mvno/)), roamingových konsorcií a později síťového slicingu pro podniky. Tím, že poskytuje jasnou, standardy založenou metodu pro sledování využití a výpočet poplatků mezi subjekty, B2B snižuje komerční třecí ztráty a podporuje inovace v nabídce služeb, což v konečném důsledku prospívá koncovým uživatelům prostřednictvím rozšířené dostupnosti služeb a konkurence.

## Klíčové vlastnosti

- Standardizované B2B účtovací datové záznamy (CDR) se specifickými poli pro vypořádání mezi subjekty
- Podpora více modelů vypořádání včetně velkoobchodního, sdílení výnosů a paušálního účtování
- Integrace s offline (OFCS) i online (OCS) účtovacími systémy pro řízení kreditu v reálném čase
- Mediační funkce pro transformaci dat o síťovém využití do formátů připravených pro vypořádání
- Rozhraní k externím fakturačním a vypořádacím systémům pro automatizované finanční zpracování
- Podpora auditování a řešení sporů prostřednictvím podrobných, časově označených transakčních záznamů

## Definující specifikace

- **TR 28.843** (Rel-18) — Technical Report on Charging Aspects for Vertical Scenarios
- **TS 32.101** (Rel-19) — Management principles and high-level requirements
- **TS 32.140** (Rel-19) — Subscription Management (SuM) requirements
- **TS 32.141** (Rel-19) — Subscription Management (SuM) Architecture

---

📖 **Anglický originál a plná specifikace:** [B2B na 3GPP Explorer](https://3gpp-explorer.com/glossary/b2b/)
