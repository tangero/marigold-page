---
slug: "bmca"
url: "/mobilnisite/slovnik/bmca/"
type: "slovnik"
title: "BMCA – Best Master Clock Algorithm"
date: 2026-01-01
abbr: "BMCA"
fullName: "Best Master Clock Algorithm"
category: "Other"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/bmca/"
summary: "BMCA je distribuovaný algoritmus používaný v sítích 5G pro výběr nejpřesnějšího a nejspolehlivějšího časového zdroje (Best Master Clock) z více dostupných zdrojů. Zajišťuje synchronizaci v celé síti,"
---

BMCA je distribuovaný algoritmus používaný v sítích 5G pro výběr nejpřesnějšího a nejspolehlivějšího časového zdroje z více dostupných zdrojů za účelem zajištění kritické synchronizace v celé síti.

## Popis

Algoritmus Best Master Clock (BMCA) je klíčovou součástí frameworku Precision Time Protocol ([PTP](/mobilnisite/slovnik/ptp/)), konkrétně definovanou v [IEEE](/mobilnisite/slovnik/ieee/) 1588, a je přijat a specifikován 3GPP pro použití v architekturách systému 5G (5GS) k dosažení přesné síťové synchronizace. Jeho primární funkcí je dynamické a autonomní určení jediného nejlepšího časového referenčního zdroje, známého jako Grandmaster Clock, v síti s více potenciálními časovými zdroji. Tento výběrový proces je kontinuální a distribuovaný, což znamená, že každý uzel (nebo hodiny) v doméně PTP provádí algoritmus nezávisle na základě přijatých časových zpráv, čímž zajišťuje konzistentní a stabilní hierarchii bez nutnosti centralizované konfigurace pro výběr hlavního zdroje.

Algoritmus funguje tak, že každý port hodin (který může být ve stavu master, slave nebo passive) vyměňuje specifické PTP zprávy, především Announce zprávy. Tyto Announce zprávy nesou klíčová data používaná v rozhodovacím procesu, organizovaná v datové sadě. Klíčové porovnávací parametry, vyhodnocované v přísném hierarchickém pořadí, jsou: 1) Priority1 (konfigurovatelná hodnota nastavená správcem), 2) Clock Class (udávající sledovatelnost a kvalitu hodin, např. k primárnímu referenčnímu časovému zdroji (PRTC)), 3) Clock Accuracy (přesnost hodin), 4) Clock Variance (Allanova variance, udávající krátkodobou stabilitu), 5) Priority2 (konfigurovatelná hodnota druhé úrovně) a 6) Unique Identifier hodin (typicky jejich [MAC](/mobilnisite/slovnik/mac/) adresa). BMCA provádí porovnání těchto datových sad – vlastní a přijaté od jiných hodin – podle tohoto prioritního pořadí. Hodiny s „lepší“ datovou sadou (např. nižší Priority1, vyšší Clock Class) vyhrávají v každém kroku porovnání. Port, který určí, že má nejlepší datovou sadu, se stane hlavním portem (master), zatímco ostatní se stanou jeho podřízenými (slave). Porty, které nejsou ani nejlepším hlavním zdrojem, ani podřízenými nejlepšího hlavního zdroje, přejdou do pasivního stavu (passive), aby se zabránilo časovým smyčkám.

V rámci architektury 5G dle 3GPP je role BMCA klíčová pro distribuci společné fázové a časové reference v přístupové rádiové síti (RAN), zejména pro funkce jako Coordinated Multipoint (CoMP) a operace New Radio (NR) v režimu [TDD](/mobilnisite/slovnik/tdd/). Systém 5G může využívat více časových zdrojů, jako je Global Navigation Satellite System ([GNSS](/mobilnisite/slovnik/gnss/)) na gNB, nebo časový tok od síťového jádra přes User Plane Function ([UPF](/mobilnisite/slovnik/upf/)). Transportní síť ([TN](/mobilnisite/slovnik/tn/)) mezi gNB a mezi gNB a UPF také využívá PTP s BMCA. BMCA tedy funguje na více vrstvách: v rámci časově distribuční sítě TN pro výběr Grandmaster hodin a v rámci 5GS pro správu toho, který časový zdroj (např. gNB s GNSS vs. časování od síťového jádra) je vybrán jako hlavní pro konkrétní časovou doménu. Jeho robustní a deterministický výběrový proces zajišťuje, že pokud se stane dostupným kvalitnější časový zdroj (jako přímo připojený GNSS přijímač), automaticky získá přednost před následným nebo méně přesným zdrojem, čímž udržuje optimální kvalitu synchronizace.

