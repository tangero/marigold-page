---
slug: "nr-u"
url: "/mobilnisite/slovnik/nr-u/"
type: "slovnik"
title: "NR-U – New Radio Unlicensed"
date: 2025-01-01
abbr: "NR-U"
fullName: "New Radio Unlicensed"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/nr-u/"
summary: "NR-U je standard 3GPP pro provoz technologie 5G New Radio v nelicencovaných kmitočtových pásmech, jako jsou 5 GHz a 6 GHz. Umožňuje vysoce výkonné služby 5G kombinací licencovaného a nelicencovaného s"
---

NR-U je standard 3GPP pro provoz technologie 5G New Radio v nelicencovaných kmitočtových pásmech za účelem rozšíření kapacity a pokrytí kombinací licencovaného a nelicencovaného spektra.

## Popis

New Radio Unlicensed (NR-U) je technologie definovaná konsorciem 3GPP, která rozšiřuje rozhraní 5G New Radio (NR) pro provoz v nelicencovaných nebo sdílených kmitočtových pásmech. Na rozdíl od tradičního NR, které funguje v licencovaném, výhradním spektru, musí NR-U v těchto sdílených pásmech spravedlivě koexistovat s jinými systémy, jako je Wi-Fi. Architektura integruje buňky NR-U do celkové 5G RAN, kde mohou být nakonfigurovány jako samostatné buňky nebo, častěji, agregovány s primární buňkou v licencovaném spektru (NR-U SCell) pomocí rámců pro agregaci nosných nebo duální konektivitu. gNB spravuje buňku NR-U, což zahrnuje novou vrstvu řízení přístupu k médiu ([MAC](/mobilnisite/slovnik/mac/)) a procedury fyzické vrstvy navržené pro provoz v nelicencovaném spektru.

Klíčem k provozu NR-U je jeho mechanismus přístupu k kanálu, který zajišťuje soulad s regionálními předpisy, jako jsou například předpisy [FCC](/mobilnisite/slovnik/fcc/) nebo [ETSI](/mobilnisite/slovnik/etsi/). Primárně používá Listen-Before-Talk ([LBT](/mobilnisite/slovnik/lbt/)), což je forma snímání nosné, kdy zařízení naslouchá kanálu, aby se ujistilo, že je volný, než začne vysílat. Tím se zabrání kolizím s jinými přenosy. Standard definuje různé kategorie LBT (např. Kategorie 2 pro kratší snímání, Kategorie 4 s náhodným odstupem) pro různé typy přenosů, jako jsou zjišťovací signály, datové dávky nebo řídicí signalizace. Fyzická vrstva si zachovává základní vlnové formy NR, jako je [OFDMA](/mobilnisite/slovnik/ofdma/), ale zahrnuje funkce jako limity doby obsazení kanálu a dynamický výběr kmitočtu pro vyhýbání se radaru v určitých pásmech.

Úlohou NR-U v síti je poskytovat doplňkovou kapacitu a pokrytí. Typicky je nasazeno jako sekundární buňka (SCell) agregovaná s primární buňkou v licencovaném NR, čímž vytváří širší šířku pásma pro uživatelské zařízení (UE). Tuto agregaci spravuje plánovač MAC v gNB, který dynamicky přiděluje prostředky napříč licencovanými a nelicencovanými nosnými na základě dostupnosti kanálu a zatížení provozu. Pro provoz sítě NR-U podporuje základní funkce, jako je počáteční přístup, kdy může UE provádět vyhledávání buněk a synchronizaci na nelicencovaném nosném, pokud je nakonfigurováno, ačkoli získání sítě často závisí na licencované kotvě. Podporuje také procedury mobility a řízení kvality služeb a integruje se do celkové 5G core sítě pro autentizaci, řízení politik a směrování dat v uživatelské rovině.

## K čemu slouží

NR-U bylo vytvořeno, aby řešilo kritický problém nedostatku spektra pro nasazení 5G. Licencované spektrum je omezený a drahý zdroj. Díky možnosti provozu 5G NR v globálně dostupných nelicencovaných pásmech (např. 5 GHz, 6 GHz) mohou operátoři a podniky výrazně rozšířit dostupnou šířku pásma bez nutnosti získávat nové licencované spektrum. Tím se přímo řeší problém uspokojení exponenciálně rostoucí poptávky po kapacitě mobilních dat a službách s ultranízkou latencí, které slibuje 5G.

Historicky technologie jako LTE-LAA (License Assisted Access) v 4G předznamenaly koncept použití nelicencovaného spektra jako posilovače kapacity, ale byly omezeny základní technologií LTE. Motivací pro NR-U bylo přenést vynikající výkonnostní charakteristiky 5G NR – jako je škálovatelná numerologie, massive [MIMO](/mobilnisite/slovnik/mimo/) a ultra-spolehlivá komunikace s nízkou latencí (URLLC) – do nelicencované domény. To umožňuje efektivnější a výkonnější využití sdíleného spektra ve srovnání s Wi-Fi nebo LTE-LAA a umožňuje skutečné zážitky na úrovni 5G v hustých městských oblastech, továrnách a areálech.

NR-U navíc řeší problém umožnění nákladově efektivního nasazení privátních 5G sítí. Podniky mohou nasazovat lokální 5G sítě využívající nelicencované nebo lehce licencované spektrum, což snižuje vstupní bariéru. Také usnadňuje pokročilé případy použití, jako je průmyslový IoT, kde jsou potřeba spolehlivá vysokokapacitní bezdrátová spojení, ale vyhrazené licencované spektrum nemusí být proveditelné. Standardizací provozu NR-U zajišťuje globální interoperabilitu a spravedlivou koexistenci se zavedenými technologiemi, jako je Wi-Fi, a zabraňuje tak scénáři „divokého západu“ v nelicencovaných pásmech.

## Klíčové vlastnosti

- Provoz v nelicencovaných/sdílených kmitočtových pásmech (např. 5 GHz, 6 GHz)
- Povinné Listen-Before-Talk (LBT) pro spravedlivou koexistenci s jinými systémy
- Podpora agregace nosných s licencovanou NR kotvou (NR-U SCell)
- Flexibilní schémata přístupu ke kanálu (LBT Kategorie 2 a Kategorie 4)
- Dynamický výběr kmitočtu (DFS) pro vyhýbání se radaru v určitých pásmech
- Integrace s kompletní sadou funkcí 5G NR včetně URLLC a mMTC

## Definující specifikace

- **TS 23.401** (Rel-19) — Evolved Packet System (EPS) Stage 2 Description
- **TS 37.890** (Rel-19) — Feasibility Study on 6 GHz for LTE/NR
- **TR 38.889** (Rel-16) — NR-based access to unlicensed spectrum study

---

📖 **Anglický originál a plná specifikace:** [NR-U na 3GPP Explorer](https://3gpp-explorer.com/glossary/nr-u/)
