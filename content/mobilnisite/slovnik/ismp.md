---
slug: "ismp"
url: "/mobilnisite/slovnik/ismp/"
type: "slovnik"
title: "ISMP – Inter-System Mobility Policy"
date: 2025-01-01
abbr: "ISMP"
fullName: "Inter-System Mobility Policy"
category: "Mobility"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/ismp/"
summary: "Inter-System Mobility Policy (ISMP) je soubor pravidel poskytovaných sítí, která řídí výběr a stanovují priority mezi různými 3GPP a ne-3GPP technologiemi rádiového přístupu (např. LTE, NR, Wi-Fi) zař"
---

ISMP je soubor pravidel poskytovaných sítí, která řídí výběr a stanovují priority mezi různými 3GPP a ne-3GPP technologiemi rádiového přístupu pro síťově řízené směrování provozu zařízením uživatele (UE).

## Popis

Inter-System Mobility Policy (ISMP) je základní funkce jádra sítě definovaná ve specifikacích 3GPP, která řídí způsob, jakým se zařízení uživatele (UE) připojuje k různým rádiovým přístupovým sítím a jak mezi nimi přechází. Tyto sítě mohou zahrnovat různé 3GPP technologie jako [E-UTRAN](/mobilnisite/slovnik/e-utran/) (LTE), NG-RAN (5G NR) a starší systémy jako UTRAN, stejně jako ne-3GPP přístupy, jako jsou důvěryhodné a nedůvěryhodné Wi-Fi sítě. ISMP se skládá ze souboru pravidel definovaných operátorem, která jsou poskytnuta UE, typicky prostřednictvím funkce [ANDSF](/mobilnisite/slovnik/andsf/) (Access Network Discovery and Selection Function) v EPS nebo funkce [PCF](/mobilnisite/slovnik/pcf/) (Policy Control Function) v 5G systému.

Pravidla ISMP jsou strukturována jako seznam výběrových kritérií se stanovenými prioritami. Každé pravidlo obsahuje podmínky (např. polohu, denní dobu, stav roamingu, konkrétní SSID pro Wi-Fi) a přidružené akce, které diktují chování UE při výběru přístupu. Například pravidlo může stanovovat: 'Pokud je UE v domovské síti a detekuje jak LTE, tak konkrétní podnikovou Wi-Fi síť, připojí se pro veškerý provoz k Wi-Fi.' Subjekt pro správu mobility v UE vyhodnocuje tato pravidla v pořadí podle priority, aby určil preferované a povolené typy přístupu pro navazování nových spojení nebo provádění předání.

Z technického hlediska je ISMP doručeno UE prostřednictvím [OMA](/mobilnisite/slovnik/oma/) Device Management ([DM](/mobilnisite/slovnik/dm/)) nebo protokolů pro bezdrátovou distribuci nastavení. UE tato pravidla ukládá a aplikuje je v reálném čase. Když je k dispozici více přístupů, UE používá ISMP k rozhodnutí, ke kterému se má registrovat nebo který použít pro konkrétní IP tok (v případě souvisejícího konceptu Inter-System Routing Policy - [ISRP](/mobilnisite/slovnik/isrp/)). Síť může tyto politiky dynamicky aktualizovat na základě měnících se podmínek, jako je zatížení sítě, úroveň předplatitele nebo požadavky aplikace. To operátorům umožňuje implementovat sofistikované strategie směrování provozu, například přesměrování dat na Wi-Fi v přetížených oblastech nebo zajištění, že služby kritické pro misi vždy využívají licencovanou 3GPP síť pro garantovanou kvalitu služeb.

## K čemu slouží

ISMP bylo vytvořeno za účelem řešení problému nekoordinovaného a potenciálně neoptimálního výběru přístupu ze strany UE v heterogenních sítích. Raná více režimová zařízení se spoléhala primárně na jednoduchá měření síly signálu (např. výběr nejsilnějšího Wi-Fi signálu) nebo preference uživatele, což často vedlo ke špatné uživatelské zkušenosti, přetížení sítě na preferovaných přístupech a neefektivnímu využití celkových síťových zdrojů. Operátoři neměli kontrolu nad tím, jak UE využívala dostupné rádiové prostředky.

Zavedení ISMP, zejména s [ANDSF](/mobilnisite/slovnik/andsf/) ve 3GPP Rel-8 a jeho vylepšení v pozdějších vydáních, poskytlo operátorům mocný nástroj pro síťově řízenou správu mobility. Řešilo potřebu inteligentního směrování provozu mezi 3GPP a ne-3GPP sítěmi za účelem optimalizace kapacity, zlepšení uživatelského zážitku a implementace obchodních politik (např. přesměrování předplatitelů na Wi-Fi při roamingu za účelem snížení nákladů). Navíc, jak se v 5G staly klíčovými síťové řezy a QoS citlivé na aplikace, ISMP se vyvinulo tak, aby podporovalo podrobnější politiky schopné směrovat konkrétní služby nebo řezy k nejvhodnějšímu typu rádiového přístupu, což zajišťuje plnění smluvních úrovní služeb v prostředí s více přístupy na hraně sítě.

## Klíčové vlastnosti

- Poskytuje pravidla pro výběr přístupové sítě a směrování provozu definovaná operátorem
- Podporuje jak 3GPP (LTE, NR), tak ne-3GPP (např. Wi-Fi) přístupové technologie
- Umožňuje síťově řízenou mobilitu na základě polohy, času, stavu roamingu a dalších podmínek
- Dynamicky doručováno UE prostřednictvím ANDSF (EPS) nebo PCF/NSSF (5GS)
- Umožňuje stanovit priority typů přístupu pro navazování spojení a předávání hovoru
- Usnadňuje efektivní vyvažování zatížení a přesměrování provozu v heterogenních sítích

## Související pojmy

- [ATSSS – Access Traffic Steering, Switching, and Splitting](/mobilnisite/slovnik/atsss/)

## Definující specifikace

- **TS 24.302** (Rel-19) — Access to EPC via non-3GPP networks; Stage 3
- **TS 24.312** (Rel-19) — ANDSF Management Objects Specification

---

📖 **Anglický originál a plná specifikace:** [ISMP na 3GPP Explorer](https://3gpp-explorer.com/glossary/ismp/)