Implementace a požadavky na BMCA v 5G jsou podrobně popsány ve specifikacích 3GPP, zejména v TS 23.501 pro principy systémové architektury a TS 33.851 pro bezpečnostní aspekty časové synchronizace. Bezpečnost je významným problémem, protože útočník může falšovat Announce zprávy a manipulovat výsledkem BMCA, což způsobí, že se síť synchronizuje s nesprávným nebo škodlivým časovým zdrojem a dojde k přerušení služeb. Proto 3GPP vyžaduje použití bezpečnostního mechanismu PTP založeného na MACsec a definovaného v IEEE 1588, který zahrnuje integritu a ochranu proti opětovnému přehrání pro PTP zprávy, aby byl rozhodovací proces BMCA zabezpečen proti takovým útokům.

## K čemu slouží

BMCA existuje k řešení základního problému vytvoření a udržování jediné, autoritativní a kvalitní časové reference v distribuované paketové síti s více potenciálními časovými zdroji. Před standardizovanými algoritmy, jako je BMCA, síťová synchronizace často spoléhala na hierarchické konfigurace master-slave, které byly ručně provozovány (např. pomocí SyncE pouze pro frekvenci), nebo na externí systémy jako [GNSS](/mobilnisite/slovnik/gnss/) na každém uzlu. Ruční konfigurace je nepružná, náchylná k chybám a nepřizpůsobí se výpadkům sítě nebo zavedení lepších hodin. Spoléhání se pouze na GNSS na každém místě je nákladné, má fyzická instalační omezení a je zranitelné vůči rušení a falšování (jamming a spoofing).

Vytvoření a přijetí BMCA v rámci IEEE 1588 a následně 3GPP bylo motivováno potřebou automatizované, spolehlivé a přesné fázové/časové synchronizace přes paketové sítě pro podporu služeb nové generace. 4G LTE-Advanced začalo vyžadovat těsné fázové sladění pro funkce jako eICIC a CoMP. 5G NR, s použitím vyšších frekvencí, massive MIMO a přísných konfigurací TDD, vyžaduje ještě přesnější synchronizaci (často v řádu stovek nanosekund). Navíc konvergence 5G s průmyslovými a kritickými aplikacemi, zahrnutá v konceptech jako integrace s Time-Sensitive Networking (TSN) a podpora Ultra-Reliable Low-Latency Communications (URLLC), činí robustní, odolnou a bezpečnou distribuci času nezbytným síťovým prvkem.

BMCA řeší omezení předchozích přístupů tím, že poskytuje plně distribuovaný algoritmus založený na stavovém automatu. Automatizuje kritický proces výběru hlavních hodin, což umožňuje samoorganizující se časové hierarchie. To umožňuje síti dynamicky se přizpůsobovat změnám topologie, výpadkům hodin nebo zavedení nového, kvalitnějšího časového zdroje bez manuálního zásahu. Tato autonomie je zásadní pro provozní robustnost a škálovatelnost ve velkých, komplexních nasazeních 5G, včetně neveřejných sítí (NPN) a scénářů síťového řezání (network slicing), kde různé řezy mohou mít různé požadavky na synchronizaci. BMCA tvoří inteligentní řídicí rovinu pro PTP a zajišťuje, že fyzicky nejlepší dostupné hodiny vždy řídí synchronizační doménu.

## Klíčové vlastnosti

- Distribuovaný algoritmus stavového automatu
- Hierarchické porovnání založené na datových sadách hodin
- Dynamický výběr a opětovný výběr Grandmaster hodin
- Prevence časových smyček prostřednictvím pasivních stavů portů
- Podpora více domén a profilů PTP
- Základ pro zabezpečené časování prostřednictvím Announce zpráv chráněných integritou

## Definující specifikace

- **TS 23.501** (Rel-20) — 5G System Architecture Stage 2
- **TR 33.851** (Rel-17) — Security for Industrial IoT in 5G

---

📖 **Anglický originál a plná specifikace:** [BMCA na 3GPP Explorer](https://3gpp-explorer.com/glossary/bmca/)
