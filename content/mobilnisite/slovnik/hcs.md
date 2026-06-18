---
slug: "hcs"
url: "/mobilnisite/slovnik/hcs/"
type: "slovnik"
title: "HCS – Hierarchical Cell Structure"
date: 2025-01-01
abbr: "HCS"
fullName: "Hierarchical Cell Structure"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/hcs/"
summary: "HCS je strategie nasazení sítě využívající překrývající se buňky různých velikostí (makro, mikro, piko) pro optimalizaci kapacity a pokrytí. Umožňuje uživatelskému zařízení (UE) upřednostnit připojení"
---

HCS je strategie nasazení sítě využívající překrývající se buňky různých velikostí pro optimalizaci kapacity a pokrytí, a to upřednostňováním připojení k menším buňkám pro kapacitu či k větším buňkám pro mobilitu.

## Popis

Hierarchická struktura buněk (HCS) je koncept plánování a provozu rádiové sítě, při kterém jsou buňky různých typů a velikostí nasazeny ve vrstvách tak, aby se překrývaly a vytvářely hierarchii. Typická hierarchie se skládá z krycích buněk (velké makro buňky poskytující rozsáhlé pokrytí), podřazených mikro buněk (pro kapacitu ve městech) a piko/femto buněk (pro kapacitu v budovách nebo horkých místech). Základním technickým mechanismem umožňujícím HCS je sada parametrů pro výběr a převýběr buňky, které každá buňka vysílá, včetně úrovně priority HCS. Uživatelské zařízení (UE) je nakonfigurováno s prahovými hodnotami HCS a tyto parametry používá během režimu nečinnosti (výběr/převýběr buňky) a potenciálně i v režimu spojení (předávání) k rozhodnutí, na které vrstvě hierarchie se má připojit nebo zůstat připojeno. Klíčovým parametrem je priorita HCS, kde nižší číselná hodnota označuje vrstvu s vyšší prioritou (např. piko buňky mohou mít nejvyšší prioritu pro kapacitu, zatímco makro buňky mají nižší prioritu). UE měří úrovně přijímaného signálu a porovnává je s prahovými hodnotami specifickými pro službu (např. pro hovor nebo data). Pokud je signál od buňky s vysokou prioritou nad jejím prahem, UE ji vybere. Pokud klesne pod něj, UE může převzít buňku s nižší prioritou (např. makro buňku), i když je její absolutní síla signálu nižší, čímž se zajistí kontinuita služby. Tento rozhodovací proces často zahrnuje hysterézní mechanismus, aby se zabránilo ping-pongovým efektům. V síti tuto hierarchii spravuje řadič rádiové sítě ([RNC](/mobilnisite/slovnik/rnc/) v UMTS) nebo základnová stanice (v LTE/5G, ačkoli se koncept vyvíjí), která spravuje sousední vztahy a parametry pro tyto hierarchické vrstvy. HCS umožňuje síti směrovat provoz: uživatelé s vysokými nároky na kapacitu v horkých místech mohou být přesměrováni na malé buňky, zatímco rychle se pohybující uživatelé jsou udržováni na robustní makro vrstvě, aby se minimalizovalo předávání.

## K čemu slouží

HCS bylo vyvinuto k řešení dvojí výzvy: poskytovat nepřerušované pokrytí široké oblasti a zároveň vysokou místní kapacitu v celulárních sítích, zejména s rostoucí hustotou uživatelů a datovými nároky. Rané celulární sítě (2G) často spoléhaly na jedinou vrstvu stejně velkých buněk, což vedlo k neefektivitám: makro buňky byly v centrech měst přetížené, zatímco nasazení dalších makro buněk vedlo ke zvýšení interference a nákladů. Účelem HCS, zavedeného ve standardech UMTS (3G), bylo vytvořit strukturovaný způsob nasazení heterogenních vrstev buněk s řízenou interakcí. Řešilo problém neřízeného předávání mezi překrývajícími se buňkami, které mohlo způsobit nadměrnou signalizaci a přerušení hovorů. Přiřazením úrovní priority umožňuje HCS operátorům sítí implementovat politiku směrování provozu, například vynucení připojení stacionárních nebo pomalu se pohybujících uživatelů na malé buňky s vysokou kapacitou, zatímco uživatelé v automobilech jsou udržováni na makro vrstvě pro odolnost při pohybu. Tím se optimalizuje jak využití rádiových prostředků, tak uživatelský prožitek. Jeho vytvoření bylo motivováno potřebou sofistikovanějších nástrojů správy rádiových prostředků pro podporu růstu mobilních dat a nástupu služeb 3G. HCS položilo základy moderních konceptů heterogenních sítí (HetNet) v LTE a 5G, kde pokročilé techniky, jako je rozšíření dosahu buňky nebo duální konektivita, staví na této hierarchické filozofii.

## Klíčové vlastnosti

- Vícevrstvé nasazení buněk (makro, mikro, piko, femto)
- Prioritizace buněk prostřednictvím vysílaného parametru priority HCS
- Prahové hodnoty úrovně signálu specifické pro službu pro (pře)výběr buňky
- Hysterézní mechanismy pro zabránění nestabilnímu převýběru (ping-pong)
- Směrování provozu mezi vrstvami na základě mobility uživatele a typu služby
- Integrace s procedurami v režimu nečinnosti a řízením předávání v režimu spojení

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 25.222** (Rel-19) — UTRA TDD Multiplexing & Channel Coding
- **TS 25.304** (Rel-19) — UTRA Idle Mode Procedures Specification
- **TS 25.331** (Rel-19) — UTRAN RRC Protocol Specification
- **TS 25.367** (Rel-19) — Home NodeB Mobility Procedures
- **TS 43.064** (Rel-19) — GPRS Radio Interface Lower-Layer Functions

---

📖 **Anglický originál a plná specifikace:** [HCS na 3GPP Explorer](https://3gpp-explorer.com/glossary/hcs/)
