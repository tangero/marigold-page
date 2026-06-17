---
slug: "colr"
url: "/mobilnisite/slovnik/colr/"
type: "slovnik"
title: "COLR – Connected Line identification Restriction"
date: 2026-01-01
abbr: "COLR"
fullName: "Connected Line identification Restriction"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/colr/"
summary: "COLR je doplňková služba, která volané straně umožňuje omezit zobrazení svého telefonního čísla (MSISDN) volající straně. Zajišťuje soukromí tím, že zabraňuje volajícímu vidět identitu spojené linky,"
---

COLR je doplňková služba, která volané straně umožňuje omezit zobrazení svého telefonního čísla volající straně za účelem zajištění soukromí.

## Popis

Connected Line identification Restriction (COLR) je standardizovaná doplňková služba v rámci 3GPP, která volanému účastníkovi umožňuje zabránit zobrazení jeho telefonního čísla ([MSISDN](/mobilnisite/slovnik/msisdn/)) volající straně během sestavování hovoru. Tato služba funguje uvnitř jádra sítě, konkrétně spolupracuje s funkcemi řízení hovorů v Mobile Switching Center ([MSC](/mobilnisite/slovnik/msc/)) pro hovory v okruhově spínané síti a v IP Multimedia Subsystem (IMS) pro paketově spínané VoIP hovory. Při zahájení hovoru síť zkontroluje profil předplatitele volané strany, aby zjistila, zda je COLR aktivní. Pokud je povolena, síť potlačí přenos identity spojené linky ([CLI](/mobilnisite/slovnik/cli/)) v signalizačních zprávách, jako jsou hlavičky [ISDN](/mobilnisite/slovnik/isdn/) User Part ([ISUP](/mobilnisite/slovnik/isup/)) nebo Session Initiation Protocol (SIP), čímž zajistí, že volající neobdrží žádnou informaci o skutečném čísle, které odpovědělo.

Z architektonického hlediska se COLR spoléhá na Home Location Register ([HLR](/mobilnisite/slovnik/hlr/)) nebo Home Subscriber Server ([HSS](/mobilnisite/slovnik/hss/)), které ukládají profil služeb účastníka včetně nastavení COLR. Během sestavování hovoru obslužné MSC nebo IMS Call Session Control Function ([CSCF](/mobilnisite/slovnik/cscf/)) tento profil dotazuje. Pokud je COLR aktivována, síť upraví signalizaci hovoru tak, že nahradí nebo vynechá identitu spojené linky, často ji nahrazuje obecným indikátorem jako „omezeno“ nebo ponechá pole prázdné. Tento proces je pro volanou stranu transparentní a nevyžaduje manuální aktivaci pro každý hovor, protože se jedná o službu založenou na předplatném spravovanou operátorem sítě.

COLR úzce spolupracuje s dalšími doplňkovými službami, jako je Calling Line Identification Presentation (CLIP) a Calling Line Identification Restriction (CLIR), a vytváří tak komplexní sadu ovládacích prvků pro soukromí a identifikaci. V sítích IMS je COLR implementována pomocí mechanismů SIP, kde může být hlavička P-Asserted-Identity změněna nebo odstraněna na základě preferencí volané strany. Služba je klíčová pro scénáře, kdy si volaná strana přeje zachovat anonymitu, například u pomocných linek, obchodních kontaktních center nebo z důvodu osobního soukromí, a zajišťuje, že volající nemůže získat spojené číslo prostřednictvím síťové signalizace.

Z pohledu protokolu je COLR definována v 3GPP specifikacích jako TS 23.018 pro základní obsluhu hovorů a TS 29.864 pro vylepšení IMS. Zahrnuje specifické informační prvky v řídicích zprávách hovorů, jako je parametr Connected Line Identity v ISUP nebo hlavička SIP Privacy. Síť musí řešit konflikty mezi COLR a dalšími službami, jako jsou funkce explicitního přepsání pro tísňové služby, aby zajistila soulad s předpisy. Celkově je COLR základní funkce ochrany soukromí, která se bezproblémově integruje do mobilních i pevných sítí a chrání identitu účastníka bez narušení spojení hovoru.

## K čemu slouží

COLR byla zavedena, aby řešila rostoucí obavy o soukromí v telekomunikacích, a umožnila volaným stranám kontrolovat zveřejňování svých telefonních čísel. Před její standardizací mohli volající často vidět identitu spojené linky prostřednictvím síťové signalizace, což představovalo riziko pro jednotlivce a organizace potřebující důvěrnost, jako jsou oběti obtěžování, důvěrné obchodní linky nebo linky veřejných služeb. Služba poskytuje standardizovaný mechanismus pro omezení těchto informací a zajišťuje konzistentní ochranu soukromí napříč různými síťovými operátory a regiony.

Vytvoření COLR v 3GPP R99 bylo motivováno potřebou doplnit stávající identifikační služby, jako jsou CLIP a CLIR, a vytvořit tak vyvážený ekosystém, kde mají jak volající, tak volané strany kontrolu nad zobrazením identity. Vyřešila omezení, kdy volané strany neměly způsob, jak zabránit odhalení svého čísla, i když omezily zobrazení čísla volajícího při odchozích hovorech. To bylo obzvláště důležité s nástupem mobilní komunikace, kde jsou osobní čísla často spojena s jednotlivci, což zvyšuje potenciál zneužití, pokud jsou odhalena.

Historicky se COLR vyvinula z funkcí pevné telefonie a byla přizpůsobena pro mobilní sítě, aby podporovala mobilitu a roaming účastníků. Řeší právní a regulační požadavky v mnoha jurisdikcích, které ukládají povinnost ochrany soukromí, a zajišťuje, že sítě mohou dodržovat zákony na ochranu dat. Tím, že poskytuje síťové řešení, COLR odstraňuje potřebu, aby koncoví uživatelé spoléhali na externí zařízení nebo manuální triky ke skrytí svých čísel, a nabízí spolehlivý a standardizovaný přístup, který bezproblémově funguje napříč mezinárodními hranicemi a síťovými technologiemi.

## Klíčové vlastnosti

- Zabraňuje zobrazení MSISDN volané strany volající straně
- Služba založená na předplatném spravovaná prostřednictvím profilů v HLR/HSS
- Integruje se s okruhově spínanými (MSC) i paketově spínanými (IMS) sítěmi
- Používá úpravy signalizace v protokolech ISUP nebo SIP
- Funguje transparentně bez zásahu volané strany pro každý hovor
- Spolupracuje s CLIP a CLIR pro komplexní správu identity

## Související pojmy

- [CLIP – Calling Line Identification Presentation](/mobilnisite/slovnik/clip/)
- [CLIR – Calling Line Identification Restriction](/mobilnisite/slovnik/clir/)
- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [MSISDN – Mobile Station International Subscriber Directory Number](/mobilnisite/slovnik/msisdn/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 22.173** (Rel-20) — IMS Multimedia Telephony Service Definition
- **TS 22.273** (Rel-7) — IMS Multimedia Telephony with PSTN/ISDN Simulation
- **TR 22.976** (Rel-2) — Release 2000 Services Overview
- **TS 23.018** (Rel-19) — Basic call handling in 3GPP CS domain
- **TS 29.864** (Rel-8) — Application Server Service Data Definition for IMS Telephony

---

📖 **Anglický originál a plná specifikace:** [COLR na 3GPP Explorer](https://3gpp-explorer.com/glossary/colr/)
