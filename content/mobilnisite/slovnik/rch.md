---
slug: "rch"
url: "/mobilnisite/slovnik/rch/"
type: "slovnik"
title: "RCH – Resume Call Handling"
date: 2025-01-01
abbr: "RCH"
fullName: "Resume Call Handling"
category: "Services"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/rch/"
summary: "Doplňková služba, která umožňuje uživateli dočasně přerušit aktivní mobilní hovor a následně jej obnovit ze stejného nebo jiného zařízení. Poskytuje kontinuitu hovoru a uživatelský komfort, zejména ve"
---

RCH je doplňková služba, která umožňuje uživateli dočasně přerušit aktivní mobilní hovor a následně jej obnovit ze stejného nebo jiného zařízení.

## Popis

Resume Call Handling (RCH) je doplňková služba v přepojování okruhů standardizovaná v 3GPP, která umožňuje účastníkovi pozastavit a později pokračovat v hlasovém hovoru. Během aktivního hovoru může obsluhovaný uživatel vyvolat RCH, aby byl hovor na úrovni sítě přerušen a rádiové spojení bylo uvolněno. Kontext hovoru, včetně spojení s druhou stranou, je udržován sítí. Následně, v rámci definovaného časového limitu, může uživatel iniciovat žádost o obnovení přerušeného hovoru. Síť poté znovu naváže spojení s původní vzdálenou stranou a pokračuje v konverzaci od bodu přerušení.

Provoz služby zahrnuje specifickou signalizaci mezi UE a jádrem sítě, primárně Mobile-services Switching Centre ([MSC](/mobilnisite/slovnik/msc/)). Při vyvolání přerušení odešle UE zprávu FACILITY obsahující invoke komponentu Resume Call Handling. MSC to potvrdí a udržuje větev hovoru směrem k druhé straně v pozastaveném stavu, často přehrává oznámení. Rádiové prostředky jsou uvolněny a UE může přejít do stavu idle. Pro obnovení uživatel zahájí proceduru sestavení hovoru a označí, že jde o obnovení RCH, pomocí specifického parametru ve zprávě SETUP. MSC žádost ověří, přiřadí ji ke kontextu přerušeného hovoru a znovu připojí strany.

Mezi klíčové architektonické komponenty patří [HLR](/mobilnisite/slovnik/hlr/), který ukládá profil služeb účastníka včetně předplatného RCH, a MSC, který vykonává servisní logiku a udržuje stav přerušeného hovoru. Služba obsahuje časovače, které omezují dobu, po kterou může být hovor přerušen, než je automaticky zrušen. RCH interaguje s dalšími doplňkovými službami, jako je Call Hold, ale zásadně se liší, protože Call Hold udržuje rádiové spojení aktivní, zatímco RCH jej uvolňuje. Tato služba poskytuje uživateli plynulý zážitek při řešení přerušení bez nutnosti, aby druhá strana znovu vytočila číslo.

## K čemu slouží

RCH byla vytvořena k řešení potřeb uživatelů při zvládání přerušení hlasových hovorů v časných sítích GSM a UMTS s přepojováním okruhů. Před existencí takových funkcí, pokud uživatel potřeboval přerušit hovor (např. k přijetí jiného hovoru nebo kvůli vstupu do oblasti bez pokrytí), byly jediné možnosti hovor ukončit nebo použít základní Call Hold, který však udržoval rádiové prostředky obsazené. To bylo neefektivní a omezovalo mobilitu a komfort uživatele.

Služba řeší problém kontinuity hovoru při dočasných výpadcích. Umožňuje uživateli záměrně přerušit hovor, čímž uvolní terminál a rádiové prostředky, a následně spolehlivě obnovit stejný hovor. To je užitečné zejména ve scénářích, jako je opuštění oblasti pokrytí, přechod na jiné zařízení nebo nutnost vyřídit krátký prioritní úkol. Rozšiřuje základní telefonní službu tím, že poskytuje větší kontrolu a flexibilitu.

Historicky byla RCH součástí sady doplňkových služeb definovaných od 3GPP Release 4 a dále, které obohacovaly základní telefonní nabídku a konkurovaly funkcím pevných linek. Řešila omezení předchozích přístupů integrací logiky přerušení/obnovení přímo do jádra sítě ([MSC](/mobilnisite/slovnik/msc/)), což zajišťovalo spolehlivost služby nezávisle na okamžitém rádiovém stavu terminálu. I když její význam poklesl s nástupem VoIP a rich communication services, představovala důležitý krok v personalizovaném síťovém řízení hovorů.

## Klíčové vlastnosti

- Umožňuje přerušení aktivního hovoru v přepojování okruhů s udržením stavu na straně sítě
- Umožňuje obnovení stejného hovoru ze stejného nebo jiného UE (pokud je předplaceno)
- Během doby přerušení uvolňuje rádiové prostředky
- Časovač udržovaný sítí omezuje dobu trvání přerušení
- Vyžaduje předplatné a podporu ze strany HLR a MSC
- Pro vyvolání a obnovení používá specifickou signalizaci FACILITY a SETUP

## Související pojmy

- [MSC – Mobile Services Switching Centre](/mobilnisite/slovnik/msc/)

## Definující specifikace

- **TS 23.079** (Rel-19) — Support of Optimal Routeing (SOR) Phase 1

---

📖 **Anglický originál a plná specifikace:** [RCH na 3GPP Explorer](https://3gpp-explorer.com/glossary/rch/)
