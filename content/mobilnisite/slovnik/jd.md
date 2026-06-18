---
slug: "jd"
url: "/mobilnisite/slovnik/jd/"
type: "slovnik"
title: "JD – Joint Detection"
date: 2025-01-01
abbr: "JD"
fullName: "Joint Detection"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/jd/"
summary: "Joint Detection je technika detekce více uživatelů používaná v uplinku systémů TD-SCDMA ke zmírnění interference. Současně detekuje a odděluje signály od více uživatelů sdílejících stejný časový slot"
---

JD (Joint Detection) je technika detekce více uživatelů používaná v uplinku TD-SCDMA ke zmírnění interference současným oddělením signálů od více uživatelů sdílejících stejný časový slot a kód.

## Popis

Joint Detection (JD) je sofistikovaný algoritmus zpracování signálu klíčový pro rozhraní [TD-SCDMA](/mobilnisite/slovnik/td-scdma/) (Time Division-Synchronous Code Division [Multiple Access](/mobilnisite/slovnik/multiple-access/)). Funguje na fyzické vrstvě, konkrétně v přijímači Node B, pro zpracování uplink přenosu, kde více uživatelských zařízení (UE) vysílá současně. Hlavní problém, který JD řeší, je přítomnost interference mezi uživateli (Multiple Access Interference – [MAI](/mobilnisite/slovnik/mai/)) a mezisymbolové interference (Inter-Symbol Interference – [ISI](/mobilnisite/slovnik/isi/)), které vznikají, když uživatelé v systému založeném na [CDMA](/mobilnisite/slovnik/cdma/) sdílejí stejný časový slot a rozprostírací kódy. Na rozdíl od konvenčních přijímačů CDMA, které považují interferenci od jiných uživatelů za šum, JD tuto interferenci aktivně modeluje a potlačuje.

Algoritmus funguje tak, že využívá znalost impulzních odezev kanálu a rozprostíracích kódů všech aktivních uživatelů v daném časovém slotu. Přijímač nejprve odhadne kanál pro každého uživatele. Pomocí těchto odhadů a známých rozprostíracích kódů sestaví systémovou matici, která matematicky modeluje kombinovaný přijímaný signál od všech uživatelů včetně efektů kanálu. JD poté řeší tuto soustavu rovnic, často pomocí algoritmů jako Zero-Forcing ([ZF](/mobilnisite/slovnik/zf/)) nebo Minimum Mean Square Error ([MMSE](/mobilnisite/slovnik/mmse/)), aby společně odhadl vysílané datové symboly od všech uživatelů současně. Tento proces efektivně odděluje překrývající se signály, extrahuje zamýšlená data pro každého uživatele a potlačuje interferenci od ostatních.

Klíčové komponenty umožňující JD zahrnují přesný odhad kanálu, přesnou znalost rozprostíracích kódů uživatelů a dostatečný výpočetní výkon v Node B pro provádění složitých maticových operací v reálném čase. Jeho role je klíčová pro výkon TD-SCDMA, protože umožňuje provoz s velmi přísným požadavkem na synchronizaci uplinku (odtud 'Synchronous' CDMA), což zjednodušuje strukturu interference a činí problém společné detekce lépe řešitelným. Potlačením MAI umožňuje JD vyšší uživatelskou zátěž na časový slot a kmitočtovou nosnou, což přímo vede ke zvýšené kapacitě systému a lepšímu pokrytí, zejména v hustých městských oblastech, kde je interference hlavním limitujícím faktorem.

## K čemu slouží

Joint Detection byl vytvořen, aby překonal základní kapacitní omezení tradičních systémů [CDMA](/mobilnisite/slovnik/cdma/), způsobená primárně interferencí mezi uživateli (Multiple Access Interference – MAI). V raných systémech CDMA, jako IS-95 a FDD režim UMTS, je kapacita uplinku převážně limitována interferencí. Problém 'near-far', kdy silný signál od blízkého uživatele přehluší slabý signál od vzdáleného uživatele, vyžaduje složitou regulaci výkonu, ale stále vede ke zbytkové interferenci, která omezuje kapacitu systému. JD poskytuje řešení tohoto problému na úrovni zpracování signálu.

Motivace pro JD v rámci 3GPP, konkrétně pro TD-SCDMA (začleněné z čínského standardu), bylo umožnit vysokokapacitní, spektrálně účinný TDD režim pro 3G. TDD systémy jsou inherentně náchylnější k interferenci v uplinku i downlinku kvůli sdíleným kmitočtovým zdrojům. JD byla klíčovou technologickou inovací, která učinila TD-SCDMA životaschopným, umožňujícím podporovat podobný počet uživatelů jako FDD-based WCDMA, ale s potenciálně větší spektrální účinností v určitých scénářích s asymetrickým provozem. Odstranil omezení předchozích detekčních metod, které interferenci ignorovaly, tím, že proměnil hlavní nevýhodu (znalost struktury rušivých signálů) ve výhodu pro oddělování signálů, a připravil tak cestu pro pokročilejší techniky detekce více uživatelů v pozdějších generacích mobilních sítí.

## Klíčové vlastnosti

- Současná detekce signálů více uživatelů ve stejném časovém slotu a kódovém prostoru
- Aktivní potlačení interference mezi uživateli (Multiple Access Interference – MAI) a mezisymbolové interference (Inter-Symbol Interference – ISI)
- Závisí na přesném odhadu kanálu a znalosti rozprostíracích kódů všech aktivních uživatelů
- Umožňuje těsnou synchronizaci uplinku, což je charakteristický rys TD-SCDMA
- Významně zvyšuje kapacitu uplinku a spektrální účinnost ve srovnání s konvenčními korelačními přijímači
- Implementováno v Node B (základnové stanici), vyžaduje značné výpočetní zdroje

## Související pojmy

- [TD-SCDMA – Time Division Synchronous Code Division Multiple Access](/mobilnisite/slovnik/td-scdma/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 25.222** (Rel-19) — UTRA TDD Multiplexing & Channel Coding
- **TR 45.914** (Rel-19) — MUROS Feasibility Study for Voice Capacity

---

📖 **Anglický originál a plná specifikace:** [JD na 3GPP Explorer](https://3gpp-explorer.com/glossary/jd/)
