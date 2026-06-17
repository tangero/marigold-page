---
slug: "a2xp"
url: "/mobilnisite/slovnik/a2xp/"
type: "slovnik"
title: "A2XP – Aircraft-to-Everything Policy"
date: 2026-01-01
abbr: "A2XP"
fullName: "Aircraft-to-Everything Policy"
category: "Services"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/a2xp/"
summary: "A2XP je rámec pro správu politik pro řízení komunikačních služeb pro letadla, včetně scénářů vzduch-země (A2G) a vzduch-vzduch (A2A). Definuje způsob aplikace síťových politik za účelem zajištění bezp"
---

A2XP je rámec pro správu politik pro řízení komunikačních služeb letadel, který definuje způsob aplikace síťových politik za účelem zajištění bezpečného, spolehlivého a kvalitativně vhodného připojení ve scénářích jako vzduch-země a vzduch-vzduch.

## Popis

Aircraft-to-Everything Policy (A2XP) je komplexní rámec pro řízení politik standardizovaný 3GPP pro správu komunikačních služeb zahrnujících letadla. Funguje v rámci funkce pro řízení politik (PCF) jádra sítě 5G a rozšiřuje správu politik na jedinečné požadavky leteckých vozidel. Rámec pokrývá scénáře, kdy je uživatelské zařízení (UE) umístěno na palubě letadla, což může být buď samotné letadlo (jako letecké UE), nebo zařízení pasažérů připojená přes palubní přístupovou síť. Politiky A2XP jsou specifické, protože musí zohledňovat pohyb letadla ve třech rozměrech, vysokou rychlost a specifické požadavky služeb jak pro operační/posádkovou komunikaci (A2A, A2G), tak pro konektivitu pasažérů.

Architektura je integrována do stávající architektury pro řízení politik a účtování (PCC) v 5G. Mezi klíčové síťové funkce zapojené do A2XP patří PCF, který je centrální entitou pro rozhodování o politikách A2XP; funkce pro správu přístupu a mobility (AMF) a funkce pro správu relací (SMF), které vynucují politiky týkající se přístupu, mobility a správy relací; a Unified Data Management (UDM), který ukládá data o účastnících a politikách. V případě A2XP PCF využívá specifické vstupy, jako je identita letadla, stav letu, poloha, nadmořská výška a typ služby (např. bezpečnostně kritická telemetrie vs. širokopásmové připojení pro pasažéry), aby odvodil příslušná pravidla politik. Tato pravidla jsou následně poskytnuta SMF a AMF jako pravidla pro řízení politik a účtování (PCC) nebo jako pravidla pro přístupovou a mobilní politiku (AMP).

Politiky A2XP pokrývají několik klíčových dimenzí. Řídí kvalitu služeb (QoS) přiřazováním specifických hodnot 5QI (5G QoS Identifier) šitých na míru leteckým službám, což zajišťuje nízkou latenci pro příkazy a řízení nebo garantovanou šířku pásma pro komunikaci kokpitu. Politiky mobility jsou zásadní, neboť diktují strategie předávání mezi pozemními základnovými stanicemi a potenciálně satelitními nebo leteckými síťovými uzly (neterestriální sítě - NTN), když letadlo prochází různými fázemi letu a jurisdikcemi. Bezpečnostní politiky jsou posíleny za účelem ochrany před hrozbami specifickými pro leteckou konektivitu, včetně bezpečné autentizace letadla a izolace kritického operačního provozu od provozu pasažérů. Dále A2XP umožňuje síťové dělení (network slicing) pro letectví, což umožňuje vytváření vyhrazených řezů pro letecké operace, řízení letového provozu nebo zábavu za letu, z nichž každý má své vlastní izolované zdroje a záruky výkonu.

Fungování tohoto rámce je dynamické a kontextově citlivé. Například během vzletu a přistání mohou politiky upřednostňovat řezy s ultra-spolehlivou nízkou latencí (URLLC) pro telemetrii a omezovat služby pro pasažéry náročné na šířku pásma. Během cestovní fáze mohou politiky umožnit vysokokapacitní širokopásmové řezy pro pasažéry při zachování samostatného, zabezpečeného řezu pro operační data. Účtovací politiky v rámci A2XP mohou být také specializované a podporovat modely jako paušál na dobu trvání letu nebo objemové účtování pro specifické typy služeb. Centralizací této logiky v PCF poskytuje A2XP standardizovaný, škálovatelný způsob, jak mohou operátoři mobilních sítí a poskytovatelé leteckých služeb nabízet řízené, účtovatelné a bezpečné služby konektivity pro letecký průmysl.

