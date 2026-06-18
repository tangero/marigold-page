---
slug: "pib"
url: "/mobilnisite/slovnik/pib/"
type: "slovnik"
title: "PIB – Policy Information Base"
date: 2025-01-01
abbr: "PIB"
fullName: "Policy Information Base"
category: "Management"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/pib/"
summary: "Standardizovaný úložný prostor pro pravidla a data politik používaná systémy správy sítě, zejména pro řízení politiky a účtování (Policy and Charging Control, PCC). Poskytuje strukturovaný formát pro"
---

PIB je standardizovaný úložný prostor pro pravidla a data politik používaná systémy správy sítě, zejména pro řízení politiky a účtování (Policy and Charging Control), k řízení kvality služeb, účtování a zacházení s účastníky.

## Popis

Policy Information Base (PIB) je konceptuální datové úložiště definované v rámci managementového rámce 3GPP, standardizované v TS 32.101. Slouží jako centrální úložiště pro informace související s politikami, které zahrnují pravidla, podmínky, akce a parametry používané síťovými funkcemi pro činění rozhodnutí v reálném čase. PIB není jedinou fyzickou databází, ale logickým modelem, který může být implementován napříč různými síťovými prvky a systémy správy. Jeho primární role je podpora architektury řízení politiky a účtování (Policy and Charging Control, [PCC](/mobilnisite/slovnik/pcc/)), kde poskytuje data potřebná funkcí pro pravidla politiky a účtování (Policy and Charging Rules Function, [PCRF](/mobilnisite/slovnik/pcrf/)) k vytváření a vynucování dynamických pravidel politiky a účtování.

Architektonicky je PIB součástí širších vrstev Telecommunications Management Network ([TMN](/mobilnisite/slovnik/tmn/)) a Network Management ([NM](/mobilnisite/slovnik/nm/)). Rozhraní s dalšími managementovými funkcemi, jako je Network Resource Model ([NRM](/mobilnisite/slovnik/nrm/)) a systémy správy Fault, Configuration, Accounting, Performance, and Security (FCAPS). PIB obsahuje strukturované informace, jako jsou profily účastníků, definice služeb, parametry účtování, QoS profily a pravidla řízení přístupu. Tyto informace jsou modelovány pomocí standardizovaného informačního modelu, často založeného na principech Common Information Model ([CIM](/mobilnisite/slovnik/cim/)) nebo specifických definicích 3GPP Management Object ([MO](/mobilnisite/slovnik/mo/)), což zajišťuje konzistenci a interoperabilitu napříč různými dodavateli a síťovými nasazeními.

PIB funguje tak, že poskytuje jednotný zdroj dat politik, ke kterému mohou přistupovat, dotazovat se na něj a aktualizovat ho rozhodovací body politik, jako je PCRF. Když účastník zahájí relaci, PCRF může načíst relevantní pravidla politik z PIB na základě identity účastníka, požadované služby a síťových podmínek. Tato pravidla jsou následně převedena na specifická pravidla řízení politiky a účtování (PCC), která jsou vynucována na funkci vynucování politiky a účtování (Policy and Charging Enforcement Function, [PCEF](/mobilnisite/slovnik/pcef/)) v bráně. PIB také podporuje managementové operace, jako je provisioning, auditování a synchronizace dat politik v síti.

Klíčovými součástmi konceptu PIB jsou definice pravidel politik, podmínky politik (např. denní doba, lokalita, zatížení sítě), akce politik (např. úprava QoS, spouštěče účtování) a přidružená metadata. Jeho role je klíčová pro umožnění pokročilých služeb, jako je vrstvená QoS, sponzorovaná data a účtování na vyžádání, protože poskytuje nezbytnou inteligenci a datový základ pro automatizované, politikami řízené síťové operace. Oddělením logiky politik od vynucovacích mechanismů PIB podporuje flexibilitu, škálovatelnost a snadnější inovace služeb.

## K čemu slouží

PIB byl zaveden, aby řešil rostoucí složitost správy politik v sítích 3GPP, zejména s příchodem služeb založených na IP a potřebou dynamického řízení politik. Před jeho standardizací byla pravidla politik často pevně zakódována v jednotlivých síťových prvcích nebo spravována prostřednictvím proprietárních, dodavatelsky specifických systémů, což vedlo k provozní neefektivitě, integračním výzvám a omezené schopnosti rychle zavádět nové služby. PIB poskytuje standardizovaný, centralizovaný model pro informace o politikách, umožňující konzistentní definici, distribuci a vynucování politik napříč více-dodavatelskými sítěmi.

Jeho vytvoření bylo motivováno evolucí směrem k plně-IP jádrovým sítím a zavedením architektury řízení politiky a účtování (Policy and Charging Control, PCC) ve 3GPP Release 7 a dále zpřesněné v Release 8. Rámec PCC vyžadoval robustní, škálovatelný způsob správy širokého spektra pravidel politik potřebných pro sofistikované účtování a QoS řízení. PIB slouží jako informační páteř tohoto rámce, zajišťující, že rozhodnutí o politikách jsou založena na přesných, aktuálních a konzistentně modelovaných datech. Řeší problém fragmentace dat politik a izolovaných systémů správy.

Historicky, jak se sítě přesouvaly od jednoduchých hlasových služeb k bohatým multimediálním a datovým službám, potřeba granulárních, na účastníka zaměřených politik se stala prvořadou. PIB umožňuje operátorům definovat komplexní politiky, které se mohou přizpůsobit podmínkám sítě v reálném čase, chování účastníků a smluvním podmínkám služeb. Řeší omezení dřívějších, statických konfiguračních metod tím, že podporuje dynamické aktualizace politik a usnadňuje automatizaci úloh správy sítě, což je nezbytné pro moderní prostředí softwarově definovaných sítí (SDN) a virtualizace síťových funkcí (NFV).

## Klíčové vlastnosti

- Standardizovaný informační model pro pravidla a data politik
- Centralizovaný logický úložný prostor podporující řízení politiky a účtování (Policy and Charging Control, PCC)
- Rozhraní se systémy správy sítě (Network Management Systems, NMS) a systémy správy prvků (Element Management Systems, EMS)
- Podporuje dynamické načítání a aktualizace politik rozhodovacími body politik
- Umožňuje konzistentní vynucování politik napříč více-dodavatelskými síťovými prvky
- Usnadňuje automatizovaný provisioning a auditování konfigurací politik

## Související pojmy

- [PCRF – Policy and Charging Rules Function](/mobilnisite/slovnik/pcrf/)
- [PCC – Performance-oriented Congestion Control](/mobilnisite/slovnik/pcc/)
- [PCEF – Policy and Charging Enforcement Function](/mobilnisite/slovnik/pcef/)
- [QoS – Quality of Service](/mobilnisite/slovnik/qos/)
- [NMS – Network Management Subsystem](/mobilnisite/slovnik/nms/)

## Definující specifikace

- **TS 32.101** (Rel-19) — Management principles and high-level requirements

---

📖 **Anglický originál a plná specifikace:** [PIB na 3GPP Explorer](https://3gpp-explorer.com/glossary/pib/)
