---
slug: "mig"
url: "/mobilnisite/slovnik/mig/"
type: "slovnik"
title: "MIG – MCPTT Imminent peril Group"
date: 2025-01-01
abbr: "MIG"
fullName: "MCPTT Imminent peril Group"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/mig/"
summary: "Předdefinovaná skupina ve službách Mission Critical Push-To-Talk (MCPTT) určená pro nouzovou komunikaci v situacích bezprostředního ohrožení. Umožňuje rychlé, prioritní skupinové volání pro záchranáře"
---

MIG je předdefinovaná skupina služby Mission Critical Push-To-Talk určená pro nouzovou komunikaci v situacích bezprostředního ohrožení, která umožňuje rychlé, prioritní volání pro záchranáře v život ohrožujících situacích.

## Popis

[MCPTT](/mobilnisite/slovnik/mcptt/) Imminent peril Group (MIG) je specializovaná funkční skupina definovaná v architektuře služeb Mission Critical Services ([MCS](/mobilnisite/slovnik/mcs/)) podle 3GPP, konkrétně pro službu Mission Critical Push-To-Talk (MCPTT). Imminent peril Group je předkonfigurovaná nebo dynamicky vytvořená skupina uživatelů MCPTT zřízená za účelem řízení komunikace v situaci bezprostředního nebezpečí nebo ohrožení života. Skupina je charakterizována svou asociací se stavem bezprostředního ohrožení, který spouští specifické chování s vysokou prioritou v rámci systému MCPTT.

Architektonicky je MIG logická entita spravovaná aplikačním serverem MCPTT. Její definice a členství jsou uloženy a řízeny v rámci frameworku služby MCPTT. Mezi klíčové síťové komponenty patří klient MCPTT na uživatelském zařízení, aplikační server MCPTT a podkladová 3GPP core síť (EPC nebo 5GC), která poskytuje prioritní přenos a mechanismy QoS. Skupina je identifikována jedinečným MCPTT Group ID a je asociována s metadaty označujícími její status jako Imminent peril Group.

Jak to funguje, zahrnuje jak konfiguraci, tak dynamický provoz. MIG může být staticky zřízena administrátorem nebo vytvořena dynamicky autorizovaným uživatelem (např. velitelem zásahu), když nastane nebezpečná situace. Při aktivaci nebo použití má komunikace v rámci MIG obvykle nejvyšší možnou prioritu. To zahrnuje preemptivní přístup k podlaze pro arbitráži mluvčího, garantovanou QoS pro mediální přenosy za účelem minimalizace latence a ztráty paketů a potenciální prioritu nad ostatním síťovým provozem. Server MCPTT zajišťuje, že hovory do nebo z MIG jsou zpracovány s minimálním časem sestavení a že účastníci dostávají jasné indikace stavu bezprostředního ohrožení skupiny. Jejím úkolem je poskytnout jednoznačný komunikační kanál s vysokou mírou jistoty, který má přednost během kritických incidentů a přímo podporuje život zachraňující operace.

## K čemu slouží

Koncept MIG byl vytvořen, aby řešil kritický nedostatek obecných systémů skupinové komunikace: neschopnost garantovat absolutní prioritu a spolehlivost komunikace během skutečných život ohrožujících nouzových situací. V oblasti veřejné bezpečnosti a operací s požadavky na spolehlivost (mission-critical) vznikají situace, kdy je personál pod bezprostřední fyzickou hrozbou (např. zraněný policista, uvězněný hasič, únik chemické látky). Standardní komunikační kanály mohou být zahlceny nebo podléhat soupeření, což způsobuje nebezpečná zpoždění.

Řeší problém zajištění, že nouzová komunikace může přerušit veškerý ostatní provoz, a to jak v rámci služby [MCPTT](/mobilnisite/slovnik/mcptt/), tak v přístupové rádiové síti a core síti. Před jeho standardizací v 3GPP existovaly podobné koncepty v legacy systémech Land Mobile Radio ([LMR](/mobilnisite/slovnik/lmr/)) (např. nouzové skupinové hovory), ale ty nebyly integrovány s frameworky QoS pro LTE/5G. MIG poskytuje standardizovaný, na síť vědomý mechanismus, který využívá sofistikované schopnosti priority a přerušení 3GPP (např. QoS Class Identifier, Allocation and Retention Priority) end-to-end.

Motivací pro jeho zavedení ve 3GPP Release 13 byl vývoj plných specifikací MCPTT pro nahrazení nebo doplnění systémů LMR. Řeší přísné požadavky uživatelů z oblasti veřejné bezpečnosti, kteří musí mít jistotu, že jejich nejkritičtější komunikace vždy projde. MIG zajišťuje, že během události bezprostředního ohrožení jsou potřebné síťové zdroje vyhrazeny a chráněny, čímž se minimalizuje jakékoli riziko selhání komunikace, když na ní nejvíce záleží.

## Klíčové vlastnosti

- Předkonfigurovaná nebo dynamicky vytvořitelná skupina pro nouzové situace
- Asociace s nejvyšší prioritou MCPTT a preemptivní kontrolou podlahy
- Vyvolání a indikace stavu 'bezprostředního ohrožení' v rámci skupiny
- Integrace s mechanismy QoS 3GPP pro garantované zdroje přenosu
- Potenciál pro síťovou prioritu nad ostatním provozem (např. pomocí ARP)
- Standardizovaná správa a autorizace pro vytváření a aktivaci skupiny

## Související pojmy

- [MCPTT – Mission Critical Push to Talk Identity](/mobilnisite/slovnik/mcptt/)
- [QCI – Quality of Service Class Identifier](/mobilnisite/slovnik/qci/)

## Definující specifikace

- **TS 24.379** (Rel-19) — Mission Critical Push To Talk (MCPTT) call control
- **TS 36.579** — 3GPP TR 36.579
- **TS 37.579** (Rel-18) — Mission Critical services conformance testing

---

📖 **Anglický originál a plná specifikace:** [MIG na 3GPP Explorer](https://3gpp-explorer.com/glossary/mig/)