## K čemu slouží

A2XP byl vytvořen, aby řešil nedostatek standardizovaného rámce pro správu politik pro integraci komunikace letadel do mobilních sítí 5G. Před prací 3GPP byla konektivita pro letadla závislá na proprietárních systémech (např. pro komunikaci vzduch-země) nebo satelitních spojích, které byly často drahé, nabízely omezenou šířku pásma a postrádaly bezproblémovou integraci s pozemními mobilními sítěmi. Rozšíření spotřebitelských zařízení na palubě letadel a potřeba digitalizace leteckého průmyslu – včetně monitorování stavu letadla v reálném čase, optimalizace letových tras a vylepšeného zážitku pasažérů – vytvořila poptávku po nákladově efektivních, výkonných a globálně interoperabilních řešeních konektivity.

Primární problém, který A2XP řeší, je mezera ve správě politik pro letecká uživatelská zařízení (UE). Politika pro pozemní UE je založena na faktorech, jako je profil účastníka a poloha. Letadlo však zavádí nové dimenze: trojrozměrnou polohu (včetně nadmořské výšky), vysokorychlostní mobilitu přes více síťových a národních hranic a koexistenci kritických letových operací s komerčními službami pro pasažéry na stejné platformě. Bez A2XP by museli operátoři sítí používat obecné politiky nebo vyvíjet nestandardní rozšíření, což by vedlo k fragmentaci, bezpečnostním zranitelnostem a neschopnosti garantovat smlouvy o úrovni služeb (SLA) pro letecké aplikace, jako je řízení dronů s nízkou latencí nebo nouzová komunikace za letu.

Historicky vychází motivace z širší iniciativy 3GPP na podporu vertikálních a LAN služeb, včetně pracovní položky '5G for Aviation'. Vytvoření A2XP ve vydání Release-18 bylo hnáno potřebou poskytnout jednotnou řídicí rovinu politik, která rozumí leteckému kontextu. Umožňuje komerční a technickou proveditelnost použití 5G jako primární nebo doplňkové přístupové technologie pro letectví a připravuje cestu pro nové obchodní modely pro operátory mobilních sítí (MNO), letecké společnosti a úřady řízení letového provozu. Řeší omezení předchozích neintegrovaných přístupů tím, že zajišťuje, aby letecký provoz získal odpovídající síťové zdroje, bezpečnostní zacházení a podporu mobility přímo v rámci standardizované architektury jádra sítě 5G.

## Klíčové vlastnosti

- Kontextově citlivé odvozování politik na základě identity letadla, fáze letu a 3D polohy
- Integrovaná podpora pro scénáře komunikace vzduch-země (A2G) i vzduch-vzduch (A2A)
- Dynamická správa QoS s přiřazováním letecky specifických hodnot 5QI pro operační služby a služby pro pasažéry
- Rozšířené politiky mobility pro plynulá předávání mezi terestrickými a neterestriálními síťovými uzly
- Bezpečnostní politiky pro autentizaci, autorizaci a izolaci provozu mezi systémy letadla a daty pasažérů
- Podpora síťového dělení (network slicing) pro vytváření vyhrazených logických sítí pro různé případy užití v letectví

## Definující specifikace

- **TS 23.503** (Rel-20) — 5G Policy and Charging Control Framework
- **TS 24.526** (Rel-19) — UE Policies for 5GS; Stage 3
- **TS 24.577** (Rel-19) — A2X Services in 5GS
- **TS 24.578** (Rel-19) — UE policies for A2X services in 5GS
- **TS 29.513** (Rel-19) — 5G PCC Signalling Flows & QoS Mapping
- **TS 29.525** (Rel-19) — 5G UE Policy Control Service Stage 3

---

📖 **Anglický originál a plná specifikace:** [A2XP na 3GPP Explorer](https://3gpp-explorer.com/glossary/a2xp/)
