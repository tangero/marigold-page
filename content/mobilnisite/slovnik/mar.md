---
slug: "mar"
url: "/mobilnisite/slovnik/mar/"
type: "slovnik"
title: "MAR – Multi-Access Rule"
date: 2025-01-01
abbr: "MAR"
fullName: "Multi-Access Rule"
category: "QoS"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/mar/"
summary: "Pravidlo politiky definované v jádře 5G sítě (5GC), které řídí, jak je provoz uživatelského zařízení (UE) distribuován napříč více současnými přístupovými sítěmi (jako 3GPP a ne-3GPP). Je součástí fra"
---

MAR je pravidlo politiky jádra 5G sítě (5G Core), které řídí, jak je uživatelský provoz distribuován napříč více současnými přístupovými sítěmi, a umožňuje tak inteligentní směrování na základě dostupnosti přístupu, vytížení sítě a požadavků aplikace.

## Popis

Multi-Access Rule (MAR) je konstrukce pravidel politiky zavedená ve verzi 3GPP Release 16 jako součást vylepšené architektury Policy and Charging Control (PCC) pro 5G System (5GS). Jedná se o specifický typ pravidla politiky poskytovaného funkcí Policy Control Function ([PCF](/mobilnisite/slovnik/pcf/)) a vynucovaného funkcí Session Management Function ([SMF](/mobilnisite/slovnik/smf/)) za účelem řízení, jak je provoz uživatelského zařízení (UE) směrován napříč více dostupnými přístupovými sítěmi, když je UE současně připojeno přes 3GPP přístup (např. 5G NR) i ne-3GPP přístup (např. Wi-Fi). MAR je v podstatě soubor podmínek a akcí, které určují, na kterou přístupovou síť by měl být konkrétní IP tok nebo 5G QoS Flow přeposlán.

Architektonicky jsou MAR pravidla nedílnou součástí frameworku PCC v 5G. PCF tato pravidla generuje na základě politiky operátora, profilu účastníka a případně vstupů v reálném čase od Network Data Analytics Function (NWDAF). Tato pravidla jsou následně poskytnuta SMF jako součást PCC pravidel v kontextu PDU Session. SMF je zodpovědná za interpretaci a vynucování MAR. Dělá to tak, že konfiguruje příslušné akce pro směrování provozu na User Plane Function ([UPF](/mobilnisite/slovnik/upf/)) a poskytuje pokyny UE prostřednictvím frameworku Access Traffic Steering, Switching and Splitting ([ATSSS](/mobilnisite/slovnik/atsss/)). MAR obsahuje několik klíčových komponent: identifikátor pravidla, hodnotu precedence, filtry service data flow (SDF) nebo identifikátory QoS Flow pro identifikaci cílového provozu, podmínky pro aktivaci (např. dostupnost přístupové sítě, prahové hodnoty vytížení) a akci směrování (např. směrovat na 3GPP přístup, směrovat na ne-3GPP přístup, rozdělit přes oba).

Fungování MAR zahrnuje dynamické vyhodnocování a vynucování. Když je vytvořena PDU Session s ATSSS schopnostmi, SMF nainstaluje příslušná MAR pravidla. Jakmile uživatelský provoz odpovídá SDF filtrům, SMF (s podporou UPF) vyhodnocuje podmínky MAR vůči aktuálnímu stavu sítě. Například, pokud MAR stanoví, že video provoz má být směrován na Wi-Fi, pokud je síla Wi-Fi signálu nad prahovou hodnotou a 3GPP přístup je přetížen, systém tyto parametry kontinuálně sleduje. Když jsou podmínky splněny, SMF instruuje UPF, aby pakety odpovídajícím způsobem označila, a může použít mechanismy ATSSS (jako [MPTCP](/mobilnisite/slovnik/mptcp/) nebo [GRE](/mobilnisite/slovnik/gre/) tunneling) k nasměrování toku přes vybraný přístup. ATSSS obsluha v UE spolupracuje v tomto procesu na základě režimu směrování (UE-assisted nebo network-assisted). MAR umožňují granularitu na úrovni jednotlivých toků, což dovoluje různým aplikacím být směrovány přes různé přístupy současně, čímž se optimalizuje výkon a využití zdrojů.

## K čemu slouží

MAR byl vytvořen, aby řešil rostoucí složitost správy provozu v heterogenních vícepřístupových sítích 5G. S rozšířením Wi-Fi 6/6E a snahou využívat nelicencované spektrum společně s licencovaným 5G NR potřebovali operátoři sofistikovaný, na politice založený mechanismus pro optimální směrování provozu napříč všemi dostupnými cestami. Předchozí vícepřístupová řešení, jako [MAPCON](/mobilnisite/slovnik/mapcon/) a [IFOM](/mobilnisite/slovnik/ifom/) ve 4G, poskytovala základní schopnosti, ale často byla statická nebo vyžadovala významné rozhodování na straně UE. MAR, jako součást frameworku ATSSS v 5G, zavádí na síť orientované, dynamické a na toky citlivé řízení pomocí pravidel politiky.

Primární problém, který MAR řeší, je jak inteligentně využívat více přístupových spojení pro jednu PDU Session, aby se zvýšil uživatelský zážitek a efektivita sítě. Bez takových pravidel by mohlo být rozdělení provozu suboptimální – například přetížení 5G RAN hromadnými daty při nedostatečném využití dostupné Wi-Fi, nebo neschopnost přesunout citlivý herní provoz s nízkou latencí na přístup s nižší latencí. MAR umožňuje operátorům definovat bohaté politiky založené na široké škále podmínek, včetně vytížení přístupové sítě, kvality (např. latence, jitteru), nákladů, typu předplatného a požadavků aplikace. To umožňuje případy použití, jako je vždy připojená konektivita, kdy kritické signalizační spojení zůstává na 5G pro spolehlivost, zatímco velké stahování je přesunuto na Wi-Fi, nebo bezproblémové přepnutí videohovoru z 5G na Wi-Fi při přesunu do interiéru.

Dále MAR podporuje vizi 5G týkající se síťového krájení a servisně orientované architektury. Různé síťové řezy mohou mít různé politiky MAR; například řeš vylepšeného mobilního širokopásmového přístupu (eMBB) může agresivně přesouvat provoz na Wi-Fi, zatímco řeš pro komunikaci s ultra spolehlivou nízkou latencí (URLLC) může ponechat veškerý provoz na 3GPP přístupu. Díky integraci s PCF a NWDAF mohou být politiky MAR adaptivní a používat analytiku k předpovídání přetížení a preventivnímu směrování provozu. To představuje významný vývoj od statických konfigurací k uzavřenému, inteligentnímu systému správy provozu, který je nezbytný pro zajištění konzistentní kvality uživatelského zážitku v vícepřístupovém prostředí 5G.

## Klíčové vlastnosti

- Typ PCC pravidla, které definuje podmínky a akce pro směrování provozu napříč 3GPP a ne-3GPP přístupy
- Podporuje granularitu směrování na úrovni jednotlivých IP toků nebo QoS Flow v rámci vícepřístupové PDU Session
- Podmínky mohou zahrnovat dostupnost přístupu, vytížení, metriky kvality (latence, ztráta paketů) a data předplatného
- Akce zahrnují směrování na konkrétní přístup, rozdělení napříč přístupy nebo dynamické přepínání přístupů
- Vynucováno SMF a UPF ve spolupráci s ATSSS schopnostmi UE
- Integruje se s NWDAF pro rozhodování pravidel politiky založená na datech a analytice sítě, umožňující adaptaci

## Související pojmy

- [ATSSS – Access Traffic Steering, Switching, and Splitting](/mobilnisite/slovnik/atsss/)
- [PCF – Positioning Calculation Function](/mobilnisite/slovnik/pcf/)
- [SMF – Service Management Function](/mobilnisite/slovnik/smf/)

## Definující specifikace

- **TS 26.804** (Rel-19) — 5G Media Streaming Extensions Study
- **TS 29.244** (Rel-19) — PFCP Specification for Control/User Plane Separation

---

📖 **Anglický originál a plná specifikace:** [MAR na 3GPP Explorer](https://3gpp-explorer.com/glossary/mar/)
